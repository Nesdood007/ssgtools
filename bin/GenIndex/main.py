#! /usr/bin/python3
# This program takes in Markdown files (with attached YAML metadata) and creates a table of contents that will be added to the final rendered pages.

import parse as p
import render as r

import os
import sys

# Global Variables should go in this function
YAML_BLOCK="---"
MAX_ENTRIES=100 #TODO implement a page limiting feature later

HEADER_FILE="_index_header.html" # Header HTML File, in SRC
CONTENT_FILE="_index_content.html" # Content HTML File, in SRC
FOOTER_FILE="_index_footer.html" # Footer HTML File, in SRC
INDEX_FILE="index.html" # File to be generated in the DST directory

FILE_TYPES=[".md", ".html"] # Supported File Extensions

# Global Variables local to this module
allFiles = {}

# Main Function
def main():
  if len(sys.argv) < 2:
    print(printUsage())
    return
    
  src = sys.argv[1]
  dst = sys.argv[2]
  
  # Get List of all files in Directory
  readAllFiles(list(os.scandir(src)), src)
  
  # Sort Entries
  #print("Sorting Entries...")
  l = []
  for k in allFiles:
    allFiles[k]["_SORT"] = parseDate(allFiles[k]["date"]) if "date" in allFiles[k].keys() else parseDate("")
    l.append((k, allFiles[k]))
  # Currently, we sort everything by date in descending order
  l = sorted(l, key = lambda x: x[1]["_SORT"], reverse = True)
    
  # Render File
  #print("Rendering Files...")
  fheader = open(src + "/" + HEADER_FILE, "r")
  fcontent = open(src + "/" + CONTENT_FILE, "r")
  ffooter = open(src + "/" + FOOTER_FILE, "r")
  findex = open(dst + "/" + INDEX_FILE, "w")
  
  header = fheader.read()
  content = fcontent.read()
  footer = ffooter.read()
  
  w = r.renderAll(l, header, content, footer)
  findex.write(w)
  findex.close()
  fheader.close()
  fcontent.close()
  ffooter.close()
  
  
def printUsage():
  return "usage: ./main.py src dst"
  
# cdir: Should be a ScanDir Iterator or list or something
# base: This is the name of the base directory where the source files are
def readAllFiles(cdir, base):
  for f in cdir:
    if f.is_dir():
      #print("Reading Directory " + str(f))
      readAllFiles(list(os.scandir(f.path)), base)
    elif f.is_file() and not f.name == HEADER_FILE and not f.name == CONTENT_FILE and not f.name == FOOTER_FILE and f.name[f.name.rfind("."):] in FILE_TYPES:
      
      print(f.path + ":")
      fl = open(f.path, "r")
      fstr = fl.read()
      d = p.parse(fstr)
      #print("Dictionary is: " + str(d))
      if d != None:
        allFiles[f.path.replace(base + "/", "")] = d
      else:
        #print(f.path + " Does not have YAML")
        pass
    
# Dates should be in YYYY-MM-DD format
# date: String of the date in YYYY-MM-DD format
# Returns -1 if invalid
def parseDate(date):
  toRet = 0
  split = date.split("-")
  if len(split) < 3:
    return -1
  toRet = int(split[0].lstrip().rstrip()) * 10000
  toRet += int(split[1].lstrip().rstrip()) * 100
  toRet += int(split[2].lstrip().rstrip()) * 1
  return toRet
  
# Only run if main module.
if __name__ == "__main__":
  main()

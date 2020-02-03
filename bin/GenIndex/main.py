#! /usr/bin/python3
# This program takes in Markdown files (with attached YAML metadata) and creates a table of contents that will be added to the final rendered pages.

import parse as p
import render as r
import docs
import idxParse

import os
import sys
import fnmatch

# Global Variables should go in this Module
MAX_ENTRIES=100 #TODO implement a page limiting feature later

HEADER_FILE="_index_header.html" # Header HTML File, in SRC
CONTENT_FILE="_index_content.html" # Content HTML File, in SRC
FOOTER_FILE="_index_footer.html" # Footer HTML File, in SRC
INDEX_FILE="index.html" # File to be generated in the DST directory
IGNORE_FILE=".ignore" # File that tells what to ignore in the Index Generation

FILE_TYPES=[".md", ".html"] # Supported File Extensions
IGNORE=[] # Files to Ignore

# Global Variables local to this module
allFiles = {}

# Main Function
def main():
  global IGNORE
  global allFiles
  src = ""
  dst = ""
  tmpl_header = HEADER_FILE
  tmpl_content = CONTENT_FILE
  tmpl_footer = FOOTER_FILE

  # Using .index file (SRC DST .index)
  if len(sys.argv) == 4:
    print("Generating Indexes from .index file...")
    src_root = sys.argv[1]
    dst_root = sys.argv[2]
    idxs = idxParse.parseIndexFile(sys.argv[3])
    for i in idxs:
      args = i.split(" ")
      allFiles = {} # Reset Global File Tree
      if len(args) == 2:
        src = (src_root + "/" + args[0]).replace("//", "/")
        dst = (dst_root + "/" + args[1]).replace("//", "/")
        tmpl_header = src + "/" + HEADER_FILE
        tmpl_content = src + "/" + CONTENT_FILE
        tmpl_footer = src + "/" + FOOTER_FILE
      elif len(args) == 5:
        src = (src_root + "/" + args[0]).replace("//", "/")
        dst = (dst_root + "/" + args[1]).replace("//", "/")
        tmpl_header = (src_root + "/" + args[2]).replace("//", "/")
        tmpl_content = (src_root + "/" + args[3]).replace("//", "/")
        tmpl_footer = (src_root + "/" + args[4]).replace("//", "/")
      else:
        print("Not enough Arguments on line", i, file=sys.stderr)
        continue
      IGNORE = parseIgnore(src)
      print("Making Index at: ", src, dst, tmpl_header, tmpl_content, tmpl_footer)
      doGen(src, dst, tmpl_header, tmpl_content, tmpl_footer)

  # Operating in Original Mode (just SRC and DST)
  # Or Operating in Extended Normal Mode (SRC, DST, HEAD, CONT, FOOT)
  elif len(sys.argv) == 3 or len(sys.argv) == 6:
    # Generate as normal
    print("Generating Index as Normal")

    src = sys.argv[1]
    dst = sys.argv[2]
    tmpl_header = src + "/" + HEADER_FILE
    tmpl_content = src + "/" + CONTENT_FILE
    tmpl_footer = src + "/" + FOOTER_FILE

    # Pull Specified Templates
    if len(sys.argv) == 6:
      tmpl_header = sys.argv[3]
      tmpl_content = sys.argv[4]
      tmpl_footer = sys.argv[5]

    IGNORE = parseIgnore(src)
    print("Ignore List:", IGNORE)
    doGen(src, dst, tmpl_header, tmpl_content, tmpl_footer)

  # Incorrect Number of Args
  else:
    print(docs.helpstr)
    return

# Gets a list of Strings from the Ignore File
def parseIgnore(src):
  ignore = []
  try:
    fignore = open(src + "/" + IGNORE_FILE, "r")
    print("Reading Ignore File...")
    for line in fignore.readlines():
      if line[0] == "#" or line == "\t" or line == "\n":
        continue
      ignore.append((src + "/" + line).rstrip("\n").replace("///", "/").replace("//", "/"))
    fignore.close()
  except IOError:
    print("Couldn't find .ignore file. Assuming nothing is being ignored.", file=sys.stderr)

  print(ignore)
  return ignore

# Generates the Index.
def doGen(src, dst, header, content, footer):
  # Get List of all files in Directory
  src = src.rstrip("/")
  dst = dst.rstrip("/")
  readAllFiles(list(os.scandir(src)), src)

  # Sort Entries
  #print("Sorting Entries...")
  l = []
  for k in allFiles:
    # Don't overwrite a specified SORT Value
    if not "_SORT" in allFiles[k].keys():
      allFiles[k]["_SORT"] = parseDate(allFiles[k]["date"]) if "date" in allFiles[k].keys() else parseDate("")
    l.append((k, allFiles[k]))
  # Currently, we sort everything by date in descending order
  l = sorted(l, key = lambda x: int(x[1]["_SORT"]), reverse = True)

  # Render File
  #print("Rendering Files...")
  fheader = open(header, "r")
  fcontent = open(content, "r")
  ffooter = open(footer, "r")
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

# cdir: Should be a ScanDir Iterator or list or something
# base: This is the name of the base directory where the source files are
def readAllFiles(cdir, base):
  for f in cdir:
    if checkIgnore(f.path):
      continue
    if f.is_dir():
      #print("Reading Directory " + str(f))
      readAllFiles(list(os.scandir(f.path)), base)
    elif f.is_file() and not f.name == HEADER_FILE and not f.name == CONTENT_FILE and not f.name == FOOTER_FILE and f.name[f.name.rfind("."):] in FILE_TYPES and not f.name[0:1] == "_":
      print(f.path + ":")
      print("\t" + f.path.replace(base + "/", ""))
      fl = open(f.path, "r")
      fstr = fl.read()
      d = p.parse(fstr)
      #print("Dictionary is: " + str(d))
      if d != None:
        allFiles[f.path.replace(base + "/", "")] = d
      else:
        #print(f.path + " Does not have YAML")
        pass

# Checks if the filename path matches something in the .ignore file
def checkIgnore(name):
  global IGNORE
  for i in IGNORE:
    if (fnmatch.fnmatch(name, i)):
      return True
  return False

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

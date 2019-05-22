#!/usr/bin/python3

# Generates the Necessary Markdown Files to use the Index Generator as a Photo Gallery Generator

import sys
import os

allFiles = []

IGNORE=['.md', '.html']

def main():
  if len(sys.argv) < 2:
    print(usage())
    return
  
  DIR = ""
  TMPL = ""
  hasTMPL = False
  
  for i, arg in enumerate(sys.argv):
    print(arg, i)
    if i == 1:
      DIR = arg
    else:
      if hasTMPL:
        TMPL = arg
      if not hasTMPL and arg == "-t":
        hasTMPL = True
        
  findFiles(list(os.scandir(DIR)), DIR)
  print(allFiles)
  if not hasTMPL:
    renderFiles(DIR, lambda fname: genContentTemplate(fname, defaultTemplate()))
  else:
    tf = open(TMPL, "r")
    template = tf.read()
    tf.close()
    renderFiles(DIR, lambda fname: genContentTemplate(fname, template))
  
# Renders Markdown Files
# base => Base Directory for everything
def renderFiles(base, render):
  for i in allFiles:
    print(base + "/" + i + ".md:")
    # Don't overwrite existing .md file!
    try:
      open(base + "/" + i + ".md", 'r').close()
      print("Skipping File: ", base + "/" + i + ".md")
    except IOError:
      f = open(base + "/" + i + ".md", 'w')
      f.write(render(i))
      f.close()
      
def findFiles(cdir, base):
  for f in cdir:
    if f.is_dir():
      #print("Reading Directory " + str(f))
      findFiles(list(os.scandir(f.path)), base)
    elif f.is_file() and not f.name[0:1] == "_" and not f.name[0:1] == "." and not f.name[f.name.rfind("."):] in IGNORE:
      print(f.path)
      allFiles.append(f.path.replace(base + "/", ""))
  
  
# Default Template to Use
def defaultTemplate():
  return "---\npath: {PATH}\nname: {NAME}\n---"
  
  
def genContentTemplate(fname, template):
  return template.replace("{PATH}", fname).replace("{NAME}", fname[fname.rfind("/") + 1:])
  
  
def usage():
  return "./main.py DIR [-t TEMPLATE]\n\twhere TEMPLATE is the Template Markdown File and DIR is the Directory of the Photos.\nIf a template file is not specified, then a basic template will be generated."  

if __name__ == "__main__":
  main()

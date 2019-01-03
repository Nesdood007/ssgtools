#!/usr/bin/python3
# Removes the Metadata from a Markdown File
import sys

YAML_STR = "---"

startFound = False
endFound = False
for line in sys.stdin:
  if not startFound and line.find(YAML_STR) >= 0:
    startFound = True
  elif startFound and line.find(YAML_STR) >= 0:
    endFound = True
  elif startFound == endFound:
    sys.stdout.write(line)
  

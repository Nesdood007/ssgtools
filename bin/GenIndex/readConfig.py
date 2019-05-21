#!/usr/bin/python3
# This file reads the configuration file that tells where to generate the indexes at.

import sys
import os

import main as m

def main():
  if len(sys.argv) < 4:
    print(usage())
    return
    
  configFile = sys.argv[1]
  SRC = sys.argv[2]
  DST = sys.argv[3]
  
  indexDest = []
  
  f = open(configFile, 'r')
  for line in f.readlines():
    if line[0] == "#" or line.find(" ") < 0:
      continue
    dst = [SRC + line[:line.find(" ")].rstrip("\n"), DST + line[line.find(" ") + 1: ].rstrip("\n")]
    indexDest.append(dst)
    
  # Calls the Index Generator Module
  for index in indexDest:
    print("Generating Index in " + str(index[1]) + " from DST " + str(index[0]))
    m.doGen(index[0], index[1])
  
  
# Returns the Text to print as the Usage
def usage():
  return "Usage: ./readConfig.py FILE SRC DST \n\twhere FILE is the Configuration File, SRC is the Source Directory, and DST is the Destination Directory"
  
  
if __name__ == "__main__":
  main()

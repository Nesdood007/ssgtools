#! /usr/bin/python3

# This is a module that parses the content of a YAML header on a MArkdown File
# WARNING: THIS VERSION OF YAML DOESN'T UNDERSTAND STRUCTURE

YAML_BLOCK="---"

# Returns a Dictionary of the YAML Tags from the markdown
# Takes the content of a file as a string
def parse(fstr):
  idx = fstr.find(YAML_BLOCK)
  if idx == -1:
    print("\tNO YAML BLOCK. SKIPPING FILE")
    return None
  if idx != 0:
    print("\tYAML BLOCK DOESN'T START AT LINE 0, INDEX 0. SKIPPING FILE")
    return None
  end = fstr.find(YAML_BLOCK, idx + 1)
  if end == -1:
    print("\tYAML BLOCK DOESN'T END! SKIPPING FILE")
    return None
  #print("Starts at: " + str(idx))
  lines = fstr[idx + len(YAML_BLOCK) + 1:end].splitlines()
  #print(lines)
  toReturn = {}
  for l in lines:
    split = l.split(":")
    if len(split) == 2:
      toReturn[split[0].lstrip().rstrip()] = split[1].lstrip().rstrip()
    elif len(split) >= 2:
      toReturn[split[0].lstrip().rstrip()] = l[l.find(":") + 1:] # This would typically happen if HTML is embedded into a value.
    else:
      print("\tWARNING: Malformed Expression " + l) 
  return toReturn
  
# Debug
if __name__ == "__main__":
  s = "---\ntest:value\n  test2:42\ntest9:0\n---\n#Hello World"
  ret = parse(s)
  print(ret)

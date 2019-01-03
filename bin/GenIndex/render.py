#! /usr/bin/python3

# This is the module that renders the Table of Contents PAge

# See String Formatting: https://docs.python.org/3/library/stdtypes.html#str.format

from urllib.parse import quote
import main

INT_TAGS = ["_STATUS", "_ERROR", "_WARNING"] # Internal Tags. "_SORT" was removed as it is added to the Dictionary after parsing

# Returns a rendered template
# yaml_dict: Dictionary of all variables in the YAML
# template: String of the template
# path: File path that will be linked to
def render(yaml_dict, template, path):
  path = quote(path.replace(".md", ".html")) # Encode the URL
  template = template.replace("{PATH}", path)
  failed = False
  #TODO get all keys from the template string to check if in the dictionary
  # Grab all Keys
  i = 0
  keys = []
  warns = ""
  #print("Finding Keys...")
  while i < len(template):
    start = template.find("{", i)
    if start == -1: # All Variables have been found
      break
    end = template.find("}", start + 1)
    #print(template[start:end + 1])
    keys.append(template[start + 1 : end])
    i = end + 1
  # Replace invalid keys with empty spaces, and make a warning
  #print("Removing Invalid Keys...")
  #print(yaml_dict.keys())
  for k in keys:
    if not k in yaml_dict.keys() and not k in INT_TAGS:
      template = template.replace("{" + k + "}", "")
      w = "WARNING: " + k + " not in YAML"
      print("\t" + w)
      warns += w + "<br>"
    # Escape Internal Tags so that there is not a KeyError
    if k in INT_TAGS:
      template = template.replace("{" + k + "}", "{{" + k + "}}")
  # Since Curly Brackets are escaped, they will be converted into regular curly brackets
  try:
    template = template.format(**yaml_dict)
  except KeyError as e:
    print("\tException Occured: " + str(type(e).__name__) + ":" + str(e))
    template = template.replace("{_STATUS}", "Failed")
    template = template.replace("{_ERROR}", str(type(e).__name__) + ":" + str(e))
    failed = True
  if not failed and len(warns) == 0:
    template = template.replace("{_STATUS}", "Success")
    template = template.replace("{_ERROR}", "")
    template = template.replace("{_WARNING}", "")
  elif len(warns) > 0:
    template = template.replace("{_STATUS}", "Success with Warnings")
    template = template.replace("{_ERROR}", "")
    template = template.replace("{_WARNING}", warns)
  #print(template)
  return template
  
# Renders all Entries in the List. Returns fully rendered string
# entries: List of (path, dictionary) in the order that will be converted into the page (first element appears at top).
# header: Header HTML String
# template: HTML String to be parsed and rendered
# footer: Footer HTML String
def renderAll(entries, header, template, footer):
  toReturn = ""
  body = ""
  for e in entries:
    (path, d) = e
    print("Rendering " + path + "...")
    body += render(d, template, path)
  toReturn = header + "\n" + body + "\n" + footer
  return toReturn
  
# Debug
if __name__ == "__main__":
  d = {'a':1, "b":2, "c":3}
  t = "<h1> {a} </h1> <p> {b} | {c} </p>"
  ret = render(d, t, "/")
  print(ret)

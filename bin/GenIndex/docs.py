# Stores Documentation Strings

helpstr = """usage: ./main.py src dst [header content footer]

or: ./main.py src dst <.index>
    This generates multiple indexes based off of the .index file present in the Source Directory (SRC). This is just like executing the Index Generator multiple times.

Generates an index.html page based off of the MArkdown files present in a given source directory.
"""

directories="""
In the Source Directory:

.ignore - File telling what patterns of file to ignore (files starting with "." or "_" are automatically ignored)
"""

ignore="""
Each Line should look like the following:

SRC DST [header content footer]

If the line is malformed, it will be ignored, and an error message will print to standard out.
"""
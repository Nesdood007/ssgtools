import sys

# Parses the Index Generator Calls from the .index file
# @param name (String) - Filename to read the indexes from
def parseIndexFile(fname):
    try:
        f = open(fname, "r")

        toRet = []
        # Parse by line
        for line in f.readlines():
            # Look for comment as a line
            if line[0] == "#":
                continue
            # Look for comment inline
            idx = line.find("#")
            if idx != -1:
                toRet.append(line[0:idx - 1].lstrip(" \n\t").rstrip(" \n\t")) # Add everything up to comment
            else:
                toRet.append(line.lstrip(" \n\t").rstrip(" \n\t"))
        f.close()
    except IOError:
        print("Couldn't open", fname, "Perhaps the .index file doesn't exist?", file=sys.stderr)
    return toRet

# Testing Function
def main():
    idx = parseIndexFile(".index")
    print(idx)

if __name__ == "__main__":
    main()
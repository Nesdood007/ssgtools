# Makefile for SSG4 generation script for acm.cse.sc.edu

PREFIX="https://acm.cse.sc.edu/"
TITLE="ACM@USC"
SRVPORT="8000"

# Make everything
all: 
	bin/ssg4 src dst $(TITLE) $(PREFIX)
	bin/GenIndex/main.py src dst

# Remove all generated files
clean: 
	cd dst && rm .files && rm -r *

# Serve the Generated HTML for testing purposes
srv:
	cd dst && python3 -m http.server $(SRVPORT)

# Generate Just the index
index: 
	bin/GenIndex/main.py src dst
	
# Re-create the proper directories if needed
init:
	mkdir dst
	mkdir src

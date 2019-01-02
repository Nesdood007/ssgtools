# Makefile for SSG4 generation script for acm.cse.sc.edu

PREFIX="https://acm.cse.sc.edu/"
TITLE="ACM@USC"
SRVPORT="8000"

all: 
	bin/ssg4 src dst $(TITLE) $(PREFIX)
	bin/GenIndex/main.py src dst

clean: 
	cd dst && rm .files && rm -r *

srv:
	cd dst && python3 -m http.server $(SRVPORT)

index: 
	bin/GenIndex/main.py src dst

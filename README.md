# ssgtools
Some tools to use when generating a Static Site

SSG4 Copyright 2018 Roman Zolotarev <hi@romanzolotarev.com>
[Source can be found here](https://www.romanzolotarev.com/bin/ssg4)

All Python Tools Copyright Brady O'Leary

# How to use the Site Generation Toolset:

## Directoryies and Files:

### bin
Contains all Binary Files used in generating the website

### dst
Destination where all rendered HTML files are located

### src
Source Directory for the Markdown Files and also for extra files as well

### tmp
Used during Markdown Preprocessing

### Makefile
Use this to render the website. Has the following Commands:
* `all` Makes all Files
* `clean` Removes all Compiled files
* `srv` Opens a Local Python Server for Testing

## Parts

### SSG4
[SSG](https://www.romanzolotarev.com/ssg.html) is a tool created by Roman Zolotarev for publishing static sites. By itself, it is quite barebones, but allows for easy customization and hacking.

### (Coming Soon) Markdown Preprocessing Toolchain
Allows for Custom Titles, and a wider variety of HTML Content within Markdown.

## Usage

### Markdown Files
Accepts regular markdown files, but with the toolchain, can also accept some metadata to go along with it.

'''
---
Variable: Value
---
# Lorem Ipsum ...
'''

This metadata is stored as YAML, much like how Jekyll would work in this manner.

### HTML Files
This generation tool also accepts HTML files, and will render them inside of the Template.

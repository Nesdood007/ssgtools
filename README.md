# ssgtools
Some tools to use when generating a Static Site

SSG4 Copyright 2018 Roman Zolotarev <hi@romanzolotarev.com>
[Source can be found here](https://www.romanzolotarev.com/bin/ssg4)

All Python Tools Copyright Brady O'Leary

# Installation

## System Requirements:

- Running Linux-based OS. May also work on BSD, I'm not sure. Tested on Ubuntu 18.04.

- The following must be installed:

    - Python 3.5+
    
    - git
    
    - make
    
    - lowdown
    
        - This can be found at (https://kristaps.bsd.lv/lowdown/)[https://kristaps.bsd.lv/lowdown/]. Follow the Instructions there.
        
        - You could alternatively modify the program to use a different Markdown Converter
        
## Setup

1. Close this repository locally

2. run `./configure` and input the following:

    ```
    Makefile.conf Generation Script
    Website Title:
    <Your Website Title Here>
    Website Base Address: 
    <Your Website Base Address, like "https://arsmachina.net", goes here>
    Source Repository Address (if none, leave blank):
    <git clone address of your Source Repository>
    Destination Repository Address (if none, leave blank):
    <git clone address of your Destination Repository>
    Makefile.conf has been generated. Next run "$ make clone"
    ```
    
    This generates the `Makefile.conf` that is used to populate Variables in the Makefile
    
3. run `make clone`. This automatically clones your source and destination repositories into the required directories

4. At this point, the setup is complete. You should try running `make && make srv` to be sure that the website is generated properly

# How to use the Site Generation Toolset:

## Directoryies and Files:

### bin
Contains all Executable Files used in generating the website

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

### configure
Creates the Makefile.conf file which specifies the Source and Destination directories and repositories, if any.

### example
Contains example template files and Markdown files to provide a reference for how the rendering system works.

## Parts

### SSG4
[SSG](https://www.romanzolotarev.com/ssg.html) is a tool created by Roman Zolotarev for publishing static sites. By itself, it is quite barebones, but allows for easy customization and hacking.

### (Coming Soon) Markdown Preprocessing Toolchain
Allows for Custom Titles, and a wider variety of HTML Content within Markdown.

### Index Generator
This generates index pages for your website.
Please See readme in `/bin/GenIndex`.

### PhotoGallery Helper
This generates Markdown Files for Files. This actually isn't just limited to Photos.
Please see readme in `/bin/photogallery`.

## Usage

### Markdown Files
Accepts regular markdown files, but with the toolchain, can also accept some metadata to go along with it.

```
---
Variable: Value
---
# Lorem Ipsum ...
```

This metadata is stored as YAML, much like how Jekyll would work in this manner.

### HTML Files
This generation tool also accepts HTML files, and will render them inside of the Template.

### Template files
In the src directory, there should be a few files to be used as a template. These are:

* For Page Generation

  * `_header.html`
  
  * `_footer.html`

* For Index Generation

  * `_index_header.html`
  
  * `_index_content.html`
  
  * `_index_footer.html`

These Files contain HTML that is attached together with the generated content to form the individual webpages in this website. However, the index and Content Pages are generated in a slightly different manner.

The Content Pages are made by SSG4, which reads the header and footer files, and also translates the html or markdown files in the src directory into html and contatinates the header before the newly-generated HTML string, and then attaches the footer file's contents after the content, thus forming a complete HTML file.

The Index Page, however, works in a different way. After the Content is rendered, the Index Generator reads through all files and sub-directories in the src directory, storing any information that appears in the Markdown File's YAML header. This data is then injected into the Index Content File by using Python's String Formatting, which replaces variables in curly brackets "{}" with the value scraped from the YAML header. This is done for each file in the SRC directory. The index.html file is created by reading the content from the Index Header, contatinating it with the content for each file (so this content is repeated for as many pages that exist in the SRC directory), and then attaching the footer file behind that to form the whole HTML file.

# Photo Gallery Helper

This tool generates the necessary Markdown files to use the Index Generator as a Photo Gallery.

## Usage

`./main.py <Directory to generate files recursively in> [-t <Markdown Template File to use>]`

__Please Note:__ The PATH is relative to the working directory where the program is run. Keep this in mind if generating an index, and all of the file paths are wrong.

## Template Format

Built-in Variables: `{PATH} - File Path of the Image`, `{NAME} - Filename`

```
---
name: {NAME}
imgpath: {PATH}
---

<img src="{NAME}">
<p> Image at {PATH} </p>

```

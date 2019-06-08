# Photo Gallery Helper

This tool generates the necessary Markdown files to use the Index Generator as a Photo Gallery. It will not overwrite existing markdown files.

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

## Additional Uses

This program isn't just limited to use with photos. It should also be able to be used with any other file format (excluding other .md and .html files for obvious reasons), although it would not be a great idea to unleash it on your root directory, as it will generate a lot of trash on your hard drive. The idea is that you primarily use the variables in the yaml header to add to the functionality of your index, such as by adding descriptions, detailed filenames, among other things.
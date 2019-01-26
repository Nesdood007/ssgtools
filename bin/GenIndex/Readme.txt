This is a tool used to create a blog-styled table of contents using a separate header and footer file from the SSG renderer.

How this works:
  This program reads all .md files in the src directory, and reads the YAML metadata from the header. This is stored in memory.
  After all files are read, then the Table of Contents Page is Generated, from the total number of articles, and also for just tags.
    For Page Generation, the body is concatinated with the header and footer. For each article, the contents of the post template are evaluated, and inserted into the _index_content.html template file, and added into the body. Posts will be added in order of most recent post (as specified by the date in the metadata).
    
Files:
  _index_header.html: Header Segment
  _index_content.html: Post Template
  _index_footer.html: Footer Segment
  
templating Info:
  Variables should look like: {varname}
  Variable naming Scheme:
    {varname}: All variables are within {}, and the names match variables given in
    All variable names that are in .md files should be lowercase in name.
    All Built-in Variables (those that are created by the program) should be in all caps.
    Any Built-in Variable that is temporarily used internally for things like sorting or whatever should be prefixed with an underscore
  Built-ins:
    {PATH}: This is the URL that points to the file
    {_SORT}: This is for internal sorting. Use only for debugging
    {_ERROR}: Prints errors that occured while processing the file. Use only for Debugging
    {_STATUS}: Prints the end status of that file. Will not print the entire error
    {_WARNING}: Prints all Warnings that occured, such as missing variables
    
Things to keep in mind:
  DATE FORMAT:
    Date should be formatted as YEAR-MONTH-DAY where all 3 categories are numbers
  YAML:
    The YAML parsed here doesn't understand structure, so any nested YAML variables will NOT work as expected. Therefore, do not nest them.

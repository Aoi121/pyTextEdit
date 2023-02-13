# pyTextEdit
Vim-like text editor I've been creating in python.

## Features
* Open files within the editor and from the terminal
  * Use the argument `-f` to open files from the terminal
* Saving and loading of files
  * Saving files as
  * Overwriting files
  * Prints the contents of the file to the terminal upon loading a file.
*  Commands used by prefixing a letter or multiple letters with `:`
  * `:h` for help 
* Appending lines to files
  * Editing lines is a WIP. 

## Todo List
- [x] Saving files
- [x] Saving files as
- [x] Overwriting files
- [x] Help text
- [x] Opening files from terminal
- [x] Opening files in the editor  
- [ ] Rework how files are read and printed.
- [ ] Allow user to move their selected line and edit pre-exising lines.
- [ ] Add more :commands
  - [ ] `:sq` for saving and quiting
    - [ ] Change `:q` to quitting without saving.
  - [ ] Add `:u` for moving up a line.
  - [ ] Add `:d` for moving down a line.

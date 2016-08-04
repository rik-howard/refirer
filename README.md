# Refirer
2016-07-26

Refirer is a REcursive FInder and REplaceR of text in file system objects.  The word 'refire' is a bit of a fingerful so the command-line program that gets invoked is `reef`.  The tool is useful for finding string instances in text-based projects; quick replacement of terms in projects where more formal tools may be available; and, used with care, refactoring when more formal tools are not available.

There are some use cases for which it fails, however, I've been using it (and meaning to fix the bugs) for a few years and it has not harmed or lost any files.  It provides a coloured preview that higlights potential changes, which usually prevents misjudged usages.  Make of that what you will :)

## Examples
The colouring is not shown.  This passes for *help*.
```
$ reef
You have not supplied a valid base.
Usage: reef base roi regex [token [@]]
where roi is one or more of: dflkpt
matching respectively: directories, files, lines, links, pipes, targets
```
Recursively find all folders
```
$ reef refirer d .
refirer
refirer/bin
refirer/etc
refirer/src
refirer/src/model
refirer/src/view
```
Find files whose names with `py`
```
$ reef refirer f py$
refirer/src/model/common.py
refirer/src/model/context.py
refirer/src/model/finder.py
refirer/src/model/previewer.py
refirer/src/model/replacer.py
refirer/src/model/validator.py
refirer/src/view/shower.py
```
Preview the replacement
```
$ reef refirer l ignoree ignored
refirer/README.md
src/model/context.ignorees
src/model/context.ignoreds

refirer/src/model/context.py
ignorees = ["\.git", "\.svn", "__pycache__", "__init__.py"]
ignoreds = ["\.git", "\.svn", "__pycache__", "__init__.py"]
    for ignoree in ignorees:
    for ignored in ignoreds:
        if not re.search (ignoree, path) is None:
        if not re.search (ignored, path) is None:
```
Replace
```
$ reef refirer l ignoree ignored @
```
Find the orginal
```
$ reef refirer l ignoree
```
Find the final
```
$ reef refirer l ignored
refirer/README.md
src/model/context.ignoreds
refirer/src/model/context.py
ignoreds = ["\.git", "\.svn", "__pycache__", "__init__.py"]
    for ignored in ignoreds:
        if not re.search (ignored, path) is None:
```

## Set-Up
The project is written in Python 3.  The entry-point script expects the Python interpreter to be `/usr/bin/python3`.  Change the first line of `bin/reef`, if the interpreter is elsewhere!  Customise `REFIRER_HOME` in `etc/environment` as appropriate!  This file may then be sourced as required.  Alternatively, it may be copied to `~/.kde/env` (where it needs to be renamed to something like `refirer.sh` -- with that extension) so that it does not require sourcing.

The program depends on Colorama.
```
cd .../download
wget http://pypi.python.org/packages/source/c/colorama/colorama-0.2.4.tar.gz#md5=2a4ad72f0deec24497e3bb2e79621914
cd .../project
tar zxvf .../download/colorama-0.2.4.tar.gz
cd colorama-0.2.4
sudo python3 setup.py install
```
To turn the colouring off, invoke `refirer_colouring=off` which can be turned back on in the obvious way!  If the colouring is on, the colours used may be changed with `refirer_backing=light` which can be reverted by setting the value to `dark`.  The list of file system objects (FSO's) that refirer ignores is maintained by `src/model/context.ignorees` which may, of course, be modified as necessary.

*Rik at LRBH Info*

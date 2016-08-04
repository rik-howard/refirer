
import os, re

# session data
origin = os.getcwd ()
home = os.environ ['REFIRER_HOME']
commands = ['find', 'preview', 'replace']
ignoreds = ["\.git", "\.svn", "__pycache__", "__init__.py"]
roit = "^[dfkplt]+$"  # folders; files, links, pipes; lines, terls
roitd  = "d"
roitf  = "f"
roitk  = "k"
roitp  = "p"
roitl  = "l"
roitt  = "t"

# operation data
prompted = False
base = '~'
roi = ''
regex = ''
token = ''
command = ''
message = ''

#

def ids_roi (mark):
    return roi.find (mark) > -1

#

def ids_ignorable (path):
    ignorable = False
    for ignored in ignoreds:
        if not re.search (ignored, path) is None:
            ignorable = True
    return ignorable

#

def ids_replaceable_last (path):
    if re.search (regex, path) is None: return False
    else:
        constants = re.split (regex, path)
        last_constant = constants [len (constants) - 1]
        return re.search (os.sep, last_constant) is None

def ids_replaceable (string):
    return not re.search (regex, string) is None

#

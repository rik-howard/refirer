
import os, re

def ids_folder (foldee_path):
    return os.path.isdir (foldee_path) and not os.path.islink (foldee_path)

def ids_file (foldee_path):
    return os.path.isfile (foldee_path) and not os.path.islink (foldee_path)

def ids_link (foldee_path):
    return os.path.islink (foldee_path)

def ids_pipe (foldee_path):
    return os.path.exists (foldee_path) and not ids_folder (foldee_path) and not ids_file (foldee_path) and not ids_link (foldee_path)

#

def folders_paths (folder_path):
    paths = []
    for subfolder_leaf in os.listdir (folder_path):
        subfolder_path = os.path.join (folder_path, subfolder_leaf)
        if ids_folder (subfolder_path):
            paths.append (subfolder_path)
    paths.sort ()
    return paths

def files_paths (folder_path):
    paths = []
    for fso_leaf in os.listdir (folder_path):
        fso_path = os.path.join (folder_path, fso_leaf)
        if ids_file (fso_path):
            paths.append (fso_path)
    paths.sort ()
    return paths

def links_paths (folder_path):
    paths = []
    for fso_leaf in os.listdir (folder_path):
        fso_path = os.path.join (folder_path, fso_leaf)
        if ids_link (fso_path):
            paths.append (fso_path)
    paths.sort ()
    return paths

def pipes_paths (folder_path):
    paths = []
    for fso_leaf in os.listdir (folder_path):
        fso_path = os.path.join (folder_path, fso_leaf)
        if ids_pipe (fso_path):
            paths.append (fso_path)
    paths.sort ()
    return paths

#

def terminal (link_path):
    return os.path.realpath (link_path)

#

def replacement_all (string, regex, token):
    return re.sub (regex, token, string)

def replacement_last (path, regex, token):
    constants = re.split (regex, path)
    variables = re.findall (regex, path)
    result = constants [0]
    for i in range (len (variables) - 1):
        result += variables [i] + constants [i + 1]
    result += token + constants [len (constants) - 1]
    return result

#

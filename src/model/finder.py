
from view import shower
from model import context, common

def find ():
    if common.ids_folder (context.base): find_folder (context.base)
    elif common.ids_file (context.base): find_file (context.base)
    elif common.ids_link (context.base): find_link (context.base)
    elif common.ids_pipe (context.base): print ("factor find_pipe from find_pipes (...)") # find_pipe (context.base)
    else: print ("unknown type of f. s. o.")

def find_folders (folder_path):
    for subfolder_path in common.folders_paths (folder_path):
        if context.ids_ignorable (subfolder_path): pass
        else: find_folder (subfolder_path)

def find_folder (folder_path):
    if context.ids_roi (context.roitd):
        if context.ids_replaceable_last (folder_path):
            shower.show_red_tipped (folder_path)
    find_files (folder_path)
    find_links (folder_path)
    find_pipes (folder_path)
    find_folders (folder_path)

def find_files (folder_path):
    for file_path in common.files_paths (folder_path):
        if context.ids_ignorable (file_path): pass
        else: find_file (file_path)

def find_file (file_path):
    headed = False
    if context.ids_roi (context.roitf):
        if context.ids_replaceable_last (file_path):
            shower.show_red_tipped (file_path)
            headed = True
    find_lines (file_path, headed)

def find_lines (file_path, headed):
    if context.ids_roi (context.roitl):
        try:
            for line in open (file_path):
                if context.ids_replaceable (line):
                    if headed: pass
                    else:
                        shower.show_blue (file_path)
                        headed = True
                    shower.show_red_matched (line.rstrip ())
        except UnicodeDecodeError: pass

def find_links (folder_path):
    for link_path in common.links_paths (folder_path):
        if context.ids_ignorable (link_path): pass
        else: find_link (link_path)

def find_link (link_path):
    headed = False
    if context.ids_roi (context.roitk):
        if context.ids_replaceable_last (link_path):
            shower.show_red_tipped (link_path)
            headed = True
    find_terl (link_path, headed)

def find_terl (link_path, headed):
    if context.ids_roi (context.roitt):
        if context.ids_replaceable (common.terminal (link_path)):
            if headed: pass
            else:
                shower.show_blue (link_path)
                headed = True
            shower.show_red_matched (common.terminal (link_path))

def find_pipes (folder_path):
    if context.ids_roi (context.roitp):
        for pipe_path in common.pipes_paths (folder_path):
            if context.ids_ignorable (pipe_path): pass
            elif context.ids_replaceable_last (pipe_path):
                shower.show_red_tipped (pipe_path)

#

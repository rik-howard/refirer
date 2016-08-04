
from view import shower
from model import context, common

def preview ():
    if common.ids_folder (context.base): preview_folder (context.base)
    elif common.ids_file (context.base): preview_file (context.base)
    elif common.ids_link (context.base): preview_link (context.base)
    elif common.ids_pipe (context.base): print ("factor preview_pipe from preview_pipes (...)") # preview_pipe (context.base)
    else: print ("unknown type of f. s. o.")

def preview_folders (folder_path):
    for subfolder_path in common.folders_paths (folder_path):
        if context.ids_ignorable (subfolder_path): pass
        else: preview_folder (subfolder_path)

def preview_folder (folder_path):
    if context.ids_roi (context.roitd):
        if context.ids_replaceable_last (folder_path):
            shower.show_red_tipped (folder_path)
            shower.show_green_tipped (common.replacement_last (folder_path, context.regex, context.token))
    preview_files (folder_path)
    preview_links (folder_path)
    preview_pipes (folder_path)
    preview_folders (folder_path)

def preview_files (folder_path):
    for file_path in common.files_paths (folder_path):
        if context.ids_ignorable (file_path): pass
        else: preview_file (file_path)

def preview_file (file_path):
    headed = False
    if context.ids_roi (context.roitf):
        if context.ids_replaceable_last (file_path):
            shower.show_red_tipped (file_path)
            shower.show_green_tipped (common.replacement_last (file_path, context.regex, context.token))
            headed = True
    preview_lines (file_path, headed)

def preview_lines (file_path, headed):
    if context.ids_roi (context.roitl):
        try:
            for line in open (file_path):
                if context.ids_replaceable (line):
                    if headed: pass
                    else:
                        shower.show_blue (file_path)
                        headed = True
                    shower.show_red_matched (line.rstrip ())
                    shower.show_green_matched (common.replacement_all (line.rstrip (), context.regex, context.token))
        except UnicodeDecodeError: pass

def preview_links (folder_path):
    for link_path in common.links_paths (folder_path):
        if context.ids_ignorable (link_path): pass
        else: preview_link (link_path)

def preview_link (link_path):
    headed = False
    if context.ids_roi (context.roitk):
        if context.ids_replaceable_last (link_path):
            shower.show_red_tipped (link_path)
            shower.show_green_tipped (common.replacement_last (link_path, context.regex, context.token))
            headed = True
    preview_terl (link_path, headed)

def preview_terl (link_path, headed):
    if context.ids_roi (context.roitp):
        if context.ids_replaceable (common.terminal (link_path)):
            if headed: pass
            else:
                shower.show_blue (link_path)
                headed = True
            shower.show_red_matched (common.terminal (link_path))
            shower.show_green_matched (common.replacement_all (common.terminal (link_path), context.regex, context.token))

def preview_pipes (folder_path):
    if context.ids_roi (context.roitp):
        for pipe_path in common.pipes_paths (folder_path):
            if context.ids_ignorable (pipe_path): pass
            elif context.ids_replaceable_last (pipe_path):
                shower.show_red_tipped (pipe_path)
                shower.show_green_tipped (common.replacement_last (pipe_path, context.regex, context.token))

#

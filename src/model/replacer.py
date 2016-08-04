
import os
from model import context, common

def replace ():
    if common.ids_folder (context.base):
        if context.ids_roi (context.roitt): replace_terls_in_folder (context.base)
        if context.ids_roi (context.roitl): replace_lines_in_folder (context.base)
        if context.ids_roi (context.roitp): replace_pipes_in_folder (context.base)
        if context.ids_roi (context.roitk): replace_links_in_folder (context.base)
        if context.ids_roi (context.roitf): replace_files_in_folder (context.base)
        if context.ids_roi (context.roitd): replace_folders_in_folder (context.base)
    elif common.ids_file (context.base):
        if context.ids_roi (context.roitl): replace_lines_in_file (context.base)
        if context.ids_roi (context.roitf): replace_file_in_file (context.base)
    elif common.ids_link (context.base):
        if context.ids_roi (context.roitt): replace_terl_in_link (context.base)
        if context.ids_roi (context.roitk): replace_link_in_link (context.base)
    elif common.ids_pipe (context.base):
        if context.ids_roi (context.roitp): replace_pipe_in_pipe (context.base)
    else: print ('unknown type of f. s. o.:', context.base)

#

def replace_folders_in_folder (folder_path):
    if context.ids_ignorable (folder_path): pass
    else:
        for subfolder_path in common.folders_paths (folder_path):
            replace_folders_in_folder (subfolder_path)
        if context.ids_replaceable_last (folder_path):
            source_folder_path = folder_path
            target_folder_path = common.replacement_last (folder_path, context.regex, context.token)
            try: os.makedirs (target_folder_path)
            except Error: pass
            os.rename (source_folder_path, target_folder_path)

def replace_files_in_folder (folder_path):
    if context.ids_ignorable (folder_path): pass
    else:
        for subfolder_path in common.folders_paths (folder_path):
            replace_files_in_folder (subfolder_path)
        for file_path in common.files_paths (folder_path):
            replace_file_in_file (file_path)

def replace_links_in_folder (folder_path):
    if context.ids_ignorable (folder_path): pass
    else:
        for subfolder_path in common.folders_paths (folder_path):
            replace_links_in_folder (subfolder_path)
        for link_path in common.links_paths (folder_path):
            if context.ids_ignorable (link_path): pass
            elif context.ids_replaceable_last (link_path):
                source_link_path = link_path
                target_link_path = common.replacement_last (link_path, context.regex, context.token)
                terminal = os.path.realpath (source_link_path)
                os.remove (source_link_path)
                os.symlink (terminal, target_link_path)

def replace_pipes_in_folder (folder_path):
    if context.ids_ignorable (folder_path): pass
    else:
        for subfolder_path in common.folders_paths (folder_path):
            replace_pipes_in_folder (subfolder_path)
        for pipe_path in common.pipes_paths (folder_path):
            if context.ids_ignorable (pipe_path): pass
            elif context.ids_replaceable_last (pipe_path):
                source_pipe_path = pipe_path
                target_pipe_path = common.replacement_last (pipe_path, context.regex, context.token)
                os.rename (source_pipe_path, target_pipe_path)

def replace_lines_in_folder (folder_path):
    if context.ids_ignorable (folder_path): pass
    else:
        for subfolder_path in common.folders_paths (folder_path):
            replace_lines_in_folder (subfolder_path)
        for file_path in common.files_paths (folder_path):
            replace_lines_in_file (file_path)

def replace_terls_in_folder (folder_path):
    if context.ids_ignorable (folder_path): pass
    else:
        for subfolder_path in common.folders_paths (folder_path):
            replace_terls_in_folder (subfolder_path)
        for link_path in common.links_paths (folder_path):
            if context.ids_ignorable (link_path): pass
            else:
                source_terminal = os.path.realpath (link_path)
                if context.ids_replaceable (source_terminal):
                    target_terminal = common.replacement_all (source_terminal, context.regex, context.token)
                    os.remove (link_path)
                    os.symlink (target_terminal, link_path)

#

def replace_file_in_file (file_path):
    if context.ids_ignorable (file_path): pass
    elif context.ids_replaceable_last (file_path):
        source_file_path = file_path
        target_file_path = common.replacement_last (file_path, context.regex, context.token)
        try: os.makedirs (os.path.dirname (target_file_path))
        except IOError: pass
        os.rename (source_file_path, target_file_path)

def replace_lines_in_file (file_path):
    if context.ids_ignorable (file_path): pass
    else:
        lines = []
        try:
            replaceable = False
            source = open (file_path)
            for line in source:
                if context.ids_replaceable (line):
                    replaceable = True
                    break
            source.close ()
            if replaceable:
                source = open (file_path)
                for line in source:
                    lines.append (common.replacement_all (line, context.regex, context.token))
                source.close ()
                target = open (file_path, "w")
                for line in lines:
                    target.write (line)
                target.close ()
        except UnicodeDecodeError: pass

#


import os, re
from view import shower
from model import context

# public

def validate (args):
    try:
        set_context_base (args)
        try:
            set_context_roi (args)
            try:
                set_context_regex (args)
                try:
                    set_context_token (args)
                    try:
                        set_context_command (args)
                        context.command = context.commands [2]
                        set_context_ids_roi ()
                    except:
                        context.command = context.commands [1]
                        set_context_ids_roi ()
                except:
                    context.command = context.commands [0]
                    set_context_ids_roi ()
            except:
                context.message = 'You have not supplied a valid regex.'
        except:
            context.message = 'You have not supplied a valid r. o. i..'
    except:
        context.message = 'You have not supplied a valid base.'

#
# private

def set_context_base (args):
    try: context.base = args [1]
    except IndexError: raise Exception

def set_context_roi (args):
    try: context.roi = args [2]
    except IndexError: raise Exception

def set_context_regex (args):
    try: context.regex = args [3]
    except IndexError: raise Exception

def set_context_token (args):
    try: context.token = args [4]
    except IndexError: raise Exception

def set_context_command (args):
    try: assert args [5] == '@'
    except IndexError: raise Exception

def set_context_ids_roi ():
    context.ids_folder_roi = not re.search (context.roitd, context.roi) is None
    context.ids_file_roi = not re.search (context.roitf, context.roi) is None
    context.ids_link_roi = not re.search (context.roitk, context.roi) is None
    context.ids_pipe_roi = not re.search (context.roitp, context.roi) is None
    context.ids_line_roi = not re.search (context.roitl, context.roi) is None
    context.ids_terl_roi = not re.search (context.roitt, context.roi) is None

#

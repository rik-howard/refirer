
import os, re
from colorama import init, Fore, Back, Style
from model import context

init ()

def show_black (string):
    print (string)

def show_blue (string):
    if colouring_is_off ():
        show_black (string)
    elif backing_is_light ():
        print (Fore.BLUE + string + Fore.RESET)
    else:
        print (Style.BRIGHT + Fore.CYAN + string + Fore.RESET + Style.NORMAL)

def show_red_matched (path):
    if colouring_is_off ():
        show_black (path)
    elif backing_is_light ():
        print (colouring_of_all_matches (path, context.regex, Fore.RED))
    else:
        print (colouring_of_all_matches (path, context.regex, Style.BRIGHT + Fore.YELLOW))

def show_red_tipped (path):
    if colouring_is_off ():
        show_black (path)
    elif backing_is_light ():
        print (colouring_of_last_match (path, context.regex, Fore.RED))
    else:
        print (colouring_of_last_match (path, context.regex, Style.BRIGHT + Fore.YELLOW))

def show_green_matched (path):
    if backing_is_light ():
        print (colouring_of_all_identicals (path, context.token, Fore.GREEN))
    else:
        print (colouring_of_all_identicals (path, context.token, Style.BRIGHT + Fore.GREEN))

def show_green_tipped (path):
    if backing_is_light ():
        print (colouring_of_last_identical (path, context.token, Fore.GREEN))
    else:
        print (colouring_of_last_identical (path, context.token, Style.BRIGHT + Fore.GREEN))

#

def colouring_of_all_matches (string, regex, colour):
    if not re.match ('\^?\.\*\$?', regex) is None: return colour + string + Fore.RESET + Style.NORMAL
    else:
        constants = re.split (regex, string)
        variables = re.findall (regex, string)
        assert len (constants) == len (variables) + 1
        result = constants [0]
        for i in range (len (variables)):
            result += colour + variables [i] + Fore.RESET + Style.NORMAL + constants [i + 1]
        return result

def colouring_of_last_match (string, regex, colour):
    if len (string) == 0: print ('yay')
    if not re.match ('\^?\.\*\$?', regex) is None: return colour + string + Fore.RESET + Style.NORMAL
    else:
        constants = re.split (regex, string)
        variables = re.findall (regex, string)
        assert len (constants) == len (variables) + 1
        last_match_index = len (variables) - 1
        result = constants [0]
        for i in range (last_match_index):
            result += variables [i] + constants [i + 1]
        result += colour + variables [last_match_index] + Fore.RESET + Style.NORMAL + constants [last_match_index + 1]
        return result

#

def colouring_of_all_identicals (string, token, colour):
    if len (token) == 0: return string
    else:
        constants = string.split (token)
        result = constants [0]
        for i in range (len (constants) - 1):
            result += colour + token + Fore.RESET + Style.NORMAL + constants [i + 1]
        return result

def colouring_of_last_identical (string, token, colour):
    constants = string.split (token)
    last_match_index = len (constants) - 2
    result = constants [0]
    for i in range (last_match_index):
        result += token + constants [i + 1]
    result += colour + token + Fore.RESET + Style.NORMAL + constants [last_match_index + 1]
    return result

#

def colouring_is_on ():
    return os.getenv ('refirer_colouring', 'on') == 'on'

def colouring_is_off ():
    return not colouring_is_on ()

def backing_is_light ():
    return os.getenv ('refirer_backing', 'dark') == 'light'

#

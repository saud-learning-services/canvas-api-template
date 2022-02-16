from termcolor import cprint
import sys

def print_error(msg):
    '''
    Prints error without shutting down
    Parameters:
        msg (string): Error message to print
    Returns:
        None
    '''
    cprint(f'\n{msg}\n', 'red')


def shut_down(msg):
    ''' 
    Shuts down the script.
    Parameters:
        msg (string): Message to print before printing 'Shutting down...' and exiting the script.
    Returns:
        None
    '''
    cprint(f'\n{msg}\n', 'red')
    print('Shutting down...')
    sys.exit()

def print_success(msg):
    '''
    Prints success message
    Parameters:
        msg (string): Success message to print
    Returns:
        None
    '''
    cprint(f'\n{msg}\n', 'green')

def print_action(msg):
    '''
    Prints a message that requires the user to do something
    Parameters:
        msg (string): Action message to print
    Returns:
        None
    '''
    cprint(f'\n{msg}\n', 'blue')

def continue_quit(in_msg, move_on=False):
    '''
    Prints a message that requires the user to confirm to move forward or quit
    Parameters:
        msg (string): Action message to print
    Returns:
        True (boolean): only when selection == "Y", otherwise no action or sys.exit()
    '''
    if move_on:
        options = f'\nY - yes, continue\nN - no, continue\nAny other key - exit'
    else:
        options = f'\nY - confirmed, continue\nN - not confirmed, continue\nAny other key - exit'

    while True:
        print(f'{in_msg}{options}')
        selection = input('Enter Y/N: ').strip().upper()

        if selection == "Y":
            return True
        elif selection == "N":
            if move_on:
                break
            else:
                return (False)
                selection
        else:
            shut_down("Shut down selected. Ending process.")
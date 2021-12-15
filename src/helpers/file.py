from os import getcwd
from os.path import normpath

def get_db_root():
    return normpath(f'{getcwd()}\\database\\')

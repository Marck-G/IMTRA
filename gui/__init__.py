# need Tkinter to install it sudo apt isntall python3-tk
from tkinter import Tk
from tkinter.filedialog import askdirectory


def show_dir_chouser(title, *args, initialdir = None):
    """
    ask for user to select a folder
    :param title: of the window
    :param initialdir:  folder to open
    :return:
    """
    from pathlib import Path
    # if ther is any dir we set the home as default dir
    if initialdir is None:
        initialdir = Path.home()
    Tk().withdraw()
    options = {
        'initialdir': str(initialdir),
        'title': title
    }
    dirname = askdirectory(**options)
    return dirname


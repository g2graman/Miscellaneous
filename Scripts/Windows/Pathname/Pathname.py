import os
import sys
from Tkinter import Tk


here = os.path.realpath(sys.argv[1])
r = Tk()
r.clipboard_append(here)
r.destroy()

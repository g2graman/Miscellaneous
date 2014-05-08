import std_cat
import os
import sys


here = os.path.realpath(sys.argv[1])
if os.path.isfile(here):
    here = here[:here.rfind("\\")]
elif len(os.path.split(os.path.split(here)[0])[-1]):
    exit()

if not(std_cat.is_categorized(here)):
    std_cat.categorize(here)
#else:
#    std_cat.decategorize(here)
#MUST FIX DECATEGORIZE BECAUSE OF REGISTRY CIRCUMSTANCES
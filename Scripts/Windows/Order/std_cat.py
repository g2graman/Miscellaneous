import media
import os
import os.path
import shutil


def join(direc, ext, char="\\"):
    '''(str, str, str) -> str'''

    return direc + char + ext


def is_categorized(direc):
    '''(list, str) -> bool'''

    categories = get_categs(direc)
    result = True
    for category in categories:
        if not(os.path.exists(join(direc, category))):
            result = False
            break
    return result


def get_categs(direc):
    '''(str) -> list.'''

    categs = []
    for fyle in os.listdir(direc):
        pre = str(fyle)[0].capitalize()
        if not(pre in categs):
            categs.append(pre)
    return categs


def categorize(direc):
    '''(str) -> NoneType'''

    categs = get_categs(direc)
    files = os.listdir(direc)
    for pref in categs:
        new = os.path.abspath(join(direc, pref))
        if not(os.path.exists(new)):
            os.mkdir(new)

    for fyle in files:
        filename = join(direc, fyle)
        pre = str(fyle)[0].capitalize()
        dest = os.path.abspath(join(direc, pre))
        shutil.move(filename, join(dest, fyle))


def decategorize(direc):
    '''(str) -> NoneType.'''

    categs = get_categs(direc)
    files = os.listdir(direc)
    for folder in os.listdir(direc):
        fold = join(direc, folder)
        for fyle in os.listdir(fold):
            filename = join(fold, fyle)
            shutil.move(filename, join(direc, fyle))
        os.removedirs(fold)

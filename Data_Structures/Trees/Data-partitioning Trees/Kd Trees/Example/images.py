from media import *
import os
import ikd


if __name__ == '__main__':
  fyle = choose_file()
  #while():
  if(os.path.isfile(fyle) and fyle.endswith(".jpg")):
    img = load_picture(fyle)
    pxs = []
    for px in get_pixels(img):
      pxs.append((get_red(px, get_green(px), get_blue(px),\
      get_x(px), get_y(px)))

    IKD = ikd.ImplicitKDTree(pxs, 5)
    print(IKD.leaves())
    #fyle = choose_file()

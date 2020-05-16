# -*- coding: utf-8 -*-
#
# memo for f in *.png; do ffmpeg -y -i $f -vcodec png $f; done 
#
#
#

import sys
import os
import re


if __name__ == '__main__':
    xmlfolderpath = "./../koura/xml/"
    #xmlfolderpath = "./../UnderwaterPhotography/xml/"
    xmlfiles = sorted( [ x for x in sorted(os.listdir(xmlfolderpath)) if x!=".DS_Store"])

    #print(xmlfiles)
    print("##################### check xml files")
    for xmlfilename in xmlfiles:
        with open(xmlfolderpath+xmlfilename) as f:
            rawfile = f.read()
        width=int(re.sub(r"\D", "", re.findall("<width>\d</width>",rawfile)[0])  )
        height=int( re.sub(r"\D", "", re.findall("<height>\d</height>",rawfile)[0]) )
        if width==0:
            print("Error width is 0: "+xmlfolderpath+xmlfilename)
        if height==0:
            print("Error height is 0: "+xmlfolderpath+xmlfilename)
        if len( re.findall("<bndbox>",rawfile) )==0:
            print("No ROI annotation: "+xmlfolderpath+xmlfilename)

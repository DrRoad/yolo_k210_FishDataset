# -*- coding: utf-8 -*-

import sys
import os
import re
from PIL import Image

if __name__ == '__main__':
    xmlfolderpath = "./../FishDB_annotations_png_xml/"
    #xmlfolderpath = "./../koura/xml/"
    #xmlfolderpath = "./../UnderwaterPhotography/xml/"
    imgfilepath = "./../FishDB_images_png/"
    #imgfilepath = "./../koura/png/"
    #imgfilepath = "./../UnderwaterPhotography/nagisa_park/"


    xmlfiles = [ x.split(".")[0] for x in sorted(os.listdir(xmlfolderpath)) if x!=".DS_Store"]
    imgfiles = [ x.split(".")[0] for x in sorted(os.listdir(imgfilepath)) if x!=".DS_Store"]

    #print(xmlfiles)
    #print(imgfiles)
    print("##################### check xml files")
    for xmlfilename in xmlfiles:
        if not xmlfilename in imgfiles:
            print( "Error: "+xmlfilename+".png" +" are not found. Please search it, or delete "+xmlfilename)
        #######
        with open(xmlfolderpath+xmlfilename+".xml") as f:
            rawfile = f.read()
        #print(xmlfilename)
        #print(rawfile)
        #print(re.findall("<width>\d{1,4}</width>",rawfile))
        width=int(re.sub(r"\D", "", re.findall("<width>\d{1,4}</width>",rawfile)[0])  )
        height=int( re.sub(r"\D", "", re.findall("<height>\d{1,4}</height>",rawfile)[0]) )

        im = Image.open(imgfilepath+xmlfilename+".png")
        #print(im.size)
        img_width=int(im.size[0])
        img_height=int(im.size[1])

        if width!=img_width:
            print("different width ({0},{1}): {2}".format(width,img_width,imgfilepath+xmlfilename) )
        if height!=img_height:
            print("different height ({0},{1}): {2}".format(height,img_height,imgfilepath+xmlfilename) )

    print("##################### check img files")
    for i,imgfilename in enumerate(imgfiles):
        if not imgfilename in xmlfiles:
            print("Error: No annotation file. " + imgfilename + ".png" + " will be deleted, [y/n] ")
            ans=input()
            if ans=="y":
                print(imgfilepath+imgfilename+"."+sorted(os.listdir(imgfilepath))[i].split(".")[1]+" is deleted.")
                os.remove( imgfilepath+imgfilename+"."+sorted(os.listdir(imgfilepath))[i].split(".")[1] )

            else:
                print(imgfilepath + imgfilename+"."+sorted(os.listdir(imgfilepath))[i].split(".")[1] + " is not deleted.")

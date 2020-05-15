# -*- coding: utf-8 -*-

import sys
import os


classestxtpath="./../classes.txt"



if __name__ == '__main__':
    xmlfolderpath = "./../FishDB_annotations_png_xml/"
    #xmlfolderpath = "./../UnderwaterPhotography/xml/"
    imgfilepath = "./../FishDB_images_png/"
    #imgfilepath = "./../UnderwaterPhotography/nagisa_park/"


    xmlfiles = [ x.split(".")[0] for x in sorted(os.listdir(xmlfolderpath)) if x!=".DS_Store"]
    imgfiles = [ x.split(".")[0] for x in sorted(os.listdir(imgfilepath)) if x!=".DS_Store"]

    #print(xmlfiles)
    #print(imgfiles)
    print("##################### check xml files")
    for xmlfilename in xmlfiles:
        if not xmlfilename in imgfiles:
            print( "Error: "+xmlfilename+".png" +" are not found. Please search it, or delete "+xmlfilename)
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

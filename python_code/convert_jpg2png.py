# -*- coding: utf-8 -*-

import sys
import os
from PIL import Image
import copy
import subprocess

classestxtpath="./../classes.txt"


template="""
<annotation>
	<folder>{foldername}</folder>
	<filename>{filename}</filename>
	<path>{filepath}</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>{width}</width>
		<height>{height}</height>
		<depth>{depth}</depth>
	</size>
	<segmented>0</segmented>
	<object>
		{object}
	</object>
</annotation>
"""

objecttag="""
<name>{name}</name>
<pose>Unspecified</pose>
<truncated>0</truncated>
<difficult>0</difficult>
<bndbox>
    <xmin>{xmin}</xmin>
    <ymin>{ymin}</ymin>
    <xmax>{xmax}</xmax>
    <ymax>{ymax}</ymax>
</bndbox>
"""

xmldict={
"foldername":"",
"filename": "",
"filepath":"/Users/shuichi-fu/Downloads/fish/hugu/hugu1.jpeg",
"width":"",
"height":"",
"depth":"3"
}
objxml={
"name":"",
"xmin":"",
"ymin":"",
"xmax":"",
"ymax":""
}


if __name__ == '__main__':
    with open(classestxtpath) as f:
        classes = f.read()

    classes_dict={ str(i):x for i,x in enumerate(classes.split("\n")) }

    txtfolderpath="./../FishDB_annotations/"
    jpgfilepath="./../FishDB_images/"
    pngfilepath="./../FishDB_images_png/"
    outputpath="./../FishDB_annotations_png_xml/"
    os.makedirs(outputpath,exist_ok=True)
    os.makedirs(pngfilepath,exist_ok=True)

    txtfiles=sorted( os.listdir(txtfolderpath) )
    jpgfiles=sorted( os.listdir(jpgfilepath) )

    for txtfile in txtfiles:
        if txtfile==".DS_Store": continue
        print(txtfile)
        with open(txtfolderpath+txtfile) as f:
            sentences = f.read().split('\n')[:-1]
            #print(sentences,len(sentences))
            sentences=[sentence.strip().split(" ") for sentence in sentences if sentence!=""]
            print(sentences)
        if txtfile.split(".")[0]+".jpg" in jpgfiles:
            jpgfilename=txtfile.split(".")[0]+".jpg"
        else:
             jpgfilename=txtfile.split(".")[0]+".jpeg"
		#
        pngfilename=txtfile.split(".")[0]+".png"
        command = ['ffmpeg', '-y', '-i',jpgfilepath+jpgfilename,pngfilepath+pngfilename]
        #subprocess.call('ffmpeg -y -i {0} {1}'.format(jpgfilepath+jpgfilename,pngfilepath+pngfilename))
        subprocess.call(command)
        
        try:
            im = Image.open(pngfilepath+pngfilename)
            print(im.size)
            img_width=int(im.size[0])
            img_height=int(im.size[1])
            depth=3
        except:
            print("cloud not open "+txtfolderpath+pngfilename)
            raise()
        # ここからtxtの一つ一つのエリアを解読
        objxmls=""
        for sentence in sentences:
            sentence=[float(x) for x in sentence]
            objxml=dict()
            objxml["name"]=classes_dict[str(int(sentence[0]))]
            objxml["xmin"]=int(img_width*sentence[1]-img_width*sentence[3]/2)
            objxml["xmax"]=int(img_width*sentence[1]+img_width*sentence[3]/2)
            objxml["ymin"]=int(img_height*sentence[2]-img_height*sentence[4]/2)
            objxml["ymax"]=int(img_height*sentence[2]+img_height*sentence[4]/2)
            print(objxmls)
            objxmls+=(objecttag.format(**objxml))

        template_xmls={"object":objxmls,"foldername":outputpath,
                       "filename":pngfilename,"filepath":pngfilepath+pngfilename,
                       "width":img_width,"height":img_height,"depth":depth}
        #
        with open(outputpath+txtfile.split(".")[0]+".xml",mode='w') as f:
            f.write(template.format(**template_xmls))
        #print(template.format(**template_xmls))

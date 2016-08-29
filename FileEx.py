#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        FileEx
# Purpose:
#
# Author:      Yi.Qiu
#
# Created:     29/08/2016
# Copyright:   (c) Yi.Qiu 2016
#-------------------------------------------------------------------------------

import os
import glob
import shutil
import tkinter.filedialog
import datetime

values = dict()

def load_list_file(list_file):
    """ load the file list script """
    with open(list_file, mode="r") as f:
        while True:
            data = f.readline().strip()
            if data == "":
                break            
            
            # find the files recursively
            if os.path.split(data)[0] == "**":
                values["tgt_files"].extend(glob.glob(data, recursive=True))
            else:
                # absolute path                
                if os.path.isabs(data):
                    try:
                        data = os.path.relpath(data, values["src_dir"])
                    except ValueError:
                        print("ERROR: Maybe " + data + " is not in the same disk as " +\
                              values["src_dir"])
                        continue
                    
                if os.path.exists(os.path.join(values["src_dir"], data)):
                    values["tgt_files"].append(data)
                else:
                    print("file " + data + " not exists!")
    print(values["tgt_files"])


def mkdir_and_copy(path):
    """ make dir and copy the files """
    dir_set = values["dir_set"]
    dirs = []
    [pname, fname] = os.path.split(path)
    while (pname != "") and (pname not in dir_set):
        dir_set.add(pname)
        dirs.insert(0, pname)
        pname = os.path.split(pname)[0]
        
    while len(dirs) > 0:
        if not os.path.exists(os.path.join(values["dir_root"], dirs[0])):
            os.mkdir(os.path.join(values["dir_root"], dirs.pop(0)))
        else:
            dirs.pop(0)
    if (os.path.isfile( path)):
        shutil.copyfile(path, os.path.join(values["dir_root"], path))
    elif (os.path.isdir(path)):
        shutil.copytree(path, os.path.join(values["dir_root"], path))        
        
    print(path + " --> " + os.path.join(values["dir_root"], path))    

def produce_dir_name(src_dir):
    """ produce the dirname upon the datetime """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return (src_dir + "_" + now)

def init():
    """ initialization """
    # pop a dialog to select the directory of project and target list file
    root = tkinter.Tk()
    # select original directory
    values["src_dir"] = tkinter.filedialog.askdirectory()
    if (not os.path.isdir(values["src_dir"])):
        exit()
    else:
        # change the current dir
        os.chdir(values["src_dir"])
        
    # open the list file
    values["list_file"] = tkinter.filedialog.askopenfilename()
    if (not os.path.isfile(values["list_file"])):
        exit()
    
    root.destroy()

    #set dir name
    values["dir_root"] = produce_dir_name(values["src_dir"])
    #init tgt_files and dir_set
    values["tgt_files"] = []
    values["dir_set"] = set()    
    
    if os.path.exists(values["list_file"]):
        #load the list file script
        load_list_file(values["list_file"])
    else:
        print(values["list_file"] + " not " + "exists!!!")
        exit()
        
    # make new dir to contain the file afer extracted    
    if os.path.exists(values["dir_root"]):
        shutil.rmtree(values["dir_root"])
    os.mkdir(values["dir_root"])


if __name__ == "__main__" :
    init()

    for tf in values["tgt_files"] :
        #mkdir and copy the file        
        mkdir_and_copy(tf)

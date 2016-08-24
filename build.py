#!/usr/bin/env python

import os
import glob
import shutil
from subprocess import Popen, PIPE

bad = ['.git']

def get_dirs(d):
    return filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d))

def recurse(d):
    l = []
    dirs = get_dirs(d)
    for subdir in dirs:
        full = os.path.join(d, subdir)
        if full[2:] not in bad:
            l.append(full)
            l.extend(recurse(d=full))
    return l

initpath = os.path.dirname(os.path.realpath(__file__))

def recursive_make(paths, makefile):
    r = [os.path.abspath(p) for p in paths]
    for directory in r:
        os.chdir(directory)
        print(directory)
        p = Popen('make -f ' + makefile, shell=True, stdout=PIPE, stderr=PIPE)
        (out, err) = p.communicate()
        print(out)

# Recursive make for .md -> .pdf
os.chdir(initpath)
rec = recurse(d='cold-calling/')
rec.append('cold-calling/')
recursive_make(rec, os.path.abspath('_build/Makefile'))
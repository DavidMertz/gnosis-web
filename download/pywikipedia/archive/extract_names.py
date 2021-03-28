"""
Script to extract all wiki page names a certain HTML file points to

The output can be used as input to some robot that takes a list of pages as input.

This script takes a single file name argument, the file should be a HTML file
as captured from one of the wikipedia servers.
"""
#
# (C) Rob W.W. Hooft, 2003
#
# Distributed under the terms of the MIT license.
#
__version__='$Id: extract_names.py,v 1.1 2006/01/16 20:49:19 wikipedian Exp $'
#
import sys,re
R=re.compile('/wiki/(.*?)" *')
fn=sys.argv[1]
f=open(fn)
text=f.read()
f.close()
for hit in R.findall(text):
    print hit

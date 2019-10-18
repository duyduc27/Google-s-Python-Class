#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
# import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_exercise_paths(dir):
  """Get path of exercises from a directory
  Input: a directory
  Output: a list contains paths 
  """

  filenames = os.listdir(dir)
  lis = [] # initial list
  for filename in filenames:
    if ".txt" in filename or ".jpg" in filename:
      lis.append(os.path.abspath(os.path.join(dir, filename)))
  return lis

def get_special_paths(dir):
  """Print one absolute path per line"""
  lis = get_exercise_paths(dir)
  for path in lis:
    print(path)

def copy_to(paths, dir):
  """do not print anything and 
  instead copy the files to the given directory"""
  paths = get_exercise_paths(paths)
  for path in paths:
    shutil.copy(path, dir)

def zip_to(paths, zipname):
  """ Create a zipfile containing the files
  zipname: file name
  paths: list path of files
  """
  paths = get_exercise_paths(paths)
  zippath = os.path.join("C:/Users/Administrator/Downloads/", zipname)
  
  cmd = '7z a '+ zippath +".7z " + ' '.join(paths) # 7zip command
  os.system(cmd)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  # for dirname in args:
  #   paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(args[0], todir)
  elif tozip:
    zip_to(args[0], tozip)

  
if __name__ == "__main__":
  main()

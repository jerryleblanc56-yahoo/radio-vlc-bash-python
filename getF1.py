# get a random file from structure 
# http://stackoverflow.com/questions/6411811/randomly-selecting-a-file-from-a-tree-of-directories-in-a-completely-fair-manner 
#
import os
import random
files = [os.path.join(path, filename)
         for path, dirs, files in os.walk("/mnt/usb1/music/iTunes")
         for filename in files
         if filename.endswith(".m4a")]
print( random.choice(files) )

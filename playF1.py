# get a random file from structure 
# http://stackoverflow.com/questions/6411811/randomly-selecting-a-file-from-a-tree-of-directories-in-a-completely-fair-manner 
#
import os
import subprocess
import random
apath = "mnt/usb1/music/iTunes"
files = [os.path.join(path, filename)
         for path, dirs, files in os.walk("/mnt/usb1/music/iTunes")
         for filename in files
         if filename.endswith(".m4a")]
afile = random.choice(files)
print( afile )
command = "sudo -u pi cvlc --audio \'file:" + str(afile) + "\'"
print( command )
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#output = process.communicate()[0]
#print output
exit(0)

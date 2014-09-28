# get a random file from structure 
# http://stackoverflow.com/questions/6411811/randomly-selecting-a-file-from-a-tree-of-directories-in-a-completely-fair-manner 
#
#
files = [os.path.join(path, filename)
         for path, dirs, files in os.walk(dir)
         for filename in files
         if filename.endswith(".m4u")]
return random.choice(files)

# Recursively rename files to their parent folder’s name
# Source: http://www.salemmarafi.com/code/recursively-rename-files-to-their-parent-folders-name/

import os

# source: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


'''

 Function: renameFiles
 Parameters: 
    @path: The path to the folder you want to traverse
    @depth: How deep you want to traverse the folder. Defaults to 99 levels. 
    
'''


def renameFiles(path, depth=99):
    # Once we hit depth, return
    if depth < 0: return

    # Make sure that a path was supplied and it is not a symbolic link
    if os.path.isdir(path) and not os.path.islink(path):
        print("Valid path\n")
        # We will use a counter to append to the end of the file name
        ind = 1

        # Loop through each file in the start directory and create a fullpath
        for file in os.listdir(path):
            fullpath = path + os.path.sep + file
            print('Working on: {}'.format(file))

            # Again we don't want to follow symbolic links
            if not os.path.islink(fullpath):

                # If it is a directory, recursively call this function
                # giving that path and reducing the depth.
                if os.path.isdir(fullpath):
                    renameFiles(fullpath, depth - 1)
                else:
                    # Find the extension (if available) and rebuild file name
                    # using the directory, new base filename, index and the old extension.
                    extension = os.path.splitext(fullpath)[1]

                    # We are only interested in changing names of images.
                    # So if there is a non-image file in there, we want to ignore it
                    if extension in ('.jpg', '.jpeg', '.png', '.gif'):

                        # We want to make sure that we change the directory we are in
                        # If you do not do this, you will not get to the subdirectory names
                        os.chdir(path)

                        # Lets get the full path of the files in question
                        dir_path = os.path.basename(os.path.dirname(os.path.realpath(file)))

                        # We then define the name of the new path in order
                        # The full path, then a dash, then 2 digits, then the extension
                        newpath = os.path.dirname(fullpath).replace(" ", "_") + os.path.sep + dir_path.replace(" ", "_") \
                                  + '-' + "{0:0=2d}".format(ind) + extension

                        # If a file exists in the new path we defined, we probably do not want
                        # to over write it. So we will redefine the new path until we get a unique name
                        while os.path.exists(newpath):
                            ind += 1
                            #newpath = os.path.dirname(fullpath) + os.path.sep + dir_path \
                            newpath = os.path.dirname(fullpath).replace(" ", "_") + os.path.sep + dir_path.replace(" ", "_") \
                                      + '-' + "{0:0=2d}".format(ind) + extension

                        # We rename the file and increment the sequence by one.
                        os.rename(fullpath, newpath)
                        ind += 1
        print ("Folder: "+os.path.dirname(os.path.realpath(path))+" had {} items\n".format(ind))
    return


path = input("Enter path of top parent folder: ")
renameFiles(path)
list_files(path)
print("Pictures renamed successfully")

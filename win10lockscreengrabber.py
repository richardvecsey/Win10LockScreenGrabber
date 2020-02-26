# -*- coding: utf-8 -*-
"""
Win10LockScreenGrabber
------------------------------------------------------------------------------
This program copy all Windows 10's Spotlight Lock Screen images to a specified
destination folder. 

------------------------------------------------------------------------------
Variables:
    folder_wallpapers   (string)    Full path to the destination folder
                                    default: None, that means destination
                                    folder is USERPROFILE\Pictures\LockScreens
    delete_sources      (boolean)   Whether delete the files from source folder
                                    or not
                                    default: False

------------------------------------------------------------------------------
MIT License

Copyright (c) 2020 Richárd Ádám Vécsey Dr.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = 'Richárd Ádám Vécsey Dr.'
__copyright__ = "Copyright 2020, Win10LockScreenGrabber Project"
__credits__ = ['Richárd Ádám Vécsey Dr.']
__license__ = 'MIT'
__version__ = '1.1'
__status__ = 'Beta'



# import section
# standard library
from os import environ, listdir, mkdir, path
from shutil import copy2
from platform import platform

# Set this value to the path of your folder that contains wallpapers.
# Whether None, images copy to the default image folder.
# Eg: folder_wallpapers ='C:\MyFolder\Wallpapers'
folder_wallpapers = None

# Set this variable True to delete the files from source folder
delete_sources = False

# Collect environments data
envdata = environ
homedrive = envdata['HOMEDRIVE']
localappdata = envdata['LOCALAPPDATA']
userprofile = envdata['USERPROFILE']

# Path to 'Assets' folder.
# It contains the images.
folder_asset = '{}\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'.format(localappdata)
folder_destination_default = '{}\Pictures\LockScreens'.format(userprofile)

def main():
    # Setup the final destination folder
    if folder_wallpapers == None:
        folder_destination = str(folder_destination_default)
    else:
        folder_destination = str(folder_wallpapers)
    
    # Check existion of destination directory, create it if not exist
    if not path.isdir(folder_destination):
        mkdir(folder_destination)
    
    # Collect images and copy them
    for filename in listdir(folder_asset):    
        # Create full source path
        source_path = path.join(folder_asset, filename)
        # Add .jpg extension to the file name
        jpegified = filename + '.jpg'
        # Create full destination path
        destination_path = path.join(folder_destination, jpegified)
        # Copy
        # It copies not just file but metadata
        copy2(source_path, destination_path)
        # Delete images if delete_sources is True
        if delete_sources:
            os.remove(source_path)
        

       
if __name__ == "__main__":
    # Check Operation System type end version
    # platfrom.platfrom() is better than sys.platfrom() since last returns only
    # with the type of platform ('win32' as windows) without version number
    if platform()[0:10] == 'Windows-10':
        print('Program running...')
        main()
        print('Program finished')
    else:
        # Handling OS mismatch error. This program runs only on Win10.
        raise OSError('This program is for Windows 10 Operation System')
else:
    # Handling error when not using as a standalone program
    raise RuntimeError('This is a standalone program, not a script.')
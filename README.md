# Win10LockScreenGrabber

This program copy all Windows 10's Spotlight Lock Screen images to a specified
destination folder.

# Version:
1.3

# Variables:
    delete_destination  (boolean)   Whether delete the non wallpaper-sized 
                                    images from source folder or not
                                    default: False
    delete_sources      (boolean)   Whether delete the files from source folder
                                    or not
                                    default: False    
    folder_wallpapers   (string)    Full path to the destination folder
                                    default: None, that means destination
                                    folder is USERPROFILE\Pictures\LockScreens
    height              (int)       Minimum height of copyable image
                                    Smaller image won't be copy to the
                                    destination folder
    width               (int)       Minimum width of copyable image
                                    Smaller image won't be copy to the
                                    destination folder                                    

# Licence
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

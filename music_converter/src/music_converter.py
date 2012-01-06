#!/bin/env python

"""
NB: a very important message before we begin:

    This was designed to work on POSIX systems, if you want it to run on windows
    rewrite it yourself.

music_converter searches through a directory given on the commandline for files
that have extentions for known music formats.

Each of these files are assigned to a list for their music format which is
searched for duplicates which the user is prompted as to delete the duplicates
or not.

for the rest of the files that are NOT in mp3 format the files are converted to
mp3 format.

this will (eventually) be threaded with four threads running concurrently.

NOTE: I would like to convert to Ogg format but given that the majority of files
in my collection are mp3 and are known to work well with my media player (synology)
all other formats will be converted to mp3.
"""

import os
import sys

# Music extention definitions
convert_format = 'mp3'
good_formats = ['mp3','ogg']
bad_formats = ['wav','wma','m4p','m4a','mp2']

# Random file cruft to remove
cruft_files = ['m3u','log','m4v','md5','nfo','part','plist','pls','rtf','sfv','txt','url','xml']

# Music video files to move / ensure are in correct location
video_files = ['mov','mpeg','avi','mpg','wmv']

# We will hold all found files in lists to process once we have finished enumerating the files
cruft_file_list = []
bad_format_list = []
video_file_list = []


def process_bad_formats():
    file_type_wav = []
    file_type_wma = []
    file_type_m4p = []
    file_type_m4a = []
    file_type_mp2 = []
    pass

def process_video_files():
    pass

def main():
    print "Move the PDF files in chinesepod else where"
    if music_root == '':
        print "Music root directory is undefined, please specify it"
        sys.exit(1)
    else:
        pass
    # go through all the directories
    # for each file add it to the correct list
    # if its good_format just discard it.
    # if its not in any of the lists print it out as a warning
    #
    # for the files in cruft remove them indescrimately
    #
    # for the files in video, check they are in the video directory FIXME: Define the DIR
    # if they are in the directly discard, if they are not move them there.
    #
    # for each of the files in bad formats create a new list for each file type

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: %s MUSIC_ROOT_PATH\n"
                         % (os.path.basename(sys.argv[0])))
        sys.exit(1)
    else:
        # Define the root of the music directory here
        music_root = sys.argv[1]
        # define movie root
        # FIXME: user could add or not add "/" on the music root directory 
        movie_root = music_root + "videos"

        main()



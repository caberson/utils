# -*- coding: utf-8 -*-
import os
import glob
import shutil

import eyed3

from os.path import basename



# print mp3_files

def cleanup_artist(input):
    return input.replace(u'/', ',').replace(u'、', ',').replace(u'/', ',')

def cleanup_title(input):
    return input.replace('/', ' ')

def rename(file):
    # print file
    test_mode = True
    test_mode = False

    try:
        mp3 = eyed3.load(file)
        tag = mp3.tag
        if not tag.artist or not tag.title:
            # print "Nothing"
            return
    except:
        return

    new_file_name = u"{} - {}.mp3".format(
        cleanup_artist(tag.artist),
        cleanup_title(tag.title)
    )
    # print new_file_name

    file_base_name = unicode(basename(file), 'utf-8')
    if file_base_name == new_file_name:
        # print u"Not renamed:" + new_file_name
        return

    # print "Rename"
    new_file = os.path.join(
        os.path.dirname(file),
        new_file_name
    )
    print file_base_name
    print u"\t>> " + new_file

    # print new_file
    #try:
    if not test_mode:
        shutil.move(file, new_file)
    #except:

    #    pass


# audiofile = eyed3.load(u"02 - 忘不了.mp3")
# print audiofile.tag
"""
audiofile.tag.artist = u"Nobunny"
audiofile.tag.album = u"Love Visions"
audiofile.tag.album_artist = u"Various Artists"
audiofile.tag.title = u"I Am a Girlfriend"
audiofile.tag.track_num = 4

audiofile.tag.save()
"""
mp3_files_dir = '/Volumes/music'
mp3_files_dir = '/Volumes/cc/music/_reviewed/_chinese_all_others_to_check'
# mp3_files_dir = '/Users/cc/Projects/mp3-rename'
mp3_files = glob.glob(mp3_files_dir + '/*.mp3')
# print mp3_files
i = 0
for mp3_file in mp3_files:
    # i = i + 1
    rename(mp3_file)
    if i > 10:
        break
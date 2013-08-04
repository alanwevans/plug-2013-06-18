#!/bin/bash

# Generate a directory tree of thumbnails for a directory tree of images using parallel
# Note: There was no need for a separate script but a separate shell is still forked.

# Sample runtime on my laptop on SD Card
#  $ time sh 04-thumbs-parallel.sh
#  
#  real	0m33.813s
#  user	1m25.654s
#  sys	0m6.941s

find freestockphotos.com/ -iname \*.jpeg -o -iname \*.jpg | parallel --gnu 'mkdir -p thumbs/{//} 2>/dev/null ; convert {} -resize 100x100 thumbs/{//}/{/}'

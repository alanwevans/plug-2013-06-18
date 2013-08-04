#!/bin/bash

# Generate a directory tree of thumbnails for a directory tree of images using xargs
# Note: I've used a separate script to do the heavy lifting...

# Sample runtime on my laptop on SD Card
#  $ time sh 03-thumbs-xargs.sh
#
#  real	1m9.423s
#  user	1m19.790s
#  sys	0m8.241s

find freestockphotos.com/ -iname \*.jpeg -o -iname \*.jpg | xargs -l sh thumb.sh

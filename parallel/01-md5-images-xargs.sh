#!/bin/sh

# Generate md5sums of a directory tree full of images with xargs

find freestockphotos.com/ -iname \*.jpeg -o -iname \*.jpg | xargs md5sum 

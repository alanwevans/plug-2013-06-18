#!/bin/sh

# Generate md5sums of a directory tree full of images with parallel

find freestockphotos.com/ -iname \*.jpeg -o -iname \*.jpg | parallel --gnu md5sum

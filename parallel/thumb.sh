#!/bin/bash

THUMBDIR=thumbs/$(dirname $1)
mkdir -p 2>/dev/null $THUMBDIR
convert $1 -resize 100x100 $THUMBDIR/$(basename $1)


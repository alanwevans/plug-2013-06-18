plug-2013-06-18
===============

Presentation notes and examples as presented to PLUG on 2013-06-18

SYNOPSIS
========
GNU Screen and GNU Parallel intro/tips

The files contained herein were presented at a meeting of the Provo Linux
User Group (PLUG) on June 18, 2013.

LICENSE
=======
See ./LICENSE

FILES
=====
screen/	- GNU screen related
screen/ns - helper script
screen/screenrc - my screenrc
screen/OUTLINE - some talking points, probably mostly useful to me... :)

parallel/ - GNU parallel related
parallel/01-md5-images-xargs.sh - md5sum a bunch of images using xargs
parallel/02-md5-images-parallel.sh - md5sum a bunch of files using parallel
parallel/03-thumbs-xargs.sh - generate thumbnails using xargs
parallel/04-thumbs-parallel.sh - generate thumbnails using parallel
parallel/05-frob.sh - run frobnicate.py to simulate some long running jobs

parallel/getimages.sh - slurp a bunch of images from freestockphotos.com
parallel/thumb.sh - helper script for 03-thumbs-xargs.sh
parallel/loremwords.txt - some random input for 05-frob.sh of word:scale pairs
parallel/frobnicate.py - a script that pretends to do some work
parallel/jobs - used by 05-frob.sh
parallel/OUTLINE - some talking points, probably most useful to me... :)

parallel/freestockphotos.com/ - created by getimages.sh if you use it
parallel/thumbs/ - created by examples 03/04 if you use them

LINKS
=====
GNU Screen
http://www.gnu.org/software/screen/

GNU Parallel
http://www.gnu.org/software/parallel/

Lorem Ipsum generated by
http://www.lipsum.com/

AUTHOR
======
Alan Evans <alanwevans@gmail.com>

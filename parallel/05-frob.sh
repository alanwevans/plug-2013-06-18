#!/bin/sh

# Run 'frobnicate.py' with 1000 words and scales in 'loremwords.txt'
# as a mock long running job with lots of input

# Usage: ./05-frob.sh [options]
#   Where [options] is a list of additional arguments for parallel
#   Hint, try:
#     --joblog joblog.log
#     --ungroup (do not use in combination w/ --joblog, there's a bug...)
#     --progress

cat loremwords.txt | parallel --gnu --jobs ./jobs $* --colsep ':' 'python frobnicate.py {1} 10 {2}'

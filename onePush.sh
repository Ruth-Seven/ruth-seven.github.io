#!/bin/bash

#deploy the html files to github.
hexo g -d

#deploy the other file to github.
echo $*
git add *
git commit -m "$*"
git push

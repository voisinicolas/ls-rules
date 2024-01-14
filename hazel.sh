#!/usr/bin/env zsh

PYTHON=`which python3`
${PYTHON} ~/.config/little-snitch/importer.py $1

message="auto-commit from $USER@$(hostname -s) on $(date)"
GIT=`which git`
REPO_DIR=~/.config/little-snitch
cd ${REPO_DIR}
${GIT} add --all .
${GIT} commit -m "$message"

gitPush=$(${GIT} push -vvv git@github.com:voisinicolas/ls-rules.git master 2>&1)
echo "$gitPush"

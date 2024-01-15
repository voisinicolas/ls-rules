#!/usr/bin/env bash

LS_DIR="/Users/nvz/.config/little-snitch"
PYTHON=$(which python3)
${PYTHON} "$LS_DIR/lsrules_cleaner.py" "$LS_DIR/ls_rules/$1"

message="auto-commit from $USER@$(hostname -s) on $(date)"
GIT=$(which git)
cd ${LS_DIR}
${GIT} add .
${GIT} commit -m "$message"

gitPush=$(${GIT} push -vvv git@github.com:voisinicolas/ls-rules.git main 2>&1)
echo "$gitPush"

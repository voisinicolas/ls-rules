#!/usr/bin/env bash

REPO_DIR="/Users/nvz/.config/little-snitch"
SCRIPT="importer.py"
PYTHON=$(which python3)
${PYTHON} "$REPO_DIR/$SCRIPT" $1

message="auto-commit from $USER@$(hostname -s) on $(date)"
GIT=$(which git)
cd ${REPO_DIR}
${GIT} add --all .
${GIT} commit -m "$message"

gitPush=$(${GIT} push -vvv git@github.com:voisinicolas/ls-rules.git main 2>&1)
echo "$gitPush"

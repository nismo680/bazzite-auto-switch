#!/usr/bin/env bash

set -e

read -rp "Commit-Nachricht: " msg

git add .
git commit -m "$msg"
git push

echo "Push erfolgreich."

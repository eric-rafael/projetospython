#!/data/data/com.termux/files/usr/bin/bash

echo "commit: "
read commit

git add -A
git commit -m "$commit"
git push

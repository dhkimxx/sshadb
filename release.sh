#!/bin/bash
# Usage: ./release.sh 0.1.0
# Example: ./release.sh 0.1.0

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

VERSION=$1
TAG="v$VERSION"

git add .
git commit -m "chore(release): $TAG"
git tag -a "$TAG" -m "Release $TAG"
git push origin main
git push origin "$TAG"

python3 -m pip install --upgrade build twine

rm -rf dist/*

python3 -m build

twine check dist/*

twine upload dist/*

echo "Release $TAG completed!"

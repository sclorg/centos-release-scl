#!/bin/sh

if [ $# -ne 1 ] ; then
    echo "Usage: `basename $0` --source|--binary"
    exit 1
fi

NAME=centos-release-scl
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VERSION=`cat $SCRIPT_DIR/../VERSION`

RPMBUILD_DIR=~/rpmbuild

mkdir -p "${RPMBUILD_DIR}/SOURCES/" "${RPMBUILD_DIR}/SPECS/"
cp -f $NAME README.md LICENSE "${RPMBUILD_DIR}/SOURCES/"
cp -f $NAME.spec "${RPMBUILD_DIR}/SPECS/"

if [ $1 == "--source" ] ; then
    echo "rpmbuild -bs ${RPMBUILD_DIR}/SPECS/$NAME.spec"
    rpmbuild -bs "${RPMBUILD_DIR}/SPECS/$NAME.spec"
elif [ $1 == "--binary" ] ; then
    echo "rpmbuild -bb ${RPMBUILD_DIR}/SPECS/$NAME.spec"
    rpmbuild -bb "${RPMBUILD_DIR}/SPECS/$NAME.spec"
fi

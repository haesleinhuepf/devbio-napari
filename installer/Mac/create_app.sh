#!/bin/bash
# This script is used to create the devbio-napari.app bundle during installation.

if [ "${INSTALLER_TYPE}" == "PKG" ]; then
    app_dir=$(dirname "$(dirname "$(dirname "$(dirname "${PREFIX}")")")")
    cd "${app_dir}" || exit
    tar -xzf "${PREFIX}/devbio-napari.app.tar.gz"
fi

# cleanup
rm -rf "${PREFIX}/devbio-napari.app.tar.gz"
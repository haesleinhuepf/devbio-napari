# devbio-napari

[![License](https://img.shields.io/pypi/l/devbio.svg?color=green)](https://github.com/haesleinhuepf/devbio/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/devbio.svg?color=green)](https://pypi.org/project/devbio)
[![Python Version](https://img.shields.io/pypi/pyversions/devbio.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/devbio/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/devbio/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/devbio/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/devbio)

A collection of napari plugins useful for studying developmental biology consisting of
* [aicsimageio](https://github.com/AllenCellModeling/napari-aicsimageio)
* [Cellpose](https://github.com/MouseLand/cellpose-napari)
* [StarDist](https://github.com/stardist/stardist-napari)
* [clEsperanto](https://clesperanto.github.io/napari_pyclesperanto_assistant/)
* [scikit-image regionprops](https://github.com/haesleinhuepf/napari-skimage-regionprops)
* [animation](https://github.com/napari/napari-animation)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `devbio-napari` via [pip]:

    pip install 'napari[all]'
    pip install devbio-napari

Windows users should install [pyopencl](https://documen.tician.de/pyopencl/) via conda in **advance**:

    conda install -c conda-forge pyopencl

## Contributing

Contributions are very welcome. If you want to suggest a new napari plugin to become part of this distribution, please make sure it interoperates nicely with the other plugins. For example, if the plugin you suggest provided cell segmentation algorithms, please check if the resulting segmented cells can be analysed using napari-skimage-regionprops.

## License

Distributed under the terms of the [BSD-3] license,
"devbio-napari" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/haesleinhuepf/devbio/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

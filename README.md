# devbio-napari

[![License](https://img.shields.io/pypi/l/devbio-napari.svg?color=green)](https://github.com/haesleinhuepf/devbio-napari/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/devbio-napari.svg?color=green)](https://pypi.org/project/devbio-napari)
[![Python Version](https://img.shields.io/pypi/pyversions/devbio-napari.svg?color=green)](https://python.org)

A collection of napari plugins useful for studying developmental biology.

* File input/output plugins
  * [aicsimageio](https://www.napari-hub.org/plugins/napari-aicsimageio)
  * [napari-itk-io](https://www.napari-hub.org/plugins/napari-itk-io) 
  * [ome-zarr](https://www.napari-hub.org/plugins/napari-ome-zarr)
* Image exploration and visualization tools
  * [animation](https://www.napari-hub.org/plugins/napari-animation)
* Image segmentation plugins
  * [Cellpose](https://www.napari-hub.org/plugins/cellpose-napari)
  * [StarDist](https://www.napari-hub.org/plugins/stardist-napari)
  * [oclrfc](https://www.napari-hub.org/plugins/napari-oclrfc)
  * [pyclesperanto-assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant)
  * [Manual split & merge labels](https://www.napari-hub.org/plugins/napari-manual-split-and-merge-labels)
* Image registration
  * [PlatyMatch](https://www.napari-hub.org/plugins/PlatyMatch)
* Quantitative measurements
  * [scikit-image regionprops](https://www.napari-hub.org/plugins/napari-skimage-regionprops)
  * [plot-profile](https://www.napari-hub.org/plugins/napari-plot-profile)
* Utilities
  * [brightness-contrast](https://www.napari-hub.org/plugins/napari-brightness-contrast)
  * [plugin-search](https://www.napari-hub.org/plugins/napari-plugin-search)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `devbio-napari` via [pip]:

    conda install -c conda-forge pyopencl jupyter notebook
    pip install devbio-napari

Windows users should install [pyopencl](https://documen.tician.de/pyopencl/) via conda **in advance**:

    conda install -c conda-forge pyopencl

[See also](https://github.com/clEsperanto/napari_pyclesperanto_assistant#Installation).

## Contributing

Contributions are very welcome. 
If you want to [suggest a new napari plugin](https://github.com/haesleinhuepf/devbio-napari/pulls) to become part of this distribution, please make sure it interoperates nicely with the other plugins. 
For example, if the plugin you suggest provided cell segmentation algorithms, please check if the resulting segmented cells can be analysed using napari-skimage-regionprops.
Furthermore, please make sure the README of the plugin you are proposing comes with user documentation, e.g. a step-by-step guide with screenshots explaining what users can do with the plugin and how to use it. 
It is recommended to provide example data as well so that end-users can try out the plugin under conditions it was developed for.

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

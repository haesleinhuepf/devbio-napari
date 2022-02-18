# devbio-napari

[![License](https://img.shields.io/pypi/l/devbio-napari.svg?color=green)](https://github.com/haesleinhuepf/devbio-napari/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/devbio-napari.svg?color=green)](https://pypi.org/project/devbio-napari)
[![Python Version](https://img.shields.io/pypi/pyversions/devbio-napari.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/devbio-napari/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-plot-profile/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/devbio-napari/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/devbio-napari)
[![Development Status](https://img.shields.io/pypi/status/devbio-napari.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/devbio-napari)](https://napari-hub.org/plugins/devbio-napari)


A bundle of napari plugins useful for 3D+t image processing and analysis for studying developmental biology.

* File input/output plugins
  * [aicsimageio](https://www.napari-hub.org/plugins/napari-aicsimageio)
  * [napari-itk-io](https://www.napari-hub.org/plugins/napari-itk-io) 
  * [ome-zarr](https://www.napari-hub.org/plugins/napari-ome-zarr)
* Image exploration and visualization tools
  * [animation](https://www.napari-hub.org/plugins/napari-animation)
  * [curtain](https://www.napari-hub.org/plugins/napari-curtain)
  * [napari-3d-ortho-viewer](https://www.napari-hub.org/plugins/napari-3d-ortho-viewer)
  * [folder-browser](https://www.napari-hub.org/plugins/napari-folder-browser)
* Image processing 
  * [RedLionfish](https://www.napari-hub.org/plugins/RedLionfish)
  * [pyclesperanto-assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant)
  * [simpleitk-image-processing](https://www.napari-hub.org/plugins/napari-simpleitk-image-processing)
* Image segmentation plugins
  * [cellpose](https://www.napari-hub.org/plugins/napari-cellpose)
  * [accelerated-pixel-and-object-classification](https://www.napari-hub.org/plugins/napari-accelerated-pixel-and-object-classification)
  * [pyclesperanto-assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant)
  * [segment-blobs-and-things-with-membranes](https://www.napari-hub.org/plugins/napari-segment-blobs-and-things-with-membranes)
  * [simpleitk-image-processing](https://www.napari-hub.org/plugins/napari-simpleitk-image-processing)
* Image registration
  * [PlatyMatch](https://www.napari-hub.org/plugins/PlatyMatch)
* Quantitative measurements
  * [scikit-image regionprops](https://www.napari-hub.org/plugins/napari-skimage-regionprops)
  * [plot-profile](https://www.napari-hub.org/plugins/napari-plot-profile)
  * [clusters-plotter](https://www.napari-hub.org/plugins/napari-clusters-plotter)
  * [pyclesperanto-assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant)
  * [simpleitk-image-processing](https://www.napari-hub.org/plugins/napari-simpleitk-image-processing)
* Utilities
  * [brightness-contrast](https://www.napari-hub.org/plugins/napari-brightness-contrast)
  * [plugin-search](https://www.napari-hub.org/plugins/napari-plugin-search)
  * [crop](https://www.napari-hub.org/plugins/napari-crop)
  * [tabu](https://www.napari-hub.org/plugins/napari-tabu)
  * [workflow-optimizer](https://www.napari-hub.org/pluginsnapari-workflow-optimizer)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `devbio-napari` via conda and pip. If you have never used conda before, please [read this guide first](https://biapol.github.io/blog/johannes_mueller/anaconda_getting_started/):

    conda create --name devbio-napari-env python=3.9
    conda activate devbio-napari-env
    conda install -c conda-forge pyopencl==2021.2.6 hdbscan
    pip install devbio-napari

Mac-users please also install this:

    conda install ocl_icd_wrapper_apple

Afterwards, run this command from the command line

```
devbio-napari
```

This window should open. It shows the [Assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant) graphical user interface. 
Read more about how to use it in its [documentation](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant).

![img.png](https://github.com/haesleinhuepf/devbio-napari/raw/master/docs/screenshot.png)

## Troubleshooting

In case installation didn't work in the first attempt, you may have to call this command line to reset the napari configuration:

```
napari --reset
```

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

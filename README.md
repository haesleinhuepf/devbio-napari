# devbio-napari

[![License](https://img.shields.io/pypi/l/devbio-napari.svg?color=green)](https://github.com/haesleinhuepf/devbio-napari/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/devbio-napari.svg?color=green)](https://pypi.org/project/devbio-napari)
[![Python Version](https://img.shields.io/pypi/pyversions/devbio-napari.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/devbio-napari/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-plot-profile/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/devbio-napari/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/devbio-napari)
[![Development Status](https://img.shields.io/pypi/status/devbio-napari.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/devbio-napari)](https://napari-hub.org/plugins/devbio-napari)

 
A bundle of napari plugins useful for 3D+t image processing and analysis for studying developmental biology.

* [accelerated-pixel-and-object-classification](https://www.napari-hub.org/plugins/napari-accelerated-pixel-and-object-classification)
  * Instance segmentation
  * Semantic segmentation
  * Object classification
  * Random Forest Classifier training
* [animation](https://www.napari-hub.org/plugins/napari-animation) 
  * Visualization
* [blob-detection](https://www.napari-hub.org/plugins/napari-blob-detection)
  * Detection
* [brightness-contrast](https://www.napari-hub.org/plugins/napari-brightness-contrast)
  * Visualization
* [clusters-plotter](https://www.napari-hub.org/plugins/napari-clusters-plotter)
  * Visualization
  * Plotting
  * Semantic object segmentation
  * Dimensionality reduction
  * Unsupervised machine learning
* [crop](https://www.napari-hub.org/plugins/napari-crop)
  * Transformation
* [curtain](https://www.napari-hub.org/plugins/napari-curtain)
  * Visualization 
* [czifile2](https://www.napari-hub.org/plugins/napari-czifile2)
  * File input/output
* [folder-browser](https://www.napari-hub.org/plugins/napari-folder-browser)
  * File input/output
* [layer-details-display](https://www.napari-hub.org/plugins/napari-layer-details-display)
  * Visualization
* [mouse-controls](https://www.napari-hub.org/plugins/napari-mouse-controls)
  * Interaction
* [PlatyMatch](https://www.napari-hub.org/plugins/PlatyMatch)
  * Image registration
* [plot-profile](https://www.napari-hub.org/plugins/napari-plot-profile)
  * Visualization
  * Quantification
* [plugin-search](https://www.napari-hub.org/plugins/napari-plugin-search)
  * Interaction
* [pyclesperanto-assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant)
  * Filtering
  * Instance segmentation
  * Semantic segmentation
  * Quantification
* [pystackreg](https://www.napari-hub.org/plugins/napari-pystackreg)
  * Image registration
  * Motion correction
* [RedLionfish](https://www.napari-hub.org/plugins/RedLionfish)
  * Deconvolution
  * Processing
* [roi](https://www.napari-hub.org/plugins/napari-roi)
  * Manual segmentation
* [segment-blobs-and-things-with-membranes](https://www.napari-hub.org/plugins/napari-segment-blobs-and-things-with-membranes)
  * Filtering
  * Instance segmentation
  * Semantic segmentation
* [simpleitk-image-processing](https://www.napari-hub.org/plugins/napari-simpleitk-image-processing)
  * Filtering
  * Instance segmentation
  * Semantic segmentation
  * Quantification
* [skimage-regionprops](https://www.napari-hub.org/plugins/napari-skimage-regionprops)
  * Quantification
* [tabu](https://www.napari-hub.org/plugins/napari-tabu)
  * Interaction
* [the-segmentation-game](https://www.napari-hub.org/plugins/the-segmentation-game)
  * Quantification
  * Segmentation quality assurance
* [workflow-inspector](https://www.napari-hub.org/plugins/napari-workflow-inspector)
  * Visualization
* [workflow-optimizer](https://www.napari-hub.org/plugins/napari-workflow-optimizer)
  * Interaction
  * Optimization

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `devbio-napari` via conda/mamba. If you have never used conda before, please [read this guide first](https://biapol.github.io/blog/johannes_mueller/anaconda_getting_started/).  
Start by installing mamba in your base environment:

```
conda install mamba -c conda-forge
```

Afterwards, create an environment using mamba.

```
mamba create --name devbio-napari-env python=3.9 devbio-napari -c conda-forge
```

Afterwards, activate the environment like this:
    
    conda activate devbio-napari-env

Afterwards, run this command from the command line

```
naparia
```

This window should open. It shows the [Assistant](https://www.napari-hub.org/plugins/napari-assistant) graphical user interface. 
Read more about how to use it in its [documentation](https://www.napari-hub.org/plugins/napari-assistant).

![img.png](https://github.com/haesleinhuepf/devbio-napari/raw/master/docs/screenshot.png)

## Troubleshooting: Graphics cards drivers

In case error messages contains "ImportError: DLL load failed while importing cl: The specified procedure could not be found" [see also](https://github.com/clEsperanto/pyclesperanto_prototype/issues/55) or ""clGetPlatformIDs failed: PLATFORM_NOT_FOUND_KHR", please install recent drivers for your graphics card and/or OpenCL device. Select the right driver source depending on your hardware from this list:

* [AMD drivers](https://www.amd.com/en/support)
* [NVidia drivers](https://www.nvidia.com/download/index.aspx)
* [Intel CPU OpenCL drivers](https://www.intel.com/content/www/us/en/developer/articles/tool/opencl-drivers.html#latest_CPU_runtime)
* [Microsoft Windows OpenCL support](https://www.microsoft.com/en-us/p/opencl-and-opengl-compatibility-pack/9nqpsl29bfff)

Sometimes, mac-users need to install this:

    conda install -c conda-forge ocl_icd_wrapper_apple

Sometimes, linux users need to install this:

    conda install -c conda-forge ocl-icd-system


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

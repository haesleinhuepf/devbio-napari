# devbio-napari

[![License](https://img.shields.io/pypi/l/devbio-napari.svg?color=green)](https://github.com/haesleinhuepf/devbio-napari/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/devbio-napari.svg?color=green)](https://pypi.org/project/devbio-napari)
[![Python Version](https://img.shields.io/pypi/pyversions/devbio-napari.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/devbio-napari/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-plot-profile/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/devbio-napari/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/devbio-napari)
[![Development Status](https://img.shields.io/pypi/status/devbio-napari.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/devbio-napari)](https://napari-hub.org/plugins/devbio-napari)


A bundle of napari plugins useful for 3D+t image processing and analysis for studying developmental biology.

<table>

<tr><td>Plugin</td>
<td>Exploration</td>
<td>Processing</td>
<td>Segmentation</td>
<td>Measurements</td>
<td>Classification</td>
<td>Visualization</td>
<td>Other</td></tr>

<tr><td>  

[3d-ortho-viewer](https://www.napari-hub.org/plugins/napari-3d-ortho-viewer)

</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td></td></tr>

<tr><td>  

[accelerated-pixel-and-object-classification](https://www.napari-hub.org/plugins/napari-accelerated-pixel-and-object-classification)

</td>
<td> </td>
<td> </td>
<td>x</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td></tr>


<tr><td>  

[animation](https://www.napari-hub.org/plugins/napari-animation)

</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td></td></tr>

<tr><td>  

[blob-detection](https://www.napari-hub.org/plugins/napari-blob-detection)

</td>
<td> </td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td></td></tr>



<tr><td>  

[brightness-contrast](https://www.napari-hub.org/plugins/napari-brightness-contrast)

</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td> </td></tr>



<tr><td>  

[cellpose](https://www.napari-hub.org/plugins/cellpose-napari)

</td>
<td> </td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td></tr>


<tr><td>  

[clusters-plotter](https://www.napari-hub.org/plugins/napari-clusters-plotter)

</td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td>x</td>
<td> </td>
<td> </td></tr>


<tr><td>  

[crop](https://www.napari-hub.org/plugins/napari-crop)

</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td></tr>


<tr><td>  

[curtain](https://www.napari-hub.org/plugins/napari-curtain)

</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td></td></tr>


<tr><td>  

[czifile2](https://www.napari-hub.org/plugins/napari-czifile2)

</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Read CZI files</td></tr>



<tr><td>  

[folder-browser](https://www.napari-hub.org/plugins/napari-folder-browser)

</td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td></tr>


<tr><td>  

[layer-details-display](https://www.napari-hub.org/plugins/napari-layer-details-display)

</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>List layer details</td></tr>

<tr><td>

[mouse-controls](https://www.napari-hub.org/plugins/napari-mouse-controls)

</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Pan through stacks, zoom by dragging</td></tr>


<tr><td>  

[PlatyMatch](https://www.napari-hub.org/plugins/PlatyMatch)

</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Registration</td></tr>

<tr><td>  

[plot-profile](https://www.napari-hub.org/plugins/napari-plot-profile)

</td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td></tr>

<tr><td>  

[plugin-search](https://www.napari-hub.org/plugins/napari-plugin-search)

</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Search plugins</td></tr>


<tr><td>

[process-points-and-surfaces](https://www.napari-hub.org/plugins/napari-process-points-and-surfaces)

</td>
<td> </td>
<td>x</td>
<td>x</td>
<td>x</td>
<td> </td>
<td>x</td>
<td> </td></tr>

<tr><td>  

[pyclesperanto-assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant)

</td>
<td> </td>
<td>x</td>
<td>x</td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td></tr>



<tr><td>  

[RedLionfish](https://www.napari-hub.org/plugins/RedLionfish)

</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td></tr>

<tr><td>  

[segment-blobs-and-things-with-membranes](https://www.napari-hub.org/plugins/napari-segment-blobs-and-things-with-membranes)

</td>
<td> </td>
<td>x</td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td></tr>


<tr><td>  

[simpleitk-image-processing](https://www.napari-hub.org/plugins/napari-simpleitk-image-processing)

</td>
<td> </td>
<td>x</td>
<td>x</td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td></tr>

<tr><td>  

[skimage-regionprops](https://www.napari-hub.org/plugins/napari-skimage-regionprops)

</td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td></tr>


<tr><td>  

[tabu](https://www.napari-hub.org/plugins/napari-tabu)

</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Handle multiple napari windows</td></tr>

<tr><td>

[the-segmentation-game](https://www.napari-hub.org/plugins/the-segmentation-game)

</td>
<td> </td>
<td> </td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td></tr>

<tr><td>  

[workflow-inspector](https://www.napari-hub.org/plugins/napari-workflow-inspector)

</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Visualize workflows</td></tr>

<tr><td>  

[workflow-optimizer](https://www.napari-hub.org/plugins/napari-workflow-optimizer)

</td>
<td> </td>
<td>x</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td>Optimize image processing parameters</td></tr>



</table>

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Installation

You can install `devbio-napari` via conda. If you have never used conda before, please [read this guide first](https://biapol.github.io/blog/johannes_mueller/anaconda_getting_started/).

    conda create --name devbio-napari-env python=3.9 devbio-napari -c conda-forge
    conda activate devbio-napari-env

Mac-users please also install this:

    conda install -c conda-forge ocl_icd_wrapper_apple
    
Linux users please also install this:
    
    conda install -c conda-forge ocl-icd-system

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

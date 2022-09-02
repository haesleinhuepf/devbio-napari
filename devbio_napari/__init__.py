
__version__ = "0.5.10"

import napari
from napari_time_slicer import time_slicer
from napari_tools_menu import register_function
from napari.types import ImageData, PointsData
from napari_workflows._workflow import _get_layer_from_data

from .__main__ import main

from napari_tools_menu import register_dock_widget

try:
    from RedLionfishDeconv.napari_plugin import RedLionfish_widget
    register_dock_widget( RedLionfish_widget, menu="Filtering / deconvolution > Richardson-Lucy (RedLionfish)")
except ImportError:
    pass



try:
    from platymatch._dock_widget import DetectNuclei, EstimateTransform, EvaluateMetrics
    register_dock_widget(DetectNuclei, menu="Registration > Detect nuclei (platymatch)")
    register_dock_widget(EstimateTransform, menu="Registration > Estimate transform (platymatch)")
    register_dock_widget(EvaluateMetrics, menu="Registration > Evaluate metrics (platymatch)")
except ImportError:
    pass

from napari_animation._qt import AnimationWidget
register_dock_widget(AnimationWidget, menu="Visualization > Animation Wizard (napari-animation)")

try:
    from cellpose_napari._dock_widget import widget_wrapper
    register_dock_widget(widget_wrapper, menu="Segmentation / labeling > Cellpose")
except ImportError:
    pass


from napari_blob_detection import difference_of_gaussian, laplacian_of_gaussian


@register_function(menu="Points > Detect blobs (Difference of Gaussian, nbt)")
@time_slicer
def difference_of_gaussian_dbn(
    image: ImageData,
    min_sigma: float = 1,
    max_sigma: float = 10,
    threshold: float = 0.1,
    viewer : napari.Viewer = None
) -> PointsData:
    image_layer = _get_layer_from_data(viewer, image)

    result = difference_of_gaussian(image_layer,
                                    dimensionality=len(image.shape),
                                    min_sigma=min_sigma,
                                    max_sigma=max_sigma,
                                    threshold=threshold)

    return result[0]


@register_function(menu="Points > Detect blobs (Laplacian of Gaussian, nbt)")
@time_slicer
def laplacian_of_gaussian_dbn(
        image: ImageData,
        min_sigma: float = 1,
        max_sigma: float = 10,
        threshold: float = 0.1,
        viewer: napari.Viewer = None
) -> PointsData:
    image_layer = _get_layer_from_data(viewer, image)

    result = laplacian_of_gaussian(image_layer,
                                    dimensionality=len(image.shape),
                                    min_sigma=min_sigma,
                                    max_sigma=max_sigma,
                                    threshold=threshold)

    return result[0]


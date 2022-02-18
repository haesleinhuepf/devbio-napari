
__version__ = "0.3.0"

from .__main__ import main

from napari_tools_menu import register_dock_widget

try:
    from RedLionfishDeconv.napari_plugin import RedLionfish_widget
    register_dock_widget( RedLionfish_widget, menu="Filtering / deconvolution > Richardson-Lucy (RedLionfish)")
except ImportError:
    pass

from napari_3d_ortho_viewer._dock_widget import OrthoViewerWidget
register_dock_widget( OrthoViewerWidget, menu="Visualization > Ortho Viewer (napari-3d-ortho-viewer)")

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

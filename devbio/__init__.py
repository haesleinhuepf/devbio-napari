
__version__ = "0.1.5"

from napari_tools_menu import register_dock_widget

from RedLionfishDeconv.napari_plugin import RedLionfish_widget
register_dock_widget( RedLionfish_widget, menu="Filtering / deconvolution > Richardson-Lucy (RedLionfish)")

from napari_3d_ortho_viewer._dock_widget import OrthoViewerWidget
register_dock_widget( OrthoViewerWidget, menu="Visualization > Ortho Viewer (napari-3d-ortho-viewer)")

from platymatch._dock_widget import DetectNuclei, EstimateTransform, EvaluateMetrics
register_dock_widget(DetectNuclei, menu="Registration > Detect nuclei (platymatch)")
register_dock_widget(EstimateTransform, menu="Registration > Estimate transform (platymatch)")
register_dock_widget(EvaluateMetrics, menu="Registration > Evaluate metrics (platymatch)")

from napari_animation._qt import AnimationWidget
register_dock_widget(EvaluateMetrics, menu="Visualization > Animation Wizard (napari-animation)")


def devbio_napari_viewer():
    import napari
    from qtpy.QtCore import QTimer

    viewer = napari.Viewer(title="devbio_napari - napari")

    #viewer.window.add_plugin_dock_widget("napari-mouse-controls", "Mouse Controls")


    def later():
        viewer.window.add_plugin_dock_widget("clEsperanto", "Assistant")

    QTimer.singleShot(300, later)

    return viewer

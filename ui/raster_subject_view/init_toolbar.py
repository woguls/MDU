from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import  QAction
import qtawesome as qta

def init_toolbar(main_window):

    main_window.toolbar = QToolBar(main_window)
    main_window.layout.addWidget(main_window.toolbar)

    # Add zoom in/out actions to the toolbar
    zoom_out_icon = qta.icon('ph.magnifying-glass-minus-thin')
    zoom_in_icon = qta.icon('ph.magnifying-glass-plus-thin')
    zoom_in_action = QAction(icon=zoom_in_icon,text="zoom in", parent=main_window)
    zoom_out_action = QAction(icon=zoom_out_icon, text="zoom out", parent=main_window)
    zoom_in_action.triggered.connect(main_window.zoom_in)
    zoom_out_action.triggered.connect(main_window.zoom_out)
    main_window.toolbar.addAction(zoom_in_action)
    main_window.toolbar.addAction(zoom_out_action)

    # Crop action to the toolbar
    crop_icon = qta.icon('ph.crop-thin')
    crop_action = QAction(icon=crop_icon, text="Set transform", parent=main_window)
    crop_action.triggered.connect(main_window.start_crop)
    main_window.toolbar.addAction(crop_action)

    return (main_window)
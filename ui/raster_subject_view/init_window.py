from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene,QVBoxLayout

def init_window(main_window):

    # Create a QGraphicsView and QGraphicsScene
    main_window.graphics_view = QGraphicsView(main_window)
    main_window.graphics_scene = QGraphicsScene(main_window)
    main_window.graphics_view.setScene(main_window.graphics_scene)

    # Set the QGraphicsView as the central widget
    main_window.layout = QVBoxLayout(main_window)
    main_window.layout.addWidget(main_window.graphics_view)

    return (main_window)
# app/subjects/raster_subject_view.py
from PyQt6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QToolBar
from PyQt6.QtGui import QPixmap, QImage, QAction
from PyQt6.QtCore import pyqtSignal
import qtawesome as qta


from .raster_subject import RasterSubject

class RasterSubjectView(QWidget):
    closed = pyqtSignal(object)

    def __init__(self,  raster_subject : RasterSubject):
        super().__init__()

        self.raster_subject = raster_subject
        self.init_ui()

    def init_ui(self):
        # Set up the main window
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create a QGraphicsView and QGraphicsScene
        self.graphics_view = QGraphicsView(self)
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.graphics_scene)

        # Set the QGraphicsView as the central widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.graphics_view)

        # Create a toolbar
        toolbar = QToolBar(self)
        layout.addWidget(toolbar)

        # Add zoom in/out actions to the toolbar
        zoom_out_icon = qta.icon('ph.magnifying-glass-minus-thin')
        zoom_in_icon = qta.icon('ph.magnifying-glass-plus-thin')
        zoom_in_action = QAction(icon=zoom_in_icon,text="zoom in", parent=self)
        zoom_out_action = QAction(icon=zoom_out_icon, text="zoom out", parent=self)
        zoom_in_action.triggered.connect(self.zoom_in)
        zoom_out_action.triggered.connect(self.zoom_out)
        toolbar.addAction(zoom_in_action)
        toolbar.addAction(zoom_out_action)

        # Initially, load and display the image
        self.update_image()

    def zoom_in(self):
        self.graphics_view.scale(1.2,1.2)

    def zoom_out(self):
        self.graphics_view.scale(0.8,0.8)

    def update_image(self):
        # Get the current state from the RasterSubject
        image_data = self.raster_subject.get_state()
        height, width, bands = image_data.shape
        bytes_per_line = bands * width
        pixmap = QPixmap.fromImage(QImage(image_data.data.tobytes(order='C'), width, height, bytes_per_line, QImage.Format.Format_RGB888))

        # Create a QPixmap and update the QGraphicsPixmapItem in the scene
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.graphics_scene.clear()
        self.graphics_scene.addItem(pixmap_item)

    def closeEvent(self, event):
        # Emit the closed signal before closing the window
        self.closed.emit(self)
        event.accept()

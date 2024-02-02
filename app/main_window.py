# app/mainwindow.py
from PyQt6.QtWidgets import (QMainWindow,   QTextEdit, 
                             QGraphicsView, QGraphicsScene,
                             QGraphicsPixmapItem, QFileDialog)
from PyQt6.QtCore import  QDateTime, QCoreApplication
from utils.log_handler import LogHandler
from app.subjects.raster_subject_view import RasterSubjectView
from app.subjects.raster_subject import RasterSubject
from app.subjects.raster_subject_view_pool import RasterSubjectViewPool

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Initialize the LogHandler
        self.log_handler = LogHandler()
        # Connect the signal to the function that displays logs
        self.log_handler.log_signal.connect(self.show_logs)
        self.log_handler.emit_log("Welcom to the Mosaic Design Utility.")

        # List to store open ImageViewer instances
        self.raster_subject_view_pool = RasterSubjectViewPool()

    def init_ui(self):
        # Create a menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # Add "Open" action to the file menu
        open_action = file_menu.addAction("Open")
        open_action.triggered.connect(self.open_files) 

        # Set up the main window
        self.setWindowTitle("Mosaic Design Utility")
        self.log_text_edit = QTextEdit(self)
        self.log_text_edit.setReadOnly(True)
        self.setCentralWidget( self.log_text_edit)


    def show_logs(self, message):
        local = QDateTime(QDateTime.currentDateTime())
        formatted_message = f"[{local.toString()}] {message}"
        self.log_text_edit.append(formatted_message)

    def open_files(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_paths, _ = file_dialog.getOpenFileNames(self, "Open Images", "", "Image Files (*.tif *.tiff *.png *.jpg *.jpeg);;All Files (*)")

        if file_paths:
            for file_path in file_paths:
                # Assuming RasterSubject takes the file path in its constructor
                raster_subject = RasterSubject(file_path)

                # Create an ImageViewer for each file and show it
                
                self.raster_subject_view_pool.open_view(raster_subject)


                # Notify observers or perform other actions as needed
                raster_subject.notify()
                self.log_handler.emit_log(f"Opened file: {file_path}")
    
    def closeEvent(self, event):
        # Close all open ImageViewer instances when the main window is closed
        self.raster_subject_view_pool.close_all_views()
        QCoreApplication.instance().quit()
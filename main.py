import sys
from PyQt6.QtWidgets import QApplication
from qdarkstyle import load_stylesheet_pyqt6
from app.main_window import MainWindow


def main():
    global diagnostics_signal
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet_pyqt6())
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
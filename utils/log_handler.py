# utils/log_handler.py
from PyQt6.QtCore import QObject, pyqtSignal, QMutex
from .threads import thread_safe_method

class LogHandler(QObject):
    # Define a signal for sending log messages
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._mutex = QMutex()

    @thread_safe_method("_mutex")
    def emit_log(self, message: str):
        # Emit the signal to show logs in the MainWindow
        try:
            self.log_signal.emit(message)
        except Exception as e: print(e)

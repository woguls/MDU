import unittest
from PyQt6.QtCore import QCoreApplication, QThread, QObject, pyqtSignal, QMutex, QMutexLocker, QTimer
from PyQt6.QtTest import QTest



from utils.log_handler import  LogHandler 

class TestLogHandlerThreadSafety(unittest.TestCase):

    def setUp(self):
        # Create a QApplication instance (required for some PyQt functionality)
        self.app = QCoreApplication([])
        self.app.processEvents()

    def test_emit_log_thread_safety(self):
        log_handler = LogHandler()

        # List to store emitted log messages
        log_messages = []

        # Slot to handle emitted log signals
        def handle_log_message(message):
            nonlocal log_messages
            log_messages.append(message)
            print(f"Received log message: {message}")


        # Connect the slot to the log_signal
        log_handler.log_signal.connect(handle_log_message)

        # Subclass QThread to create a worker thread
        class LogThread(QThread):
            def run(self):
                QTest.qWait(100)  # Simulate some work in the thread
                log_handler.emit_log("Thread-safe log message")

        # Define a function to be run in multiple threads
        def emit_log_in_thread():
            QTest.qWait(100)  # Simulate some work in the thread
            log_handler.emit_log("Thread-safe log message")
            self.app.processEvents()

        # Create multiple threads and run the function concurrently
        threads = []
        for _ in range(5):
            thread = LogThread()
            threads.append(thread)
            QTest.qWait(100)
            thread.start()

            
        # Wait for all threads to finish
        for thread in threads:
            thread.wait()


        # Ensure that the log messages were emitted and handled
        print(len(log_messages))
        self.assertTrue(len(log_messages) == 5)

if __name__ == '__main__':
    unittest.main()

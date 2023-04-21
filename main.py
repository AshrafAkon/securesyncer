import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"Modified file: {event.src_path}")

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"Created file: {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"Deleted file: {event.src_path}")

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Sync Window")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: white;")

        # Create input fields and button
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.sync_button = QPushButton("Sync")

        # Add widgets to layout
        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.sync_button)

        # Set layout for the window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

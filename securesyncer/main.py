from securesyncer.mainwindow import MainWindow
from PyQt6.QtWidgets import QApplication
import sys
import os
from securesyncer import constants


def main():
    app = QApplication(sys.argv)
    stylesheet_path = os.path.join(constants.ROOT_DIR, 'style.css')
    with open(stylesheet_path) as f:
        app.setStyleSheet(f.read())

    window = MainWindow(root_dir=constants.ROOT_DIR)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

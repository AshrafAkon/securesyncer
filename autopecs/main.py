import os
import sys
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QApplication, QMainWindow, QWidget, QFileDialog, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6. QtCore import Qt
from typing import Callable

FIELD_HEIGHT = 40
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.setWindowTitle("Sync Directories")
        self.setGeometry(100, 100, 500, 250)
        # Set maximum window height and width
        self.setMaximumSize(800, 600)

        # create input fields
        self.create_input_fields()

        # create buttons
        self.create_buttons()

        # add input fields and buttons to layout
        self.create_layout()

        # add fonts to this current window
        self.set_font()

    def set_font(self):
        font_path = os.path.join(
            ROOT_DIR, "assets/fonts/Roboto/Roboto-Bold.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            roboto_font = QFont(font_families[0])
            self.setFont(roboto_font)

    def create_input_fields(self):
        self.input1 = self.input_field('Select directory')
        self.input2 = self.input_field('Select directory')

    def input_field(self, placeholder: str):
        _field = QLineEdit()
        _field.setPlaceholderText(placeholder)
        _field.setFixedHeight(FIELD_HEIGHT)
        _field.setMinimumWidth(450)
        self.add_drop_shadow_effect(_field)
        return _field

    def create_buttons(self):
        self.button1 = self.create_button("...", self.select_encrypted)
        self.button2 = self.create_button("...", self.select_unencrypted)
        self.sync_button = self.create_button(
            "Sync", self.sync_directories, 'SyncButton')

        self.sync_button.setEnabled(False)  # disable the button initially
        self.sync_button.setMinimumWidth(70)
        self.sync_button.setMaximumWidth(200)  # reduce width to 150 pixels

    def create_button(self, text: str, func: Callable, name: str | None = None,):
        button = QPushButton(text, self)
        button.clicked.connect(func)
        if name:
            button.setObjectName(name)
        button.setFixedHeight(FIELD_HEIGHT)
        button.setMinimumWidth(40)
        return button

    def create_layout(self):
        h_layout1 = QHBoxLayout()
        h_layout1.addStretch()  # Add stretch before the widgets
        h_layout1.addWidget(self.input1)
        h_layout1.addWidget(self.button1)
        h_layout1.addStretch()  # Add stretch after the widgets

        h_layout2 = QHBoxLayout()

        h_layout2.addStretch()  # Add stretch before the widgets
        h_layout2.addWidget(self.input2)
        h_layout2.addWidget(self.button2)
        h_layout2.addStretch()  # Add stretch after the widgets

        v_layout = QVBoxLayout()

        v_layout.addStretch(1)  # Add stretch before the layouts

        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addSpacing(10)
        v_layout.addWidget(self.sync_button,
                           alignment=Qt.AlignmentFlag.AlignHCenter)
        v_layout.addStretch(1)  # Add stretch after the layouts

        v_layout.setSpacing(10)
        widget = QWidget()
        widget.setLayout(v_layout)

        self.setCentralWidget(widget)

    def add_drop_shadow_effect(self, widget: QWidget):
        return
        shadow_effect = QGraphicsDropShadowEffect(
            self)
        shadow_effect.setBlurRadius(5)
        shadow_effect.setXOffset(2)
        shadow_effect.setYOffset(2)
        widget.setGraphicsEffect(shadow_effect)

    def select_unencrypted(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.input1.setText(directory)
        self.check_sync_button()

    def select_encrypted(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.input2.setText(directory)
        self.check_sync_button()

    def check_sync_button(self):
        pass

    def sync_directories(self):
        pass


def main():
    app = QApplication(sys.argv)
    stylesheet_path = os.path.join(ROOT_DIR, 'style.css')
    with open(stylesheet_path) as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

import os
import sys
from typing import Callable

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtWidgets import (QApplication, QDialog, QFileDialog,
                             QGraphicsDropShadowEffect, QHBoxLayout, QLabel,
                             QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                             QSpacerItem, QToolBar, QToolButton, QVBoxLayout,
                             QWidget)

from securesyncer.settings_dialog import SettingsDialog
from PyQt6.QtCore import QSize
FIELD_HEIGHT = 40


class MainWindow(QMainWindow):
    def __init__(self, root_dir: str):
        super().__init__()
        self.root_dir = root_dir
        # set window properties
        self.setWindowTitle("Sync Directories")
        self.setGeometry(100, 100, 500, 250)
        # Set maximum window height and width
        self.setMaximumSize(800, 600)
        self.add_toolbar()

        # create input fields
        self.create_input_fields()

        # create buttons
        self.create_buttons()

        # add input fields and buttons to layout
        self.create_layout()

        # add fonts to this current window
        self.set_font()

    def add_toolbar(self):
        toolbar = QToolBar("Main")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        settings_icon = QToolButton()
        icon_path = os.path.join(
            self.root_dir, 'assets', 'icons', 'icons8-settings-150.png')
        settings_icon.setIcon(QIcon(icon_path))
        settings_icon.setFixedSize(45, 45)
        settings_icon.setIconSize(QSize(30, 30))
        settings_icon.clicked.connect(self.open_password_dialog)

        layout = QHBoxLayout()

        spacer = QSpacerItem(
            45, 45, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)
        layout.addWidget(settings_icon)

        container = QWidget()  # Create a QWidget to hold the layout
        container.setLayout(layout)  # Set the layout to the QWidget
        toolbar.addWidget(container)  # Add the QWidget to the toolbar

    def open_password_dialog(self):
        password_dialog = SettingsDialog()
        password_dialog.exec()

    def set_font(self):
        font_path = os.path.join(
            self.root_dir, "assets/fonts/Roboto/Roboto-Bold.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            roboto_font = QFont(font_families[0])
            self.setFont(roboto_font)

    def create_input_fields(self):
        self.encrypted_dir_field = self.input_field(
            'Select encrypted directory')
        self.unencrypted_dir_field = self.input_field(
            'Select unencrypted directory')

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
        h_layout1.addWidget(self.encrypted_dir_field)
        h_layout1.addWidget(self.button1)
        h_layout1.addStretch()  # Add stretch after the widgets

        h_layout2 = QHBoxLayout()

        h_layout2.addStretch()  # Add stretch before the widgets
        h_layout2.addWidget(self.unencrypted_dir_field)
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

    def select_encrypted(self):
        directory = QFileDialog.getExistingDirectory(
            self, "Select encrypted directory")
        self.encrypted_dir_field.setText(directory)
        self.check_sync_button()

    def select_unencrypted(self):
        directory = QFileDialog.getExistingDirectory(
            self, "Select unencrypted directory")
        self.unencrypted_dir_field.setText(directory)
        self.check_sync_button()

    def check_sync_button(self):
        dir1 = self.encrypted_dir_field.text()
        dir2 = self.unencrypted_dir_field.text()

        dir1_valid = os.path.isdir(dir1) and os.access(dir1, os.W_OK)
        dir2_valid = os.path.isdir(dir2) and os.access(dir2, os.W_OK)

        if dir1_valid and dir2_valid:
            self.sync_button.setEnabled(True)
        else:
            self.sync_button.setEnabled(False)

    def sync_directories(self):
        pass

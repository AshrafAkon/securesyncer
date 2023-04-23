import os
import sys

import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QApplication

from main_window import MainWindow

app = QApplication(sys.argv)


@pytest.fixture
def main_window():
    return MainWindow(root_dir=os.path.dirname(os.path.realpath(__file__)))


def test_title(main_window):
    assert main_window.windowTitle() == "Sync Directories"


def test_geometry(main_window):
    assert main_window.geometry().x() == 100
    assert main_window.geometry().y() == 100
    assert main_window.geometry().width() == 500
    assert main_window.geometry().height() == 250


def test_max_size(main_window):
    assert main_window.maximumSize().width() == 800
    assert main_window.maximumSize().height() == 600


def test_input_fields(main_window):
    encrypted_dir_field = main_window.encrypted_dir_field
    assert encrypted_dir_field.placeholderText() == "Select encrypted directory"
    assert encrypted_dir_field.minimumWidth() == 450

    unencrypted_dir_field = main_window.unencrypted_dir_field
    assert unencrypted_dir_field.placeholderText() == "Select unencrypted directory"
    assert unencrypted_dir_field.minimumWidth() == 450


def test_buttons(main_window):
    button1 = main_window.button1
    assert button1.text() == "..."
    assert button1.minimumWidth() == 40

    button2 = main_window.button2
    assert button2.text() == "..."
    assert button2.minimumWidth() == 40

    sync_button = main_window.sync_button
    assert sync_button.text() == "Sync"
    assert sync_button.minimumWidth() == 70
    assert sync_button.maximumWidth() == 200
    assert sync_button.isEnabled() == False


def test_sync_button_enabled(main_window):
    main_window.encrypted_dir_field.setText("/")
    main_window.unencrypted_dir_field.setText("/")
    main_window.check_sync_button()
    assert main_window.sync_button.isEnabled() == True

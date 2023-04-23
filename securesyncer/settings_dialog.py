import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QToolBar
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setModal(True)

        layout = QVBoxLayout()

        self.password_label = QLabel("Enter password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_password)

        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_password(self):
        password = self.password_input.text()
        print(f"Password: {password}")
        self.close()


# class MainWindow(QMainWindow):
    #     def __init__(self):
    #         super().__init__()

    #         self.init_ui()

    #     def init_ui(self):
    #         self.setWindowTitle("Main Window")
    #         self.resize(400, 300)

    #         toolbar = QToolBar("Main")
    #         self.addToolBar(toolbar)

    #         settings_icon = QAction(QIcon("settings_icon.png"), "Settings", self)
    #         settings_icon.triggered.connect(self.open_password_dialog)
    #         toolbar.addAction(settings_icon)

    #     def open_password_dialog(self):
    #         password_dialog = PasswordDialog()
    #         password_dialog.exec()

    # if __name__ == "__main__":
    #     app = QApplication(sys.argv)
    #     main_window = MainWindow()
    #     main_window.show()
    #     sys.exit

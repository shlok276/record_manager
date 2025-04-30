# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui.login import LoginWindow
from gui.main_window import MainWindow

def run_app():
    app = QApplication(sys.argv)

    # Define the outer main window in advance
    main_window = MainWindow()

    def launch_main():
        main_window.show()

    login_window = LoginWindow(switch_to_main_callback=launch_main)
    login_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()

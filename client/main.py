"""Điểm khởi chạy Client PySide6."""

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    """Cửa sổ khung ban đầu của Client."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Quản lý dịch vụ điện lạnh")
        self.resize(900, 600)
        self.setCentralWidget(QLabel("Client đã khởi động. Các module sẽ được phát triển theo phân công."))


def main() -> int:
    """Khởi chạy vòng lặp giao diện."""
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())

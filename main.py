import sys
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


class MainWindow(QWidget):
    def __init__(self, app:QApplication):
        super().__init__()
        self.app = app
        self.main_window = QWidget()
        self.set_window()
        self.add_btn()
        self.set_layout()
        self.show()

    def closeEvent(self, event):
        """
        becauseof subwindow doest closed, so rewrite the closeEvent
        """
        sys.exit(0)
    
    def set_window(self):
        self.setWindowTitle('Designer Tools')
        self.setMinimumWidth(260)
        #self.setMinimumSize(QSize(220, 130))
        icon = QIcon("main.ico")
        self.setWindowIcon(icon)
    
    def add_btn(self):
        self.rename_btn = QPushButton("rename")
        self.rename_btn.clicked.connect(self.context_widget)
        self.generatexml_btn = QPushButton("generatexml")
    
    def set_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.rename_btn)
        layout.addWidget(self.generatexml_btn)
        self.setLayout(layout)
    
    def context_widget(self):
        self.context = QWidget()
        icon = QIcon("main.ico")
        self.context.setWindowIcon(icon)
        but = QPushButton("dddd", self.context)
        self.context.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    app.exec()
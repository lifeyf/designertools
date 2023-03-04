import sys
from PySide6.QtWidgets import QWidget, QPushButton, QApplication

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        main_window = QWidget(self)
        self.add_btn()
        self.show()

    def add_btn(self):
        self.open_btn = QPushButton("open a new Widget", self)
        self.open_btn.clicked.connect(self.child_widget)
    
    def child_widget(self):
        self.context = QWidget()
        # self.context.setParent(self)
        self.context.setParent(self.main_window)  #加了这句就不能了，想
        self.context.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
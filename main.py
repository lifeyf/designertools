from concurrent.futures import ThreadPoolExecutor
import sys
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextBrowser, QTextEdit, QGroupBox, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QScreen, QPixmap, QTextCursor, QAction, QCursor
from PySide6.QtCore import QSize, QFileInfo, Qt, QObject, Signal, QEventLoop,QTimer, SIGNAL, QPoint
from create_xml import CreateXML
from pathlib import Path, WindowsPath
from texists import Texists as ts

# class EmittingStr(QObject):
#     textWritten = Signal(str)  # 定义一个发送str的信号，这里用的方法名与PyQt5不一样
# 
#     def write(self, text):
#         self.textWritten.emit(str(text))
#         loop = QEventLoop()
#         QTimer.singleShot(1000, loop.quit)
#         loop.exec()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = QWidget()
        self.set_window()
        self.add_btn()
        self.set_layout()
        # self.center()
        self.system_trayicon()
        self.show()

    def closeEvent(self, event):
        """
        becauseof subwindow doest closed, so rewrite the closeEvent
        """
        sys.exit(0)
    
    def set_window(self):
        self.setWindowTitle('Designer Tools')
        self.setMinimumWidth(150)
        #self.setMinimumSize(QSize(120, 130))
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        icon = QIcon("main.png")
        self.setWindowIcon(icon)
    
    def add_btn(self):
        self.rename_btn = QPushButton("Rename Pics")
        self.setXML_btn = QPushButton("Generate XML")
        self.setXML_btn.clicked.connect(self.setXML_widget)
    
    def set_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.rename_btn)
        layout.addWidget(self.setXML_btn)
        self.setLayout(layout)
    
    def setXML_widget(self):
        self.context = QWidget()
        # print(11111)
        # self.context.setParent(self.main_window)
        self.context.setWindowFlags(Qt.CustomizeWindowHint)
        self.context.setWindowFlags(Qt.WindowCloseButtonHint)
        parent_width = self.width()
        self.context.move(self.x()+parent_width, self.y())
        icon = QIcon("main.png")
        self.context.setWindowIcon(icon)
        self.context.setLayout(self.setXML_layout())
        self.context.show()
    
    def setXML_layout(self):
        lable = QLabel()
        lable.setText("Project Root:")
        xml_go_btn = QPushButton("Go")
        xml_go_btn.clicked.connect(self.create_xml)

        self.root_editor = QLineEdit()
    
        self.XMLTextBrowser = QTextEdit()
        self.XMLTextBrowser.setReadOnly(True)
        layout_info = QVBoxLayout()
        layout_info.addWidget(self.XMLTextBrowser)
        group_info = QGroupBox()
        group_info.setTitle("Info")
        group_info.setLayout(layout_info)

        section_inner = QHBoxLayout()
        section_inner.addWidget(self.root_editor)
        section_inner.addWidget(xml_go_btn)

        layout = QVBoxLayout()
        layout.addWidget(lable)

        layout_intruduction = QVBoxLayout()
        lable_intruduction = QLabel()
        lable_intruduction.setText("    depend on the project pos, auto generate \nthe xml file on desktop.")
        layout_intruduction.addWidget(lable_intruduction)

        group_help = QGroupBox()
        group_help.setTitle("Introduction")
        group_help.setLayout(layout_intruduction)

        layout.addLayout(section_inner)
        layout.addWidget(group_help)
        layout.addWidget(group_info)
        # layout.setAlignment()

#        sys.stdout = EmittingStr()
#        self.XMLTextBrowser.connect(sys.stdout, SIGNAL("textWritten(QString)"), self.outputWritten)
#        sys.stderr = EmittingStr()
#        self.XMLTextBrowser.connect(sys.stderr, SIGNAL("textWritten(QString)"), self.outputWritten)
        return layout
    
    def create_xml(self):
        current_root = WindowsPath(self.root_editor.text())
        self.XMLTextBrowser.append("Examine folder exists ...")
        self.XMLTextBrowser.moveCursor(QTextCursor.End)
        p = ts().exists(current_root)
        if p and str(current_root)!=".":
            self.XMLTextBrowser.append("Input folder accept")
            self.XMLTextBrowser.append("Begain create xml file...")
            create_obj = CreateXML(WindowsPath(current_root), WindowsPath(r"C:\Program Files\te181009\layout"))
            result_file = create_obj.make()
            self.XMLTextBrowser.append("create xml file succeed")
            self.XMLTextBrowser.append("file at:" + str(result_file))

        else:
            self.XMLTextBrowser.append("the root folder you input is NOT exist, please correct it.")
        self.XMLTextBrowser.moveCursor(QTextCursor.End)
    
        # 托盘菜单初始化
    def system_trayicon(self):
        self.tray_ico = QSystemTrayIcon()
        self.tray_ico.setIcon(QIcon(r'main.png'))

        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(app.quit)

        self.tray_ico_menu = QMenu(self)
        self.tray_ico_menu.addAction(self.quit_action)

        self.tray_ico.setContextMenu(self.tray_ico_menu)
        self.tray_ico.show()
        self.tray_ico.activated.connect(self.system_trayicon_activated)
    
    def system_trayicon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showNormal()
        if reason == QSystemTrayIcon.Context:
            # self.tray_ico_menu.exec(QPoint(QCursor.pos().x() - 55, QCursor.pos().y() - 90))
            self.tray_ico_menu.exec(QCursor.pos())

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    

#    def outputWritten(self, text):
#        cursor = self.XMLTextBrowser.textCursor()
#        cursor.movePosition(QTextCursor.End)
#        cursor.insertText(text)
#
#        self.XMLTextBrowser.setTextCursor(cursor)
#        self.XMLTextBrowser.ensureCursorVisible()

    def center(self):
        '''
        Function to show window in the center of screen
        '''
        qRect = self.frameGeometry() # frameGeometry will give us a QtCore.QRect object, it will hold height, width and other dimension of window
        centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        # move window to centerPoint
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
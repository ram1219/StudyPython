import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):         # 초기화
        super().__init__()
        self.initUI()
    def initUI(self):
        # 화면 창 생성
        self.setWindowTitle('My Qt App')
        self.setWindowIcon(QIcon('box.png'))
        #self.move(200, 200)
        #self.resize(640, 400)
        self.setGeometry(200, 200, 640, 400)
        
        # 버튼 생성
        button = QPushButton('Quit', self)
        button.move(50, 50)
        button.resize(button.sizeHint())
        button.clicked.connect(self.btn_clicked)

        exitAction = QAction(QIcon('logout.png'), 'EXIT', self)
        exitAction.setShortcut('ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.btn_clicked)

        menubar = self.menuBar()
        #menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        self.show()
        
    def btn_clicked(self):
        #QCoreApplication.instance().Quit
        sys.exit(0)

# 메인 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    exit(app.exec_())
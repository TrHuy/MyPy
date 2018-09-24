import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)


        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        viewMenu = menubar.addMenu('&View')

        exitAct = QAction(QIcon('exit.png'), '&Exit...', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        viewStatAct = QAction('View statusbar', self, checkable = True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        fileMenu.addMenu(impMenu)


        chooseAct = QAction(QIcon('pen.png'), "Choose Pen", self)
        chooseAct.setShortcut("Ctrl+P")

        choose_pen = self.addToolBar('Choose')
        choose_pen.addAction(chooseAct)
        exit_toolbar = self.addToolBar('Exit')
        exit_toolbar.addAction(exitAct)

        self.setGeometry(300, 200, 600, 400)
        self.setWindowTitle('Simple menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
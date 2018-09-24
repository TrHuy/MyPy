import sys

import pyglet as pyglet
from PyQt5.QtWidgets import QWidget, QMainWindow, QComboBox, QCheckBox, QCalendarWidget, QProgressBar,  QLabel, QToolTip, QColorDialog, QFontDialog, QPushButton,QFileDialog, QApplication, QMessageBox, QDesktopWidget, QAction, QMenu, qApp, QTextEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.resize(600, 400)
        self.center()

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        EditMenu = menubar.addMenu('Edit')
        FormatMenu = menubar.addMenu('Format')
        ViewMenu = menubar.addMenu('View')
        HelpMenu = menubar.addMenu('Help')

        openFile = QAction(QIcon('open.png'), '&Open...', self)
        openFile.setStatusTip("Open a file in editor")
        openFile.setShortcut("Ctrl+O")
        openFile.triggered.connect(self.openFile)

        newAct = QAction('New...', self)
        newAct.setStatusTip("Create a new file")

        saveAct = QAction(QIcon('save.png'), 'Save', self)
        saveAct.setShortcut("Ctrl+S")
        saveAct.triggered.connect(self.saveFile)

        save_asAct = QAction('Save As..', self)
        save_asAct.triggered.connect(self.saveFile_as)

        settingAct = QAction(QIcon('setting.png'), 'Settings...', self)
        settingAct.setStatusTip("Edit application setting")

        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        fontAct = QAction('Font', self)
        fontAct.triggered.connect(self.showFont)

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        ViewMenu.addAction(viewStatAct)

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        view_helpAct = QAction('View Help', self)

        aboutAct = QAction("About You Draw", self)

        fileMenu.addAction(openFile)
        fileMenu.addAction(newAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(save_asAct)
        fileMenu.addAction(settingAct)
        fileMenu.addAction(exitAct)

        EditMenu.addMenu(impMenu)
        FormatMenu.addAction(fontAct)

        HelpMenu.addAction(view_helpAct)

        HelpMenu.addAction(aboutAct)

        # self.styleChoice = QLabel("Tag Color", self)

        choiceColor = QAction(QIcon('pen.png'), "Choose Pen", self)
        choiceColor.setShortcut("Ctrl+P")
        choiceColor.triggered.connect(self.font_color)

        choice_pen = self.addToolBar('Choose')
        choice_pen.addAction(choiceColor)

        self.filepath = ""

        self.setWindowTitle("MindDraw")
        self.setWindowIcon(QIcon('FirstProicon.png'))
        self.show()

    def showFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "C:")

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def saveFile(self):

        if not self.filepath:
            filename, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getOpenFileName()", "NewFile",
                                                      "All Files (*);;Python Files (*.py)")
            self.filepath = filename



        else:
            filename = self.filepath
            f = open(filename, 'w')
            filedata = self.textEdit.toPlainText()
            f.write(filedata)
            f.close()

    def saveFile_as(self):
        filename, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getOpenFileName()", "NewFile",
                                                  "All Files (*);;Python Files (*.py)")

        if filename == "":
            pass

        else:
            f = open(filename, 'w')
            filedata = self.textEdit.toPlainText()
            f.write(filedata)
            f.close()

    def toggleMenu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def font_color(self):
        color = QColorDialog.getColor()
        # self.styleChoice.setStyleSheet("QWidget {background-color : %s}" % color.name())

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        undoAct = cmenu.addAction("Undo")
        cutAct = cmenu.addAction("Cut")
        copyAct = cmenu.addAction("Copy")
        pasteAct = cmenu.addAction("Paste")
        selecAct = cmenu.addAction("Select all")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
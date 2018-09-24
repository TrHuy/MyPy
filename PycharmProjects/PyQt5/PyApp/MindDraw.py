import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from pyglet import font


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.editor = QPlainTextEdit()
        # defaultfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        # defaultfont.setPointSize(10)
        defaultfont = QFont('Consolas', 10)
        self.editor.setFont(defaultfont)

        self.setCentralWidget(self.editor)

        self.path = None

        self.resize(600, 400)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        EditMenu = menubar.addMenu('Edit')
        FormatMenu = menubar.addMenu('Format')
        ViewMenu = menubar.addMenu('View')
        HelpMenu = menubar.addMenu('Help')

        openFile = QAction(QIcon(os.path.join('images_app', 'open.png')), '&Open...', self)
        openFile.setStatusTip("Open a file in editor")
        openFile.setShortcut("Ctrl+O")
        openFile.triggered.connect(self.openFile)

        newAct = QAction(QIcon(os.path.join('images_app','new.png')), 'New...', self)
        newAct.setStatusTip("Create a new file")
        newAct.setShortcut("Ctrl+N")

        saveAct = QAction(QIcon(os.path.join("images_app",'save.png')), 'Save', self)
        saveAct.setShortcut("Ctrl+S")
        saveAct.triggered.connect(self.saveFile)

        save_asAct = QAction(QIcon(os.path.join('images_app', 'saveas.png')),'Save As..', self)
        save_asAct.setShortcut("Ctrl+Shift+S")
        save_asAct.triggered.connect(self.saveFile_as)

        settingAct = QAction(QIcon(os.path.join("images_app", 'setting.png')), 'Settings...', self)
        settingAct.setStatusTip("Edit application setting")

        exitAct = QAction(QIcon(os.path.join("images_app",'exit.png')),'Exit', self)
        exitAct.setShortcut('Ctrl+Q')

        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        fontAct = QAction(QIcon(os.path.join('images_app', 'font.png')),'Font', self)
        fontAct.triggered.connect(self.showFont)

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        ViewMenu.addAction(viewStatAct)


        view_helpAct = QAction(QIcon(os.path.join('images_app', 'help')),'View Help', self)

        aboutAct = QAction(QIcon(os.path.join('images_app', 'info.png')),"About You Draw", self)

        undo_action = QAction(QIcon(os.path.join('images_app', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)

        redo_action = QAction(QIcon(os.path.join('images_app', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)

        cut_action = QAction(QIcon(os.path.join('images_app', 'cut.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.editor.cut)

        copy_action = QAction(QIcon(os.path.join('images_app', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.editor.copy)

        paste_action = QAction(QIcon(os.path.join('images_app', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.editor.paste)

        select_action = QAction(QIcon(os.path.join('images_app', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(self.editor.selectAll)

        impMenu = QMenu('Import', self)
        impAct = QAction(QIcon(os.path.join('images_app', 'import.png')),'Import mail', self)
        impMenu.addAction(impAct)

        fileMenu.addAction(openFile)
        fileMenu.addAction(newAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(save_asAct)
        fileMenu.addAction(settingAct)
        fileMenu.addAction(exitAct)
        EditMenu.addAction(undo_action)
        EditMenu.addAction(redo_action)
        EditMenu.addAction(cut_action)
        EditMenu.addAction(copy_action)
        EditMenu.addAction(paste_action)
        EditMenu.addMenu(impMenu)
        FormatMenu.addAction(fontAct)

        HelpMenu.addAction(view_helpAct)

        HelpMenu.addAction(aboutAct)

        # self.styleChoice = QLabel("Tag Color", self)

        choiceColor = QAction(QIcon(os.path.join("images_app", 'color-picker.png')), "Choose Pen", self)
        choiceColor.setShortcut("Ctrl+P")
        choiceColor.triggered.connect(self.font_color)

        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)
        toolbar.setIconSize(QSize(18, 18))
        toolbar.addAction(openFile)
        toolbar.addAction(newAct)
        toolbar.addAction(saveAct)
        toolbar.addAction(settingAct)

        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(18, 18))
        self.addToolBar(edit_toolbar)
        edit_toolbar.addAction(undo_action)
        edit_toolbar.addAction(redo_action)
        edit_toolbar.addAction(cut_action)
        edit_toolbar.addAction(copy_action)
        edit_toolbar.addAction(paste_action)
        edit_toolbar.addAction(choiceColor)
        edit_toolbar.addAction(fontAct)

        tool_bar = QToolBar("Tool & Help")
        tool_bar.setIconSize(QSize(18, 18))
        self.addToolBar(tool_bar)
        tool_bar.addAction(view_helpAct)
        tool_bar.addAction(aboutAct)

        self.setWindowIcon(QIcon(os.path.join("images_app", 'logo.png')))
        self.update_title()
        self.show()

    def showFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setFont(font)

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def openFile(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);;All files (*.*)")

        try:
            with open(path, 'r') as f:
                text = f.read()
        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.editor.setPlainText(text)
            self.update_title()

    def saveFile(self):

        if self.path is None:
            return self.saveFile_as()

        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
        except Exception as e:
            self.dialog_critical(str(e))

    def saveFile_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);;All files (*.*)")
        text = self.editor.toPlainText()
        if not path:
            # If dialog is cancelled, will return ''
            return

        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def update_title(self):
        self.setWindowTitle("%s - MindDraw" % (os.path.basename(self.path) if self.path else "Untitled"))

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
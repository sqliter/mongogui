import sys
from PyQt4 import QtGui,QtCore
from mainwindow import MainWindow

def main():
    app=QtGui.QApplication(sys.argv)
   # app.setStyleSheet("QWidget{background:darkgray} QMenu{background:darkgray} QToolButton{background:darkgray}")
    mw=MainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

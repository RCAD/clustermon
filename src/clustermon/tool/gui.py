import sys, os, re, textwrap
from PyQt4 import QtCore, QtGui
from ui.clustermon import Ui_ClusterMon


class clusterMonGui(QtGui.QMainWindow, Ui_ClusterMon):
    def __init__(self, parent=None):
        super(clusterMonGui, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Ringling Cluster Monitor')
        
    # Provides a browser wondow to choose a flie to output
    def browse(self):
        filename = QtGui.QFileDialog.getOpenFileName()
        if filename:
            self.field_filename.setText(filename)
            
    # Selects all cluster buttons
    def selectAll(self):
        for button in self.box_clusterChoice.children():
            if not button.isChecked():
                button.toggle()
    
    # Deselects all cluster buttons
    def deselectAll(self):
        for button in self.box_clusterChoice.children():
            if button.isChecked():
                button.toggle()
        
    # starts a custom cluster search
    def custom(self):
        str = 1
    
    # starts a comprehensive search of all clusters
    def comprehensive(self):
        str = 1    
            
# main
def clustermon_gui():
    app = QtGui.QApplication(sys.argv)
    gui = clusterMonGui()
    gui.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__': clustermon_gui()


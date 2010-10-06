import sys, os, re, textwrap
from PyQt4 import QtCore, QtGui
from clustermon.tool.ui.clustermon import Ui_ClusterMon

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ClusterMon(object):
    def setupUi(self, ClusterMon):
        ClusterMon.setObjectName(_fromUtf8("ClusterMon"))
        ClusterMon.setEnabled(True)
        ClusterMon.resize(800, 766)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ClusterMonIco.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ClusterMon.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ClusterMon)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.box_output = QtGui.QGroupBox(self.centralwidget)
        self.box_output.setGeometry(QtCore.QRect(10, 340, 781, 371))
        self.box_output.setObjectName(_fromUtf8("box_output"))
        self.field_output = QtGui.QTextBrowser(self.box_output)
        self.field_output.setEnabled(False)
        self.field_output.setGeometry(QtCore.QRect(10, 20, 761, 341))
        self.field_output.setObjectName(_fromUtf8("field_output"))
        self.box_customReport = QtGui.QGroupBox(self.centralwidget)
        self.box_customReport.setGeometry(QtCore.QRect(10, 10, 781, 161))
        self.box_customReport.setObjectName(_fromUtf8("box_customReport"))
        self.box_reportContent = QtGui.QGroupBox(self.box_customReport)
        self.box_reportContent.setEnabled(True)
        self.box_reportContent.setGeometry(QtCore.QRect(10, 30, 120, 111))
        self.box_reportContent.setFlat(False)
        self.box_reportContent.setCheckable(False)
        self.box_reportContent.setObjectName(_fromUtf8("box_reportContent"))
        self.check_users = QtGui.QCheckBox(self.box_reportContent)
        self.check_users.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.check_users.setObjectName(_fromUtf8("check_users"))
        self.check_jobs = QtGui.QCheckBox(self.box_reportContent)
        self.check_jobs.setGeometry(QtCore.QRect(10, 40, 101, 17))
        self.check_jobs.setObjectName(_fromUtf8("check_jobs"))
        self.check_overview = QtGui.QCheckBox(self.box_reportContent)
        self.check_overview.setGeometry(QtCore.QRect(10, 60, 101, 17))
        self.check_overview.setChecked(True)
        self.check_overview.setObjectName(_fromUtf8("check_overview"))
        self.check_nodes = QtGui.QCheckBox(self.box_reportContent)
        self.check_nodes.setGeometry(QtCore.QRect(10, 80, 101, 17))
        self.check_nodes.setObjectName(_fromUtf8("check_nodes"))
        self.box_clusterChoice = QtGui.QGroupBox(self.box_customReport)
        self.box_clusterChoice.setEnabled(True)
        self.box_clusterChoice.setGeometry(QtCore.QRect(140, 30, 521, 111))
        self.box_clusterChoice.setObjectName(_fromUtf8("box_clusterChoice"))
        self.rad_sgi1 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi1.setGeometry(QtCore.QRect(130, 20, 82, 17))
        self.rad_sgi1.setObjectName(_fromUtf8("rad_sgi1"))
        self.rad_sgi2 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi2.setGeometry(QtCore.QRect(130, 40, 82, 17))
        self.rad_sgi2.setObjectName(_fromUtf8("rad_sgi2"))
        self.rad_sgi3 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi3.setGeometry(QtCore.QRect(130, 60, 82, 17))
        self.rad_sgi3.setObjectName(_fromUtf8("rad_sgi3"))
        self.rad_sgi4 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi4.setGeometry(QtCore.QRect(130, 80, 82, 17))
        self.rad_sgi4.setObjectName(_fromUtf8("rad_sgi4"))
        self.rad_sgi8 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi8.setGeometry(QtCore.QRect(230, 80, 82, 17))
        self.rad_sgi8.setObjectName(_fromUtf8("rad_sgi8"))
        self.rad_sgi7 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi7.setGeometry(QtCore.QRect(230, 60, 82, 17))
        self.rad_sgi7.setObjectName(_fromUtf8("rad_sgi7"))
        self.rad_sgi5 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi5.setGeometry(QtCore.QRect(230, 20, 82, 17))
        self.rad_sgi5.setObjectName(_fromUtf8("rad_sgi5"))
        self.rad_sgi6 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi6.setGeometry(QtCore.QRect(230, 40, 82, 17))
        self.rad_sgi6.setObjectName(_fromUtf8("rad_sgi6"))
        self.rad_sgi12 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi12.setGeometry(QtCore.QRect(330, 80, 82, 17))
        self.rad_sgi12.setObjectName(_fromUtf8("rad_sgi12"))
        self.rad_sgi11 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi11.setGeometry(QtCore.QRect(330, 60, 82, 17))
        self.rad_sgi11.setObjectName(_fromUtf8("rad_sgi11"))
        self.rad_sgi9 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi9.setGeometry(QtCore.QRect(330, 20, 82, 17))
        self.rad_sgi9.setObjectName(_fromUtf8("rad_sgi9"))
        self.rad_sgi10 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi10.setGeometry(QtCore.QRect(330, 40, 82, 17))
        self.rad_sgi10.setObjectName(_fromUtf8("rad_sgi10"))
        self.rad_sgi16 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi16.setGeometry(QtCore.QRect(430, 80, 82, 17))
        self.rad_sgi16.setObjectName(_fromUtf8("rad_sgi16"))
        self.rad_sgi15 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi15.setGeometry(QtCore.QRect(430, 60, 82, 17))
        self.rad_sgi15.setObjectName(_fromUtf8("rad_sgi15"))
        self.rad_sgi13 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi13.setGeometry(QtCore.QRect(430, 20, 82, 17))
        self.rad_sgi13.setObjectName(_fromUtf8("rad_sgi13"))
        self.rad_sgi14 = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_sgi14.setGeometry(QtCore.QRect(430, 40, 82, 17))
        self.rad_sgi14.setObjectName(_fromUtf8("rad_sgi14"))
        self.rad_mgr = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_mgr.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.rad_mgr.setObjectName(_fromUtf8("rad_mgr"))
        self.rad_master = QtGui.QRadioButton(self.box_clusterChoice)
        self.rad_master.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.rad_master.setChecked(True)
        self.rad_master.setObjectName(_fromUtf8("rad_master"))
        self.button_select = QtGui.QPushButton(self.box_customReport)
        self.button_select.setGeometry(QtCore.QRect(690, 40, 75, 23))
        self.button_select.setObjectName(_fromUtf8("button_select"))
        self.button_deselect = QtGui.QPushButton(self.box_customReport)
        self.button_deselect.setGeometry(QtCore.QRect(690, 110, 75, 23))
        self.button_deselect.setObjectName(_fromUtf8("button_deselect"))
        self.box_generate = QtGui.QGroupBox(self.centralwidget)
        self.box_generate.setGeometry(QtCore.QRect(10, 190, 781, 131))
        self.box_generate.setObjectName(_fromUtf8("box_generate"))
        self.button_browse = QtGui.QPushButton(self.box_generate)
        self.button_browse.setEnabled(True)
        self.button_browse.setGeometry(QtCore.QRect(720, 90, 51, 23))
        self.button_browse.setObjectName(_fromUtf8("button_browse"))
        self.check_saveToFile = QtGui.QCheckBox(self.box_generate)
        self.check_saveToFile.setGeometry(QtCore.QRect(260, 90, 111, 17))
        self.check_saveToFile.setObjectName(_fromUtf8("check_saveToFile"))
        self.button_customReport = QtGui.QCommandLinkButton(self.box_generate)
        self.button_customReport.setGeometry(QtCore.QRect(10, 20, 201, 41))
        self.button_customReport.setToolTip(_fromUtf8(""))
        self.button_customReport.setObjectName(_fromUtf8("button_customReport"))
        self.field_filename = QtGui.QLineEdit(self.box_generate)
        self.field_filename.setEnabled(True)
        self.field_filename.setGeometry(QtCore.QRect(370, 90, 341, 21))
        self.field_filename.setObjectName(_fromUtf8("field_filename"))
        self.button_compReport = QtGui.QCommandLinkButton(self.box_generate)
        self.button_compReport.setGeometry(QtCore.QRect(10, 80, 201, 41))
        self.button_compReport.setToolTip(_fromUtf8(""))
        self.button_compReport.setObjectName(_fromUtf8("button_compReport"))
        ClusterMon.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ClusterMon)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        ClusterMon.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ClusterMon)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ClusterMon.setStatusBar(self.statusbar)
        self.actionProvide_credentials = QtGui.QAction(ClusterMon)
        self.actionProvide_credentials.setObjectName(_fromUtf8("actionProvide_credentials"))
        self.actionExit = QtGui.QAction(ClusterMon)
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionProvide_credentials)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ClusterMon)
        QtCore.QObject.connect(self.button_select, QtCore.SIGNAL(_fromUtf8("clicked()")), ClusterMon.selectAll)
        QtCore.QObject.connect(self.button_deselect, QtCore.SIGNAL(_fromUtf8("clicked()")), ClusterMon.deselectAll)
        QtCore.QObject.connect(self.button_customReport, QtCore.SIGNAL(_fromUtf8("clicked()")), ClusterMon.custom)
        QtCore.QObject.connect(self.button_compReport, QtCore.SIGNAL(_fromUtf8("clicked()")), ClusterMon.comprehensive)
        QtCore.QObject.connect(self.button_browse, QtCore.SIGNAL(_fromUtf8("clicked()")), ClusterMon.browse)
        QtCore.QMetaObject.connectSlotsByName(ClusterMon)

    def retranslateUi(self, ClusterMon):
        ClusterMon.setWindowTitle(QtGui.QApplication.translate("ClusterMon", "ClusterMon", None, QtGui.QApplication.UnicodeUTF8))
        self.box_output.setTitle(QtGui.QApplication.translate("ClusterMon", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.box_customReport.setTitle(QtGui.QApplication.translate("ClusterMon", "Custom Report Options", None, QtGui.QApplication.UnicodeUTF8))
        self.box_reportContent.setTitle(QtGui.QApplication.translate("ClusterMon", "Report Content", None, QtGui.QApplication.UnicodeUTF8))
        self.check_users.setText(QtGui.QApplication.translate("ClusterMon", "Active Users", None, QtGui.QApplication.UnicodeUTF8))
        self.check_jobs.setText(QtGui.QApplication.translate("ClusterMon", "Active Jobs", None, QtGui.QApplication.UnicodeUTF8))
        self.check_overview.setText(QtGui.QApplication.translate("ClusterMon", "Overview", None, QtGui.QApplication.UnicodeUTF8))
        self.check_nodes.setText(QtGui.QApplication.translate("ClusterMon", "Member Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.box_clusterChoice.setTitle(QtGui.QApplication.translate("ClusterMon", "Choose Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi1.setText(QtGui.QApplication.translate("ClusterMon", "SGI1NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi2.setText(QtGui.QApplication.translate("ClusterMon", "SGI2NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi3.setText(QtGui.QApplication.translate("ClusterMon", "SGI3NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi4.setText(QtGui.QApplication.translate("ClusterMon", "SGI4NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi8.setText(QtGui.QApplication.translate("ClusterMon", "SGI8NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi7.setText(QtGui.QApplication.translate("ClusterMon", "SGI7NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi5.setText(QtGui.QApplication.translate("ClusterMon", "SGI5NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi6.setText(QtGui.QApplication.translate("ClusterMon", "SGI6NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi12.setText(QtGui.QApplication.translate("ClusterMon", "SGI12NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi11.setText(QtGui.QApplication.translate("ClusterMon", "SGI11NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi9.setText(QtGui.QApplication.translate("ClusterMon", "SGI9NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi10.setText(QtGui.QApplication.translate("ClusterMon", "SGI01NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi16.setText(QtGui.QApplication.translate("ClusterMon", "SGI16NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi15.setText(QtGui.QApplication.translate("ClusterMon", "SGI15NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi13.setText(QtGui.QApplication.translate("ClusterMon", "SGI13NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_sgi14.setText(QtGui.QApplication.translate("ClusterMon", "SGI14NODE1", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_mgr.setText(QtGui.QApplication.translate("ClusterMon", "ClusterMgr-A", None, QtGui.QApplication.UnicodeUTF8))
        self.rad_master.setText(QtGui.QApplication.translate("ClusterMon", "masternode", None, QtGui.QApplication.UnicodeUTF8))
        self.button_select.setText(QtGui.QApplication.translate("ClusterMon", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.button_deselect.setText(QtGui.QApplication.translate("ClusterMon", "Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.box_generate.setTitle(QtGui.QApplication.translate("ClusterMon", "Generate Report", None, QtGui.QApplication.UnicodeUTF8))
        self.button_browse.setText(QtGui.QApplication.translate("ClusterMon", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.check_saveToFile.setText(QtGui.QApplication.translate("ClusterMon", "Save report to file", None, QtGui.QApplication.UnicodeUTF8))
        self.button_customReport.setText(QtGui.QApplication.translate("ClusterMon", "Custom Report", None, QtGui.QApplication.UnicodeUTF8))
        self.button_compReport.setText(QtGui.QApplication.translate("ClusterMon", "Comprehensive Report", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("ClusterMon", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProvide_credentials.setText(QtGui.QApplication.translate("ClusterMon", "Provide credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("ClusterMon", "Exit", None, QtGui.QApplication.UnicodeUTF8))

def clustermon_gui():
    app = QtGui.QApplication(sys.argv)
    gui = Ui_ClusterMon()
    gui.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__': clustermon_gui()
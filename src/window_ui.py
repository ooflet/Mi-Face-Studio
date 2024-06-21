# Form implementation generated from reading ui file 'c:\Users\Justin\Mi-Create\src\window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from translate import QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/MiCreate48x48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 4, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.workspace = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.workspace.setDocumentMode(False)
        self.workspace.setTabsClosable(True)
        self.workspace.setMovable(True)
        self.workspace.setTabBarAutoHide(False)
        self.workspace.setObjectName("workspace")
        self.gridLayout_2.addWidget(self.workspace, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuZoom = QtWidgets.QMenu(parent=self.menuView)
        self.menuZoom.setObjectName("menuZoom")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuLayers = QtWidgets.QMenu(parent=self.menuEdit)
        self.menuLayers.setObjectName("menuLayers")
        self.menuBuild = QtWidgets.QMenu(parent=self.menubar)
        self.menuBuild.setObjectName("menuBuild")
        self.menuInsert = QtWidgets.QMenu(parent=self.menubar)
        self.menuInsert.setTearOffEnabled(False)
        self.menuInsert.setObjectName("menuInsert")
        self.menuLogo = QtWidgets.QMenu(parent=self.menubar)
        icon = QtGui.QIcon.fromTheme("application-logo")
        self.menuLogo.setIcon(icon)
        self.menuLogo.setObjectName("menuLogo")
        self.menuAbout = QtWidgets.QMenu(parent=self.menuLogo)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.explorerWidget = QtWidgets.QDockWidget(parent=MainWindow)
        self.explorerWidget.setMinimumSize(QtCore.QSize(300, 150))
        self.explorerWidget.setStyleSheet("")
        self.explorerWidget.setObjectName("explorerWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.explorerWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.explorerWidget)
        self.propertiesWidget = QtWidgets.QDockWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propertiesWidget.sizePolicy().hasHeightForWidth())
        self.propertiesWidget.setSizePolicy(sizePolicy)
        self.propertiesWidget.setMinimumSize(QtCore.QSize(300, 150))
        self.propertiesWidget.setStyleSheet("")
        self.propertiesWidget.setObjectName("propertiesWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.propertiesWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.propertiesWidget)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.resourcesWidget = QtWidgets.QDockWidget(parent=MainWindow)
        self.resourcesWidget.setMinimumSize(QtCore.QSize(204, 262))
        self.resourcesWidget.setObjectName("resourcesWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reloadResource = QtWidgets.QToolButton(parent=self.dockWidgetContents_3)
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.reloadResource.setIcon(icon)
        self.reloadResource.setIconSize(QtCore.QSize(16, 16))
        self.reloadResource.setObjectName("reloadResource")
        self.gridLayout_3.addWidget(self.reloadResource, 2, 4, 1, 1)
        self.openResourceFolder = QtWidgets.QToolButton(parent=self.dockWidgetContents_3)
        icon = QtGui.QIcon.fromTheme("folder")
        self.openResourceFolder.setIcon(icon)
        self.openResourceFolder.setIconSize(QtCore.QSize(16, 16))
        self.openResourceFolder.setObjectName("openResourceFolder")
        self.gridLayout_3.addWidget(self.openResourceFolder, 2, 6, 1, 1)
        self.resourceSearch = QtWidgets.QLineEdit(parent=self.dockWidgetContents_3)
        self.resourceSearch.setInputMask("")
        self.resourceSearch.setText("")
        self.resourceSearch.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.resourceSearch.setClearButtonEnabled(True)
        self.resourceSearch.setObjectName("resourceSearch")
        self.gridLayout_3.addWidget(self.resourceSearch, 0, 0, 1, 7)
        self.resourceList = QtWidgets.QListWidget(parent=self.dockWidgetContents_3)
        self.resourceList.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.resourceList.setProperty("showDropIndicator", False)
        self.resourceList.setDragEnabled(True)
        self.resourceList.setIconSize(QtCore.QSize(64, 64))
        self.resourceList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.resourceList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.resourceList.setFlow(QtWidgets.QListView.Flow.TopToBottom)
        self.resourceList.setProperty("isWrapping", False)
        self.resourceList.setResizeMode(QtWidgets.QListView.ResizeMode.Adjust)
        self.resourceList.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.resourceList.setUniformItemSizes(False)
        self.resourceList.setWordWrap(True)
        self.resourceList.setObjectName("resourceList")
        self.gridLayout_3.addWidget(self.resourceList, 1, 0, 1, 7)
        self.addResource = QtWidgets.QToolButton(parent=self.dockWidgetContents_3)
        icon = QtGui.QIcon.fromTheme("insert-image")
        self.addResource.setIcon(icon)
        self.addResource.setIconSize(QtCore.QSize(16, 16))
        self.addResource.setObjectName("addResource")
        self.gridLayout_3.addWidget(self.addResource, 2, 5, 1, 1)
        self.resourcesWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.resourcesWidget)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSave = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout_MiFaceStudio = QtGui.QAction(parent=MainWindow)
        self.actionAbout_MiFaceStudio.setObjectName("actionAbout_MiFaceStudio")
        self.actionPreferences = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("preferences-system")
        self.actionPreferences.setIcon(icon)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionBuild = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("project-build")
        self.actionBuild.setIcon(icon)
        self.actionBuild.setObjectName("actionBuild")
        self.actionToggleExplorer = QtGui.QAction(parent=MainWindow)
        self.actionToggleExplorer.setCheckable(True)
        self.actionToggleExplorer.setChecked(True)
        self.actionToggleExplorer.setObjectName("actionToggleExplorer")
        self.actionToggleProperties = QtGui.QAction(parent=MainWindow)
        self.actionToggleProperties.setCheckable(True)
        self.actionToggleProperties.setChecked(True)
        self.actionToggleProperties.setObjectName("actionToggleProperties")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEdit = QtGui.QAction(parent=MainWindow)
        self.actionEdit.setCheckable(True)
        self.actionEdit.setChecked(True)
        self.actionEdit.setObjectName("actionEdit")
        self.actionFile = QtGui.QAction(parent=MainWindow)
        self.actionFile.setCheckable(True)
        self.actionFile.setChecked(True)
        self.actionFile.setObjectName("actionFile")
        self.actionLayout = QtGui.QAction(parent=MainWindow)
        self.actionLayout.setCheckable(True)
        self.actionLayout.setChecked(True)
        self.actionLayout.setObjectName("actionLayout")
        self.actionNewFile = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.actionNewFile.setIcon(icon)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionOpenFile = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.actionOpenFile.setIcon(icon)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionUndo = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-undo")
        self.actionUndo.setIcon(icon)
        self.actionUndo.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-redo")
        self.actionRedo.setIcon(icon)
        self.actionRedo.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionRedo.setObjectName("actionRedo")
        self.actionAbout_Qt = QtGui.QAction(parent=MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionThirdPartyNotice = QtGui.QAction(parent=MainWindow)
        self.actionThirdPartyNotice.setObjectName("actionThirdPartyNotice")
        self.actionUnpack = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Dark/package-open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUnpack.setIcon(icon1)
        self.actionUnpack.setObjectName("actionUnpack")
        self.actionCut = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-cut")
        self.actionCut.setIcon(icon)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-copy")
        self.actionCopy.setIcon(icon)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.actionPaste.setIcon(icon)
        self.actionPaste.setObjectName("actionPaste")
        self.actionProject_XML_File = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("project-source")
        self.actionProject_XML_File.setIcon(icon)
        self.actionProject_XML_File.setObjectName("actionProject_XML_File")
        self.actionResize_Images = QtGui.QAction(parent=MainWindow)
        self.actionResize_Images.setObjectName("actionResize_Images")
        self.actionImage = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("widget-image")
        self.actionImage.setIcon(icon)
        self.actionImage.setObjectName("actionImage")
        self.actionImage_List = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("widget-imagelist")
        self.actionImage_List.setIcon(icon)
        self.actionImage_List.setObjectName("actionImage_List")
        self.actionDigital_Number = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("widget-digitalnumber")
        self.actionDigital_Number.setIcon(icon)
        self.actionDigital_Number.setObjectName("actionDigital_Number")
        self.actionAnalog_Display = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("widget-analogdisplay")
        self.actionAnalog_Display.setIcon(icon)
        self.actionAnalog_Display.setObjectName("actionAnalog_Display")
        self.actionArc_Progress = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("widget-arcprogress")
        self.actionArc_Progress.setIcon(icon)
        self.actionArc_Progress.setObjectName("actionArc_Progress")
        self.actionDocumentation = QtGui.QAction(parent=MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionConsole = QtGui.QAction(parent=MainWindow)
        self.actionConsole.setObjectName("actionConsole")
        self.actionFull_Screen = QtGui.QAction(parent=MainWindow)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionDelete = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.actionDelete.setIcon(icon)
        self.actionDelete.setObjectName("actionDelete")
        self.actionBring_to_Front = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("go-top")
        self.actionBring_to_Front.setIcon(icon)
        self.actionBring_to_Front.setObjectName("actionBring_to_Front")
        self.actionBring_Forwards = QtGui.QAction(parent=MainWindow)
        self.actionBring_Forwards.setObjectName("actionBring_Forwards")
        self.actionSend_to_Back = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("go-bottom")
        self.actionSend_to_Back.setIcon(icon)
        self.actionSend_to_Back.setObjectName("actionSend_to_Back")
        self.actionSend_Backwards = QtGui.QAction(parent=MainWindow)
        self.actionSend_Backwards.setObjectName("actionSend_Backwards")
        self.actionZoom_In = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("zoom-in")
        self.actionZoom_In.setIcon(icon)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("zoom-out")
        self.actionZoom_Out.setIcon(icon)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionOpen_NewFormat = QtGui.QAction(parent=MainWindow)
        self.actionOpen_NewFormat.setObjectName("actionOpen_NewFormat")
        self.actiontest = QtGui.QAction(parent=MainWindow)
        self.actiontest.setObjectName("actiontest")
        self.actionToggleToolbar = QtGui.QAction(parent=MainWindow)
        self.actionToggleToolbar.setCheckable(True)
        self.actionToggleToolbar.setChecked(True)
        self.actionToggleToolbar.setObjectName("actionToggleToolbar")
        self.actionToggleResources = QtGui.QAction(parent=MainWindow)
        self.actionToggleResources.setCheckable(True)
        self.actionToggleResources.setChecked(True)
        self.actionToggleResources.setObjectName("actionToggleResources")
        self.actionManage_Project = QtGui.QAction(parent=MainWindow)
        self.actionManage_Project.setObjectName("actionManage_Project")
        self.actionWelcome = QtGui.QAction(parent=MainWindow)
        self.actionWelcome.setObjectName("actionWelcome")
        self.actionClose_Project = QtGui.QAction(parent=MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionManage_Project)
        self.menuFile.addAction(self.actionClose_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuZoom.addAction(self.actionZoom_In)
        self.menuZoom.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionToggleExplorer)
        self.menuView.addAction(self.actionToggleProperties)
        self.menuView.addAction(self.actionToggleResources)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToggleToolbar)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuZoom.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFull_Screen)
        self.menuLayers.addAction(self.actionBring_to_Front)
        self.menuLayers.addAction(self.actionBring_Forwards)
        self.menuLayers.addSeparator()
        self.menuLayers.addAction(self.actionSend_to_Back)
        self.menuLayers.addAction(self.actionSend_Backwards)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuLayers.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionProject_XML_File)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuBuild.addAction(self.actionBuild)
        self.menuBuild.addAction(self.actionUnpack)
        self.menuBuild.addSeparator()
        self.menuInsert.addAction(self.actionImage)
        self.menuInsert.addAction(self.actionImage_List)
        self.menuInsert.addSeparator()
        self.menuInsert.addAction(self.actionDigital_Number)
        self.menuInsert.addAction(self.actionAnalog_Display)
        self.menuInsert.addAction(self.actionArc_Progress)
        self.menuAbout.addAction(self.actionAbout_MiFaceStudio)
        self.menuAbout.addAction(self.actionAbout_Qt)
        self.menuLogo.addAction(self.actionDocumentation)
        self.menuLogo.addAction(self.menuAbout.menuAction())
        self.menuLogo.addSeparator()
        self.menuLogo.addAction(self.actionWelcome)
        self.menuLogo.addSeparator()
        self.menuLogo.addAction(self.actionExit)
        self.menubar.addAction(self.menuLogo.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuBuild.menuAction())
        self.toolBar.addAction(self.actionNewFile)
        self.toolBar.addAction(self.actionOpenFile)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBuild)

        self.retranslateUi(MainWindow)
        self.workspace.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mi Create"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuZoom.setTitle(_translate("MainWindow", "Zoom"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuLayers.setTitle(_translate("MainWindow", "Layers"))
        self.menuBuild.setTitle(_translate("MainWindow", "Build"))
        self.menuInsert.setTitle(_translate("MainWindow", "Create"))
        self.menuLogo.setTitle(_translate("MainWindow", "logo"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.explorerWidget.setWindowTitle(_translate("MainWindow", "Explorer"))
        self.propertiesWidget.setWindowTitle(_translate("MainWindow", "Properties"))
        self.resourcesWidget.setWindowTitle(_translate("MainWindow", "Resources"))
        self.reloadResource.setText(_translate("MainWindow", "Reload"))
        self.openResourceFolder.setText(_translate("MainWindow", "openFolder"))
        self.resourceSearch.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.addResource.setText(_translate("MainWindow", "addImage"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbout_MiFaceStudio.setText(_translate("MainWindow", "About Mi Create"))
        self.actionPreferences.setText(_translate("MainWindow", "Settings"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionBuild.setText(_translate("MainWindow", "Build..."))
        self.actionBuild.setToolTip(_translate("MainWindow", "Build"))
        self.actionBuild.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionToggleExplorer.setText(_translate("MainWindow", "Explorer"))
        self.actionToggleProperties.setText(_translate("MainWindow", "Properties"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionLayout.setText(_translate("MainWindow", "Layout"))
        self.actionNewFile.setText(_translate("MainWindow", "New..."))
        self.actionNewFile.setToolTip(_translate("MainWindow", "New File"))
        self.actionNewFile.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpenFile.setText(_translate("MainWindow", "Open..."))
        self.actionOpenFile.setToolTip(_translate("MainWindow", "Open File"))
        self.actionOpenFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionThirdPartyNotice.setText(_translate("MainWindow", "Third Party Notices"))
        self.actionUnpack.setText(_translate("MainWindow", "Unpack..."))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionProject_XML_File.setText(_translate("MainWindow", "Project Source Code"))
        self.actionResize_Images.setText(_translate("MainWindow", "Resize Images"))
        self.actionImage.setText(_translate("MainWindow", "Image"))
        self.actionImage_List.setText(_translate("MainWindow", "Image List"))
        self.actionDigital_Number.setText(_translate("MainWindow", "Digital Number"))
        self.actionAnalog_Display.setText(_translate("MainWindow", "Analog Display"))
        self.actionArc_Progress.setText(_translate("MainWindow", "Arc Progress"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionDocumentation.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionConsole.setText(_translate("MainWindow", "Console"))
        self.actionFull_Screen.setText(_translate("MainWindow", "Full Screen"))
        self.actionFull_Screen.setShortcut(_translate("MainWindow", "F11"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionBring_to_Front.setText(_translate("MainWindow", "Bring to Front"))
        self.actionBring_Forwards.setText(_translate("MainWindow", "Bring Forwards"))
        self.actionSend_to_Back.setText(_translate("MainWindow", "Send to Back"))
        self.actionSend_Backwards.setText(_translate("MainWindow", "Send Backwards"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionOpen_NewFormat.setText(_translate("MainWindow", "Open New Format..."))
        self.actiontest.setText(_translate("MainWindow", "test"))
        self.actionToggleToolbar.setText(_translate("MainWindow", "Toolbar"))
        self.actionToggleResources.setText(_translate("MainWindow", "Resources"))
        self.actionManage_Project.setText(_translate("MainWindow", "Manage Project"))
        self.actionManage_Project.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionWelcome.setText(_translate("MainWindow", "Welcome"))
        self.actionClose_Project.setText(_translate("MainWindow", "Close Project"))
        self.actionClose_Project.setShortcut(_translate("MainWindow", "Ctrl+W"))

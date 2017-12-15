from PyQt4.QtGui import QFileDialog
from GUI.ui_newSessionWindow import Ui_dialogStartNewSession


class newSessionWindow:

    def __init__( self, dialog, sqlConnection ):

        self.dialog         = dialog
        self.sqlConnection  = sqlConnection
        self.ui             = Ui_dialogStartNewSession()
        self.ui.setupUi( self.dialog )

        self.ui.listMediaTypes.itemSelectionChanged.connect( self.onListMediaTypes )
        self.ui.listQuestionCategories.itemSelectionChanged.connect( self.onListQuestionCategories )
        self.ui.listQuestionTypes.itemSelectionChanged.connect( self.onListQuestionTypes )
        self.ui.checkboxWriteToFile.clicked.connect( self.onCheckBoxWriteToFile )
        self.ui.btnBrowseFilename.clicked.connect( self.onBtnBrowseFilename )


    def onListMediaTypes( self ):
        # TODO : self.ui.spinboxNumberOfQuestions.setMaximum()
        pass


    def onListQuestionCategories( self ):
        # TODO : self.ui.spinboxNumberOfQuestions.setMaximum()
        pass


    def onListQuestionTypes( self ):
        # TODO : self.ui.spinboxNumberOfQuestions.setMaximum()
        pass


    def onCheckBoxWriteToFile( self ):
        if self.ui.checkboxWriteToFile.isChecked():
            self.ui.groupBox.setEnabled( True )
        else:
            self.ui.groupBox.setEnabled( False )

    def onBtnBrowseFilename( self ):
        fname = QFileDialog.getSaveFileName( self.dialog,
                                            "Write results to file",
                                            'C:\\',
                                            "Text file (*.txt)" )
        self.ui.leditFilename.setText( fname )


    def getNumberOfQuestions( self ):
        return self.ui.spinboxNumberOfQuestions.value()


    def getMediaTypes( self ):
        return [ item.text() for item in self.ui.listMediaTypes.selectedItems() ]


    def getQuestionCategories( self ):
        return [ item.text() for item in self.ui.listQuestionCategories.selectedItems() ]


    def getQuestionTypes( self ):
        return [ item.text() for item in self.ui.listQuestionTypes.selectedItems() ]


    def writeToFile( self ):
        return self.ui.checkboxWriteToFile.isChecked()


    def getUsername( self ):
        return self.ui.leditUsername.text()


    def getFilename( self ):
        return self.ui.leditFilename.text()


    def encryptFile( self ):
        return self.ui.cboxEncrypt.isChecked()
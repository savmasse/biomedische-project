# Imports
import sys
import ntpath
import pyqtgraph as pg
import numpy as np
from scipy.io import wavfile
from trainingToolLogic import TTL
from PyQt4.QtGui import QApplication, QMainWindow, QFileDialog, QMessageBox

sys.path.append( "../GUI/" )
from mainwindow import Ui_MainWindow
from TrainingTool import Ui_dialogStartNewSession

sys.path.append( "../src/" )
from sqlConnection import SqlConnection


class TrainingTool:

    sql = None

    def __init__( self ):

        # Start up the application
        self.app    = QApplication( sys.argv )
        self.window = QMainWindow()
        self.ui     = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.centralwidget.setEnabled( True )
        self.ui.statusbar.showMessage( "No database loaded!" )

        self.ui.actionNew_session.triggered.connect( self.onActionNewSession )
        self.ui.actionOpen_DB.triggered.connect( self.onActionOpen_DB )
        self.ui.actionExit.triggered.connect( self.onActionExit )
        self.ui.btnSubmit.clicked.connect( self.onBtnSubmit )

        self.window.show()
        
        # Execute
        sys.exit( self.app.exec_() )


    def onBtnSubmit( self ):
        print ("Clicked")


    def onActionOpen_DB( self ):
        
        fname   = QFileDialog.getOpenFileName( self.window,
                                               "Open DB",
                                               'C:\\',
                                               "Database files (*.db)" )
            
        try:
            self.sql     = SqlConnection( fname )
            self.ui.statusbar.showMessage( "Succesfully loaded database (" + ntpath.basename( fname ) + ")!" )
            
        except FileExistsError:
            pass
        
        except Exception as error:
            choice = QMessageBox.warning( self.window,
                                          "Warning",
                                          str( error ),
                                          QMessageBox.Ok | QMessageBox.Retry )

            if choice == QMessageBox.Retry:
                self.onActionOpen_DB()


    def onActionExit( self ):

        choice = QMessageBox.question( self.window,
                                       "Exit",
                                       "Are you sure you want to exit?",
                                       QMessageBox.Yes | QMessageBox.No )

        if choice == QMessageBox.Yes:
            sys.exit()


    def onActionNewSession( self ):
        pass
        # TODO : Setup the dialog UI


tt = TrainingTool()
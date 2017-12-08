# Imports
import sys
import pyqtgraph as pg
import numpy as np
from PyQt4.QtGui import QApplication, QMainWindow
from mainwindow import Ui_MainWindow
sys.path.append("../src/");
from sqlConnection import SqlConnection
from scipy.io import wavfile

# Start up the application
app = QApplication(sys.argv);
window = QMainWindow();
ui = Ui_MainWindow();
ui.setupUi(window);
window.show();

# Function for active UI components
def onClick (checked):
    
    sql = SqlConnection("../data/main.db");
    content = sql.selectContent("main", 4);
    sql.closeConnection();
    
    content = content[1];

    f = open('../data/file.wav', 'wb');
    f.write (content);
    f.close();
    
    print ("done writing")
    
    sampleRate, dataY = wavfile.read("../data/file.wav");
        
    print ("done reading");
    
    # Create an x-axis for the plot
    dataX = np.arange(len(dataY));
    
    print ("created x-axis");
    
    # Show the plot !
    imgServer.plot(dataX, dataY);
    
    print ("Done");
    
# Handle active UI components
btn = ui.btnSubmit;
btn.clicked.connect(onClick);
imgServer = ui.graphicsView;

# Execute
sys.exit(app.exec_());

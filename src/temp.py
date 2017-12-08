import pyqtgraph as pg
import numpy as np
from sqlConnection import SqlConnection;
import cv2;

#x = np.random.normal(size=1000)
#y = np.random.normal(size=1000)
#pg.plot(x, y, pen=None, symbol='o')  ## setting pen=None disables line drawing

s = SqlConnection("../data/main.db");
content = s.selectContent("main", 3);
s.closeConnection();

content = content[1];

f = open('file.jpg', 'wb');
f.write (content);
f.close();

file = cv2.imread ('file.jpg');
file = cv2.cvtColor(file, cv2.COLOR_BGR2RGB);
file = cv2.transpose(file);

pg.image(file);
pg.QtGui.QApplication.exec_()

## Write file away
#f = open("file.mp4", 'wb');
#f.write(content);
#f.close();
#
## Read file with openCV
#cap = cv2.VideoCapture('file.mp4')
#
#while(cap.isOpened()):
#    ret, frame = cap.read()
#
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
##    cv2.imshow('frame',gray)
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
#
#    imv.setImage(gray);
#
#cap.release()

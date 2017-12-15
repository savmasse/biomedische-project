
"""
This class handles the fetching of content from the database.
"""

from content import Content
import numpy as np
import PIL

class ContentServer (object):
    
    def __init__(self, sqlConnection, dbTable):
        self.contentList = []
        self.sqlConnection = sqlConnection
        self.dbTable = dbTable
        
    def fetchContentList (self, contentIDs):
        for ID in contentIDs:
            self.fetchContent(ID)
        
    def fetchContent(self, contentID):
        """
        Get content from the database.
        """
        # Get data
        query = "SELECT * from " + self.dbTable + " where id = '" + str(contentID) + "'"
        data = self.sqlConnection.executeSelectQuery(query)
        
        # Convert and add to list
        self.convertContent(data)
        
    def convertContent (self, contentTuples):
        """
        Get the content from the tuples into objects.
        """
        for content in contentTuples:
            self.contentList.append( Content(content) ) 
    
    def getContentList (self):
        return self.contentList
    
    def getImageContent (self, content):
        """
        Get image data from content. For now just write to file and then read again to read it in the correct format.
        """
        # Open a jpg file to write the binary data
        f = open('../data/image.jpg', 'wb');
        f.write (content);
        f.close();
        
        # Now read the image so we can use it
        img = np.asarray(PIL.Image.open("../data/image.jpg"))
        return img;
    
    def getSignalContent (self, content):
        """
        Get signal data from content.
        """
        pass
    
    def getAudioContent (self, content):
        """
        Get audio signal data from content.
        """
        pass
        
        
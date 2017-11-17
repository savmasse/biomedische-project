"""
Handle database connection here.
"""
import sqlite3
import os.path
from os import listdir, getcwd

class SqlConnection (object):
    
    def __init__(self, dbName):
        if (os.path.exists(dbName)):
            self.conn = sqlite3.connect(dbName);
            self.cursor = self.conn.cursor();
        else:
            raise FileExistsError("Could not find the database file");
        
    def createTable(self, tableName, columns):
        cols = "";
        for i in range (len(columns)-1):
            col = columns[i];
            cols = cols + " " + str(col[0]) + " " + str(col[1]) + ",";
        
        # Handle last element (no comma here)
        cols = cols + " " + str(col[0]) + " " + str(col[1]);
        
        # Execute query
        self.cursor.execute('CREATE TABLE ' + tableName + ' ( ' + cols + ' )');
        
    def deleteTable(self):
        pass;
        
    def selectData(self, table, columns):
        pass;
    
    def insertData(self, table, data):
        # Create query from data
        query = "INSERT INTO " + table + " VALUES (";
        
        # Go through data
        for i in range (len(data)-1):
            query = query +  "'" + data[i] + "', "
        # Do last element
        query = query + "'" + data[i] + "' ";
        
        print (query);
        
        # Execute query
        self.cursor.execute (query);
        
        # Commit changes
        self.conn.commit();
        
    
    # Insert a blob of binary data into a table.
    def insertContent(self, table, content):
        
        pass;
        
    def updateData(self, data):
        pass;
        
    def closeConnection(self):
        self.conn.close();
        
    
# MAIN CODE #
try:
    s = SqlConnection("sqlTesfdsfsst.db");
    #s.insertData("table", )
except FileExistsError as error:
    print (repr(error));
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
            raise Exception ("Failed to connect to the database.");
        
    def createTable(self, tableName, columns):
        cols = "";
        for i in range (len(columns)-1):
            col = columns[i];
            cols = cols + " " + str(col[0]) + " " + str(col[1]) + ",";
        
        # Handle last element (no comma here)
        cols = cols + " " + str(col[0]) + " " + str(col[1]);
        
        # Execute query
        self.cursor.execute('CREATE TABLE IF NOT EXISTS ' + tableName + ' ( ' + cols + ' )');
        
    def deleteTable(self, table):
        query = "DROP TABLE IF EXISTS " + table;
        self.cursor.execute(query);
        
    def selectData(self, table, columns, condition=None):
        query = "SELECT FROM " + table + " ";
        
        for i in range (len(columns)-1):
            query = query + "";
        
        if (condition != None):
            query = query + " WHERE " + condition;
        
        # Send query
        self.cursor.execute(query);
        
        # Get data in array form
        data = self.cursor.fetchall();
        
        # Return the resulting data as an array
        return data;
        
    
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
        
    def executeSelectQuery (self, query):
        return self.cursor.execute(query);
        
#        return self.cursor.fetchall;
                
    def selectContent(self, table, contentID):
        query = "SELECT ID, content, type, category FROM " + table + " WHERE id = " + str(contentID);
        self.cursor.execute(query);
        #contentID, content, contentType, category = self.cursor.fetchone();
        
        return self.cursor.fetchone();
        
    def updateData(self, table, data, condition=None):
        # Create query from data
        query = "UPDATE " + table + " SET ";
        for i in range (len(data)-1):
            query = query + " " + data[0] + " = " + str(data[1]) + ",";
        query = query + " " + data[0] + " = " + str(data[1]);
        
        # Add condition
        if (condition == None):
            query = query + " WHERE " + condition;
            
        # Send query
        self.cursor.execute(query);
        self.conn.commit();
        
    def closeConnection(self):
        self.conn.close();
        
    
## MAIN CODE #
#try:
#    s = SqlConnection("main.db");
#    s.selectContent("main", 1);
#    s.closeConnection();
#    
#except Exception as error:
#    print (repr(error));
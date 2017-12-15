from sqlConnection import SqlConnection
from contentServer import ContentServer

"""
Contains the logic for the training tool; this class allows for full
logic seperation from the UI components of the application.
"""
class TTL (object): # TTL = Training Tool Logic
    
    # Static properties
    sql = None
    score = 0;
    DB_TABLE_MAIN = 'main'
    DB_TABLE_QUESTIONS = 'questions'
    contentServer = None
    
    @staticmethod
    def init ():
        TTL.contentServer = ContentServer(TTL.sql, TTL.DB_TABLE_MAIN)
        
    @staticmethod
    def submit ():
        """ Handle submitting of an answer """
        TTL.contentServer.fetchContent(1)
        
    @staticmethod
    def setMainTable (table):
        """ Set content table """
        TTL.DB_TABLE_MAIN = table;
        
    @staticmethod
    def setQuestionsTable (table):
        """ Set questions table """
        TTL.DB_TABLE_QUESTIONS = table
        
    @staticmethod
    def connect (dbName):
        """
        Connect to the database.
        """
        TTL.sql = SqlConnection(dbName)
        
    @staticmethod    
    def closeConnection():
        """
        Close the database connection.
        """
        TTL.sql.closeConnection();
    
    @staticmethod
    def getQuestionCount ():
        query = "SELECT count(*) from " + TTL.DB_TABLE_QUESTIONS;
        data = TTL.sql.executeSelectQuery(query);
        for d in data :
            print (d[0])
            
    @staticmethod
    def getQuestionTypeCount (questionType):
       """
       How many elements are there of a certain type of question?
       """
       query = "SELECT count(*) from " + TTL.DB_TABLE_QUESTIONS + " where type = '" + questionType + "'";
       data = TTL.sql.executeSelectQuery(query);
       for d in data:
           print (d[0])
           
    @staticmethod
    def getQuestionCategoryCount (questionCategory):
        """
        How many elements of a certain category of question?
        """
        query = "SELECT count(*) from " + TTL.DB_TABLE_QUESTIONS + " where category = '" + questionCategory + "'";
        data = TTL.sql.executeSelectQuery(query);
        for d in data:
            print (d[0])
            
    @staticmethod
    def getContentTypeCount (contentType):
        query = "SELECT count(*) from " + TTL.DB_TABLE_MAIN + " where type = '" + contentType + "'";
        data = TTL.sql.executeSelectQuery(query);
        for d in data:
            print (d[0])
            
## Main
#
#TTL.connect("../data/main.db");
#TTL.getQuestionCount();
#TTL.getQuestionTypeCount("Regular");
        
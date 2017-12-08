from sqlConnection import SqlConnection
from questionServer import QuestionServer

"""
Contains the logic for the training tool; this class allows full
logic seperation from the UI components of the application.
"""
class TTL (object): # TTL = Training Tool Logic
    
    # Static properties
    sql = None
    questions = None
    currentQuestion = None
    questionIter = None # iterate through questions
    score = 0;
    DB_TABLE_MAIN = 'main'
    DB_TABLE_QUESTIONS = 'questions'
    
    @staticmethod
    def init ():
        TTL.fetchQuestions();
        TTL.questionIter = iter(TTL.questions);
    
    @staticmethod
    def submit ():
        """
        Handle the clicking of the submit button.
        """
        print ("Submit clicked");
        
        # Check if correct answer
        
        # Go to the next question if not the last
        
        # If last question, show score
        
    @staticmethod
    def setMainTable (table):
        super.DB_TABLE_MAIN = table;
        
    @staticmethod
    def nextQuestion():
        """
        Serve the next question to the user.
        """
        TTL.currentQuestion = next(TTL.questionIter);
        
        
    @staticmethod
    def getCurrentQuestion ():
        return TTL.currentQuestion;
        
    @staticmethod
    def isCorrectAnswer(submittedAnswer, correctAnswer):
        """
        Check if the submitted answer is the correct one.
        """
        return submittedAnswer == correctAnswer;
        
    @staticmethod
    def fetchQuestions():
        q = QuestionServer(4, TTL.sql, TTL.DB_TABLE_QUESTIONS);
        q.fetchRandomQuestions();
        TTL.questions = q.getQuestionList();
        TTL.currentQuestion = TTL.questions[0];
        
    @staticmethod
    def connect (dbName):
        """
        Connect to the database.
        """
        TTL.sql = SqlConnection(dbName);
        
    @staticmethod    
    def closeConnection():
        """
        Close the database connection.
        """
        TTL.sql.closeConnection();
        
    @staticmethod
    def fetchContent ():
        """
        Fetch the content that belongs to the question from the main table
        """
        # Get the contentID from the question
        contentID = TTL.currentQuestion[1];
        
        # Fetch data
        content = TTL.sql.selectContent(TTL.DB_TABLE_MAIN, contentID);
        return content[1];
    
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
            
    def getContentTypeCount (contentType):
        query = "SELECT count(*) from 
       
## Main
#
#TTL.connect("../data/main.db");
#TTL.getQuestionCount();
#TTL.getQuestionTypeCount("Regular");
        
import numpy as np
from sqlConnection import SqlConnection

class QuestionServer (object):
    
    def __init__(self, questionCount, sqlConnection, dbTable):
        self.questionCount = questionCount;
        self.sqlConnection = sqlConnection;
        self.dbTable = dbTable;
        self.questionList = [];
        self.sql = 0;
        
    def fetchRandomQuestions (self):
        # Clear the previous list of questions
        self.questionList = []
        
        # Get a random list of questions from the specified type
        query = "SELECT * from " + self.dbTable + " order by RANDOM() limit " + str(self.questionCount);
        data = self.sqlConnection.executeSelectQuery(query);
        
        # Put the questions in the list
        for d in data:
            self.questionList.append(d);
        
    def getQuestionList (self):
        return self.questionList;
    
    """
    Some methods to request parts of the data from a question.
    """
    @staticmethod
    def getQuestionID (question):
        return question[0];
    
    @staticmethod
    def getQuestionContentID (question):
        return question[1];
    
    @staticmethod
    def getQuestionType (question):
        return question[2];
        
    @staticmethod
    def getQuestionText (question):
        return question[3];
    
    @staticmethod
    def getQuestionChoices(question):
        return question[4];
    
    @staticmethod
    def getQuestionAnswers(question):
        return question[5];
    
## Main code
#q = QuestionServer(4, "../data/main.db", "questions");
#q.fetchRandomQuestions();
#data = q.getQuestionList();
#for d in data:
#    print d[2]
#q.closeQuestionConnection();
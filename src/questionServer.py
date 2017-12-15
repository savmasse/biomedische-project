# TTL will be imported by the time this is called
from question import Question

class QuestionServer (object):
    
    def __init__(self, sqlConnection, dbTable):
#        self.questionCount = questionCount;
        self.sqlConnection = sqlConnection;
        self.dbTable = dbTable;
        self.questionList = [];
        
    def convertQuestions (self, questionTuples):
        for questionTuple in questionTuples:
            self.questionList.append( Question(questionTuple) )
            
    def fetchQuestions (self, contentID):
        """ 
        Fetch all questions attached to a contentID and add them to the list.
        """
        # Create query and get data
        query = "SELECT * from " + self.dbTable + " where main_ID = '" + str(contentID) + "'";
        data = self.sqlConnection.executeSelectQuery(query);
        
        # Convert the data into Question objects
        self.convertQuestions(data)
        
    def getQuestionList (self):
        return self.questionList;
    
    
## Main code
#q = QuestionServer(4, "../data/main.db", "questions");
#q.fetchRandomQuestions();
#data = q.getQuestionList();
#for d in data:
#    print (d[2])
#q.closeQuestionConnection();
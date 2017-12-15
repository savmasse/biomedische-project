from question import Question

class Content (object):
    
    def __init__ (self, contentTuple):
        if ( len(contentTuple) < 4):
            raise Exception ("Could not convert tuple to Content; not enough elements in the tuple.")
        
        self.ID = contentTuple[0]
        self.content = contentTuple[1]
        self.type = contentTuple[2]
        self.category = contentTuple[3]
        self.questionList = []
        
    def getID (self):
        return self.ID
    
    def getContent (self):
        return self.content
    
    def getType (self):
        return self.type
    
    def getCategory (self):
        return self.category
    
    def fetchQuestions (self):
        """ 
        Fetch all questions attached to a contentID and add them to the list.
        """
        # Create query and get data
        query = "SELECT * from " + self.dbTable + " where main_ID = '" + str(self.ID) + "'";
        data = self.sqlConnection.executeSelectQuery(query);
        
        # Convert the data into Question objects
        self.convertQuestions(data)
        
    def convertQuestions (self, questionTuples):
        for questionTuple in questionTuples:
            self.questionList.append( Question(questionTuple) )
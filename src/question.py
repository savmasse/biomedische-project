"""
Question class for easy access to question information.
"""
class Question (object):
    
    def __init__ (self, questionTuple):
        if (len(questionTuple) < 6):
            raise Exception ("Could not convert tuple to question. Not enough elements present.")
        
        self.ID = questionTuple[0]
        self.contentID = questionTuple[1]
        self.type = questionTuple[2]
        self.text = questionTuple[3]
        self.choices = questionTuple[4]
        self.answers = questionTuple[5]
    
    def getQuestionID (self):
        return self.ID;
    
    def getQuestionText (self):
        return self.text;
    
    def getQuestionContentID (self):
        return self.contentID;
    
    def getQuestionType (self):
        return self.type;
    
    def getQuestionChoices (self):
        return self.choices;
    
    def getQuestionAnswers (self):
        return self.answers;
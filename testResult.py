class testResult: 
 
    def __init__(self): 
        self.anger = 0 
        self.disgust = 0 
        self.fear = 0 
        self.happy = 0 
        self.sad = 0 
        self.surprise = 0 
        self.neutral = 0 
         
    def evaluate(self,label): 
         
        if (0 == label): 
            self.anger = self.anger+1 
        if (1 == label): 
            self.disgust = self.disgust+1 
        if (2 == label): 
            self.fear = self.fear+1 
        if (3 == label): 
            self.happy = self.happy+1 
        if (4 == label): 
            self.sad = self.sad+1 
        if (5 == label): 
            self.surprise = self.surprise+1 
        if (6 == label): 
            self.neutral = self.neutral+1 
 
    def display_result(self,evaluations): 
        print("anger = "    + 
              str((self.anger/float(evaluations))*100)    + "%") 
        print("disgust = "  + 
              str((self.disgust/float(evaluations))*100)  + "%") 
        print("fear = "     + 
              str((self.fear/float(evaluations))*100)     + "%") 
        print("happy = "    + 
              str((self.happy/float(evaluations))*100)    + "%") 
        print("sad = "      + 
              str((self.sad/float(evaluations))*100)      + "%") 
        print("surprise = " + 
              str((self.surprise/float(evaluations))*100) + "%") 
        print("neutral = "  + 
              str((self.neutral/float(evaluations))*100)  + "%") 
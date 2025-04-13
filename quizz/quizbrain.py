

class qbrain:
    def __init__(self,qlist):
        self.qnumber=0
        self.questionlist=qlist
        self.score=0
    def stillquestions(self):
        return self.qnumber<len(self.questionlist)
               
    def nextq(self):
        self.current_q=self.questionlist[self.qnumber]
        self.qnumber+=1
        self.answer=str(input(f"qno.{self.qnumber}{self.current_q.text} : true/false(?)"))
        
    def check_score(self):
        if(self.current_q.answer==self.answer):
            self.score=self.score+1
            print(f"correct!!  your score:{self.score}/{len(self.questionlist)})")

        else:
            
            print(f"you loose!! your score is {self.score}/{len(self.questionlist)}")
            exit(0)

            

class QuizBrain:
    def __init__(self,question_bank):
        self.question_number=0
        self.question_bank=question_bank
        self.score=0

    def still_has_question(self):
        if self.question_number==len(self.question_bank):
            return False
        return True
    
    def next_question(self):
        current_question=self.question_bank[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print(f"You got it right. Score: ({self.score}/{self.question_number})")
        else:
            print(f"You got it wrong.  Score: ({self.score}/{self.question_number})")
        print(f"Correct answer: {correct_answer}.")
        print()
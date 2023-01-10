class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return  self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        choice = ""
        self.question_number +=1
        while choice not in [ "true", "false"]:
            choice =  input(f"Q.{self.question_number}: {question.text} (true/false): ").lower()
            self.check_answer(choice, question.answer)


    def check_answer(self, answer, correct_answer):
        if answer == correct_answer.lower():
            self.score += 1
            print("You got it")
        else:
            print("Wrong.")
        print(f"Your score is : {self.score}/{self.question_number}\n")


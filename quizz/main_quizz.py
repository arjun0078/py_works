from quizz_q_a import question_model
from quizz_question import Questions
from quizbrain import qbrain

question_bank=[]
for q in question_model:
    question_text=q["text"]
    question_answer=q["answer"]
    q_obj=Questions(question_text,question_answer)
    question_bank.append(q_obj)

quiz=qbrain(question_bank)
while quiz.stillquestions(): 
    quiz.nextq()
    quiz.check_score()
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Access question_data
# print(question_data[0]['text'])
# print(question_data[0]['answer'])

#TODO Write a for loop to iterate over the question data
#TODO Create a Question object from each entry in question_data
#TODO Append each Question object to the question_bank

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Completed all Trivia Questions!")
print(f"Final Score: {quiz.score}/{quiz.question_number}")

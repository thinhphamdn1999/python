import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[self.question_number]

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return question_text

    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        is_correct = user_answer.lower() == correct_answer.lower()
        if is_correct:
            self.score += 1
        return is_correct

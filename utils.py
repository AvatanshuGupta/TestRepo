from questions import QUESTIONS

def evaluate_quiz(user_answers):
    score = 0
    for key, answer in user_answers.items():
        if answer == QUESTIONS[key]["answer"]:
            score += 1
    return score

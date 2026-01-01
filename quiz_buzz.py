""" Quiz Buzz App """
import json

""" Extract questionnaire from quiz_questions.json file"""
with open("files/quiz_questions.json", 'r') as file:
    content = file.read()

questions = json.loads(content)
user_response = []

""" Function to print Question Details """
def print_questionnaire(question_local):
    
    print(question_local["question_text"])
    print("Options:")

    for index, option in enumerate(question_local["alternatives"]):
        print(f"{index + 1}. {option}")
        
    stringified_user_input = input("Enter option number:")
    user_input_local = int(stringified_user_input)

    """ If user entered number out of the range 1-4: show Invalid Option msg and re-ask thq question"""
    if user_input_local < 1 or user_input_local > 4:
        print("Invalid Option!")
        
        """ Recursively call the print_questionnaire function until user passes in range number"""
        user_input_local = print_questionnaire(question_local)

    return user_input_local

""" Main Quiz Code Block """
try:
    for question in questions:
        
        user_input = print_questionnaire(question)

        isCorrect = False

        if user_input == question["correct_answer"]:
            isCorrect = True

        response = {}

        response["question_id"] = question["question_id"]
        response["user_answer"] = int(user_input)
        response["correct_answer"] = question["correct_answer"]
        response["is_correct"] = isCorrect
        
        user_response.append(response)

    total_score = 0

    print("\n***Result***\n")

    for response in user_response:
    
        print(f"Question No. - {response['question_id']} : User Answer - {response['user_answer']} : Correct Answer - {response['correct_answer']}")

        if response["is_correct"] == True:
            total_score = total_score + 1

    print(f"\nYour Score: {total_score} / {len(questions)}\n")

except ValueError:
    print('Invalid Value!')
    print('Start the quiz again!')
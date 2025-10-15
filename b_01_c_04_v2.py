#Upload Results to File
from datetime import datetime

questions_answered = 'fewfgew'
correct_answers = 'feggh'
wrong_answers = 'fehriuth'
questions_answered_array = []
correct_answers_array = []
wrong_answers_array = []
questions_answered_array.append(questions_answered)
correct_answers_array.append(correct_answers)
wrong_answers_array.append(wrong_answers)

#File Information
file_name = "quiz_game_history"
file_path = "{}.html".format(file_name)

#Current Time
timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")

#Writing Information to the File
with open("quiz_game_history.html","w") as text_file:
    text_file.write("<html><body><table><tr><th>Time</th><th>Questions Answered</th><th>Correct</th><th>Incorrect</th></tr>")

    for i in questions_answered_array:
        text_file.write(f"<tr><td>{timestamp}</td><td>{questions_answered}</td><td>{correct_answers}</td><td>{wrong_answers}</td></tr>")
    text_file.write("</table><hr></body></html>")
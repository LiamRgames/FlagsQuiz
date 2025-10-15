#Upload Results to File
from datetime import datetime
import os

questions_answered = 'gvfdgb'
correct_answers = 'vgfg'
wrong_answers = 'huhyuifchy'
questions_answered_array = []
correct_answers_array = []
wrong_answers_array = []
questions_answered_array.append(questions_answered)
correct_answers_array.append(correct_answers)
wrong_answers_array.append(wrong_answers)

#File Information
file_name = "quiz_game_history"
file_path = "{}.html".format(file_name)
text_file = open(file_path, "a+")


#Current Time
timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")

#Writing Information to the File
try:
    if os.path.getsize(file_path) == 0:
        text_file.write("<html><body><h1>Results</h1><table border='1'><tr><th>Time</th><th>Score</th><th>Questions Answered</th><th>Correct</th><th>Incorrect</th></tr>")
        text_file.write("<style>th,td {padding: 10px;}</style>")
    for i in questions_answered_array:
        text_file.write(f"<tr><td>{timestamp}</td><td>{(correct_answers / questions_answered) * 100}%</td><td>{questions_answered}</td><td>{correct_answers}</td><td>{wrong_answers}</td></tr>")

except FileNotFoundError:
    text_file.write("<html><body><h1>Results</h1><table border='1'><tr><th>Time</th><th>Score</th><th>Questions Answered</th><th>Correct</th><th>Incorrect</th></tr>")
    text_file.write("<style>th,td {padding: 10px;}</style>")
    for i in questions_answered_array:
        text_file.write(f"<tr><td>{timestamp}</td><td>{(correct_answers / questions_answered) * 100}%</td><td>{questions_answered}</td><td>{correct_answers}</td><td>{wrong_answers}</td></tr>")

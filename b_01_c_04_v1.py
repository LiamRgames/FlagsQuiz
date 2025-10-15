#Upload Results to File

questions_answered = 'huih'
correct_answers = 'hguiuih'
wrong_answers = 'uhiuh'

file_name = "quiz_game_history"
file_path = "{}.html".format(file_name)
text_file = open(file_path, "a+")

text_file.write("<html><body>")
text_file.write(f"Questions answered: {questions_answered}")
text_file.write(f"Questions correct: {correct_answers}")
text_file.write(f"Questions incorrect: {wrong_answers}")
text_file.write("<hr></body></html>")
#Imports
from tkinter import *
import random
from PIL import Image, ImageTk
import pygame
from datetime import datetime
import os

#Window
window = Tk()
window.geometry("420x420")
window.title("Flags Quiz")

#Variable Definitions
countries = [
    "afganistan", "aland", "albania", "algeria", "american samoa", "andorra","angola","anguilla","antarctica","antigua and barbuda","argentina","armenia","aruba","australia","austria","azerbaijan","bahamas","bahrain","bangladesh","barbados","belarus","belgium","belize","benin","bermuda","bhutan","bolivia","bonaire","bosnia and herzegovina","botswana","bouvet island","brazil","british indian ocean territory","british virgin islands","brunei","bulgaria","burkina faso","burundi","cabo verde","cambodia","cameroon","canada","cayman islands","central african republic","chad","chile","christmas island", "cocos (keeling) islands","colombia","comoros","congo","cook islands", "costa rica", "croatia","cuba","curacao","cyprus","czechia","democratic republic of the congo","denmark","djibouti","dominica","dominican republic","ecuador","egypt","el salvador","england","equatorial guinea","eritrea","estonia","eswatini","ethiopia","falkland islands","faroe islands","fiji","finland","france","french guiana","french polynesia","french southern and antarctic lands","gabon","gambia","georgia","germany","ghana","gibraltar","greece","greenland","grenada","guadeloupe","guam","guatemala","guernsey","guinea","guinea bissau","guyana","haiti","heard and macdonald islands","honduras","hong kong","hungary","iceland","india","indonesia","ir", "iraq","ireland","isle of man","israel","italy","ivory coast","jamaica","japan","jersey","jordan","kazakhstan","kenya","kiribati","kosovo","kuwait","kyrgyzstan","laos","latvia","lebanon","lesotho","liberia","libya","liechtenstein","lithuania","luxembourg","macau","madagascar","malawi","malaysia","maldives","mali","malta","marshall islands","martinique","mauritania","mauritius","mayotte","mexico","micronesia","moldova","monaco","mongolia","montenegro","montserrat","morocco","mozambique","myanmar","namibia","nauru","nepal","netherlands","new caledonia","new zealand","nicaragua","niger","nigeria","niue","norfolk island","north korea","north macedonia","northern ireland","northern mariana islands","norway","oman","pakistan","palau","palestine","panama","papua new guinea","paraguay","peru","philippines","pitcairn islands","poland","portugal","puerto rico","qatar","reunion","romania","russia","rwanda","saint barthlemy","saint helena","saint kitts and nevis","saint lucia","saint martin","saint pierre and miquelon","saint vincent and the grenadines","samoa","san marino","sao tome and principe","saudi arabia","scotland","senegal","serbia","seychelles","sierra leone","singapore","sint maarten","slovakia","slovenia","solomon islands","somalia","south africa","south georgia and the south sandwich islands","south korea","south sudan", "spain","sri lanka","sudan","suriname","svalbard and jan mayen","sweden","switzerland","syria","taiwan","tajikstan","tanzania","thailand","timor-leste","togo","tokelau","tonga","trinidad and tobago","tunisia","turkey","turkmenistan","turks and caicos islands","tuvalu","uganda","ukraine","united arab emirates","united kingdom","united states minor outlying islands","united states of america","united states virgin islands","uruguay","uzbekistan","vanuatu","vatican city","venezuela","vietnam","wales","wallis and futuna","western sahara","yemen","zambia","zimbabwe"
]
num_of_questions = 0
difficulty_options = ["easy",",medium","hard"]
user_difficulty = ''
response = ''
correct_answers = 0
wrong_answers = 0
questions_answered = 0
user_entered_answer_text = ''
question_frame = Frame(window)
question_frame.config(bg='lightblue')
question_label = Label(question_frame)
option1 = Button(question_frame)
option2 = Button(question_frame)
option3 = Button(question_frame)
option4 = Button(question_frame)
user_entered_answer = Entry(question_frame, width=50)
user_question_number = 0
answer = ''
error_label = ''

#Music
pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)
button_press_sound = pygame.mixer.Sound("button_sound.mp3")
correct_sound = pygame.mixer.Sound("correct.mp3")
wrong_sound = pygame.mixer.Sound("wrong.mp3")

#Icon and Background
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(background="lightblue")

def frame_toggle(frame_to_hide, frame_to_show, things_to_pack):
    if frame_to_hide.winfo_ismapped():
        frame_to_hide.pack_forget()
        frame_to_show.pack()
        for i in things_to_pack:
            i.pack()

def int_checker(event):
    global user_question_number_entry
    global user_question_number
    global error_label
    if error_label == '':
        error_label = Label(user_questions_frame, font=('Sans Serif',14,'bold'), fg='red')

    while True:
        try:
            user_question_number = user_question_number_entry.get()
            user_question_number = float(user_question_number)
            if 10 <= user_question_number <= 200:
                user_question_number_entry.delete(0, 'end')
                frame_toggle(user_questions_frame,difficulty_frame,[difficulty_options_heading,easy_button,medium_button,hard_button])
                break
            else:
                error_label.config(text='Please enter a valid number between 10-200')
                error_label.pack()
                user_question_number_entry.delete(0,'end')
                break

        except ValueError:
            error_label.config(text='Please enter a number between 10-200')
            error_label.pack()
            user_question_number_entry.delete(0,'end')
            break

def set_difficulty(difficulty):
    global user_difficulty
    user_difficulty = difficulty


def random_question_generator():
    global answer
    global option2
    global option3
    global option4
    global question_label
    global option1
    global user_entered_answer_text

    answer = answer1 = random.choice(countries)
    answer2 = random.choice(countries)
    answer3 = random.choice(countries)
    answer4 = random.choice(countries)
    order = [answer1,answer2,answer3,answer4]
    random.shuffle(order)

    flag_image = "flags/" + answer.lower() + ".png"
    resized_flag_image = ImageTk.PhotoImage(Image.open(flag_image).resize((100, 100)))
    question_label.image = resized_flag_image
    user_entered_answer.pack_forget()

    if user_difficulty == "easy":
        question_label.config(text="What is this flag?", font=('Sans Serif',20, 'bold'), image=f'{resized_flag_image}', compound="bottom", bg='lightblue', pady=50)
        option1.config(text=order[0], width=28, font=('Sans Serif',10,'bold'), bg='white', command=lambda: (answer_checker(order[0])), image='')
        option2.config(text=order[1], width=28, font=('Sans Serif', 10, 'bold'), bg='white', command=lambda: (answer_checker(order[1])), image='')
        option3.config(text=order[2], width=28, font=('Sans Serif', 10, 'bold'), bg='white', command=lambda: (answer_checker(order[2])), image='')
        option4.config(text=order[3], width=28, font=('Sans Serif', 10, 'bold'), bg='white', command=lambda: (answer_checker(order[3])), image='')

    elif user_difficulty == "medium":
        question_label.config(text=f"Which flag is {answer}", font=('Sans Serif',20, 'bold'), bg='lightblue', image='')
        flag_image1 = "flags/" + order[0].lower() + ".png"
        resized_flag_image1 = ImageTk.PhotoImage(Image.open(flag_image1).resize((100, 50)))
        option1.image = resized_flag_image1
        option1.config(width=100, font=('Sans Serif', 10, 'bold'), bg='white', image=f'{resized_flag_image1}', command=lambda: (answer_checker(order[0])))

        flag_image2 = "flags/" + order[1].lower() + ".png"
        resized_flag_image2 = ImageTk.PhotoImage(Image.open(flag_image2).resize((100, 50)))
        option2.image = resized_flag_image2
        option2.config(width=100, font=('Sans Serif', 10, 'bold'), bg='white', image=f'{resized_flag_image2}', command=lambda: (answer_checker(order[1])))

        flag_image3 = "flags/" + order[2].lower() + ".png"
        resized_flag_image3 = ImageTk.PhotoImage(Image.open(flag_image3).resize((100, 50)))
        option3.image = resized_flag_image3
        option3.config(width=100, font=('Sans Serif', 10, 'bold'), bg='white', image=f'{resized_flag_image3}', command=lambda: (answer_checker(order[2])))

        flag_image4 = "flags/" + order[3].lower() + ".png"
        resized_flag_image4 = ImageTk.PhotoImage(Image.open(flag_image4).resize((100, 50)))
        option4.image = resized_flag_image4
        option4.config(width=100, font=('Sans Serif', 10, 'bold'), bg='white', image=f'{resized_flag_image4}', command=lambda: (answer_checker(order[3])))

    else:
        option1.pack_forget()
        option2.pack_forget()
        option3.pack_forget()
        option4.pack_forget()
        question_label.config(text="What is this flag?", font=('Sans Serif', 20, 'bold'), image=f'{resized_flag_image}',compound="bottom", bg='lightblue', pady=50)
        user_entered_answer_text = ''
        user_entered_answer.bind("<Return>", answer_checker)
        user_entered_answer.pack()

class Results:
    def __init__(self, wrong, right, total_questions_answered):
        self.wrong = wrong_answers
        self.right = correct_answers
        self.total_questions_answered = total_questions_answered

    def file_upload(self, wrong, right, total_questions_answered):
        questions_answered_array = []
        correct_answers_array = []
        wrong_answers_array = []
        questions_answered_array.append(total_questions_answered)
        correct_answers_array.append(right)
        wrong_answers_array.append(wrong)

        # File Information
        file_name = "quiz_game_history"
        file_path = "{}.html".format(file_name)
        text_file = open(file_path, "a+")

        #Current Time
        timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")

        #Writing Information to the File
        try:
            if os.path.getsize(file_path) == 0:
                text_file.write(
                    "<html><body><h1>Results</h1><table border='1'><tr><th>Time</th><th>Score</th><th>Questions Answered</th><th>Correct</th><th>Incorrect</th></tr>")
                text_file.write("<style>th,td {padding: 10px;}</style>")
            for i in questions_answered_array:
                text_file.write(
                    f"<tr><td>{timestamp}</td><td>{(right / total_questions_answered) * 100}%</td><td>{total_questions_answered}</td><td>{right}</td><td>{wrong}</td></tr>")

        except FileNotFoundError:
            text_file.write(
                "<html><body><h1>Results</h1><table border='1'><tr><th>Time</th><th>Score</th><th>Questions Answered</th><th>Correct</th><th>Incorrect</th></tr>")
            text_file.write("<style>th,td {padding: 10px;}</style>")
            for i in questions_answered_array:
                text_file.write(
                    f"<tr><td>{timestamp}</td><td>{(right / total_questions_answered) * 100}%</td><td>{total_questions_answered}</td><td>{right}</td><td>{wrong}</td></tr>")


    def display_stats(self, wrong,right,total_questions_answered):
        global questions_answered
        global correct_answers
        global wrong_answers
        stats_frame = Frame(window)
        stats_frame.config(bg='lightblue')
        stats_heading = Label(stats_frame, text="Your Results:", font=('Sans Serif', 20, 'bold'), bg='lightblue')
        total_wrong = Label(stats_frame,text=f"Incorrect: {wrong}", font=('Sans Serif', 10, 'bold'), bg='lightblue')
        total_right = Label(stats_frame,text=f"Correct: {right}", font=('Sans Serif', 10, 'bold'), bg='lightblue')
        total_questions = Label(stats_frame,text=f"Total Questions Answered: {total_questions_answered}", font=('Sans Serif', 10, 'bold'), bg='lightblue')
        back_button = Button(stats_frame,text="Back to Main Menu", font=('Sans Serif', 10, 'bold'), command=lambda: (button_press_sound.play(), frame_toggle(stats_frame, main_menu_frame,[header,play_button,settings_button,help_button])))
        questions_answered = correct_answers = wrong_answers = 0
        frame_toggle(question_frame,stats_frame, [stats_heading,total_right,total_wrong,total_questions, back_button])
        self.file_upload(wrong,right,total_questions_answered)



def answer_checker(order_number):
    global correct_answers
    global questions_answered
    global user_question_number
    global wrong_answers
    global answer
    global user_entered_answer
    global user_entered_answer_text

    user_entered_answer_text = user_entered_answer.get()
    if user_entered_answer_text != '':
        order_number = user_entered_answer_text.lower()
        user_entered_answer.delete(0, 'end')

    if order_number == answer:
        correct_answers += 1
        correct_sound.play()
    else:
        wrong_answers += 1
        wrong_sound.play()

    questions_answered += 1

    if questions_answered < user_question_number:
        random_question_generator()
    else:
        persons_results = Results(wrong_answers, correct_answers, questions_answered)
        persons_results.display_stats(wrong_answers, correct_answers, questions_answered)


def toggle_sound(variable):
    if variable == 1:
        pygame.mixer.music.set_volume(1)
    elif variable == 0:
        pygame.mixer.music.set_volume(0)

def close_window():
    window.destroy()
    exit()

while True:
    #Difficulty Frame
    difficulty_frame = Frame(window)
    difficulty_frame.config(bg='lightblue')
    difficulty_options_heading = Label(difficulty_frame, text="Difficulty", font=('Arial', 40, 'bold'),foreground="black", background='lightblue', padx=20, pady=20)
    easy_button = Button(difficulty_frame, text="Easy", font=('Sans Serif', 20, 'bold'), border=4, padx=10, pady=10,command=lambda: (button_press_sound.play(), set_difficulty("easy"),frame_toggle(difficulty_frame, question_frame,[question_label, option1, option2, option3, option4]),random_question_generator()))
    medium_button = Button(difficulty_frame, text="Medium", font=('Sans Serif', 20, 'bold'), border=4, padx=10, pady=10,command=lambda: (button_press_sound.play(), set_difficulty("medium"),frame_toggle(difficulty_frame, question_frame,[question_label, option1, option2, option3, option4]),random_question_generator()))
    hard_button = Button(difficulty_frame, text="Hard", font=('Sans Serif', 20, 'bold'), border=4, padx=10, pady=10,command=lambda: (button_press_sound.play(), set_difficulty("hard"),frame_toggle(difficulty_frame, question_frame, [question_label, user_entered_answer]),random_question_generator()))

    user_questions_frame = Frame(window, bg='lightblue')
    user_question_number_entry = Entry(user_questions_frame, width=50)
    user_questions_heading = Label(user_questions_frame, text="How many Questions do you want? (10 - 200)", font=('Arial', 20, 'bold'), bg='lightblue')
    user_question_number_entry.bind("<Return>", int_checker)

    #Settings Frame
    settings_frame = Frame(window)
    settings_frame.config(bg='lightblue')
    settings_heading = Label(settings_frame, text="Settings", font=('Arial', 40, 'bold'), foreground="black",background='lightblue', padx=20, pady=20)
    var = IntVar()
    var.set(1)
    sound_toggle_button = Checkbutton(settings_frame, text="Sound", activebackground='lightblue',font=('Sans Serif', 20, 'bold'), variable=var, bg='lightblue',command=lambda: (button_press_sound.play(), toggle_sound(var.get())))
    settings_back_button = Button(settings_frame, text="Back to Main Menu", font=('Sans Serif', 10, 'bold'),command=lambda: frame_toggle(settings_frame,main_menu_frame,[header, play_button,settings_button,help_button]))


    #Help Frame
    help_frame = Frame(window)
    help_frame.config(bg='lightblue')
    help_heading = Label(help_frame, text="Help", font=('Arial', 40, 'bold'), foreground="black",background='lightblue', padx=20, pady=20)
    help_text = Label(help_frame,text="This is a Quiz about Flags. Are you up for the Challenge?\nClick on the Play Button on the Main Menu to Start and Choose a Difficulty.\n\nIf you want to change any Settings, click the Settings Button on the Main Menu\n\nThe following is a list of all people who have gotten every flag correct on Hard Difficulty:\nHarrison McQuillan",font=('Arial', 15), background='lightblue')
    help_back_button = Button(help_frame, text="Back to Main Menu", font=('Sans Serif', 10, 'bold'),command=lambda: frame_toggle(help_frame, main_menu_frame,[header, play_button, settings_button,help_button]))

    #Main Menu Frame
    main_menu_frame = Frame(window)
    main_menu_frame.config(bg='lightblue')
    header = Label(main_menu_frame, text="Flags Quiz", font=('Arial', 40, 'bold'), foreground="black",background='lightblue', padx=20, pady=20)
    play_button = Button(main_menu_frame)
    settings_button = Button(main_menu_frame)
    help_button = Button(main_menu_frame)

    play_button.config(text="Play", font=('Sans Serif', 20, 'bold'), bg='#fff', fg='#000', border=4,command=lambda: (button_press_sound.play(),frame_toggle(main_menu_frame, user_questions_frame, [user_questions_heading, user_question_number_entry])))
    settings_button.config(text="Settings", font=('Sans Serif', 20, 'bold'), bg='#fff', fg='#000', border=4,command=lambda: (button_press_sound.play(),frame_toggle(main_menu_frame, settings_frame,[settings_heading, sound_toggle_button,settings_back_button])))
    help_button.config(text="Help", font=('Sans Serif', 20, 'bold'), bg='#fff', fg='#000', border=4,command=lambda: (button_press_sound.play(),frame_toggle(main_menu_frame, help_frame, [help_heading, help_text, help_back_button])))

    #Main Menu Rendering
    main_menu_frame.pack()
    header.pack()
    play_button.pack()
    settings_button.pack()
    help_button.pack()

    #Display Window
    window.protocol("WM_DELETE_WINDOW", close_window)
    window.mainloop()


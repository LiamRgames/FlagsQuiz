#Question Answering Component
#Imports
from tkinter import *
import random
from PIL import Image, ImageTk

countries = ["afganistan", "aland", "albania", "algeria", "american samoa", "andorra","angola","anguilla","antarctica","antigua and barbuda","argentina","armenia","aruba","australia","austria","azerbaijan","bahamas","bahrain","bangladesh","barbados","belarus","belgium","belize","benin","bermuda","bhutan","bolivia","bonaire","bosnia and herzegovina","botswana","bouvet island","brazil","british indian ocean territory","british virgin islands","brunei","bulgaria","burkina faso","burundi","cabo verde","cambodia","cameroon","canada","cayman islands","central african republic","chad","chile","christmas island", "cocos (keeling) islands","colombia","comoros","congo","cook islands", "costa rica", "croatia","cuba","curacao","cyprus","czechia","democratic republic of the congo","denmark","djibouti","dominica","dominican republic","ecuador","egypt","el salvador","england","equatorial guinea","eritrea","estonia","eswatini","ethiopia","falkland islands","faroe islands","fiji","finland","france","french guiana","french polynesia","french southern and antarctic lands","gabon","gambia","georgia","germany","ghana","gibraltar","greece","greenland","grenada","guadeloupe","guam","guatemala","guernsey","guinea","guinea bissau","guyana","haiti","heard and macdonald islands","honduras","hong kong","hungary","iceland","india","indonesia","ir", "iraq","ireland","isle of man","israel","italy","ivory coast","jamaica","japan","jersey","jordan","kazakhstan","kenya","kiribati","kosovo","kuwait","kyrgyzstan","laos","latvia","lebanon","lesotho","liberia","libya","liechtenstein","lithuania","luxembourg","macau","madagascar","malawi","malaysia","maldives","mali","malta","marshall islands","martinique","mauritania","mauritius","mayotte","mexico","micronesia","moldova","monaco","mongolia","montenegro","montserrat","morocco","mozambique","myanmar","namibia","nauru","nepal","netherlands","new caledonia","new zealand","nicaragua","niger","nigeria","niue","norfolk island","north korea","north macedonia","northern ireland","northern mariana islands","norway","oman","pakistan","palau","palestine","panama","papua new guinea","paraguay","peru","philippines","pitcairn islands","poland","portugal","puerto rico","qatar","reunion","romania","russia","rwanda","saint barthlemy","saint helena","saint kitts and nevis","saint lucia","saint martin","saint pierre and miquelon","saint vincent and the grenadines","samoa","san marino","sao tome and principe","saudi arabia","scotland","senegal","serbia","seychelles","sierra leone","singapore","sint maarten","slovakia","slovenia","solomon islands","somalia","south africa","south georgia and the south sandwich islands","south korea","south sudan", "spain","sri lanka","sudan","suriname","svalbard and jan mayen","sweden","switzerland","syria","taiwan","tajikstan","tanzania","thailand","timor-leste","togo","tokelau","tonga","trinidad and tobago","tunisia","turkey","turkmenistan","turks and caicos islands","tuvalu","uganda","ukraine","united arab emirates","united kingdom","united states minor outlying islands","united states of america","united states virgin islands","uruguay","uzbekistan","vanuatu","vatican city","venezuela","vietnam","wales","wallis and futuna","western sahara","yemen","zambia","zimbabwe"
]
correct_answers = 0
wrong_answers = 0
questions_answered = 0

#Window
window = Tk()
window.geometry("420x420")
window.title("Flags Quiz")



#Question Frame
question_frame = Frame(window, bg='lightblue')
option1 = Button(question_frame)
option2 = Button(question_frame)
option3 = Button(question_frame)
option4 = Button(question_frame)
question_label = Label(question_frame)
question_frame.pack()



def random_question_generator():
    answer = random.choice(countries)
    flag_image = "flags/" + answer.lower() + ".png"
    resized_flag_image = ImageTk.PhotoImage(Image.open(flag_image).resize((100,100)))
    question_label.image = resized_flag_image
    question_label.config(text="What is this flag?", font=('Sans Serif',20, 'bold'), image=f'{resized_flag_image}', compound="bottom", bg='lightblue', pady=50)
    option1.config(command=lambda: check_answer(1), text=answer, width=28, font=('Sans Serif',10,'bold'), bg='white', image='')
    option2.config(command=lambda: check_answer(2), text=random.choice(countries), width=28, font=('Sans Serif', 10, 'bold'), bg='white', image='')
    option3.config(command=lambda: check_answer(3), text=random.choice(countries), width=28, font=('Sans Serif', 10, 'bold'), bg='white', image='')
    option4.config(command=lambda: check_answer(4), text=random.choice(countries), width=28, font=('Sans Serif', 10, 'bold'), bg='white', image='')
    question_frame.pack()
    question_label.pack()
    option1.pack()
    option2.pack()
    option3.pack()
    option4.pack()

class Results:
    def __init__(self, wrong, right, total_questions_answered):
        self.wrong = wrong_answers
        self.right = correct_answers
        self.total_questions_answered = total_questions_answered
        self.stats_frame = Frame(window)
        self.stats_heading = Label(self.stats_frame, text="Your Results:", font=('Sans Serif', 20, 'bold'), bg='lightblue')
        self.total_wrong = Label(self.stats_frame, text=f"Incorrect: {wrong}", font=('Sans Serif', 10, 'bold'),
                                 bg='lightblue')
        self.total_right = Label(self.stats_frame, text=f"Correct: {right}", font=('Sans Serif', 10, 'bold'),
                                 bg='lightblue')
        self.total_questions = Label(self.stats_frame, text=f"Total Questions Answered: {total_questions_answered}",
                                     font=('Sans Serif', 10, 'bold'), bg='lightblue')

    def display_stats(self, wrong, right, total_questions_answered):
        global questions_answered
        global correct_answers
        global wrong_answers
        self.total_wrong = Label(self.stats_frame, text=f"Incorrect: {wrong}", font=('Sans Serif', 10, 'bold'),bg='lightblue')
        self.total_right = Label(self.stats_frame, text=f"Correct: {right}", font=('Sans Serif', 10, 'bold'),bg='lightblue')
        self.total_questions = Label(self.stats_frame, text=f"Total Questions Answered: {total_questions_answered}",font=('Sans Serif', 10, 'bold'), bg='lightblue')
        self.stats_frame.config(bg='lightblue')
        self.stats_frame.pack()
        self.stats_heading.pack()
        self.total_wrong.pack()
        self.total_right.pack()
        self.total_questions.pack()
        questions_answered = correct_answers = wrong_answers = 0

    def forget(self):
        self.stats_frame.pack_forget()
        self.stats_heading.pack_forget()
        self.total_wrong.pack_forget()
        self.total_right.pack_forget()
        self.total_questions.pack_forget()

user_results = Results(wrong_answers,correct_answers,questions_answered)

def check_answer(option_number):
    global correct_answers
    global wrong_answers
    global questions_answered
    global user_results
    if option_number == 1:
        correct_answers += 1
        questions_answered += 1
    else:
        wrong_answers += 1
        questions_answered += 1
    if questions_answered < 10:
        user_results.forget()
        random_question_generator()
    else:
        user_results.display_stats(wrong_answers,correct_answers,questions_answered)


for i in range (0,5):
    random_question_generator()
    
while True:
    random_question_generator()
    window.mainloop()
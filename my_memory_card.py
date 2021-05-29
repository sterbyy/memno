from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
QGroupBox, QRadioButton, QPushButton, QLabel,QButtonGroup)
from random import randint,shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question("Что сделала студия remedy entertaiment в 2001 году?","Max Payne","Max Payne2","Alan wake","портировала Max Payne на nintendo gameboy"))
question_list.append(Question("Кем был создан популярный мессенджер facebook?","Стив Джобс","Гейб Ниювел","Марк Цукенберг","Здесь нет правильного ответа"))
question_list.append(Question("Когда вышел первый сезон самого популярного сериала Игра Прсетолов?","2008","2013","2011","2019"))
question_list.append(Question("Какая игра позаимствовала стилистику из Майнкрафта?","Terraria","Teardown","Minecraft Dungeon","Здесь нет правильного ответа"))
question_list.append(Question("В какой стране воздух больше всего имеет игровых издателей?","США","Китай","Германия","Казахстан"))
question_list.append(Question("Какая студия сделала игру Half Life 1?","VALVe","ubisoft","electronic arts","crytek"))
question_list.append(Question("когда вышел Фейсбук?","2004","2001","2012","2010"))
question_list.append(Question("CD project RED и remedy entertaiment это какие студий?","из финляндии","из германий","из США","из франций"))
question_list.append(Question("Благодаря какой игре Rockstar Games стала знаменита по всему миру?","GTA 3","Midnight club","Red Dead Redemption","GTA V"))
question_list.append(Question("В каком году появился Reddit?","2005","2013","2019","2010"))
question_list.append(Question("Какая часть Counter Strike стала основной?","CS 1.6","CS:S","CS:GO","нет правильного ответа"))
question_list.append(Question("В каких жанрах игр бывает частые сложности во время прохождения?","RPG","soulslike","шутеры от 1-го лица","песочница"))
question_list.append(Question("Какая соцсеть самая популярная среди молодежи в данный момент?","TikTok","Facebook","Instagram","VK"))
question_list.append(Question("Чем Майнкрафт выдается на фоне среди других игр?","ее создавал один человек","количество игроков превысило около 500 млн","эта самая лучшая песочница среди других","здесь другая причина"))
question_list.append(Question("Для чего используют приложение Spotify?","чтобы найти музыку, которая играет поблизости","рандомно под предпочтение пользователя выбирает и проигрывает музыку","на ней делают музыку","передают одному полбзователю другому музыку"))
question_list.append(Question("VALVe это что?","рынок игр на пк","компания, которая создала Steam","это студия, которая создает игры","это группа людей, которая создает поп-музыку"))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')

# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()# объеденяем для снятия флажка с переключателей.
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_questions():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answer=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_questions()
def show__correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        show__correct("Правильно!")
        window.score+=1
        print("Статистика\n-Всего вопросов:", window.total, "\n- Правильных ответов:", window.score)
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show__correct("Неверно!")
            print("Рейтинг", (window.score/window.total*100), "%")
def next_question():
    window.total += 1
    print("Статистика\n-Всего вопросов:", window.total, "\n- Правильных ответов:", window.total)
    q = question_list[window.cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()
window.cur_question = -1
window.setLayout(layout_card)
btn_OK.clicked.connect(click_OK)
window.resize(400, 300)
window.score = 0
window.total = 0

next_question()
window.show() 
app.exec()
from PySide2 import QtUiTools, QtWidgets
global exp
exp = ""

def test2():
	print('hello')

def test():
    global exp
    exp += '1'
    ui.text.setText(exp)

def clkbtn0():
    global exp
    exp += '0'
    ui.text.setText(exp)

def clkbtn1():
    global exp
    exp += '1'
    ui.text.setText(exp)

def clkbtn2():
    global exp
    exp += '2'
    ui.text.setText(exp)

def clkbtn3():
    global exp
    exp += '3'
    ui.text.setText(exp)

def clkbtn4():
    global exp
    exp += '4'
    ui.text.setText(exp)

def clkbtn5():
    global exp
    exp += '5'
    ui.text.setText(exp)

def clkbtn6():
    global exp
    exp += '6'
    ui.text.setText(exp)

def clkbtn7():
    global exp
    exp += '7'
    ui.text.setText(exp)

def clkbtn8():
    global exp
    exp += '8'
    ui.text.setText(exp)

def clkbtn9():
    global exp
    exp += '9'
    ui.text.setText(exp)

def clkAdd():
    global exp
    exp += '+'
    ui.text.setText(exp)

def clkSub():
    global exp
    exp += '-'
    ui.text.setText(exp)

def clkMul():
    global exp
    exp += '*'
    ui.text.setText(exp)

def clkDiv():
    global exp
    exp += '/'
    ui.text.setText(exp)

def clkPre():
    global exp
    exp = str(eval(exp) / 100)
    ui.text.setText(exp)

def clkDel():
    global exp
    exp = exp[:-1]
    ui.text.setText(exp)

def clkDot():
    global exp
    exp += '.'
    ui.text.setText(exp)

def clkEven():
    global exp
    ui.text.setText(str(eval(exp)))
    exp = str(eval(exp))

def clkClear():
    global exp
    exp = ""
    ui.text.setText(exp)

app = QtWidgets.QApplication([])
ui = QtUiTools.QUiLoader().load("form 2.ui")

ui.button0.clicked.connect(clkbtn0)
ui.button1.clicked.connect(clkbtn1)
ui.button2.clicked.connect(clkbtn2)
ui.button3.clicked.connect(clkbtn3)
ui.button4.clicked.connect(clkbtn4)
ui.button5.clicked.connect(clkbtn5)
ui.button6.clicked.connect(clkbtn6)
ui.button7.clicked.connect(clkbtn7)
ui.button8.clicked.connect(clkbtn8)
ui.button9.clicked.connect(clkbtn9)

ui.add.clicked.connect(clkAdd)
ui.sub.clicked.connect(clkSub)
ui.mul.clicked.connect(clkMul)
ui.div.clicked.connect(clkDiv)
ui.decimal.clicked.connect(clkDot)
ui.percentage.clicked.connect(clkPre)
ui.even.clicked.connect(clkEven)
ui.dele.clicked.connect(clkDel)
ui.clear.clicked.connect(clkClear)

ui.button0.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button1.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button2.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button3.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button4.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button5.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button6.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button7.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button8.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.button9.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")

ui.add.setStyleSheet("background: #737373; color: white; border : 2px solid #5a5a5a")
ui.sub.setStyleSheet("background: #737373; color: white; border : 2px solid #5a5a5a")
ui.mul.setStyleSheet("background: #737373; color: white; border : 2px solid #5a5a5a")
ui.div.setStyleSheet("background: #737373; color: white; border : 2px solid #5a5a5a")
ui.decimal.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.percentage.setStyleSheet("background: #737373; color: white; border : 2px solid #5a5a5a")
ui.even.setStyleSheet("background: #737373; color: white;border : 2px solid #5a5a5a")
ui.dele.setStyleSheet("background: #737373; color: white; border : 2px solid #5a5a5a")
ui.clear.setStyleSheet("background: #737373; color: white; border : 2px solid #5a5a5a")
ui.text.setStyleSheet("background: #c6c6c6; font-size: 14px; border : 2px solid #5a5a5a")

ui.show()
app.exec_()
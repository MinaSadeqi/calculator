import math
from PySide2 import QtUiTools, QtWidgets

global exp , memory
global ismem
ismem = False
exp , memory = "" , ""

def lastNumber(ex):
    txt = ex[ : : -1]
    a = txt.find("+")
    b = txt.find("-")
    c = txt.find("/")
    d = txt.find("%")
    e = txt.find("*")
    f = txt.find("**")
    ansr = [a,b,c,d,e,f]

    if ansr == [-1 ,-1 ,-1 ,-1 ,-1 ,-1] :
        ex = txt[ : : -1]
        m  = len(ex)
        return ex , m

    else :
        one = ansr.count(-1)
        while one != 0:
            ansr.remove(-1)
            one-=1
        m = min(ansr)
        number = txt[0:m]
        number = number[ : : -1]
        return number , m

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
    num , m = lastNumber(exp)
    exp = exp[:-m]
    tmp = exp[len(exp) - 1]
    exp = exp[:-1]
    if exp[len(exp) - 1] == '*':
        tmp += '*'
        exp = exp[:-1]
    a = int(eval(exp))
    num = int(num)
    exp += tmp
    exp += str(a * num / 100)
    ui.text.setText(exp)

def clkPow():
    global exp
    num , m = lastNumber(exp)
    exp = exp[:-m]
    num = int(num)
    num = num * num
    num = str(num)
    exp += num
    ui.text.setText(exp)

def clkFrac():
    global exp
    if exp.find("+" or "-" or "/" or "%" or "*" or "**" ) != -1 :
        num , m = lastNumber(exp)
        f = str(1 / eval(num))
        exp = exp[:-m]
        exp += f
        ui.text.setText(exp)
    else :
        exp = str(1/eval(exp))
        ui.text.setText(exp)

def clkDot():
    global exp
    exp += '.'
    ui.text.setText(exp)

def clkEven():
    global exp
    ui.text.setText(str(eval(exp)))
    exp = str(eval(exp))

def clkDel():
    global exp
    exp = ""
    ui.text.setText(exp)

def clkBack():
    global exp
    exp = exp[:-1]
    ui.text.setText(exp)

def clkCE():
    global exp
    num , m = lastNumber(exp)
    if m == len(exp) :
        clkDel()
    else :
        if m == 0:
            exp = exp[:-1]
        else:
            exp = exp[:-m]
        ui.text.setText(exp)

def clkRad():
    global exp
    num , m = lastNumber(exp)
    exp = exp[:-m]
    exp += 'math.sqrt('
    exp += num
    exp += ')'
    ui.text.setText(exp)


def clkMemory():
    global memory , exp
    global ismem
    if ismem == False :
        ismem = True
        ui.text.setText(memory)
    elif ismem == True:
        ismem = False
        ui.text.setText(exp)

def clkMemoryStore():
    global memory , exp
    num , m = lastNumber(exp)
    memory = num

def clkMemoryRecall():
    global memory , exp
    num , m = lastNumber(exp)
    exp = exp[:-m]
    exp += memory
    ui.text.setText(exp)

def clkMemoryClear():
    global memory
    memory = ""

def clkMemoryPlus():
    global memory , exp
    num , m = lastNumber(exp)
    num = int(num)
    memory = int(memory)
    memory += num
    memory = str(memory)
    return memory

def clkMemoryMinus():
    global memory , exp
    num , m = lastNumber(exp)
    num = int(num)
    memory = int(memory)
    memory -= num
    memory = str(memory)
    return memory

def clik(x):
    global exp
    x = str(x)
    exp += x
    ui.text.setText(exp)

app = QtWidgets.QApplication([])
ui = QtUiTools.QUiLoader().load("form.ui")

ui.button0.clicked.connect(lambda: clik(0))
ui.button1.clicked.connect(lambda: clik(1))
ui.button2.clicked.connect(lambda: clik(2))
ui.button3.clicked.connect(lambda: clik(3))
ui.button4.clicked.connect(lambda: clik(4))
ui.button5.clicked.connect(lambda: clik(5))
ui.button6.clicked.connect(lambda: clik(6))
ui.button7.clicked.connect(lambda: clik(7))
ui.button8.clicked.connect(lambda: clik(8))
ui.button9.clicked.connect(lambda: clik(9))

ui.add.clicked.connect(clkAdd)
ui.sub.clicked.connect(clkSub)
ui.mul.clicked.connect(clkMul)
ui.div.clicked.connect(clkDiv)
ui.decimal.clicked.connect(clkDot)
ui.percentage.clicked.connect(clkPre)
ui.power.clicked.connect(clkPow)
ui.fraction.clicked.connect(clkFrac)
ui.radical.clicked.connect(clkRad)
ui.even.clicked.connect(clkEven)
ui.back.clicked.connect(clkBack)
ui.dele.clicked.connect(clkDel)
ui.ce.clicked.connect(clkCE)

ui.memory.clicked.connect(clkMemory)
ui.memoryStore.clicked.connect(clkMemoryStore)
ui.memoryRecall.clicked.connect(clkMemoryRecall)
ui.memoryClear.clicked.connect(clkMemoryClear)
ui.memoryPlus.clicked.connect(clkMemoryPlus)
ui.memoryMinus.clicked.connect(clkMemoryMinus)

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

ui.add.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.sub.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.mul.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.div.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.decimal.setStyleSheet("background: #9f9f9f; border : 2px solid #5a5a5a")
ui.percentage.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.power.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.fraction.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.radical.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.back.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.even.setStyleSheet("background: #454545; color: white;border : 2px solid #5a5a5a")
ui.dele.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")
ui.ce.setStyleSheet("background: #454545; color: white; border : 2px solid #5a5a5a")

ui.memory.setStyleSheet("background: #000000; color: white; border : 2px solid #5a5a5a")
ui.memoryStore.setStyleSheet("background: #000000; color: white; border : 2px solid #5a5a5a")
ui.memoryRecall.setStyleSheet("background: #000000; color: white; border : 2px solid #5a5a5a")
ui.memoryClear.setStyleSheet("background: #000000; color: white; border : 2px solid #5a5a5a")
ui.memoryPlus.setStyleSheet("background: #000000; color: white; border : 2px solid #5a5a5a")
ui.memoryMinus.setStyleSheet("background: #000000; color: white; border : 2px solid #5a5a5a")

ui.text.setStyleSheet("background: #c6c6c6; font-size: 14px; border : 2px solid #5a5a5a")

ui.show()
app.exec_()

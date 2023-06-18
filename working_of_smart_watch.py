import tkinter 
import threading 
import time
import math
from textblob import TextBlob
import pytz
import datetime
import speech_recognition as sr
import pyttsx3

def start(): 
    global tim 
    if(f==False): 
         
       lbl.configure(text=str(tim)) 
       lbl.configure(anchor='center') 
       lbl.after(10, start) 
       tim=round(tim+0.01, 2)

def stop(): 
    global f 
    f=True 
 
def resume(): 
    global f 
    f=False 
    start() 
 
def reset(): 
    global f 
    global tim 
    f=True 
    tim=0 
    lbl.configure(text=str(tim)) 
    f=False

def howtouse(): 
    rules=tkinter.Tk() 
    rules.title('Rules of using stopwatch') 
     
    tkinter.Label(rules, text='HERE ARE THE RULES TO USE THE STOPWATCH:', font=('Times', 13)).pack() 
    tkinter.Label(rules, text='1. To start the stopwatch, press Start button.', font=('Times', 13)).pack() 
    tkinter.Label(rules, text='2. To stop the stopwatch, press Stop button.', font=('Times', 13)).pack() 
    tkinter.Label(rules, text='3. To resume the stopwatch, press Resume.', font=('Times', 13)).pack() 
    tkinter.Label(rules, text='4. Handle this stopwatch with care.', font=('Times', 13)).pack() 
    tkinter.Label(rules, text='5. This stopwatch counts milliseconds.', font=('Times', 13)).pack() 
    tkinter.Label(rules, text='6. To reset the watch, press Stop+Reset sequentially', font=('Times', 13)).pack() 
    tkinter.Label(rules, text='9. ENJOY', font=('Times', 13)).pack()

def lapse(): 
    global j 
    global i 
    m=tkinter.Label(watch,text="Lapse "+str(i)+" : "+str(tim), bg='yellow') 
    m.grid(row=j, column=1) 
    j=j+2 
    i=i+1

def add(): 
    x=float(e1.get()) 
    y=float(e2.get()) 
    z= x+y 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
def subtract(): 
    x=float(e1.get()) 
    y=float(e2.get()) 
    z= x-y 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
def multiply(): 
    x=float(e1.get()) 
    y=float(e2.get()) 
    z= x*y 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
def dvide(): 
    x=float(e1.get()) 
    y=float(e2.get()) 
    z= y/x 
    k=str(round(z, 4)) 
    m=tkinter.Label(c, text=k, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def power(): 
    x=float(e1.get()) 
    y=float(e2.get()) 
    z= math.pow(x, y) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def log(): 
    x=float(e1.get()) 
    y=float(e2.get()) 
    z= math.log(x,y) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def log10(): 
    x=float(e1.get()) 
     
    z=math.log(x,10) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def loge(): 
    x=float(e1.get()) 
     
    z= math.log(x) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def sine(): 
    x=float(e1.get()) 
     
    z= math.sin(x) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def cosine(): 
    x=float(e1.get()) 
     
    z= math.cos(x) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def tan(): 
    x=float(e1.get()) 
     
    z= math.tan(x) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def radian(): 
    x=float(e1.get()) 
     
    z= ((math.pi)*x)/(180) 
    m=tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange') 
    m.grid(row=3, column=1) 
 
def e(): 
    x=float(e1.get()) 
 
    z=math.exp(x) 
    tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
 
def pi(): 
    x=float(e1.get()) 
 
    z=(math.pi)**(x) 
    tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
 
def factorial(): 
    x=int(e1.get()) 
 
    z=math.factorial(x) 
    tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
 
def squareroot(): 
    x=float(e1.get()) 
 
    z=math.sqrt(x) 
    tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
 
def absolute(): 
    x=float(e1.get()) 
 
    z=math.fabs(x) 
    tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
 
def quadratic(): 
    p=tkinter.Tk() 
    tkinter.Label(p, text='a=', font='Helvetica', fg='black', background='green').grid(row=1, column=0) 
    tkinter.Label(p, text='b=', font='Helvetica', fg='black', background='green').grid(row=2, column=0) 
    tkinter.Label(p, text='c=', font='Helvetica', fg='black', background='green').grid(row=3, column=0) 
    at=tkinter.Entry(p) 
    a2=tkinter.Entry(p) 
    a3=tkinter.Entry(p) 
    at.grid(row=1, column=1) 
    a2.grid(row=2, column=1) 
    a3.grid(row=3, column=1) 
 
    a=float(at.get()) 
    b=float(a2.get()) 
    c=float(a3.get()) 
 
    D= (b*b - 4*a*c)**(1/2) 
 
    x1=( -b+D)/(2*a) 
    x2=( -b-D)/(2*a) 
 
    tkinter.Label(p, text=x1, font='Helvetica', fg='green', background='green').grid(row=5, column=1) 
    tkinter.Label(p, text=x2, font='Helvetica', fg='green', background='green').grid(row=6, column=1) 
 
 
def arcsine(): 
    x=float(e1.get()) 
 
    z=math.asin(x) 
    tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
 
def arccosine(): 
     x=float(e1.get()) 
 
     z=math.acos(x) 
     tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
 
def arctan(): 
    x=float(e1.get()) 
 
    z=math.atan(x) 
    tkinter.Label(c, text=z, font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
     
     
     
def shift(): 
    button1=tkinter.Button(c, text='arcsin(x)', background='white', font='Times', command=arcsine) 
    button1.grid(row=7, column=3) 
 
    button1=tkinter.Button(c, text='arccos(x)', background='white', font='Times', command=arccosine) 
    button1.grid(row=8, column=0) 
 
    button1=tkinter.Button(c, text='arctan(x)', background='white', font='Times', command=arctan) 
    button1.grid(row=8, column=1) 
 
def reverse(): 
    button1=tkinter.Button(c, text='sine(x)', background='white', font='Times', command=sine) 
    button1.grid(row=7, column=3) 
 
    button1=tkinter.Button(c, text='cosine(x)', background='white', font='Times', command=cosine) 
    button1.grid(row=8, column=0) 
 
    button1=tkinter.Button(c, text='tangent(x)', background='white', font='Times', command=tan) 
    button1.grid(row=8, column=1) 
 
def cancel(): 
    return c.destroy() 
 
def clear(): 
    n=tkinter.Label(c, text='                                                                                               ', background='orange') 
    n.grid(row=3, column=1) 
 
def T(): 
    aman=tkinter.Tk() 
    aman.title('ABOUT THIS CALCULATOR') 
    aman.configure(background='orange') 
    tkinter.Label(aman, text='Brought to you by PRANAV and RAMTEJA', font='Helvetica', fg='black', background='orange').grid(row=1, column=1) 
    tkinter.Label(aman, text='RULES :', font='Helvetica', fg='black', background='orange').grid(row=2, column=1) 
    tkinter.Label(aman, text='there are opearations like add , subtract and so on  ', font='Helvetica', fg='black', background='orange').grid(row=3, column=1) 
    tkinter.Label(aman, text='we can also find inverse functions by clicking on shift button', font='Helvetica', fg='black', background='orange').grid(row=4, column=1) 
    tkinter.Label(aman, text='clear option is used to clear the values which was displayed on to the screen', font='Helvetica', fg='black', background='orange').grid(row=5, column=1) 
    tkinter.Label(aman, text='cancel is used to close the window ', font='Helvetica', fg='black', background='orange').grid(row=6, column=1)
    tkinter.Label(aman, text='return option is used to again change the option from inverse to normal function', font='Helvetica', fg='black', background='orange').grid(row=7, column=1)     
    tkinter.Label(aman, text='Thank You For Using!', font='Helvetica', fg='black', background='orange').grid(row=8, column=1) 
 
    button9=tkinter.Button(aman, text='Done', font='Times', fg='black', background='green', command=aman.destroy) 
    button9.grid(row=9, column=1) 
print("        welcome to smart watch working    ")
print("do you want to search through voice or keyboard ...??")
print("1.voice\n2.keyboard\n")
m=int(input())
if(m==1):
    print("choose the below given options")
    print("\n 1.stopwatch\n 2.autocorrection\n 3.calculator\n 4.timeconversion\n ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("please talk")
        audio = r.listen(source)
    try:
        n=r.recognize_google(audio)
        print("recognising")
        print(n)

    except sr.UnknownValueError:
        print("google cannot understand your audio")
    except sr.RequestError as e:
        print("cannot request results from google ; [0]".format(e)) 
else:
    print("choose the below given options")
    print("\n 1.stopwatch\n 2.autocorrection\n 3.calculator\n 4.timeconversion\n ")
    n=input()

if(n=="stop watch" or n=="stopwatch"):
    watch=tkinter.Tk()
    watch.geometry("700x700")
    watch.title(" Stopwatch")
    watch.configure(background='yellow')
    tim=0
    f=False
    tkinter.Label(watch, text='  ', bg='yellow').grid(row=1, column=0)
    tkinter.Label(watch, text='  ', bg='yellow').grid(row=2, column=0)
    tkinter.Label(watch, text='  ', bg='yellow').grid(row=4, column=0)
    tkinter.Label(watch, text='  ', bg='yellow').grid(row=8, column=0)
    tkinter.Label(watch, text='  ', bg='yellow').grid(row=6, column=0)
    tkinter.Label(watch, text='  ', bg='yellow').grid(row=10, column=0)
    lbl=tkinter.Label(watch, text='Stopwatch', font=('Times', 12), fg='black',bg='yellow')
    lbl.grid(row=1, column=1)
    lbl2=tkinter.Label(watch, text='Time',font=('Times',12), bg='yellow',fg='black')
    lbl2.grid(row=1, column=2)
    j=18
    i=1

    button1=tkinter.Button(watch, text='Start Stopwatch', command=start, activebackground='green',bg='green', fg='black')
    button1.grid(row=4, column=1)
    button2=tkinter.Button(watch, text='Stop Stopwatch', command=stop, activebackground='red',bg='red', fg='black')
    button2.grid(row=6, column=1)
    button3=tkinter.Button(watch, text='Resume Stopwatch', command=resume, activebackground='blue',bg='blue', fg='black')
    button3.grid(row=8, column=1)
    button4=tkinter.Button(watch, text='How to Use?', command=howtouse, activebackground='white',bg='white', fg='black')
    button4.grid(row=2, column=1)
    button5=tkinter.Button(watch, text='Reset Stopwatch',command=reset, activebackground='yellow',bg='yellow', fg='black')
    button5.grid(row=10, column=1)
    button6=tkinter.Button(watch, text='Lapse',command=lapse, activebackground='blue',bg='blue', fg='black')
    button6.grid(row=12,column=1)

elif(n=="auto correction" or n=="autocorrection"):
    string=input("enter the string :")
    text=TextBlob(string)
    b=""
    a=text.correct()
    for i in a:
        b+=i
    b=b[0].capitalize()+b[1:]
    print(b)

elif(n=="calculator"):
    c=tkinter.Tk()
    c.configure(width='1000', height='1000')
    c.title("Calculator")
    c.configure(background='orange')

    tkinter.Label(c, text='x=', font='Times', background='orange', fg='green').grid(row=1, column=0)
    e1=tkinter.Entry(c, fg='brown', font='Helvetica')
    e1.grid(row=1, column=1)
    tkinter.Label(c, text='y=', font='Times', background='orange', fg='green').grid(row=2, column=0)
    e2=tkinter.Entry(c, fg='brown', font='Helvetica')
    e2.grid(row=2, column=1)
    tkinter.Label(c, text='Your result is:', font='Times', background='orange', fg='green').grid(row=3, column=0) 
    
    button1=tkinter.Button(c, text='Clear', background='white', font='Times', command=clear)
    button1.grid(row=5, column=0)

    button1=tkinter.Button(c, text='Shift', background='white', font='Times', command=shift)
    button1.grid(row=5, column=1)

    button1=tkinter.Button(c, text='Return', background='white', font='Times', command=reverse)
    button1.grid(row=5, column=2)

    button1=tkinter.Button(c, text='Cancel', background='white', font='Times', command=cancel)
    button1.grid(row=5, column=3)

    button1=tkinter.Button(c, text='x+y', background='white', font='Times', command=add)
    button1.grid(row=6, column=0)

    button1=tkinter.Button(c, text='x-y', background='white', font='Times', command=subtract)
    button1.grid(row=6, column=1)

    button1=tkinter.Button(c, text='x*y', background='white', font='Times', command=multiply)
    button1.grid(row=6, column=2)

    button1=tkinter.Button(c, text='y/x', background='white', font='Times', command=dvide)
    button1.grid(row=6, column=3)

    button1=tkinter.Button(c, text='x^y', background='white', font='Times', command=power)
    button1.grid(row=7, column=0)

    button1=tkinter.Button(c, text='log(x)', background='white', font='Times', command=log10)
    button1.grid(row=7, column=1)

    button1=tkinter.Button(c, text='In(x)', background='white', font='Times', command=loge)
    button1.grid(row=7, column=2)

    button1=tkinter.Button(c, text='sine(x)', background='white', font='Times', command=sine)
    button1.grid(row=7, column=3)

    button1=tkinter.Button(c, text='cosine(x)', background='white', font='Times', command=cosine)
    button1.grid(row=8, column=0)

    button1=tkinter.Button(c, text='tangent(x)', background='white', font='Times', command=tan)
    button1.grid(row=8, column=1)

    button1=tkinter.Button(c, text='e^x', background='white', font='Times', command=e)
    button1.grid(row=8, column=2)

    button1=tkinter.Button(c, text='x!', background='white', font='Times', command=factorial)
    button1.grid(row=8, column=3)

    button1=tkinter.Button(c, text='|x|', background='white', font='Times', command=absolute)
    button1.grid(row=9, column=0)

    button1=tkinter.Button(c, text='log(x) base y', background='white', font='Times', command=log)
    button1.grid(row=9, column=1)

    button1=tkinter.Button(c, text='pi^x', background='white', font='Times', command=pi)
    button1.grid(row=9, column=2)

    button1=tkinter.Button(c, text='sqrt(x)', background='white', font='Times', command=squareroot)
    button1.grid(row=9, column=3)

    button1=tkinter.Button(c, text='T&C', background='white', font='Times', command=T)
    button1.grid(row=10, column=1)

elif(n=="time conversion" or n=="timeconversion" or n=="conversion"):
    year=int(input("enter the year :"))
    month=int(input("enter the month :"))
    day=int(input("enter the date :"))
    hour=int(input("enter the hour :"))
    minute=int(input("enter the minute :"))

    users_time=datetime.datetime(year,month,day,hour,minute)

    cairo_timezone=pytz.timezone('Africa/Cairo')
    london_timezone=pytz.timezone('UTC')
    delhi_timezone=pytz.timezone('Asia/Kolkata')
    sydney_timezone=pytz.timezone('Australia/Sydney')
    

    cairo_time=pytz.utc.localize(users_time).astimezone(cairo_timezone)
    london_time=pytz.utc.localize(users_time).astimezone(london_timezone)
    delhi_time=pytz.utc.localize(users_time).astimezone(delhi_timezone)
    sydney_time=pytz.utc.localize(users_time).astimezone(sydney_timezone)



    print("current location time :",users_time)

    print("cairo time :",cairo_time.isoformat())
    print("london time :",london_time.isoformat())
    print("new delhi time :",delhi_time.isoformat())
    print("sydney time :",sydney_time.isoformat())
        
else:
    print("enter the correct choice")
    
    

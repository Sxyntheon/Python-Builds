from tkinter import *

root = Tk()                 #create window
root.title("Mathe Doktor")  #define window-name


points = 0  #define points



exercise1 = Label(root, text="6 x ? = 48")  #create exercise 1
exercise2 = Label(root, text="3 x ? = 21")  #create exercise 2
exercise3 = Label(root, text="5 x ? = 25")  #create exercise 3
exercise4 = Label(root, text="9 x ? = 81")  #create exercise 4
exercise5 = Label(root, text="8 x ? = 32")  #create exercise 5
exercise6 = Label(root, text="10 x ? = 60") #create exercise 6
exercise7 = Label(root, text="3 x ? = 18")  #create exercise 7
exercise8 = Label(root, text="5 x ? =  15") #create exercise 8
exercise9 = Label(root, text="4 x ? = 4")   #create exercise 9
exercise10 = Label(root, text="6 x ? = 36") #create exercise 10
################################################################################
exercise1.grid(row=0)  #visualize exercise
num = Entry(root)   #create input
num.grid(row=1)     #visualize input
x = 48 / 6          #define solution

def solve_exercise1():            #complain input with solution and give output
    try:
        if int(num.get()) == x:
            global right
            right = Label(text=num.get() + " ist richtig!")    #define right-answer output
            right.grid(row=4)                                  #visualize right-answer output
            command = submit1.destroy()                        #destroy submit-button
            global points                                      #define points as global
            points += 1                                        #add 1 to points
            try:
                global error
                error.destroy()
            except:
                pass
        else:
            global false
            false = Label(text=num.get() + " ist falsch")      #define false-answer output
            false.grid(row=4)                                  #visualize false-answer output
            command = submit1.destroy()                        #destroy submit button
            show_right_answer_btn1.grid(row=5)                 #visualize show-solution button
            try:
                error.destroy()
            except:
                pass
    except:
        error = Label(root, text="Das ist keine gültige Zahl")      #define error
        error.grid(row=5)                                           #visualize error

def solve_exercise2():            #complain input with solution and give output
    try:
        if int(num.get()) == x:
            global right
            right = Label(text=num.get() + " ist richtig!")    #define right-answer output
            right.grid(row=4)
            global submit2                                 #visualize right-answer output
            command = submit2.destroy()                         #destroy submit-button
            try:
                global error
                error.destroy()                                     #destroy error
            except:
                pass
            global points                                       #define points as global
            points += 1                                         #add 1 to points
        else:
            global false
            false = Label(text=num.get() + " ist falsch")      #define false-answer output
            false.grid(row=4)                                  #visualize false-answer output
            command = submit2.destroy()                         #destroy submit button
            try:
                error.destroy()                                     #destroy error
            except:
                pass
            points -= 1
            show_right_answer_btn2.grid(row=5)                   #visualize show-solution button
    except:
        error = Label(root, text="Das ist keine gültige Zahl")      #define error
        error.grid(row=5)

def solve_exercise3():            #complain input with solution and give output
    try:
        if int(num.get()) == x:
            global right
            right = Label(text=num.get() + " ist richtig!")    #define right-answer output
            right.grid(row=4)                                  #visualize right-answer output
            global submit3
            command = submit3.destroy()                         #destroy submit-button
            try:
                global error
                error.destroy()                                     #destroy error
            except:
                pass
            global points                                       #define points as global
            points += 1                                         #add 1 to points
        else:
            global false
            false = Label(text=num.get() + " ist falsch")      #define false-answer output
            false.grid(row=4)                                  #visualize false-answer output
            command = submit3.destroy()                         #destroy submit button
            try:
                error.destroy()                                     #destroy error
            except:
                pass
            points -= 1
            show_right_answer_btn3.grid(row=5)                   #visualize show-solution button
    except:
        error = Label(root, text="Das ist keine gültige Zahl")      #define error
        error.grid(row=5)

def solve_exercise4():            #complain input with solution and give output
    try:
        if int(num.get()) == x:
            global right
            right = Label(text=num.get() + " ist richtig!")    #define right-answer output
            right.grid(row=4)                                  #visualize right-answer output
            global submit4
            command = submit4.destroy()                         #destroy submit-button
            try:
                global error
                error.destroy()                                     #destroy error
            except:
                pass
            global points                                       #define points as global
            points += 1                                         #add 1 to points
        else:
            global false
            false = Label(text=num.get() + " ist falsch")      #define false-answer output
            false.grid(row=4)                                  #visualize false-answer output
            command = submit4.destroy()                         #destroy submit button
            try:
                error.destroy()                                     #destroy error
            except:
                pass
            points -= 1
            show_right_answer_btn4.grid(row=5)                   #visualize show-solution button
    except:
        error = Label(root, text="Das ist keine gültige Zahl")      #define error
        error.grid(row=5)

submit1 = Button(root, text="Antwort bestätigen", command=solve_exercise1)      #define solve-button
submit2 = Button(root, text="Antwort bestätigen", command=solve_exercise2)      #define new solve-button
submit3 = Button(root, text="Antwort bestätigen", command=solve_exercise3)      #define new solve-button
submit4 = Button(root, text="Antwort bestätigen", command=solve_exercise4)      #define new solve-button
#submit5 = Button(root, text="Antwort bestätigen", command=solve_exercise5)      #define new solve-button
#submit6 = Button(root, text="Antwort bestätigen", command=solve_exercise6)      #define new solve-button
#submit7 = Button(root, text="Antwort bestätigen", command=solve_exercise7)      #define new solve-button
#submit8 = Button(root, text="Antwort bestätigen", command=solve_exercise8)      #define new solve-button
#submit9 = Button(root, text="Antwort bestätigen", command=solve_exercise9)      #define new solve-button
#submit10 = Button(root, text="Antwort bestätigen", command=solve_exercise10)     #define new solve-button

submit1.grid(row=2)                    #visualize solve-button


def go_to_exercise2():                          #define go to next exercise
    exercise1.destroy()                         #destroy old exercise
    submit1.destroy()                           #destroy old submit-button
    global right                                #destroy old right-answer output
    try:
        right.destroy()
    except:
        pass
    global false                                #destroy old false-answer output
    try:
        false.destroy()
    except:
        pass
    next_exercise2.destroy()                    #destroy old next-exercise-button
    global show_right_answer_btn1               #destroy old show-right-answer-button
    try:
        show_right_answer_btn1.destroy()
    except:
        pass
    global right_answer1                        #destroy old solution
    try:
        right_answer1.destroy()
    except:
        pass
    global x
    x = 21 / 3                                  #define new solution
    exercise2.grid(row=0)                       #visualize new exercise
    submit2.grid(row=2)
    next_exercise3.grid(row=7)
def go_to_exercise3():                          #define go to next exercise
    exercise2.destroy()                         #destroy old exercise
    submit2.destroy()                           #destroy old submit-button
    global right                                #destroy old right-answer output
    try:
        right.destroy()
    except:
        pass
    global false                                #destroy old false-answer output
    try:
        false.destroy()
    except:
        pass
    next_exercise3.destroy()                    #destroy old next-exercise-button
    global show_right_answer_btn2               #destroy old show-right-answer-button
    try:
        show_right_answer_btn2.destroy()
    except:
        pass
    global right_answer2                        #destroy old solution
    try:
        right_answer2.destroy()
    except:
        pass
    global x
    x = 25 / 5                                  #define new solution
    exercise3.grid(row=0)                       #visualize new exercise
    submit3.grid(row=2)
    next_exercise4.grid(row=7)
def go_to_exercise4():                          #define go to next exercise
    exercise3.destroy()                         #destroy old exercise
    submit3.destroy()                           #destroy old submit-button
    global right                                #destroy old right-answer output
    try:
        right.destroy()
    except:
        pass
    global false                                #destroy old false-answer output
    try:
        false.destroy()
    except:
        pass
    next_exercise4.destroy()                    #destroy old next-exercise-button
    global show_right_answer_btn3               #destroy old show-right-answer-button
    try:
        show_right_answer_btn3.destroy()
    except:
        pass
    global right_answer3                        #destroy old solution
    try:
        right_answer3.destroy()
    except:
        pass
    global x
    x = 81 / 9                                  #define new solution
    exercise4.grid(row=0)                       #visualize new exercise
    submit4.grid(row=2)
    #next_exercise5.grid(row=7)
next_exercise2 = Button(root, text="Nächste Aufgabe", command=go_to_exercise2)
next_exercise3 = Button(root, text="Nächste Aufgabe", command=go_to_exercise3)
next_exercise4 = Button(root, text="Nächste Aufgabe", command=go_to_exercise4)

def show_right_answer1():            #define show solution
    global right_answer1
    right_answer1 = Label(root, text="Die richtige Antwort lautet " + str(int(x)))
    right_answer1.grid(row=6)
    command = show_right_answer_btn1.destroy()
def show_right_answer2():            #define show solution
    global right_answer2
    right_answer2 = Label(root, text="Die richtige Antwort lautet " + str(int(x)))
    right_answer2.grid(row=6)
    command = show_right_answer_btn2.destroy()
def show_right_answer3():            #define show solution
    global right_answer3
    right_answer3 = Label(root, text="Die richtige Antwort lautet " + str(int(x)))
    right_answer3.grid(row=6)
    command = show_right_answer_btn3.destroy()
def show_right_answer4():            #define show solution
    global right_answer4
    right_answer4 = Label(root, text="Die richtige Antwort lautet " + str(int(x)))
    right_answer4.grid(row=6)
    command = show_right_answer_btn4.destroy()

show_right_answer_btn1 = Button(root, text="Lösung", command=show_right_answer1) # define show-solution button
show_right_answer_btn2 = Button(root, text="Lösung", command=show_right_answer2) # define show-solution button
show_right_answer_btn3 = Button(root, text="Lösung", command=show_right_answer3) # define show-solution button
show_right_answer_btn4 = Button(root, text="Lösung", command=show_right_answer4) # define show-solution button



next_exercise2.grid(row=7)
root.mainloop()

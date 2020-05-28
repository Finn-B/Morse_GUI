import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font
from tkinter import messagebox

# USE GPIO NUMBERS NOT PIN NUMBERS
GPIO.setmode(GPIO.BCM)

# PIN DEFINITION
led = 18

#GPIO SETUP
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)


# MORSE CODE TIME DEFINITIONS
dot_length = 0.3
dash_length = 0.9

# MORSE CODE DICT
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

# FUNCITON DEFINITIONS
def convert_to_morse():
    led_code = string_to_blink.get()
    if (len(led_code)>12):
        messagebox.showinfo("Error", "Please only type a word up to 12 characters!")
    else:
        for letter in led_code:
            if letter.upper() in CODE:
                for component in CODE[letter.upper()]:
                    if component == '-':
                        dash()
                    elif component == '.':
                        dot()
                    else:
                        time.sleep(dash_length)
            else:
                messagebox.showinfo("Error", "Please only type valid characters!")

def dot():
    print(". ")
    GPIO.output(led, GPIO.HIGH)
    time.sleep(dot_length)
    GPIO.output(led, GPIO.LOW)
    time.sleep(dot_length)


def dash():
    print("- ")
    GPIO.output(led, GPIO.HIGH)
    time.sleep(dash_length)
    GPIO.output(led, GPIO.LOW)
    time.sleep(dot_length)


def close():
    GPIO.cleanup()
    win.destroy()

# GUI DEFINITIONS
win = Tk()
win.title("5.3D RPI - Blink Morse Code Using GUI")
myFont1 = tkinter.font.Font(family = 'Arial', size = 12, weight = "bold", underline = 1)
myFont2 = tkinter.font.Font(family = 'Arial', size = 10)
win.geometry("330x120")

# WIDGET DEFINITIONS
gui_title_label = Label(win, text = 'Text to Morse Code with LED', font = myFont1, bg = "#DDDDDD")
string_label = Label(win, text = 'Type a word up to 12 Characters', font = myFont2, bg = "#DDDDDD")
string_to_blink = Entry(win, font = myFont2, width = 18)
convert_button = Button(win, text = 'Blink Morse Code', font = myFont2, command = convert_to_morse, bg = "green")
exit_button = Button(win, text = 'Exit', font = myFont2, command = close, bg = 'red')

# DRAW GUI + WIDGETS
gui_title_label.grid(row = 0, column = 0, columnspan = 2)
string_label.grid(row = 1, column = 0)
string_to_blink.grid(row = 1, column = 1)
convert_button.grid(row = 2, column = 0, columnspan = 2)
exit_button.grid(row = 3, column = 0, columnspan = 2)

win.protocol("WM_DELETE_WINDOW", close) #EXIT CLEANLY

win.mainloop() #LOOP FOREVER
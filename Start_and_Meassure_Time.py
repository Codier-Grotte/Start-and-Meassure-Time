from ctypes import sizeof
from email.mime import image
from fileinput import filename
import tkinter as tk
from tkinter import Button, filedialog, Text, ttk
import os  # ermöglicht app auszuführen
import os.path # Dient zur Pfadsuche
from tkinter import font
from turtle import bgcolor, width
import customtkinter as ctk
from PIL import Image, ImageTk
import webbrowser


ctk.set_default_color_theme("blue")

root = tk.Tk()

apps = []

running = False

hours, minutes, seconds = 0, 0, 0

root.title("SaMT")

save_path = "C:/Users/Bigby.DESKTOP-JQSV84T/Desktop/Projekte/Main/save"

file_name = "saved_apps.txt"

completeName = os.path.join(save_path, file_name)

new = 1

url = "https://www.codier-grotte.org"

def openweb():
    webbrowser.open(url,new=new)



def delete_listed_apps():                           # Löscht gespeicherte start Liste

    if os.path.exists(completeName):
        os.remove(completeName)
    else:
        print("The file does not exist") 



def start():                                        # Startet Timer
    global running
    if not running:
        update()
        running = True


def pause():                                        # Pausiert Timer
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False


def reset():                                        # Stellt Timer zurück
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    stopwatch_label.config(text='00:00:00')


def update():                                       # Stoppuhr
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    global update_time
    update_time = stopwatch_label.after(1000, update)


stopwatch_label = ctk.CTkLabel(text='00:00:00', text_font=('Calibri', 70), corner_radius=20, width=500, height=140) # Erscheinungsbild für die Stoppuhr
stopwatch_label.configure(fg_color="#5cb9f2", text_color="#F2F2F2", bg_color="#242540")
stopwatch_label.place(x=90, y=-20)


if os.path.isfile(completeName):                    # Liest die gespeicherte Liste zum ausführen der Apps
    with open(completeName, "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]



def addApp():                                       # Fügt Apps der Liste hinzu


    for widget in frame.winfo_children():
        widget.destroy()


    filename= filedialog.askopenfilename(initialdir="/", title="Select File",           # Aussuchbare .exe
    filetypes=(("executables" ,"*.exe"), ("all files", "*.*")))
                                                    

    apps.append(filename)                           # Abbildung der Speicherpfade 
    for app in apps:

        label = ctk.CTkLabel(frame, text=app, text_font=("Calibri", 14), text_color="black")
    
        label.pack()


def time_app():                                     # Kombiniert funktionen start() und runApps() = 2 Funktionen, 1 Knopfdruck
    start()
    runApps()


def saving_list():                                  # Speichert die einzelnen Apps
    with open(completeName, "w") as f:
        for app in apps:
            f.write(app + ",")


def runApps():                                      # Führt die gespeicherten Apps aus
    for app in apps:
        os.startfile(app)


root.geometry("900x600")

root.configure(bg="#1a2e40")

root.resizable(0, 0)                                # Fenstereinstellungen


frame_bg = ctk.CTkLabel(root, bg_color="#1a2e40", corner_radius=10, fg_color="#5cb9f2", text="")
frame_bg.place(height=350, width=580, x=90, y=150)  # Hintergrund der angezeigten Anwendungen


frame_bg_2 = ctk.CTkLabel(root, bg_color="#f0f0f0", fg_color="#f0f0f0", text="")
frame_bg_2.place(height=330, width=560, x=100, y=160)# Innere Box der angezeigten Anwendungen

frame = tk.Label(root)
frame.place(x=100, y=170)                           # Verantwortlich für die App Liste
                        

button_bg = ctk.CTkLabel(root, text="", corner_radius=10)
button_bg.configure(bg_color="#1a2e40", fg_color="#5cb9f2", width=230, height=350)
button_bg.place(x=710, y=150)                       # Hintergrund der Buttons, rechte Seite


logo_img = Image.open("logo.png")
logo_img2 = ImageTk.PhotoImage(logo_img)
logo = tk.Button(root, image=logo_img2, borderwidth=0, background="#1a2e40", command=openweb, activebackground="#1a2e40")
logo.place(x=775, y=50)                             # Logo platzierung


add_Apps = ctk.CTkButton(root, text="Add apps", command=addApp, text_font=('Calibri', 14), corner_radius=10)
add_Apps.configure(fg_color="#06080d", text_color="#F2F2F2", width=150, height=40, bg_color="#5cb9f2", hover_color="#0A4DA6")
add_Apps.place(x=730, y=180)                        # Darstellung des "Add apps" Button


runApp = ctk.CTkButton(root, text="Run apps", command=time_app, text_font=('Calibri', 14), corner_radius=10)
runApp.configure(fg_color="#06080d", text_color="#F2F2F2", width=150, height=40, bg_color="#5cb9f2", hover_color="#0A4DA6")
runApp.place(x=730, y=230)                          # Darstellung des "Run apps" Button


pause_timer = ctk.CTkButton(root, text="Pause timer", command=pause, text_font=('Calibri', 14), corner_radius=10)
pause_timer.configure(fg_color="#06080d", text_color="#F2F2F2", width=150, height=40, bg_color="#5cb9f2", hover_color="#0A4DA6")
pause_timer.place(x=730, y=280)                     # Darstellung des "Pause timer" Button


reset_timer = ctk.CTkButton(root, text="Reset timer", command=reset, text_font=('Calibri', 14), corner_radius=10)
reset_timer.configure(fg_color="#06080d", text_color="#F2F2F2", width=150, height=40, bg_color="#5cb9f2", hover_color="#0A4DA6")
reset_timer.place(x=730, y=330)                     # Darstellung des "Reset timer" Button


delete_listed_apps = ctk.CTkButton(root, text="Delete list", command=delete_listed_apps, text_font=('Calibri', 14), corner_radius=10)
delete_listed_apps.configure(fg_color="#06080d", text_color="#F2F2F2", width=150, height=40, bg_color="#5cb9f2", hover_color="#0A4DA6")
delete_listed_apps.place(x=730, y=380)              # Darstellung des "Delete list" Button


saving_list = ctk.CTkButton(root, text="Save list", command=saving_list, text_font=('Calibri', 14), corner_radius=10)
saving_list.configure(fg_color="#06080d", text_color="#F2F2F2", width=150, height=40, bg_color="#5cb9f2", hover_color="#0A4DA6")
saving_list.place(x=730, y=430)                     # Darstellung des "Save list" Button


for app in apps:
    label = ctk.CTkLabel(frame, text=app, text_font=("Calibri", 14), text_color="black")
    
    label.pack()                                    # Hängt mit der Abbildung der Speicherpfade zusammen


root.mainloop()


 




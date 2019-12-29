import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from PIL import ImageTk, Image
from tkinter import *
import cv2
import easygui  
import csv
import pickle
from gpiozero import Button
import time
from picamera import PiCamera
import threading
import subprocess
#import output

camera = PiCamera()
camera.resolution = (320,320)


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.PlayerTwo=PhotoImage("file=2.png")
        self.PlayerThree=PhotoImage("file=3.png")
        self.PlayerFour=PhotoImage("file=4.png")
        label = tk.Label(self,text="CHOOSE THE NUMBER OF PLAYERS THAT WILL BE PLAYING",
                             fg="white",
                             bg="#85C1E9").pack(fill="x",ipady=40)

        button1 = tk.Button(self, text="CLICK HERE TO START THE GAME", 
                                command=lambda: master.switch_frame(PageOne)).pack(fill="x",ipady=40)
        button2 = tk.Button(self, image=self.PlayerTwo, command=lambda: master.switch_frame(PageTwo)).pack(ipadx=15, side="left", ipady=10)
        button3 = tk.Button(self, image=self.PlayerThree, command=lambda: master.switch_frame(PageThree)).pack(ipadx=15, side="left", ipady=10)
        button4 = tk.Button(self, image=self.PlayerFour, command=lambda: master.switch_frame(PageFour)).pack(ipadx=20, side="left", ipady=10)



        
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        with open("players.txt", "r") as text_file :
                message = text_file.read()
                self.players = message.split()

        if len(self.players) == 2:
            button = tk.Button(self, text="Go to the start page",
                           command=lambda: master.switch_frame(StartPage))
            button.grid(column = 0,row=2)
            text_file = open("players.txt", "r")
            message = text_file.read()
            players = message.split()
            Player1 = self.players[0]  
            Player2 = self.players[1]
            player1 = tk.Label(self,
                                 text=Player1,
                                 font="Times 45",
                                 fg="white",
                                 bg="#0000FF")
            player1.grid(row=0, column=0)
            player1.config(width=8)

            player2 = tk.Label(self,
                                 text=Player2,
                                 font="Times 45",
                                 fg="white",
                                 bg="#FF0000")
            player2.grid(row=0, column=1)
            player2.config(width=8)


            text1 = tk.Text(self, height=20, width=30)
            text1.grid(column=0, row=1, sticky='N')

            text2 = tk.Text(self, height=20, width=30)
            text2.grid(column=1, row=1, sticky='N')

            proc = output.ImageProcess()

            camera.capture('/home/pi/Desktop/Test/lets.jpg')
            img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")
            print(proc.calibrate_board(img))

            button = Button(6)

            def image_capture():
              global globvar
              globvar = -1
              proc = output.ImageProcess()
              while True:
                  button.wait_for_press()
                  globvar += 1
                  camera.capture('/home/pi/Desktop/Test/lets.jpg')
                  img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")

                  print(proc.frame_table(img))
                    
                  player_number = globvar%len(self.players)

                  print(player_number)
                    
                  pickle_in = open("game_file.pickle","rb")
                  example_dict = pickle.load(pickle_in)
                  player1_words = []
                  player1_score = []
                  player2_words = []
                  player2_score = []

                  if player_number == 0:
                      text1.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player != 1:
                              player1_words.append(key)
                              player1_score.append(value)
                      players1 = list(zip(player1_words,player1_score))
                      print(players1)
                      text1.insert(tk.INSERT,players1)
                      total_score1 = sum(player1_score)
                      player1.config(text = total_score1)

                      
                  if player_number == 1:
                      text2.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player != 0:
                              player2_words.append(key)
                              player2_score.append(value)
                      players2 = list(zip(player2_words,player2_score))
                      text2.insert(tk.INSERT,players2)
                      total_score2 = sum(player2_score)
                      player2.config(text = total_score2)
                  

            th= threading.Thread(target=image_capture) #initialise the thread
            th.setDaemon(True)
            th.start() #start the thread

        if len(self.players) == 3:
            button = tk.Button(self, text="Go to the start page",
                           command=lambda: master.switch_frame(StartPage))
            button.grid(column = 0,row=3)
            Player1 = self.players[0]  
            Player2 = self.players[1]
            Player3 = self.players[2]

            player1 = tk.Label(self,
                                 text=Player1,
                                 font="Times 45",
                                 fg="white",
                                 bg="#0000FF")
            player1.grid(row=0, column=0)
            player1.config(width=5,pady=17)

            player2 = tk.Label(self,
                             text=Player2,
                             font="Times 45",
                             fg="white",
                             bg="#FF0000")

            player2.grid(row=1, column=0)
            player2.config(width=5,pady=17)

            player3 = tk.Label(self,
                             text=Player3,
                             font="Times 45",
                             fg="white",
                             bg="#BDB76B")
            player3.grid(row=2, column=0)
            player3.config(width=5,pady=17)

            text1 = tk.Text(self, height=7, width=50)
            text1.grid(column=1, row=0, sticky='N')

            text2 = tk.Text(self, height=7, width=50)
            text2.grid(column=1, row=1, sticky='N')

            text3 = tk.Text(self, height=7, width=50)
            text3.grid(column=1, row=2, sticky='N')

            proc = output.ImageProcess()

            camera.capture('/home/pi/Desktop/Test/lets.jpg')
            img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")
            print(proc.calibrate_board(img))

            button = Button(6)

            def image_capture():
              global globvar
              globvar = -1
              proc = output.ImageProcess()
              while True:
                  button.wait_for_press()
                  globvar += 1
                  camera.capture('/home/pi/Desktop/Test/lets.jpg')
                  img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")

                  print(proc.frame_table(img))
                    
                  player_number = globvar%len(self.players)

                  print(player_number)

                  pickle_in = open("game_file.pickle","rb")
                  example_dict = pickle.load(pickle_in)
                  player1_words = []
                  player1_score = []
                  player2_words = []
                  player2_score = []
                  player3_words = []
                  player3_score = []

                  if player_number == 0:
                      text1.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player == 0:
                              player1_words.append(key)
                              player1_score.append(value)
                      players1 = list(zip(player1_words,player1_score))
                      print(players1)
                      text1.insert(tk.INSERT,players1)
                      total_score1 = sum(player1_score)
                      player1.config(text = total_score1)

                      
                  if player_number == 1:
                      text2.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player == 1:
                              player2_words.append(key)
                              player2_score.append(value)
                      players2 = list(zip(player2_words,player2_score))
                      text2.insert(tk.INSERT,players2)
                      total_score2 = sum(player2_score)
                      player2.config(text = total_score2)

                  if player_number == 2:
                      text3.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player == 2:
                              player3_words.append(key)
                              player3_score.append(value)
                      players3 = list(zip(player3_words,player3_score))
                      text3.insert(tk.INSERT,players3)
                      total_score3 = sum(player3_score)
                      player3.config(text = total_score3)
                  

            th= threading.Thread(target=image_capture) #initialise the thread
            th.setDaemon(True)
            th.start() #start the thread
            
        if len(self.players) == 4:
            button = tk.Button(self, text="Go to the start page",
                           command=lambda: master.switch_frame(StartPage))
            button.grid(column = 0,row=4)
            Player1 = self.players[0]  
            Player2 = self.players[1]
            Player3 = self.players[2]
            Player4 = self.players[3]

            player1 = tk.Label(self,
                                 text=Player1,
                                 font="Times 45",
                                 fg="white",
                                 bg="#0000FF")
            player1.grid(row=0, column=0)
            player1.config(width=5,pady=4)

            player2 = tk.Label(self,
                             text=Player2,
                             font="Times 45",
                             fg="white",
                             bg="#FF0000")

            player2.grid(row=1, column=0)
            player2.config(width=5,pady=4)

            player3 = tk.Label(self,
                             text=Player3,
                             font="Times 45",
                             fg="white",
                             bg="#BDB76B")
            player3.grid(row=2, column=0)
            player3.config(width=5,pady=4)

            player4 = tk.Label(self,
                             text=Player4,
                             font="Times 45",
                             fg="white",
                             bg="#DA70D6")
            player4.grid(row=3, column=0)
            player4.config(width=5,pady=4)
            
            text1 = tk.Text(self, height=5, width=50)
            text1.grid(column=1, row=0, sticky='N')

            text2 = tk.Text(self, height=5, width=50)
            text2.grid(column=1, row=1, sticky='N')

            text3 = tk.Text(self, height=5, width=50)
            text3.grid(column=1, row=2, sticky='N')

            text4 = tk.Text(self, height=5, width=50)
            text4.grid(column=1, row=3, sticky='N')

            proc = output.ImageProcess()

            camera.capture('/home/pi/Desktop/Test/lets.jpg')
            img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")
            print(proc.calibrate_board(img))

            button = Button(6)

            def image_capture():
              global globvar
              globvar = -1
              proc = output.ImageProcess()
              while True:
                  button.wait_for_press()
                  globvar += 1
                  camera.capture('/home/pi/Desktop/Test/lets.jpg')
                  img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")

                  print(proc.frame_table(img))
                    
                  player_number = globvar%len(self.players)

                  print(player_number)
                    
                  pickle_in = open("game_file.pickle","rb")
                  example_dict = pickle.load(pickle_in)
                  player1_words = []
                  player1_score = []
                  player2_words = []
                  player2_score = []
                  player3_words = []
                  player3_score = []
                  player4_words = []
                  player4_score = []

                  if player_number == 0:
                      text1.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player == 0:
                              player1_words.append(key)
                              player1_score.append(value)
                      players1 = list(zip(player1_words,player1_score))
                      print(players1)
                      text1.insert(tk.INSERT,players1)
                      total_score1 = sum(player1_score)
                      player1.config(text = total_score1)

                      
                  if player_number == 1:
                      text2.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player == 1:
                              player2_words.append(key)
                              player2_score.append(value)
                      players2 = list(zip(player2_words,player2_score))
                      text2.insert(tk.INSERT,players2)
                      total_score2 = sum(player2_score)
                      player2.config(text = total_score2)

                  if player_number == 2:
                      text3.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player == 2:
                              player3_words.append(key)
                              player3_score.append(value)
                      players3 = list(zip(player3_words,player3_score))
                      text3.insert(tk.INSERT,players3)
                      total_score3 = sum(player3_score)
                      player3.config(text = total_score3)

                  if player_number == 3:
                      text4.delete('1.0',END)
                      for key,value, player in example_dict:
                          if player == 3:
                              player4_words.append(key)
                              player4_score.append(value)
                      players4 = list(zip(player4_words,player4_score))
                      text4.insert(tk.INSERT,players4)
                      total_score4 = sum(player4_score)
                      player4.config(text = total_score4)
                  

            th= threading.Thread(target=image_capture) #initialise the thread
            th.setDaemon(True)
            th.start() #start the thread

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        def toggleKeyboard(username_entry):
            p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
            if not "" == p.stderr.readline():
                subprocess.Popen(['florence'], shell=True)
                
        label_1 = tk.Label(self, text="Player1 Name: ")
        label_1.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        label_1 = tk.Label(self, text="Player2 Name: ")
        label_1.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.username_entry = tk.Entry(self, width=20)
        self.username_entry .grid(row=0, column=1, padx=5, pady=5)
        self.username_entry .bind('<FocusIn>',toggleKeyboard)
        self.username_entry1 = tk.Entry(self, width=20)
        self.username_entry1 .grid(row=1, column=1, padx=5, pady=5)
        self.username_entry1 .bind('<FocusIn>',toggleKeyboard)
        self.save_button = tk.Button(self, text="Save", command=lambda: self.read_username())
        self.save_button.grid(row=4, column=1, columnspan=2, pady=20)
        self.name_valid = False
        self.username = None
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: master.switch_frame(StartPage))
        button.grid(column = 1,row=5, columnspan=2, pady=20)
  

    def read_username(self):
        temp_username = self.username_entry.get()
        temp_username1 = self.username_entry1.get()
        if temp_username == '':
            print("No valid name")
            return
        else:
            self.name_valid = True
            self.username = temp_username
            self.username1 = temp_username1
            with open("players.txt", "w") as text_file :
                text_file.write(temp_username + ' ')
                text_file.write(temp_username1)
                text_file.close()

class PageThree(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        def toggleKeyboard(username_entry):
            p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
            if not "" == p.stderr.readline():
                subprocess.Popen(['florence'], shell=True)
                
        label_1 = tk.Label(self, text="Player1 Name: ")
        label_1.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        label_1 = tk.Label(self, text="Player2 Name: ")
        label_1.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        label_1 = tk.Label(self, text="Player3 Name: ")
        label_1.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.username_entry = tk.Entry(self, width=20)
        self.username_entry .grid(row=0, column=1, padx=5, pady=5)
        self.username_entry .bind('<FocusIn>',toggleKeyboard)
        self.username_entry1 = tk.Entry(self, width=20)
        self.username_entry1 .grid(row=1, column=1, padx=5, pady=5)
        self.username_entry1 .bind('<FocusIn>',toggleKeyboard)
        self.username_entry2= tk.Entry(self, width=20)
        self.username_entry2 .grid(row=2, column=1, padx=5, pady=5)
        self.username_entry2 .bind('<FocusIn>',toggleKeyboard)
        self.save_button = tk.Button(self, text="Save", command=lambda: self.read_username())
        self.save_button.grid(row=4, column=1, columnspan=2, pady=20)
        self.name_valid = False
        self.username = None
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: master.switch_frame(StartPage))
        button.grid(column = 1,row=5, columnspan=2, pady=20)

        
    def read_username(self):
        temp_username = self.username_entry.get()
        temp_username1 = self.username_entry1.get()
        temp_username2 = self.username_entry2.get()
        if temp_username == '':
            print("No valid name")
            return
        else:
            self.name_valid = True
            self.username = temp_username
            self.username1 = temp_username1
            self.username2 = temp_username2
            text_file = open("players.txt", "w")
            text_file.write(temp_username+ ' ')
            text_file.write(temp_username1+ ' ')
            text_file.write(temp_username2)
            text_file.close()

class PageFour(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        def toggleKeyboard(username_entry):
            p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
            if not "" == p.stderr.readline():
                subprocess.Popen(['florence'], shell=True)
                
        label_1 = tk.Label(self, text="Player1 Name: ")
        label_1.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        label_1 = tk.Label(self, text="Player2 Name: ")
        label_1.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        label_1 = tk.Label(self, text="Player3 Name: ")
        label_1.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        label_1 = tk.Label(self, text="Player4 Name: ")
        label_1.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.username_entry = tk.Entry(self, width=20)
        self.username_entry .grid(row=0, column=1, padx=5, pady=5)
        self.username_entry .bind('<FocusIn>',toggleKeyboard)
        self.username_entry1 = tk.Entry(self, width=20)
        self.username_entry1 .grid(row=1, column=1, padx=5, pady=5)
        self.username_entry1 .bind('<FocusIn>',toggleKeyboard)
        self.username_entry2= tk.Entry(self, width=20)
        self.username_entry2 .grid(row=2, column=1, padx=5, pady=5)
        self.username_entry2 .bind('<FocusIn>',toggleKeyboard)
        self.username_entry3= tk.Entry(self, width=20)
        self.username_entry3 .grid(row=3, column=1, padx=5, pady=5)
        self.username_entry3 .bind('<FocusIn>',toggleKeyboard)
        self.save_button = tk.Button(self, text="Save", command=lambda: self.read_username())
        self.save_button.grid(row=4, column=1, columnspan=2, pady=20)
        self.name_valid = False
        self.username = None
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: master.switch_frame(StartPage))
        button.grid(column = 1,row=5, columnspan=2, pady=20)

    def read_username(self):
        temp_username = self.username_entry.get()
        temp_username1 = self.username_entry1.get()
        temp_username2 = self.username_entry2.get()
        temp_username3 = self.username_entry3.get()
        if temp_username == '':
            print("No valid name")
            return
        else:
            self.name_valid = True
            self.username = temp_username
            self.username1 = temp_username1
            self.username2 = temp_username2
            self.username3 = temp_username3
            text_file = open("players.txt", "w")
            text_file.write(temp_username+ ' ')
            text_file.write(temp_username1+ ' ')
            text_file.write(temp_username2+ ' ')
            text_file.write(temp_username3)
            text_file.close()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

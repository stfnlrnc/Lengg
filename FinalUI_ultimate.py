import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from PIL import ImageTk, Image
from tkinter import *
import cv2
import numpy as np
import copy
import os
import conf
from sklearn.externals import joblib
from skimage.feature import hog
import warnings
import easygui  
import csv
import sys
import pickle
#import RPi.GPIO as GPIO
from gpiozero import Button
import time
from picamera import PiCamera
import threading
import subprocess
from subprocess import call
warnings.filterwarnings("ignore")

camera = PiCamera()
camera.resolution = (460,320)

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        w,h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w,h))
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
        self.master.title("Scrabble")
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Shutdown", command=self.client_exit)
        menu.add_cascade(label="Exit", font=("Times New Roman",10), menu=file)
        self.PlayerTwo=PhotoImage(file="scrab.png")
        panel = tk.Label(self, image=self.PlayerTwo)
        panel.pack()

        button1 = tk.Button(self, text="CLICK HERE TO START THE GAME", 
                                command=lambda: master.switch_frame(PageZero)).pack(fill="x",ipady=10)



        
    def client_exit(self):
        file1 = os.path.isfile("/home/pi/Desktop/Test/array_save.npy")
        file2 = os.path.isfile("/home/pi/Desktop/Test/blanktile.txt")
        file3 = os.path.isfile("/home/pi/Desktop/Test/clone_coordinates.pickle")
        file4 = os.path.isfile("/home/pi/Desktop/Test/clone_dict.pickle")
        file5 = os.path.isfile("/home/pi/Desktop/Test/clone_placed_word.pickle")
        file6 = os.path.isfile("/home/pi/Desktop/Test/coordinates.pickle")
        file7 = os.path.isfile("/home/pi/Desktop/Test/dict.pickle")
        file8 = os.path.isfile("/home/pi/Desktop/Test/game_file.pickle")
        file9 = os.path.isfile("/home/pi/Desktop/Test/no_players.pickle")
        file10 = os.path.isfile("/home/pi/Desktop/Test/placed_word.pickle")
        if file1 is True:
            os.remove("/home/pi/Desktop/Test/array_save.npy")
        if file2 is True:
            os.remove("/home/pi/Desktop/Test/blanktile.txt")
        if file3 is True:
            os.remove("/home/pi/Desktop/Test/clone_coordinates.pickle")
        if file4 is True:
            os.remove("/home/pi/Desktop/Test/clone_dict.pickle")
        if file5 is True:
            os.remove("/home/pi/Desktop/Test/clone_placed_word.pickle")
        if file6 is True:
            os.remove("/home/pi/Desktop/Test/coordinates.pickle")
        if file7 is True:
            os.remove("/home/pi/Desktop/Test/dict.pickle")
        if file8 is True:
            os.remove("/home/pi/Desktop/Test/game_file.pickle")
        if file9 is True:
            os.remove("/home/pi/Desktop/Test/no_players.pickle")
        if file10 is True:
            os.remove("/home/pi/Desktop/Test/placed_word.pickle")
        call("sudo shutdown -h now", shell=True)

class PageZero(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self,text="CHOOSE THE NUMBER OF PLAYERS THAT WILL BE PLAYING",font="Helvetica 13 bold",
                             fg="white",
                             bg="#04391B").pack(fill="x",ipady=40)
        self.PlayerTwo=PhotoImage(file="2_player.png")
        self.PlayerThree=PhotoImage(file="3_player.png")
        self.PlayerFour=PhotoImage(file="4_player.png")
        button2 = tk.Button(self, image=self.PlayerTwo, command=lambda: master.switch_frame(PageTwo)).pack(ipadx=15, side="left", ipady=10)
        button3 = tk.Button(self, image=self.PlayerThree, command=lambda: master.switch_frame(PageThree)).pack(ipadx=15, side="left", ipady=10)
        button4 = tk.Button(self, image=self.PlayerFour, command=lambda: master.switch_frame(PageFour)).pack(ipadx=20, side="left", ipady=10)

        
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        cv2.destroyAllWindows()
        with open("players.txt", "r") as text_file :
                message = text_file.read()
                self.players = message.split()

        if len(self.players) == 2:
            def countdown(t):
                while t > -1:
                    mins, sec = divmod(t,60)
                    timeformat = '{:02d}:{:02d}'.format(mins,sec)
                    label.config(text=timeformat)
                    self.update()
                    var1 = player1.cget("text")
                    var2 = player2.cget("text")
                    end = label.cget("text")
                    if end == "00:00":
                        if var1 > var2:
                            player1.config(text="Winner")
                        elif var2 > var1:
                            player2.config(text="Winner")
                            
                        file1 = os.path.isfile("/home/pi/Desktop/Test/array_save.npy")
                        file2 = os.path.isfile("/home/pi/Desktop/Test/blanktile.txt")
                        file3 = os.path.isfile("/home/pi/Desktop/Test/clone_coordinates.pickle")
                        file4 = os.path.isfile("/home/pi/Desktop/Test/clone_dict.pickle")
                        file5 = os.path.isfile("/home/pi/Desktop/Test/clone_placed_word.pickle")
                        file6 = os.path.isfile("/home/pi/Desktop/Test/coordinates.pickle")
                        file7 = os.path.isfile("/home/pi/Desktop/Test/dict.pickle")
                        file8 = os.path.isfile("/home/pi/Desktop/Test/game_file.pickle")
                        file9 = os.path.isfile("/home/pi/Desktop/Test/no_players.pickle")
                        file10 = os.path.isfile("/home/pi/Desktop/Test/placed_word.pickle")
                        if file1 is True:
                            os.remove("/home/pi/Desktop/Test/array_save.npy")
                        if file2 is True:
                            os.remove("/home/pi/Desktop/Test/blanktile.txt")
                        if file3 is True:
                            os.remove("/home/pi/Desktop/Test/clone_coordinates.pickle")
                        if file4 is True:
                            os.remove("/home/pi/Desktop/Test/clone_dict.pickle")
                        if file5 is True:
                            os.remove("/home/pi/Desktop/Test/clone_placed_word.pickle")
                        if file6 is True:
                            os.remove("/home/pi/Desktop/Test/coordinates.pickle")
                        if file7 is True:
                            os.remove("/home/pi/Desktop/Test/dict.pickle")
                        if file8 is True:
                            os.remove("/home/pi/Desktop/Test/game_file.pickle")
                        if file9 is True:
                            os.remove("/home/pi/Desktop/Test/no_players.pickle")
                        if file10 is True:
                            os.remove("/home/pi/Desktop/Test/placed_word.pickle")
              
                    time.sleep(1)
                    t -= 1
                    
            
            label=tk.Label(self, text="Time")
            label.grid(column = 0,row=2)
            button1 = tk.Button(self, text="Click to activate Time",
                           command=lambda: countdown(600))
            button1.grid(column = 1,row=2)
            #button = tk.Button(self, text="Go to the start page",
                           #command=lambda: master.switch_frame(StartPage))
            #button.grid(column = 0,row=2)
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


            text1 = tk.Text(self, height=11, width=30)
            text1.grid(column=0, row=1, sticky='N')

            text2 = tk.Text(self, height=11, width=30)
            text2.grid(column=1, row=1, sticky='N')

            proc = ImageProcess()

            #camera.capture('/home/pi/Desktop/Test/lets.jpg')
            #img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")
            #print(proc.calibrate_board(img))

            button = Button(6)

            def image_capture():
              global globvar
              globvar = -1
              proc = ImageProcess()
              while True:
                  button.wait_for_press()
                  globvar += 1
                  camera.capture('/home/pi/Desktop/Test/lets.jpg')
                  img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")

                  print(proc.frame_table(img))
                    
                  player_number = globvar%len(self.players)

                  #print(player_number)
                    
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
                      #print(players1)
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
                      #print(players2)
                      text2.insert(tk.INSERT,players2)
                      total_score2 = sum(player2_score)
                      player2.config(text = total_score2)
                  

            th= threading.Thread(target=image_capture) #initialise the thread
            th.setDaemon(True)
            th.start() #start the thread

        if len(self.players) == 3:
            def countdown(t):
                while t > -1:
                    mins, sec = divmod(t,60)
                    timeformat = '{:02d}:{:02d}'.format(mins,sec)
                    label.config(text=timeformat)
                    self.update()
                    var1 = player1.cget("text")
                    var2 = player2.cget("text")
                    var3 = player3.cget("text")
                    end = label.cget("text")
                    if end == "00:00":
                        if var1 > var2 and var1 > var3:
                            player1.config(text="Winner")
                        if var2 > var1 and var2 > var3:
                            player2.config(text="Winner")
                        if var3 > var1 and var3 > var2:
                            player3.config(text="Winner")
                    time.sleep(1)
                    t -= 1
                    
            
            label=tk.Label(self, text="Time")
            label.grid(column = 0,row=3)
            button1 = tk.Button(self, text="Click to activate Time",
                           command=lambda: countdown(600))
            button1.grid(column = 1,row=3)
            #button = tk.Button(self, text="Go to the start page",
                          # command=lambda: master.switch_frame(StartPage))
            #button.grid(column = 0,row=3)
            Player1 = self.players[0]  
            Player2 = self.players[1]
            Player3 = self.players[2]

            player1 = tk.Label(self,
                                 text=Player1,
                                 font="Times 45",
                                 fg="white",
                                 bg="#0000FF")
            player1.grid(row=0, column=0)
            player1.config(width=5,pady=6)

            player2 = tk.Label(self,
                             text=Player2,
                             font="Times 45",
                             fg="white",
                             bg="#FF0000")

            player2.grid(row=1, column=0)
            player2.config(width=5,pady=6)

            player3 = tk.Label(self,
                             text=Player3,
                             font="Times 45",
                             fg="white",
                             bg="#BDB76B")
            player3.grid(row=2, column=0)
            player3.config(width=5,pady=6)

            text1 = tk.Text(self, height=5, width=50)
            text1.grid(column=1, row=0, sticky='N')

            text2 = tk.Text(self, height=5, width=50)
            text2.grid(column=1, row=1, sticky='N')

            text3 = tk.Text(self, height=5, width=50)
            text3.grid(column=1, row=2, sticky='N')

            #proc = ImageProcess()

            #camera.capture('/home/pi/Desktop/Test/lets.jpg')
            #img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")
            #print(proc.calibrate_board(img))

            button = Button(6)

            def image_capture():
              global globvar
              globvar = -1
              proc = ImageProcess()
              while True:
                  button.wait_for_press()
                  globvar += 1
                  camera.capture('/home/pi/Desktop/Test/lets.jpg')
                  img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")

                  print(proc.frame_table(img))
                    
                  player_number = globvar%len(self.players)

                  #print(player_number)

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
                      #print(players1)
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
            def countdown(t):
                while t > -1:
                    mins, sec = divmod(t,60)
                    timeformat = '{:02d}:{:02d}'.format(mins,sec)
                    label.config(text=timeformat)
                    self.update()
                    var1 = player1.cget("text")
                    var2 = player2.cget("text")
                    var3 = player3.cget("text")
                    var4 = player4.cget("text")
                    end = label.cget("text")
                    if end == "00:00":
                        if var1 > var2 and var1 > var3 and var1 > var4:
                            player1.config(text="Winner")
                        if var2 > var1 and var2 > var3 and var2 > var4:
                            player2.config(text="Winner")
                        if var3 > var1 and var3 > var2 and var3 > var4:
                            player3.config(text="Winner")
                        if var4 > var3 and var4 > var2 and var4 > var1:
                            player4.config(text="Winner")
                    time.sleep(1)
                    t -= 1
                    
            
            label=tk.Label(self, text="Time")
            label.grid(column = 0,row=4)
            button1 = tk.Button(self, text="Click to activate Time",
                           command=lambda: countdown(600))
            button1.grid(column = 1,row=4)
            #button = tk.Button(self, text="Go to the start page",
                          # command=lambda: master.switch_frame(StartPage))
            #button.grid(column = 0,row=4)
            Player1 = self.players[0]  
            Player2 = self.players[1]
            Player3 = self.players[2]
            Player4 = self.players[3]

            player1 = tk.Label(self,
                                 text=Player1,
                                 font="Times 35",
                                 fg="white",
                                 bg="#0000FF")
            player1.grid(row=0, column=0)
            player1.config(width=5,pady=1)

            player2 = tk.Label(self,
                             text=Player2,
                             font="Times 35",
                             fg="white",
                             bg="#FF0000")

            player2.grid(row=1, column=0)
            player2.config(width=5,pady=1)

            player3 = tk.Label(self,
                             text=Player3,
                             font="Times 35",
                             fg="white",
                             bg="#BDB76B")
            player3.grid(row=2, column=0)
            player3.config(width=5,pady=1)

            player4 = tk.Label(self,
                             text=Player4,
                             font="Times 35",
                             fg="white",
                             bg="#DA70D6")
            player4.grid(row=3, column=0)
            player4.config(width=5,pady=1)
            
            text1 = tk.Text(self, height=4, width=50)
            text1.grid(column=1, row=0, sticky='N')

            text2 = tk.Text(self, height=4, width=50)
            text2.grid(column=1, row=1, sticky='N')

            text3 = tk.Text(self, height=4, width=50)
            text3.grid(column=1, row=2, sticky='N')

            text4 = tk.Text(self, height=4, width=50)
            text4.grid(column=1, row=3, sticky='N')

            #proc = ImageProcess()

            #camera.capture('/home/pi/Desktop/Test/lets.jpg')
            #img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")
            #print(proc.calibrate_board(img))

            button = Button(6)

            def image_capture():
              global globvar
              globvar = -1
              proc = ImageProcess()
              while True:
                  button.wait_for_press()
                  globvar += 1
                  camera.capture('/home/pi/Desktop/Test/lets.jpg')
                  img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")

                  print(proc.frame_table(img))
                    
                  player_number = globvar%len(self.players)

                  #print(player_number)
                    
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
                      #print(players1)
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
        button = tk.Button(self, text="Capture the board",
                           command=lambda: master.switch_frame(PageFive))
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
        button = tk.Button(self, text="Capture the board",
                           command=lambda: master.switch_frame(PageFive))
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
        button = tk.Button(self, text="Capture the board",
                           command=lambda: master.switch_frame(PageFive))
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

class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        proc = ImageProcess()

        camera.capture('/home/pi/Desktop/Test/lets.jpg')
        img = cv2.imread("/home/pi/Desktop/Test/lets.jpg")
        print(proc.calibrate_board(img))
        label_1 = tk.Label(self, text="Do you want to recalibrate?")
        label_1.pack()
        save_button = tk.Button(self, text="Yes", command=lambda:proc.calibrate_board(img))
        save_button1 = tk.Button(self, text="No", command=lambda: master.switch_frame(PageOne))
        save_button.pack(fill=X)
        save_button1.pack(fill=X)

class ImageProcess:
    param1 = 70
    param2 = 15
    fields1 = fields2 = []
    FieldTable = [[1 for j in range(15)] for i in range(15)]

    def mouseEvent(self, event, x, y, flags, param):                                
        if event == cv2.EVENT_MOUSEMOVE:                                            
            self.ImgCopy2 = copy.deepcopy(self.ImgCopy)                             
            cv2.circle(self.ImgCopy2, (x, y), 3, (0, 255, 0), -1)                  

        if event == cv2.EVENT_LBUTTONUP:                                          
            self.splitPointsTemp.append([x, y])                                   
            cv2.circle(self.ImgCopy, (x, y), 3, (255, 255, 255), -1)            
            self.ImgCopy2 = copy.deepcopy(self.ImgCopy)                          

    def calibrate_board(self,img):       #remove mouseEvent and calibrate_board after finding the coordinates                                                                                                          
        cv2.destroyAllWindows()
        self.img = img                                                            
        self.ImgCopy = copy.deepcopy(self.img)                                     
        self.ImgCopy2 = copy.deepcopy(self.img)                                    
        cv2.namedWindow('image')                                                  
        cv2.setMouseCallback('image', self.mouseEvent)                           
        self.splitPointsTemp = []                                                   
        while True:                                                                 
            cv2.imshow('image', self.ImgCopy2)                                      
            if len(self.splitPointsTemp) == 4 or cv2.waitKey(1) & 0xFF == 27:       
                break
        cv2.waitKey(1)
        if len(self.splitPointsTemp) == 4:                                          
            self.splitPoints = self.splitPointsTemp                                 
        
        conf.set('splitPoints', self.splitPoints)
        #print(self.splitPoints) #check the 4 corners of the board
        #cv2.destroyAllWindows()  
        
                                       
    def imageSplit(self):
        majorCorners = conf.get('splitPoints')                                     

        self.splitPoints = eval(str(majorCorners))
        if len(self.splitPoints) != 4:
            print("Board not detected!")
        rows, cols, ch = self.img.shape
        pts1 = np.float32(self.splitPoints)
        pts2 = np.float32([[0, 0], [602, 0], [0, 602], [602, 602]])

        M = cv2.getPerspectiveTransform(pts1, pts2)
        self.trimmed = cv2.warpPerspective(self.img, M, (602, 602))

        #~~~~~~~~~~~~~~IMAGE ROTATION~~~~~~~~~~~~

        rows, cols, depth = self.trimmed.shape  # Without this code the image will be upside down

        matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45 * int(conf.get('rotate')), 1)
        self.trimmed = cv2.warpAffine(self.trimmed, matrix, (cols, rows))

        #~~~~~~~~~~~~~~~generating edges image~~~~~~~~~~~~
        self.edgesImage = cv2.cvtColor(self.trimmed, cv2.COLOR_BGR2GRAY)
        self.edgesImage = cv2.medianBlur(self.edgesImage, 5)                # CHANGE
        self.edgesImage = cv2.GaussianBlur(self.edgesImage, (3, 3), 0)      # CHANGE
        #self.edgesImage = copy.deepcopy(image)
        self.edgesImage = cv2.Canny(self.edgesImage, float(conf.get('param1')), float(conf.get('param2'))) #90, 200
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.normalImage = copy.deepcopy(self.trimmed)

        #~~~~~ROTATING FOR ALGORITHM:~~~~~~~~~~~~~~~~~~~~~~
        rows, cols, depth = self.trimmed.shape
        matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), -180, 1)
        self.trimmed = cv2.warpAffine(self.trimmed, matrix, (cols, rows))

        points = []
        for i in range(1, 602, 40):
            for j in range(1, 602, 40):
                points.append([j, i])

        dic = {}
        for i in range(0, 16):
            for j in range(0, 16):
                dic[i, j] = points[(16 * i) + j]

        self.trimmed = cv2.cvtColor(self.trimmed, cv2.COLOR_BGR2GRAY)
        for i in range(15):
            for j in range(15):
                x1 = dic[i, j][0]
                y1 = dic[i, j][1]
                x2 = dic[i + 1, j + 1][0]
                y2 = dic[i + 1, j + 1][1]
                self.FieldTable[i][j] = self.trimmed[y1:y2, x1:x2]

                
        for i in range(15):
            for j in range(15):
                x1 = dic[i, j][0]
                y1 = dic[i, j][1]
                x2 = dic[i + 1, j + 1][0]
                y2 = dic[i + 1, j + 1][1]
                cv2.circle(self.trimmed, (x1, y1), 2, (0, 0, 255))
                cv2.circle(self.trimmed, (x2, y2), 2, (0, 0, 255))

        #cv2.imshow('result', self.trimmed) ###
        #cv2.waitKey(0) ###

    def frame_table(self, image):
        Trydetect = joblib.load('Tiles_detect.pkl')
        self.img = copy.deepcopy(image)
        self.imageSplit()
        my_list = []
        my_list2 = []
        #num=0
        predict_map = {0:'#', 1:'0', 2:'0', 3:'0', 4:'0', 5:'0',
              6:'A', 7:'B', 8:'C', 9:'D', 10:'E', 11:'F',
              12:'G', 13:'H', 14:'I', 15:'J', 16:'K', 17:'L',
              18:'M', 19:'N', 20:'O', 21:'P', 22:'Q', 23:'R',
              24:'S', 25:'T', 26:'U', 27:'V', 28:'W', 29:'X',
              30:'Y', 31:'Z' }
        points_dictionary = {
            'A': 1, 'B': 3, 'C': 3,
            'D': 2, 'E': 1, 'F': 4, 'G': 2,
            'H': 4, 'I': 1, 'J': 8, 'K': 5,
            'L': 1, 'M': 3, 'N': 1, 'O': 1,
            'P': 3, 'Q': 10, 'R': 1, 'S': 1,
            'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
            'Y': 4, 'Z': 10, '#': 0, '0':3
        }
        
        premium_tiles_letter = [[ 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1 ],
                                [ 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1 ],
                                [ 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1 ],
                                [ 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2 ],
                                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                                [ 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1 ],
                                [ 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1 ],
                                [ 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1 ],
                                [ 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1 ],
                                [ 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1 ],
                                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                                [ 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2 ],
                                [ 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1 ],
                                [ 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1 ],
                                [ 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1 ]]

        premium_tiles_word = [[ 3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3 ],
                            [ 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1 ],
                            [ 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1 ],
                            [ 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1 ],
                            [ 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1 ],
                            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                            [ 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 3 ],
                            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                            [ 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1 ],
                            [ 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1 ],
                            [ 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1 ],
                            [ 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1 ],
                            [ 3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3 ]]

        used = [[ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],
                            [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]]

        
        Words = []
        coord = []
        players = []
        final_player = []
        final_Words = []
        final_coord = []
        final_clone1 = []
        final_clone2 = []
        clone_Words = []
        clone_coord = []
        clones = []
        clone_out_dict = []
        clone_out_dict2 = []
        out_dict = []
        out_dict2 = []
        wrong_words = []
        with_coord = []
        with_player = []
        

        #path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python37-32\\Thesis\\Storing"
        exists = os.path.isfile('/home/pi/Desktop/Test/array_save.npy')
        exists1 = os.path.isfile('/home/pi/Desktop/Test/blanktile.txt')
        for i in range(15):
            for j in range(15):

                    #cv2.imshow('tile', self.FieldTable[i][j])   
                    fd, hog_image = hog(self.FieldTable[i][j],visualise=True)
                    Prediction = Trydetect.predict(fd.reshape(1,-1))
                    if exists == False:
                        my_list.append(predict_map[int(Prediction[0])])
                    elif exists == True:
                        my_list2.append(predict_map[int(Prediction[0])]) 
 
#----------------------------------------------------------For the first array----------------------------------------------------
        if exists == True:
            k =  np.load('array_save.npy')      
        elif exists == False:
            k = np.save('array_save', my_list) # save the file as "array_save.npy"
            k =  np.load('array_save.npy')
        #For the first picture
        
                        
        my_board = np.array(k).reshape((15,15))
        clone = np.copy(my_board)
        if not my_list2:
             
            #print(my_board)
            #print(clone)
            for i, row in enumerate(clone):
                for j, cell in enumerate(row):
                    if cell == '#':
                                
                        def read_save():
                            blank_tile = entry_1.get()
                            blank_letter = blank_tile
                            text_file = open("blanktile.txt", "w")
                            text_file.write(blank_letter)
                            text_file.close()
                            f = open('blanktile.txt','r')
                            input_tile = f.read()
                            clone[i][j] = input_tile
                            pop.destroy()

                        def toggleKeyboard(entry_1):
                            p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
                            if not "" == p.stderr.readline():
                                subprocess.Popen(['florence'], shell=True)
                           
                        pop = tk.Tk()
                        #root.geometry("200x100")                     
                        label_1 = tk.Label(pop,text = "Please input a letter for the blank tile")
                        label_1.pack()
                        entry_1 = tk.Entry(pop)
                        entry_1.pack(fill=X)
                        entry_1.bind('<FocusIn>',toggleKeyboard)
                        save_button = tk.Button(pop, text="Save", command=read_save)
                        save_button.pack(fill=X)

                        pop.mainloop()


            for j in range(my_board.shape[1]):
                for i in range(my_board.shape[0]):
                    if my_board[i][j] == '0':
                        continue
                        
                    # across
                    if j == 0 or my_board[i][j - 1] == '0':
                        k, l = i, j
                        word_across = ''
                        word_across_pos = []
                        while l < 15 and k < 15 and my_board[k][l] != '0':
                            word_across += my_board[k][l]
                            word_across_pos.append((k, l))
                            l += 1

                        if len(word_across) > 1:
                            out_dict.append([word_across, word_across_pos])

                    # down
                    if i == 0 or my_board[i - 1][j] == '0':
                        k, l = i, j
                        word_down = ''
                        word_down_pos = []
                        while l < 15 and k < 15 and my_board[k][l] != '0':
                            word_down += my_board[k][l]
                            word_down_pos.append((k, l))
                            k += 1

                        if len(word_down) > 1:
                            out_dict.append([word_down, word_down_pos])

            #print(out_dict)

            for key, value in out_dict:
                global globvar
                #print(globvar)
                text_file = open("players.txt", "r")
                message = text_file.read()
                play = message.split()
                #print(len(play))
                player_number = globvar%len(play)
                Words.append(key)
                coord.append(value)
                players.append(player_number)
                
                    
            combine = list(zip(Words, coord, players))
            #print(combine)

            # Clone to check for words and points seperated for the blank tile
            for j in range(clone.shape[1]):
                for i in range(clone.shape[0]):
                    if clone[i][j] == '0':
                        continue
                    
                    # across
                    if j == 0 or clone[i][j - 1] == '0':
                        k, l = i, j
                        clone_word_across = ''
                        clone_word_across_pos = []
                        while l < 15 and k < 15 and clone[k][l] != '0':
                            clone_word_across += clone[k][l]
                            clone_word_across_pos.append((k, l))
                            l += 1

                        if len(clone_word_across) > 1:
                            clone_out_dict.append([clone_word_across, clone_word_across_pos])

                    # down
                    if i == 0 or clone[i - 1][j] == '0':
                        k, l = i, j
                        clone_word_down = ''
                        clone_word_down_pos = []
                        while l < 15 and k < 15 and clone[k][l] != '0':
                            clone_word_down += clone[k][l]
                            clone_word_down_pos.append((k, l))
                            k += 1

                        if len(clone_word_down) > 1:
                            clone_out_dict.append([clone_word_down, clone_word_down_pos])

            for key1, value1 in clone_out_dict:
                clone_Words.append(key1)
                clone_coord.append(value1)
                    
            combine1 = list(zip(clone_Words, clone_coord))

                                    

            for key, value in combine1:
                words = [line.rstrip('\n') for line in open('sowpods.txt')] #Gets each word
                if key in words:
                    print(key + ' ' + "Exist in the dictionary")
                else:
                    print(key + ' ' + "Does not exist in the dictionary")
                    wrong_words.append(key)
                    with_coord.append(value)
            
            #print(combine1)
            throw_words = list(zip(wrong_words, with_coord))

            pickle_out = open("dict.pickle","wb")
            pickle.dump(out_dict, pickle_out)
            pickle_out.close()
         
            pickle_out = open("placed_word.pickle","wb")
            pickle.dump(Words, pickle_out)
            pickle_out.close()

            pickle_out = open("coordinates.pickle","wb")
            pickle.dump(coord, pickle_out)
            pickle_out.close()

            pickle_out = open("no_players.pickle","wb")
            pickle.dump(players, pickle_out)
            pickle_out.close()

            pickle_out = open("clone_dict.pickle","wb")
            pickle.dump(clone_out_dict, pickle_out)
            pickle_out.close()
         
            pickle_out = open("clone_placed_word.pickle","wb")
            pickle.dump(clone_Words, pickle_out)
            pickle_out.close()

            pickle_out = open("clone_coordinates.pickle","wb")
            pickle.dump(clone_coord, pickle_out)
            pickle_out.close()

            #pickle_in = open("placed_word.pickle","rb")
            #prevword = pickle.load(pickle_in)

            '''for words in prevword:
                for word in words:
                    if words == prevword[m + 1]:
                        sum1 = sum1 + points_dictionary[word]
                    else:
                        sumsOfwords.append(sum1)
                        sum1 = 0
                        sum1 = sum1 + points_dictionary[word]
                        m = m + 1'''
            for word, values, player in combine:
                if (word, values) not in throw_words:
                    final_Words.append(word)
                    final_coord.append(values)
                    final_player.append(player)

            final = list(zip(final_Words, final_coord, final_player))
            #print(final)
                    
            
            
            sumsOfwords = []
            for key, value, player in final:
                sum1 = 0
                for idx, (i, j) in enumerate(value):
                    sum1 += premium_tiles_letter[i][j] * points_dictionary[key[idx]]
                
                for i, j in value:
                    if not used[i][j]:
                       sum1 *= premium_tiles_word[i][j]
                       used[i][j] = True

                #print(sum1)

                sumsOfwords.append(sum1)

            #print(sumsOfwords)

            
            dictionary = list(zip(final_Words, sumsOfwords, final_player))
            #print(dictionary)
          
            pickle_out = open("game_file.pickle","wb")
            pickle.dump(dictionary, pickle_out)
            pickle_out.close()
          
            
            with open("gamefile.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerows(dictionary)
#-----------------------------------------------------------For the second array-----------------------------------------------------------              
        if my_list2:
            a = np.save('array_save', my_list2)
            a = np.load('array_save.npy')
                    
                        
            my_board2 = np.array(a).reshape(15,15)
            clone2 = np.copy(my_board2)
            #clone = np.copy(arr2)
            check = np.array_equal(my_board,my_board2) # Checks if the two arrays are the same
            #print(check)

            if check is True:
                easygui.msgbox('Player will now skip a turn!', 'Message')
                
            elif check is False:
                #print(my_board2)

                if exists1 == False:
                    for i, row in enumerate(clone2):
                        for j, cell in enumerate(row):
                            if cell == '#':
                                        
                                def read_save():
                                    blank_tile = entry_1.get()
                                    blank_letter = blank_tile
                                    text_file = open("blanktile.txt", "w")
                                    text_file.write(blank_letter)
                                    text_file.close()
                                    f = open('blanktile.txt','r')
                                    input_tile = f.read()
                                    clone2[i][j] = input_tile
                                    pop.destroy()

                                def toggleKeyboard(entry_1):
                                    p = subprocess.Popen(['florence show'], shell=True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
                                    if not "" == p.stderr.readline():
                                        subprocess.Popen(['florence'], shell=True)
                                    
                                pop = tk.Tk()
                                #root.geometry("200x100")                     
                                label_1 = tk.Label(pop,text = "Please input a letter for the blank tile")
                                label_1.pack()
                                entry_1 = tk.Entry(pop)
                                entry_1.pack(fill=X)
                                entry_1.bind('<FocusIn>',toggleKeyboard)
                                save_button = tk.Button(pop, text="Save", command=read_save)
                                save_button.pack(fill=X)
                                
                                pop.mainloop()

                                
                elif exists1 == True:
                    for i, row in enumerate(clone2):
                        for j, cell in enumerate(row):
                            if cell == '#':
                                f = open('blanktile.txt','r')
                                input_tile = f.read()
                                clone2[i][j] = input_tile

                
                for j in range(my_board2.shape[1]):
                    for i in range(my_board2.shape[0]):
                        if my_board2[i][j] == '0':
                            continue
                        
                        # across
                        if j == 0 or my_board2[i][j - 1] == '0':
                            k, l = i, j
                            word_across = ''
                            word_across_pos = []
                            while l < 15 and k < 15 and my_board2[k][l] != '0':
                                word_across += my_board2[k][l]
                                word_across_pos.append((k, l))
                                l += 1

                            if len(word_across) > 1:
                                out_dict2.append([word_across, word_across_pos])

                        # down
                        if i == 0 or my_board2[i - 1][j] == '0':
                            k, l = i, j
                            word_down = ''
                            word_down_pos = []
                            while l < 15 and k < 15 and my_board2[k][l] != '0':
                                word_down += my_board2[k][l]
                                word_down_pos.append((k, l))
                                k += 1

                            if len(word_down) > 1:
                                out_dict2.append([word_down, word_down_pos])

                #print(out_dict2)

                pickle_in = open("dict.pickle","rb")
                prevdict = pickle.load(pickle_in)

                pickle_in = open("placed_word.pickle","rb")
                prevword = pickle.load(pickle_in)
             

                pickle_in = open("coordinates.pickle","rb")
                prevcoord = pickle.load(pickle_in)

                pickle_in = open("no_players.pickle","rb")
                prevplayers = pickle.load(pickle_in)

                pickle_in = open("clone_dict.pickle","rb")
                clone_prevdict = pickle.load(pickle_in)

                pickle_in = open("clone_placed_word.pickle","rb")
                clone_prevword = pickle.load(pickle_in)

                pickle_in = open("clone_coordinates.pickle","rb")
                clone_prevcoord = pickle.load(pickle_in)


        
                for key, value in out_dict2:
                    if value not in prevcoord:
                        text_file = open("players.txt", "r")
                        message = text_file.read()
                        play = message.split()
                        #print(len(play))
                        player_number = globvar%len(play)
                        prevword.append(key)
                        prevcoord.append(value)
                        prevplayers.append(player_number)
                    
                combine = list(zip(prevword, prevcoord,prevplayers))
                #print(combine)

                # Clone to check for words and points seperated for the blank tile
                for j in range(clone2.shape[1]):
                    for i in range(clone2.shape[0]):
                        if clone2[i][j] == '0':
                            continue
                        
                        # across
                        if j == 0 or clone2[i][j - 1] == '0':
                            k, l = i, j
                            clone_word_across = ''
                            clone_word_across_pos = []
                            while l < 15 and k < 15 and clone2[k][l] != '0':
                                clone_word_across += clone2[k][l]
                                clone_word_across_pos.append((k, l))
                                l += 1

                            if len(clone_word_across) > 1:
                                clone_out_dict2.append([clone_word_across, clone_word_across_pos])

                        # down
                        if i == 0 or clone2[i - 1][j] == '0':
                            k, l = i, j
                            clone_word_down = ''
                            clone_word_down_pos = []
                            while l < 15 and k < 15 and clone2[k][l] != '0':
                                clone_word_down += clone2[k][l]
                                clone_word_down_pos.append((k, l))
                                k += 1

                            if len(clone_word_down) > 1:
                                clone_out_dict2.append([clone_word_down, clone_word_down_pos])

                #print(clone_out_dict2)

                for key1, value1 in clone_out_dict2:
                    if value1 not in clone_prevcoord:
                        clone_prevword.append(key1)
                        clone_prevcoord.append(value1)
                    
                combine1 = list(zip(clone_prevword, clone_prevcoord))
                #print(combine1)



                #Searching if the word is valid in the text file
                for word, value in combine1:
                    text_file = open("players.txt", "r")
                    message = text_file.read()
                    play = message.split()
                    #print(len(play))
                    player_number = globvar%len(play)
                    words = [line.rstrip('\n') for line in open('sowpods.txt')] #Gets each word 
                    if word not in words:
                        print(word + ' ' + "Does not exist in the dictionary")
                        easygui.msgbox('Player will now skip a turn!', 'Message')
                        wrong_words.append(word)
                        with_coord.append(value)
                        with_player.append(player_number)

                throw_words = list(zip(wrong_words, with_coord, with_player))
                throw_words_clone = list(zip(wrong_words, with_coord))
                #print(throw_words)

                for key, item in combine1:
                    if (key, item) not in throw_words_clone:
                        final_clone1.append(key)
                        final_clone2.append(item)

                final_clone = list(zip(final_clone1, final_clone2))
                #print(final_clone)

                for word, values, player in combine:
                    if (word, values, player) not in throw_words:
                        final_Words.append(word)
                        final_coord.append(values)
                        final_player.append(player)

                final = list(zip(final_Words, final_coord, final_player))
                #print(final)

                pickle_out = open("dict.pickle","wb")
                pickle.dump(final_clone, pickle_out)
                pickle_out.close()
             
                pickle_out = open("placed_word.pickle","wb")
                pickle.dump(final_Words, pickle_out)
                pickle_out.close()

                pickle_out = open("coordinates.pickle","wb")
                pickle.dump(final_coord, pickle_out)
                pickle_out.close()

                pickle_out = open("no_players.pickle","wb")
                pickle.dump(final_player, pickle_out)
                pickle_out.close()

                pickle_out = open("clone_dict.pickle","wb")
                pickle.dump(final_clone, pickle_out)
                pickle_out.close()
             
                pickle_out = open("clone_placed_word.pickle","wb")
                pickle.dump(final_clone1, pickle_out)
                pickle_out.close()

                pickle_out = open("clone_coordinates.pickle","wb")
                pickle.dump(final_clone2, pickle_out)
                pickle_out.close()

                #pickle_in = open("placed_word.pickle","rb")
                #currword = pickle.load(pickle_in)

                #pickle_in = open("no_players.pickle","rb")
                #nextplayer = pickle.load(pickle_in)
                        

                #Calculate the points of the tile

                sumsOfwords = []
                for key, value, player in final:
                    sum1 = 0
                    for idx, (i, j) in enumerate(value):
                        sum1 += premium_tiles_letter[i][j] * points_dictionary[key[idx]]
                    
                    for i, j in value:
                        if not used[i][j]:
                           sum1 *= premium_tiles_word[i][j]
                           used[i][j] = True

                    #print(sum1)

                    sumsOfwords.append(sum1)
                    

                dictionary = list(zip(final_Words, sumsOfwords, final_player))
                #print(dictionary)
        
                pickle_out = open("game_file.pickle","wb")
                pickle.dump(dictionary, pickle_out)
                pickle_out.close()
        
                with open("gamefile.csv", "w") as f:
                    writer = csv.writer(f)
                    writer.writerows(dictionary)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

import tkinter as tk
import random
import time 
class obstacleavoider:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Obstacle Avoider")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.canvas =tk.Canvas(self.root,width=800,heigth=600,bg="white")
        self.canvas.pack()
        self.player_size=30
        self.player_x=400 -self.player_size//2
        self.player_y=500
        self.player= self.canvas.create_rectangle 
            (
        self.player_x,self.player_y,
        self.player_x +self.player_size,self.player_y +self.player_ size,
        fill='blue'
            )  
        self.obstacles=[]
        self.obstacle_speed= 3
        self.obstacles_size=30
        self.score=0
        self.score_text=self.canvas.create_text(10,10,anchor='nw',text=f'Score 0',font=("Arial,16"))
        
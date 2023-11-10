#Software Engineering Course Project Useful Links Module
#Group 3
#Cooper Poole
#Christian Chow Quan 
#Jason Barican
#Jian Gong

import tkinter as tk

class HelpCenterFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="We're here to help").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("GeneralWindow"))
        backButton.pack(padx=10, pady=10)


class AboutFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("GeneralWindow"))
        backButton.pack(padx=10, pady=10)


class PressFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="In College Pressroom: Stay on top of the latest news, updates, and reports").pack(padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("GeneralWindow"))
        backButton.pack(padx=10, pady=10)

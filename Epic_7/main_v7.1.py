#Software Engineering Course Project
#Group 3
#Cooper Poole
#Christian Chow Quan 
#Jason Barican
#Jian Gong

import re
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import *
import Important_Links as IL
import Useful_Links as UL
#import Profile_Functions as PF

#global arrays to store account information during runtime

loginUsername = ''
accEmailPrefs = 1
accSMSPrefs = 1
accTAPrefs = 1
accLangPrefs = "English"
PrevWindow = 'MainMenu'

#presents menu for user to utilize application functions
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.controller.geometry("800x800")
        self.controller.title('InCollege beta v0.5.3')
        
        tk.Label(self, text = "Welcome to InCollege Beta!\n\nINCOLLEGE SUCCESS STORY\nJohn used LinkedIn.\nHe could not get a job.\nJohn then started using InCollege.\nHe got a job.\n\nPlease select an option below.").pack(padx=10, pady=10)
        
        # Create a dropdown menu with the options "General", "Browse InCollege", "Business Solutions", and "Directories"
        menu_var = tk.StringVar()
        menu_var.set("Useful Links")
        options = ["General", "Browse InCollege", "Business Solutions", "Directories"]
        option_menu = tk.OptionMenu(self, menu_var, *options)
        option_menu.pack(padx=10, pady=10)
        option_menu.config(width=25, height =2)

        
        # Create buttons to navigate to different frames based on the selected option
        loginButton = tk.Button(self, text="Login", command=lambda: controller.show_frame("LoginWindow"), width = 25, height = 2)
        loginButton.pack(padx=10, pady=10)
        
        signInButton = tk.Button(self, text="Sign-Up", command=lambda: controller.show_frame("SignUpWindow"), width = 25, height = 2)
        signInButton.pack(padx=10, pady=10)
        
        videoButton = tk.Button(self, text="Play Video", command=lambda: controller.show_frame("VideoWindow"), width = 25, height = 2)
        videoButton.pack(padx=10, pady=10)
        
        findSomeoneButton = tk.Button(self, text="Find Someone", command=lambda: controller.show_frame("FindSomeoneFrame"), width = 25, height = 2)
        findSomeoneButton.pack(padx=10, pady=10)
        
        option_menu['menu'].entryconfig(0, command=lambda: controller.show_frame("GeneralWindow"))
        # Bind the "Browse InCollege", "Business Solutions", and "Directories" options to the "under_construction" function
        option_menu['menu'].entryconfig(1, command=lambda: controller.show_frame("UnderConstruction"))
        option_menu['menu'].entryconfig(2, command=lambda: controller.show_frame("UnderConstruction"))
        option_menu['menu'].entryconfig(3, command=lambda: controller.show_frame("UnderConstruction"))
        
        exitButton = tk.Button(self, text="Exit", command=self.quit, width = 25, height = 2)
        exitButton.pack(padx=10, pady=10)

        # Create the second dropdown menu with the options "Copyright Notice", "About", "Accessibility", "User Agreement", "Privacy Policy", "Cookie Policy", "Copyright Policy", "Brand Policy", "Guest Controls", and "Languages"
        menu_var2 = tk.StringVar()
        menu_var2.set("InCollege Important Links")
        options2 = ["Copyright Notice",
                    "About",
                    "Accessibility",
                    "User Agreement",
                    "Privacy Policy",
                    "Cookie Policy",
                    "Copyright Policy",
                    "Brand Policy",
                    "Languages"]
        option_menu2 = tk.OptionMenu(self, menu_var2, *options2)
        option_menu2.pack(padx=10, pady=10)
        option_menu2['menu'].entryconfig(0, command=lambda: controller.show_frame("CopyrightNoticeFrame"))
        option_menu2['menu'].entryconfig(1, command=lambda: controller.show_frame("InCollegeAboutFrame"))
        option_menu2['menu'].entryconfig(2, command=lambda: controller.show_frame("AccessibilityNoticeFrame"))
        option_menu2['menu'].entryconfig(3, command=lambda: controller.show_frame("UserAgreementFrame"))
        option_menu2['menu'].entryconfig(4, command=lambda: controller.show_frame("PrivacyPolicyFrame"))
        option_menu2['menu'].entryconfig(5, command=lambda: controller.show_frame("CookiePolicyFrame"))
        option_menu2['menu'].entryconfig(6, command=lambda: controller.show_frame("CopyrightPolicyFrame"))
        option_menu2['menu'].entryconfig(7, command=lambda: controller.show_frame("BrandPolicyFrame"))
        option_menu2['menu'].entryconfig(9, command=lambda: controller.show_frame("LanguageFrame"))
        option_menu2.config(width=25, height =2)
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):
       global PrevWindow
       PrevWindow = "MainMenu"

class GuestControlsFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor()

    # Create a label for the frame
    label = tk.Label(self, text="Guest Controls")
    label.pack(pady=10)

    # Create the InCollege Email checkbox
    self.email_var = tk.BooleanVar()
    self.email_checkbutton = tk.Checkbutton(self, text="InCollege Email", variable=self.email_var, onvalue = 1, offvalue = 0)
    self.email_checkbutton.select()
    self.email_checkbutton.pack(pady=5)

    # Create the SMS checkbox
    self.sms_var = tk.BooleanVar()
    self.sms_checkbutton = tk.Checkbutton(self, text="SMS", variable=self.sms_var, onvalue = 1, offvalue = 0)
    self.sms_checkbutton.select()
    self.sms_checkbutton.pack(pady=5)

    # Create the Targeted Advertising checkbox
    self.targeting_var = tk.BooleanVar()
    self.targeting_checkbutton = tk.Checkbutton(self, text="Targeted Advertising", variable=self.targeting_var, onvalue = 1, offvalue = 0)
    self.targeting_checkbutton.select()
    self.targeting_checkbutton.pack(pady=5)

    # Create a button to go back to the previous frame
    back_button = tk.Button(self, text="Back", command=self.save_prefs)
    back_button.pack(pady=10)

    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):
    get_email_pref_query = "SELECT EMAIL_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"
    get_sms_pref_query = "SELECT SMS_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"
    get_ta_pref_query = "SELECT TA_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"

    self.cursor.execute(get_email_pref_query)
    selected_email = self.cursor.fetchone()
    sel_email = selected_email[0]
 
    if sel_email == 1:
      self.email_checkbutton.select()
    else:
      self.email_var.set(0)

    self.cursor.execute(get_sms_pref_query)
    selected_sms = self.cursor.fetchone()
    sel_sms = selected_sms[0]

    if sel_sms == 1:
      self.sms_checkbutton.select()
    else:
      self.sms_var.set(0)

    self.cursor.execute(get_ta_pref_query)
    selected_ta = self.cursor.fetchone()
    sel_ta = selected_ta[0]
 
    if sel_ta == 1:
      self.targeting_checkbutton.select()
    else:
      self.targeting_var.set(0)

  def save_prefs(self):
    global loginUsername
    global PrevWindow
    update_email_pref_query = "UPDATE USER_DATA SET EMAIL_PREF = 1 WHERE USERNAME = '"+ loginUsername +"'"
    if self.email_var.get() == 0:
      update_email_pref_query = "UPDATE USER_DATA SET EMAIL_PREF = 0 WHERE USERNAME = '"+ loginUsername +"'"

    update_sms_pref_query = "UPDATE USER_DATA SET SMS_PREF = 1 WHERE USERNAME = '"+ loginUsername +"'" 
    if self.sms_var.get() == 0:
      update_sms_pref_query = "UPDATE USER_DATA SET SMS_PREF = 0 WHERE USERNAME = '"+ loginUsername +"'"

    update_ta_pref_query = "UPDATE USER_DATA SET TA_PREF = 1 WHERE USERNAME = '"+ loginUsername +"'"  
    if self.targeting_var.get() == 0:
      update_ta_pref_query = "UPDATE USER_DATA SET TA_PREF = 0 WHERE USERNAME = '"+ loginUsername +"'"

    self.cursor.execute(update_email_pref_query)
    self.cursor.execute(update_sms_pref_query)
    self.cursor.execute(update_ta_pref_query)
    self.conn.commit()

    self.controller.show_frame(PrevWindow)


class LanguageFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor()

    # Create a label
    label = tk.Label(self, text="Please select your preferred language:")
    label.pack(pady=10)

    # Create a StringVar to hold the selected language
    self.language_var = tk.StringVar()

    self.bind("<<ShowFrame>>", self.on_show_frame)
    # Create two checkboxes for English and Spanish, and make them mutually exclusive
    self.english_checkbox = tk.Checkbutton(self, text="English", variable=self.language_var, onvalue="English", offvalue="")
    self.spanish_checkbox = tk.Checkbutton(self, text="Spanish", variable=self.language_var, onvalue="Spanish", offvalue="")
    self.english_checkbox.select()
    self.english_checkbox.pack(pady=5)
    self.spanish_checkbox.pack(pady=5)
    # Create a button to save the selected language and return to the previous frame
    save_button = tk.Button(self, text="Save and Return", command=self.save_language)
    save_button.pack(pady=10)

  def on_show_frame(self, event):
    selected_language = self.language_var.get() 
    get_lang_pref_query = "SELECT LANG_PREF FROM USER_DATA WHERE USERNAME = '"+ loginUsername +"'"

    print(get_lang_pref_query)
    self.cursor.execute(get_lang_pref_query)
    selected_language = self.cursor.fetchone()
    sel_lang = selected_language[0]
 
    if sel_lang == "English":
      self.english_checkbox.select()
    elif sel_lang == "Spanish":
      self.spanish_checkbox.select()


  def save_language(self):
    global loginUsername
    global PrevWindow
    # Get the selected language from the StringVar and save it
    update_lang_pref_query = "UPDATE USER_DATA SET LANG_PREF = 'English' WHERE USERNAME = '"+ loginUsername +"'"
    if self.language_var.get() == "English":
      update_lang_pref_query = "UPDATE USER_DATA SET LANG_PREF = 'English' WHERE USERNAME = '"+ loginUsername +"'"
    elif self.language_var.get() == "Spanish":
      update_lang_pref_query = "UPDATE USER_DATA SET LANG_PREF = 'Spanish' WHERE USERNAME = '"+ loginUsername +"'"
    self.cursor.execute(update_lang_pref_query)
    self.conn.commit()

    # Return to the previous frame
    self.controller.show_frame(PrevWindow)


class GeneralWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.prevWindow = tk.StringVar()
    
    tk.Label(self, text = "General", font = ("Arial", 14)).pack(pady = 10)
    
    signUpButton = tk.Button(self, text="Sign Up", command=lambda: controller.show_frame("SignUpWindow"))
    signUpButton.pack(pady = 10)
    
    helpCenterButton = tk.Button(self, text="Help Center", command=lambda: controller.show_frame("HelpCenterFrame"))
    helpCenterButton.pack(pady = 10)
    
    aboutButton = tk.Button(self, text="About", command=lambda: controller.show_frame("AboutFrame"))
    aboutButton.pack(pady = 10)
    
    pressButton = tk.Button(self, text="Press", command=lambda: controller.show_frame("PressFrame"))
    pressButton.pack(pady = 10)
    
    blogButton = tk.Button(self, text="Blog", command=lambda: controller.show_frame("UnderConstruction"))
    blogButton.pack(pady = 10)
    
    careersButton = tk.Button(self, text="Careers", command=lambda: controller.show_frame("UnderConstruction"))
    careersButton.pack(pady = 10)
    
    developersButton = tk.Button(self, text="Developers", command=lambda: controller.show_frame("UnderConstruction"))
    developersButton.pack(pady = 10)
    
    backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(self.prevWindow))
    backButton.pack(pady = 10)
    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):
    global PrevWindow
    self.prevWindow = PrevWindow
    PrevWindow = "GeneralWindow"


class LoginWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Please enter username and password.").pack(padx=10, pady=10)
    self.loggedIn = False

    usernameLabel = tk.Label(self, text = "Username:")
    usernameLabel.pack(padx=10, pady=10)
    self.usernameEntry = tk.Entry(self, bd = 5)
    self.usernameEntry.pack(padx=10, pady=10)

    passwordLabel = tk.Label(self, text = "Password:")
    passwordLabel.pack(padx=10, pady=10)
    self.passwordEntry = tk.Entry(self, bd = 5)
    self.passwordEntry.pack(padx=10, pady=10)

    buttonframe = tk.Frame(self)
    buttonframe.pack()
    enterButton = tk.Button(buttonframe, text = "Enter", command = lambda: self.login())
    enterButton.pack(padx = 10, pady = 10)

    global PrevWindow
    backButton = tk.Button(buttonframe, text = "Back", command = lambda: controller.show_frame(PrevWindow))
    backButton.pack(padx=10, pady=10)



  def login(self):
    global loginUsername
    loginUsername = self.usernameEntry.get()
    loginPassword = self.passwordEntry.get()

    self.database = sqlite3.connect('database.db')  
    self.databaseCursor = self.database.cursor()

    self.databaseCursor.execute("SELECT * from USER_DATA")
    accounts = self.databaseCursor.fetchall()

    for i in range(0, len(accounts)):
      if loginUsername in accounts[i]:
        if loginPassword in accounts[i]:
          
          self.loggedIn = True
          messagebox.showinfo("Logged In", "You have successfully logged in.")
          self.controller.show_frame("ApplicationWindow")

    if self.loggedIn == False:
      messagebox.showerror("Error", "Incorrect username/password. Please try again.")
              
    
class SignUpWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    #opens database
    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor()
    
    #username entry
    tk.Label(self, text="Create Username:").pack(padx=10, pady=10)
    self.newUsernameEntry = tk.Entry(self,bd = 5)
    self.newUsernameEntry.pack(padx=10, pady=10)

    #password entry
    tk.Label(self,text= "Create Password:").pack(padx=10, pady=10)
    self.newPasswordEntry = tk.Entry(self,bd = 5)
    self.newPasswordEntry.pack(padx=10, pady=10)

    #full name entry
    tk.Label(self,text= "Enter your first and last name:").pack(padx=10, pady=10)
    self.fullNameEntry = tk.Entry(self,bd = 5)
    self.fullNameEntry.pack(padx=10, pady=10)

    tk.Label(self,text= "Please select account tier:").pack(padx=10, pady=10)
    self.clicked = StringVar()
    self.clicked.set("Select Tier")

    tiers = ["Standard", "Plus"]
    self.dropdown = tk.OptionMenu(self, self.clicked, *tiers)
    self.dropdown.pack(padx=10, pady=10)

    self.enterButton = tk.Button(self, text = "Enter", command = lambda: self.checkIfValid())
    self.enterButton.pack(padx = 10, pady = 10)
    global PrevWindow
    self.backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame(PrevWindow))
    self.backButton.pack(padx=10, pady=10)
        

  def checkIfValid(self):

    count = 0
    self.cursor.execute('''SELECT * from USER_DATA''')
    database = self.cursor.fetchall()
    
    usernameValid = False
    passwordValid = False
    fullNameValid = False
    tierValid = False

    count += len(database)
    
    if count >= 10:
      tk.Label(self, text="All permitted accounts have been created. Please come back later.").pack(padx=10, pady=10)
    else:
      self.newUsername = self.newUsernameEntry.get().replace(" ","")
      
      if len(database) != 0:
        self.cursor.execute("SELECT USERNAME from USER_DATA")
        usernames = self.cursor.fetchall()

        for i in range(0, len(usernames)):

          #ensuring username is unique
          if self.newUsername in usernames[i] or self.newUsername == "":
            messagebox.showerror("Error", "Invalid Entry/Account username already in use. Please try again.")
            self.newUsernameEntry.delete(0, 'end')
          else:
             usernameValid = True

      elif self.newUsername == "":
        messagebox.showerror("Error", "Invalid Entry/Account username already in use. Please try again.")
      
      elif len(database) == 0:
         usernameValid = True
  
    
    hasDigit = False
    hasNonAlphaNumeric = False
    
    self.newPassword = self.newPasswordEntry.get().replace(" ","")

    #validation check for length and presence of upercase, special, and numeric character.
    if len(self.newPassword) >= 8 and len(self.newPassword) <= 12 and self.newPassword.lower() != self.newPassword:
      for char in self.newPassword:
        if char.isdigit():
          hasDigit = True
        if not char.isalpha():
          hasNonAlphaNumeric = True
    if hasDigit is False or hasNonAlphaNumeric is False:
      messagebox.showerror("Error", "Invalid Password. Try a better password.")
      self.newPasswordEntry.delete(0, 'end')
    else:
      passwordValid = True

 
    self.name = self.fullNameEntry.get()
    nameCount = self.name.split()

    if len(nameCount) != 2:
      messagebox.showerror("Error", "Invalid format, Two names not found. Please try again.")
      self.fullNameEntry.delete(0, 'end')

    else:
      fullNameValid = True
      self.firstName = nameCount[0]
      self.lastName = nameCount[1]

    if self.clicked.get() == "Select Tier":
       messagebox.showerror("Error", "Please select an account tier.")
    else:
       tierValid = True

    if usernameValid is True and passwordValid is True and fullNameValid is True and tierValid is True:
      data_insert_query = ('''INSERT INTO USER_DATA(
                          USER_ID, USERNAME, PASSWORD, FIRSTNAME, LASTNAME, EMAIL_PREF, SMS_PREF, TA_PREF, LANG_PREF, TIER) VALUES
                          (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                          ''')
      count += 1
      #executed through tuples since insert query cant read from variable
      data_insert_tuple = (count, self.newUsername, self.newPassword, 
                           self.firstName, self.lastName, accEmailPrefs, 
                           accSMSPrefs, accTAPrefs, accLangPrefs, 
                           self.clicked.get())

      self.cursor.execute(data_insert_query, data_insert_tuple)
      self.conn.commit()
      
      messagebox.showinfo("Account Created", "You have successfully created a new account.")

      self.newUsernameEntry.delete(0, 'end')
      self.newPasswordEntry.delete(0, 'end')
      self.fullNameEntry.delete(0, 'end')
      self.clicked.set("Select Tier")
      self.controller.show_frame("MainMenu")

      usernameValid = False
      passwordValid = False
      fullNameValid = False
      tierValid = False


class VideoWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Video is now playing").pack(padx=10, pady=10)
    backButton = tk.Button(self, text = "Back", 
                          command = lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx=10, pady=10)


class ApplicationWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller    
    
    
    tk.Label(self, text = "You have successfully logged in!\nPlease select an option.").pack(padx=10, pady=10) 

    menu_var = tk.StringVar()
    menu_var.set("Useful Links")
    options = ["General", "Browse InCollege", "Business Solutions", "Directories"]
    option_menu = tk.OptionMenu(self, menu_var, *options)
    option_menu.pack(padx = 10, pady = 10)
    self.bind("<<ShowFrame>>", self.on_show_frame)

    option_menu['menu'].entryconfig(0, command=lambda: controller.show_frame("GeneralWindow"))
    # Bind the "Browse InCollege", "Business Solutions", and "Directories" options to the "under_construction" function
    option_menu['menu'].entryconfig(1, command=lambda: controller.show_frame("UnderConstruction"))
    option_menu['menu'].entryconfig(2, command=lambda: controller.show_frame("UnderConstruction"))
    option_menu['menu'].entryconfig(3, command=lambda: controller.show_frame("UnderConstruction"))

    CreateProfileButton = tk.Button(self, text = "Create Profile", command = lambda: controller.show_frame("ProfileFrame"))
    CreateProfileButton.pack(padx = 10, pady = 10)

    DisplayProfileButton = tk.Button(self, text = "Display Profile", command = lambda: controller.show_frame("DisplayProfileFrame"))
    DisplayProfileButton.pack(padx = 10, pady = 10)

    jobSearchButton = tk.Button(self, text = "Job/Internship Search", command = lambda: controller.show_frame("JobSearchFrame"))
    jobSearchButton.pack(padx = 10, pady = 10)

    findSomeoneButton = tk.Button(self, text = "Find Someone", command = lambda: controller.show_frame("FindSomeoneFrame"))
    findSomeoneButton.pack(padx = 10, pady = 10)

    learnSkillButton = tk.Button(self, text = "Learn a new skill", command = lambda: controller.show_frame("LearnSkillWindow"))
    learnSkillButton.pack(padx = 10, pady = 10)

    postJobButton = tk.Button(self, text = "Post a new job", command = lambda: controller.show_frame("AddJobFrame"))
    postJobButton.pack(padx = 10, pady = 10)

    FriendButton = tk.Button(self, text = "Show my network", command = lambda: controller.show_frame("FriendFrame"))
    FriendButton.pack(padx = 10, pady = 10)

    messagingButton = tk.Button(self, text = "Messaging", command = lambda: controller.show_frame("MessageFrame"))
    messagingButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
    backButton.pack(padx = 10, pady = 10)

# Create the second dropdown menu with the options "Copyright Notice", "About", "Accessibility", "User Agreement", "Privacy Policy", "Cookie Policy", "Copyright Policy", "Brand Policy", "Guest Controls", and "Languages"
    menu_var2 = tk.StringVar()
    menu_var2.set("InCollege Important Links")
    options2 = ["Copyright Notice",
                "About",
                "Accessibility",
                "User Agreement",
                "Privacy Policy",
                "Cookie Policy",
                "Copyright Policy",
                "Brand Policy",
                "Languages"]
    option_menu2 = tk.OptionMenu(self, menu_var2, *options2)
    option_menu2.pack(padx = 10, pady = 10)
    option_menu2['menu'].entryconfig(0, command=lambda: controller.show_frame("CopyrightNoticeFrame"))
    option_menu2['menu'].entryconfig(1, command=lambda: controller.show_frame("InCollegeAboutFrame"))
    option_menu2['menu'].entryconfig(2, command=lambda: controller.show_frame("AccessibilityNoticeFrame"))
    option_menu2['menu'].entryconfig(3, command=lambda: controller.show_frame("UserAgreementFrame"))
    option_menu2['menu'].entryconfig(4, command=lambda: controller.show_frame("PrivacyPolicyFrame"))
    option_menu2['menu'].entryconfig(5, command=lambda: controller.show_frame("CookiePolicyFrame"))
    option_menu2['menu'].entryconfig(6, command=lambda: controller.show_frame("CopyrightPolicyFrame"))
    option_menu2['menu'].entryconfig(7, command=lambda: controller.show_frame("BrandPolicyFrame"))
    option_menu2['menu'].entryconfig(9, command=lambda: controller.show_frame("LanguageFrame"))

  def on_show_frame(self, event):
    global PrevWindow
    PrevWindow = "ApplicationWindow"

class LearnSkillWindow(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text = "Please select a skill to learn.").pack(padx=10, pady=10) 

    skill1Button = tk.Button(self, text = "Skill 1", command = lambda: controller.show_frame("UnderConstruction"))
    skill1Button.pack(padx = 10, pady = 10)

    skill2Button = tk.Button(self, text = "Skill 2",command = lambda: controller.show_frame("UnderConstruction"))
    skill2Button.pack(padx = 10, pady = 10)

    skill3Button = tk.Button(self, text = "Skill 3",command = lambda: controller.show_frame("UnderConstruction"))
    skill3Button.pack(padx = 10, pady = 10)

    skill4Button = tk.Button(self, text = "Skill 4",command = lambda: controller.show_frame("UnderConstruction"))
    skill4Button.pack(padx = 10, pady = 10)

    skill5Button = tk.Button(self, text = "Skill 5",command = lambda: controller.show_frame("UnderConstruction"))
    skill5Button.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("ApplicationWindow"))
    backButton.pack(padx = 10, pady = 10)

    exitButton = tk.Button(self, text = "Exit", command = self.quit)
    exitButton.pack(padx = 10, pady = 10)
    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):
    global PrevWindow
    PrevWindow = "LearnSkillWindow"


    
class UnderConstruction(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller  

    tk.Label(self, text="Under Construction.").pack(padx=10, pady=10)
    global PrevWindow
    backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame(PrevWindow))
    backButton.pack(padx=10, pady=10)

          


class FindSomeoneFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller 
    self.conn = sqlite3.connect('database.db')
    self.create_widgets()
    self.bind("<<ShowFrame>>", self.on_show_frame)
    self.prevWindow = tk.StringVar()

  def create_widgets(self):
      self.name_label = tk.Label(self, text="Enter full name of person:")
      self.name_entry = tk.Entry(self)
      self.name_label.pack(padx=10, pady=10)
      self.name_entry.pack(padx=10, pady=10)

      self.search_button = tk.Button(self, text="Search", command=self.search)
      self.search_button.pack(padx=10, pady=10)

      backButton = tk.Button(self, text = "Back", command = lambda: self.controller.show_frame(self.prevWindow))
      backButton.pack(padx=10, pady=10)


  def on_show_frame(self, event):
    global PrevWindow
    self.prevWindow = PrevWindow
    PrevWindow = "FindSomeoneFrame"


  def search(self):
    searched_name = self.name_entry.get()
    nameCount = searched_name.split()
    displayButtons = False

    if len(nameCount) != 2:
      messagebox.showerror("Error", "Invalid format, Two names not found. Please try again.")
    else:
        firstName = nameCount[0]
        lastName = nameCount[1]
        cursor = self.conn.execute(f"SELECT * FROM USER_DATA WHERE FIRSTNAME = '{firstName}' AND LASTNAME = '{lastName}'")
        name = cursor.fetchall()
        print(name)
        if len(name) < 1:
            result_text = f"{searched_name} is not a part of the InCollege system yet."
            displayButtons = False
        else:
            result_text = f"{searched_name} is part of the InCollege system. Login or sign up to join them!"
            displayButtons = True

    result_label = tk.Label(self, text=result_text)
    result_label.pack(padx=5, pady=5)

    if displayButtons == True:
        loginButton = tk.Button(self, text = "login", command = lambda: self.controller.show_frame("LoginWindow"))
        loginButton.pack(padx=10, pady=10)
        signupButton = tk.Button(self, text = "Sign up", command = lambda: self.controller.show_frame("SignUpWindow"))
        signupButton.pack(padx=10, pady=10)


      
class JobSearchFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    tk.Label(self, text="Welcome to Job/Internship Search!\nPlease select an option below.").pack(padx=10, pady=10)

    applyForJobButton = tk.Button(self, text = "Apply For Job", command = lambda: controller.show_frame("JobApplicationFrame"))
    applyForJobButton.pack(padx = 10, pady = 10)

    viewApplicationsButton = tk.Button(self, text = "Your Job Applications", command = lambda: controller.show_frame("ViewJobApplicationFrame"))
    viewApplicationsButton.pack(padx = 10, pady = 10)

    viewNotAppliedButton = tk.Button(self, text = "Unapplied Jobs", command = lambda: controller.show_frame("ViewJobNotAppliedFrame"))
    viewNotAppliedButton.pack(padx = 10, pady = 10)

    savedJobsButton = tk.Button(self, text = "Saved Jobs", command = lambda: controller.show_frame("ViewSavedJobsFrame"))
    savedJobsButton.pack(padx = 10, pady = 10)

    addJobButton = tk.Button(self, text = "Add Job", command = lambda: controller.show_frame("AddJobFrame"))
    addJobButton.pack(padx = 10, pady = 10)

    removeJobButton = tk.Button(self, text = "Remove Job", command = lambda: controller.show_frame("RemoveJobFrame"))
    removeJobButton.pack(padx = 10, pady = 10)

    backButton = tk.Button(self, text = "Back", command = lambda: controller.show_frame("ApplicationWindow"))
    backButton.pack(padx=10, pady=10)

class AddJobFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.create_widgets()
    
    self.conn = sqlite3.connect('database.db')  	
    self.cursor = self.conn.cursor()

  def create_widgets(self):
      self.title_label = tk.Label(self, text="Enter title:")
      self.title_entry = tk.Entry(self)
      self.title_label.grid(row=0, column=0, padx=5, pady=5)
      self.title_entry.grid(row=0, column=1, padx=5, pady=5)

      self.description_label = tk.Label(self, text="Enter description:")
      self.description_entry = tk.Entry(self)
      self.description_label.grid(row=1, column=0, padx=5, pady=5)
      self.description_entry.grid(row=1, column=1, padx=5, pady=5)

      self.employer_label = tk.Label(self, text="Enter employer:")
      self.employer_entry = tk.Entry(self)
      self.employer_label.grid(row=2, column=0, padx=5, pady=5)
      self.employer_entry.grid(row=2, column=1, padx=5, pady=5)

      self.location_label = tk.Label(self, text="Enter location:")
      self.location_entry = tk.Entry(self)
      self.location_label.grid(row=3, column=0, padx=5, pady=5)
      self.location_entry.grid(row=3, column=1, padx=5, pady=5)

      self.salary_label = tk.Label(self, text="Enter salary:")
      self.salary_entry = tk.Entry(self)
      self.salary_label.grid(row=4, column=0, padx=5, pady=5)
      self.salary_entry.grid(row=4, column=1, padx=5, pady=5)

      self.post_button = tk.Button(self, text="Post job", command=self.post_job)
      self.post_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

      self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("ApplicationWindow"))
      self.back_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

  def post_job(self):
      global loginUsername	
      	
      count = 0	
      self.cursor.execute('''SELECT * from JOB_DATA''')	
      jobs = self.cursor.fetchall()
      user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]
      	
      count += len(jobs)	
      #checking if amount of accounts has exceeded maximum	
      if count >= 10:	
        result_text = "All permitted jobs have been created, please come back later"	
      else:	
        job_id = self.cursor.execute(f'SELECT COUNT(*) FROM JOB_DATA').fetchone()[0]
        job_id += 1
        title = self.title_entry.get()	
        description = self.description_entry.get()	
        employer = self.employer_entry.get()	
        location = self.location_entry.get()	
        salary = self.salary_entry.get()	
        data_insert_query = ('''INSERT INTO JOB_DATA(	
                            JOB_ID, TITLE, DESCRIPTION, EMPLOYER, LOCATION, SALARY, POSTED_BY) VALUES	
                            (?, ?, ?, ?, ?, ?, ?)	
                            ''')	
        data_insert_tuple = (job_id, title, description, employer, location, salary, user_id)	
        	
        self.cursor.execute(data_insert_query, data_insert_tuple)	
        self.conn.commit()	
        	
        result_text = "New job posted!"

        #clears values in entry
        self.title_entry.delete(0, END)
        self.description_entry.delete(0, END)
        self.employer_entry.delete(0, END)
        self.location_entry.delete(0, END)
        self.salary_entry.delete(0, END)

      result_label = tk.Label(self, text=result_text)
      result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
      

class RemoveJobFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    
    self.conn = sqlite3.connect('database.db')  	
    self.cursor = self.conn.cursor()

    #widget declarations for if database is empty
    self.emptyJobList_label= tk.Label(self, text="There are currently no posted jobs.")
    self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))
    

    #widget declarations for if database isn't empty
    self.dropdown_label = tk.Label(self, text="Please select job to delete.")

    self.dropdown = None

    self.delete_button = tk.Button(self, text="Delete", command=self.delete_job)
    self.back_button2 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))
    self.bind("<<ShowFrame>>", self.on_show_frame)
    
    
    
        
  def on_show_frame(self, event):
    self.cursor.execute('''SELECT TITLE, EMPLOYER from JOB_DATA''')
    database = self.cursor.fetchall()

    try:

      self.emptyJobList_label.grid_remove()
      self.back_button.grid_remove()
      self.dropdown_label.grid_remove()
      self.dropdown.grid_remove()
      self.delete_button.grid_remove()
      self.back_button2.grid_remove()
      

    except AttributeError:
          pass
    
    finally:

      if len(database) == 0:
        #hides widgets in else condition
        try:
          self.dropdown_label.grid_remove()
          self.dropdown.grid_remove()
          self.delete_button.grid_remove()
          self.back_button2.grid_remove()
        except AttributeError:
          pass
        finally:
          self.emptyJobList_label.grid(row=0, column=0, padx=5, pady=5)
          self.back_button.grid(row=1, column=0, padx=10, pady=10)
        
          
      
      else:
        #hides widgets in if condition
        
        self.emptyJobList_label.grid_remove()
        self.back_button.grid_remove()
            

        self.dropdown_label.grid(row=0, column=0, padx=5, pady=5)

        jobList = []
        
        for i in range(0, len(database)):
          jobList.append(f"{database[i][0]} at {database[i][1]}")

        self.clicked = StringVar()
        self.clicked.set("Select Job")

        self.dropdown = tk.OptionMenu(self, self.clicked, *jobList)
        self.dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.delete_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.back_button2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

      
        
      
  def delete_job(self):
    
    value = self.clicked.get().split()

    self.cursor.execute(f'DELETE FROM JOB_DATA WHERE TITLE = "{value[0]}" AND EMPLOYER = "{value[2]}"')
    self.conn.commit()

    self.cursor.execute(f'DELETE FROM APPLICATIONS WHERE TITLE = "{value[0]}" AND EMPLOYER = "{value[2]}"')
    self.conn.commit()

    self.cursor.execute(f'DELETE FROM SAVED_JOBS WHERE TITLE = "{value[0]}" AND EMPLOYER = "{value[2]}"')
    self.conn.commit()
    

    messagebox.showinfo("Job Deleted", "You have successfully deleted the job.")
    self.controller.show_frame("JobSearchFrame")

class JobApplicationFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    self.conn = sqlite3.connect('database.db')  	
    self.cursor = self.conn.cursor()

    #widget declarations for if database is empty
    self.emptyJobList_label= tk.Label(self, text="There are currently no posted jobs.")
    self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))
    
    #widget declarations for if database isn't empty
    self.dropdown_label = tk.Label(self, text="Please select job.")
    self.dropdown = None

    self.display_button = tk.Button(self, text="Display", command=self.display_job)
    self.back_button2 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))

    #widget declarations for 'display_job' function
    
    self.apply_button = tk.Button(self, text="Apply for Job", command=self.application_info)
    self.save_button = tk.Button(self, text="Save Job", command=self.save_job)
    self.back_button3 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobApplicationFrame"))

    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):
    self.user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]
    self.job_id = self.cursor.execute(f'SELECT JOB_ID FROM APPLICATIONS WHERE USER_ID = "{self.user_id}"').fetchall()

    if self.job_id: #if list has data
      self.cursor.execute(f"SELECT * FROM JOB_DATA jd LEFT JOIN APPLICATIONS a ON jd.JOB_ID = a.JOB_ID AND a.USER_ID ={self.user_id} WHERE POSTED_BY != {self.user_id} AND a.JOB_ID IS NULL AND a.USER_ID IS NULL")
    else: #if job_id list is empty
      self.cursor.execute(f"SELECT TITLE, EMPLOYER FROM JOB_DATA WHERE POSTED_BY != {self.user_id}")
    
    database = self.cursor.fetchall()
    
    

    try:
      self.job_title.grid_remove()
      self.job_description.grid_remove()
      self.job_employer.grid_remove()
      self.job_location.grid_remove()
      self.job_salary.grid_remove()
      
    except AttributeError:
      pass
    try:
      self.emptyJobList_label.grid_remove()
      self.back_button.grid_remove()
      self.dropdown_label.grid_remove()
      self.dropdown.grid_remove()
      self.display_button.grid_remove()
      self.back_button2.grid_remove()
    except AttributeError:
      pass
    try:
      self.apply_button.grid_remove()
      self.save_button.grid_remove()
      self.back_button3.grid_remove()
    except AttributeError:
       pass
    try:
      self.graduation_label.grid_remove()
      self.graduation_entry.grid_remove()
      self.start_label.grid_remove()
      self.start_entry.grid_remove()
      self.why_label.grid_remove()
      self.why_entry.grid_remove()
      self.apply_button.grid_remove()
      
      self.back_button.grid_remove()
    finally:
      if len(database) == 0:
        #hides widgets in else condition
        try:
          self.dropdown_label.grid_remove()
          self.dropdown.grid_remove()
          self.display_button.grid_remove()
          self.back_button2.grid_remove()
        except AttributeError:
          pass
        finally:
          self.emptyJobList_label.grid(row=0, column=0, padx=5, pady=5)
          self.back_button.grid(row=1, column=0, padx=10, pady=10)

      else:
        #hides widgets in if condition
        self.emptyJobList_label.grid_remove()
        self.back_button.grid_remove()

        self.dropdown_label.grid(row=0, column=0, padx=5, pady=5)
        jobList = []

        for i in range(0, len(database)):
          
          jobList.append(f"{database[i][0]} at {database[i][1]}")

        self.clicked = StringVar()
        self.clicked.set(jobList[0])

        self.dropdown = OptionMenu(self, self.clicked, *jobList)
        self.dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.display_button.grid(row=2, column=0, padx=5, pady=5 )
        self.back_button2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
      

  def display_job(self):
    try:
      self.job_title.grid_remove()
      self.job_description.grid_remove()
      self.job_employer.grid_remove()
      self.job_location.grid_remove()
      self.job_salary.grid_remove()
      self.apply_button.grid_remove()
      self.back_button3.grid_remove()
      
    except AttributeError:
      pass
    try:
      self.emptyJobList_label.grid_remove()
      self.back_button.grid_remove()
    except AttributeError:
      pass
    try:
      self.dropdown_label.grid_remove()
      self.dropdown.grid_remove()
      self.display_button.grid_remove()
      self.back_button2.grid_remove()
    except AttributeError:
       pass
    finally:
    
      value = self.clicked.get().split()
      self.cursor.execute(f'SELECT * FROM JOB_DATA WHERE TITLE = "{value[0]}" AND EMPLOYER = "{value[2]}"')
      self.job = self.cursor.fetchall()
      

      self.job_id = tk.Label(self, text=f"{self.job[0][0]}")
      self.job_title = tk.Label(self, text=f"{self.job[0][1]}")
      self.job_description = tk.Label(self, text=f"{self.job[0][2]}")
      self.job_employer = tk.Label(self, text=f"{self.job[0][3]}")
      self.job_location = tk.Label(self, text=f"{self.job[0][4]}")
      self.job_salary = tk.Label(self, text=f"{self.job[0][5]}")
      
      self.job_title.grid(row=0, column=0, padx=5, pady=5)
      
      self.job_description.grid(row=1, column=0, padx=5, pady=5)
      
      self.job_employer.grid(row=2, column=0, padx=5, pady=5)
      
      self.job_location.grid(row=3, column=0, padx=5, pady=5)
      
      self.job_salary.grid(row=4, column=0, padx=5, pady=5)
      
      self.apply_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

      self.save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
      
      self.back_button3.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

  
  def application_info(self):
    try:
      self.job_title.grid_remove()
      self.job_description.grid_remove()
      self.job_employer.grid_remove()
      self.job_location.grid_remove()
      self.job_salary.grid_remove()
      self.apply_button.grid_remove()
      self.back_button3.grid_remove()
    except AttributeError:
      pass


    self.graduation_label = tk.Label(self, text="Graduation Date (mm/dd/yyyy): ")
    self.graduation_label.grid(row=1, column=1, padx=5, pady=5)

    self.graduation_entry = tk.Entry(self)
    self.graduation_entry.grid(row=1, column=2, padx=5, pady=5)

    self.start_label = tk.Label(self, text="Start Working Date (mm/dd/yyyy): ")
    self.start_label.grid(row=2, column=1, padx=5, pady=5)

    self.start_entry = tk.Entry(self)
    self.start_entry.grid(row=2, column=2, padx=5, pady=5)

    self.why_label = tk.Label(self, text="Why are you a good fit for this job?")
    self.why_label.grid(row=3, column=1, padx=5, pady=5)

    self.why_entry = tk.Text(self, height=5)
    self.why_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    self.apply_button = tk.Button(self, text="Apply", command=self.apply_job)
    self.apply_button.grid(row=5, column=1, padx=5, pady=5)

    self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))
    self.back_button.grid(row=5, column=2, padx=5, pady=5)

  def save_job(self):
      global loginUsername

      user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]

      job_id = self.job[0][0]
      job_title = self.job[0][1]
      job_employer = self.job[0][3]
      job_description = self.job[0][2]

      self.cursor.execute(f'INSERT OR IGNORE INTO SAVED_JOBS (JOB_ID, USER_ID, TITLE, EMPLOYER, DESCRIPTION) VALUES (?,?,?,?,?)',
                          (job_id, user_id, job_title, job_employer, job_description))
      self.conn.commit()

      messagebox.showinfo("Job Saved", "Job successfully saved.")
      self.controller.show_frame("JobSearchFrame")

  def apply_job(self):
      # Retrieve the job details
      global loginUsername

      user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]

      job_id = self.job[0][0]
      job_title = self.job[0][1]
      job_employer = self.job[0][3]
      job_description = self.job[0][2]
      graduation_date = self.graduation_entry.get()
      start_date = self.start_entry.get()
      why = self.why_entry.get(1.0, "end-1c")

      # Insert the application data into the database
      self.cursor.execute('INSERT OR IGNORE INTO APPLICATIONS (JOB_ID, USER_ID, TITLE, EMPLOYER, DESCRIPTION, GRADUATION_DATE, START_DATE, WHY) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                            (job_id, user_id, job_title, job_employer, job_description, graduation_date, start_date, why))
      self.conn.commit()

      # Show a confirmation message
      messagebox.showinfo("Application Submitted", "Your job application has been submitted.")

      # Clear the form
      self.graduation_entry.delete(0, END)
      self.start_entry.delete(0, END)
      self.why_entry.delete("1.0", "end")

      self.controller.show_frame("JobSearchFrame")
      

class ViewJobApplicationFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    self.conn = sqlite3.connect('database.db')  	
    self.cursor = self.conn.cursor()
    
    #widget declarations for if job applications is empty
    self.emptyJobList_label= tk.Label(self, text="You currently have no job applications.")
    self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))

    #widget declarations for if job applications isn't empty
    self.dropdown_label = tk.Label(self, text="Your Job Applications:")
    self.dropdown = None

    self.back_button2 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))

    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):

    self.user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]
    self.cursor.execute(f"SELECT TITLE, EMPLOYER FROM APPLICATIONS WHERE USER_ID = {self.user_id}")

    database = self.cursor.fetchall()

    try:
      self.emptyJobList_label.grid_remove()
      self.back_button.grid_remove()
      self.dropdown_label.grid_remove()
      self.dropdown.grid_remove()
      
      self.back_button2.grid_remove()
    except AttributeError:
      pass
    finally:
      if len(database) == 0:
        #hides widgets in else condition
        try:
          self.dropdown_label.grid_remove()
          self.dropdown.grid_remove()
          self.back_button2.grid_remove()
        except AttributeError:
          pass
        finally:
          self.emptyJobList_label.grid(row=0, column=0, padx=5, pady=5)
          self.back_button.grid(row=1, column=0, padx=10, pady=10)

      else:
        #hides widgets in if condition
        self.emptyJobList_label.grid_remove()
        self.back_button.grid_remove()

        self.dropdown_label.grid(row=0, column=0, padx=5, pady=5)
        jobAppList = []

        for i in range(0, len(database)):
          
          jobAppList.append(f"{database[i][0]} at {database[i][1]}")

        self.clicked = StringVar()
        self.clicked.set(jobAppList[0])

        self.dropdown = OptionMenu(self, self.clicked, *jobAppList)
        self.dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.back_button2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

class ViewJobNotAppliedFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    self.conn = sqlite3.connect('database.db')  	
    self.cursor = self.conn.cursor()
    
    #widget declarations for if job applications is empty
    self.emptyJobList_label= tk.Label(self, text="You currently have no unapplied jobs.")
    self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))

    #widget declarations for if job applications isn't empty
    self.dropdown_label = tk.Label(self, text="Jobs You Haven't Applied for:")
    self.dropdown = None

    self.back_button2 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))

    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):

    self.user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]
    self.app_user_id = self.cursor.execute("SELECT USER_ID FROM APPLICATIONS").fetchall()
    self.cursor.execute(f"SELECT TITLE, EMPLOYER FROM JOB_DATA WHERE JOB_ID NOT IN (SELECT JOB_ID FROM APPLICATIONS)")

    database = self.cursor.fetchall()

    try:
      self.emptyJobList_label.grid_remove()
      self.back_button.grid_remove()
      self.dropdown_label.grid_remove()
      self.dropdown.grid_remove()
      
      self.back_button2.grid_remove()
    except AttributeError:
      pass
    finally:
      if len(database) == 0:
        #hides widgets in else condition
        try:
          self.dropdown_label.grid_remove()
          self.dropdown.grid_remove()
          self.back_button2.grid_remove()
        except AttributeError:
          pass
        finally:
          self.emptyJobList_label.grid(row=0, column=0, padx=5, pady=5)
          self.back_button.grid(row=1, column=0, padx=10, pady=10)

      else:
        #hides widgets in if condition
        self.emptyJobList_label.grid_remove()
        self.back_button.grid_remove()

        self.dropdown_label.grid(row=0, column=0, padx=5, pady=5)
        jobAppList = []

        for i in range(0, len(database)):
          
          jobAppList.append(f"{database[i][0]} at {database[i][1]}")

        self.clicked = StringVar()
        self.clicked.set(jobAppList[0])

        self.dropdown = OptionMenu(self, self.clicked, *jobAppList)
        self.dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.back_button2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

class ViewSavedJobsFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    self.conn = sqlite3.connect('database.db')  	
    self.cursor = self.conn.cursor()
    
    #widget declarations for if job applications is empty
    self.emptyJobList_label= tk.Label(self, text="You currently have no saved job applications.")
    self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))

    #widget declarations for if job applications isn't empty
    self.dropdown_label = tk.Label(self, text="Your Saved Jobs:")
    self.dropdown = None

    self.back_button2 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("JobSearchFrame"))

    self.bind("<<ShowFrame>>", self.on_show_frame)

  def on_show_frame(self, event):

    self.user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]
    self.cursor.execute(f"SELECT TITLE, EMPLOYER FROM SAVED_JOBS WHERE USER_ID = {self.user_id}")

    database = self.cursor.fetchall()

    try:
      self.emptyJobList_label.grid_remove()
      self.back_button.grid_remove()
      self.dropdown_label.grid_remove()
      self.dropdown.grid_remove()
      
      self.back_button2.grid_remove()
    except AttributeError:
      pass
    finally:
      if len(database) == 0:
        #hides widgets in else condition
        try:
          self.dropdown_label.grid_remove()
          self.dropdown.grid_remove()
          self.back_button2.grid_remove()
        except AttributeError:
          pass
        finally:
          self.emptyJobList_label.grid(row=0, column=0, padx=5, pady=5)
          self.back_button.grid(row=1, column=0, padx=10, pady=10)

      else:
        #hides widgets in if condition
        self.emptyJobList_label.grid_remove()
        self.back_button.grid_remove()

        self.dropdown_label.grid(row=0, column=0, padx=5, pady=5)
        jobAppList = []

        for i in range(0, len(database)):
          
          jobAppList.append(f"{database[i][0]} at {database[i][1]}")

        self.clicked = StringVar()
        self.clicked.set(jobAppList[0])

        self.dropdown = OptionMenu(self, self.clicked, *jobAppList)
        self.dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.back_button2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
class FriendFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        # Create Scrollbar widget and Canvas widget
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas = tk.Canvas(self, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.canvas.yview)
        # Create a Frame widget to contain all the elements and buttons
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
  
    def on_show_frame(self, event):
        global loginUsername
        # Add the Pending Requests LabelFrame
        if not hasattr(self, 'pending_frame'):
            self.pending_frame = tk.LabelFrame(self.frame, text="Pending Requests")
            self.pending_frame.pack(pady=10)
        self.conn = sqlite3.connect('database.db')
        cursor = self.conn.execute(f"SELECT USER_ID FROM USER_DATA WHERE USERNAME = '{loginUsername}'")
        userid = cursor.fetchone()[0]
        self.userid=userid
        self.myfirst = self.conn.execute(f"SELECT FIRSTNAME FROM USER_DATA WHERE USER_ID = {userid}").fetchone()[0]
        self.mylast = self.conn.execute(f"SELECT LASTNAME FROM USER_DATA WHERE USER_ID = {userid}").fetchone()[0]
        # Display the elements and buttons in the Pending Requests LabelFrame
        cursor = self.conn.execute(f"SELECT F.PENDING_FIRST, F.PENDING_LAST, F.PENDING_USER, P.University, P.Major FROM PENDING F LEFT JOIN PROFILE_DATA P ON F.PENDING_USER = P.USERNAME WHERE F.USER_ID = '{self.userid}'")
        self.pendingUsers = cursor.fetchall()
        self.add_pending_elements(self.pending_frame)
        # Add the Friends LabelFrame
        if not hasattr(self, 'friends_frame'):
            self.friends_frame = tk.LabelFrame(self.frame, text="Friends")
            self.friends_frame.pack(pady=10)
        # Display the elements and buttons in the Friends LabelFrame
        cursor = self.conn.execute(f"SELECT F.FRIEND_FIRST, F.FRIEND_LAST, P.University, P.Major FROM FRIENDS F LEFT JOIN PROFILE_DATA P ON F.FRIEND_USER = P.USERNAME WHERE F.USER_ID = '{self.userid}'")
        self.friendUsers = cursor.fetchall()
        self.add_friends_elements(self.friends_frame)
        if not hasattr(self, 'search_frame'):
            self.search_frame = tk.LabelFrame(self.frame, text="Search a friend by last name, university, or major")
            self.search_frame.pack(pady=10)
        # Display the elements and buttons in the search LabelFrame
        cursor = self.conn.execute(f"SELECT FIRSTNAME, LASTNAME FROM USER_DATA WHERE USER_ID = '{userid}'")
        self.results = cursor.fetchall()
        self.add_search_elements(self.search_frame)
        # Allow the Canvas widget to automatically adjust its size
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def add_pending_elements(self, frame):
        # Clear the Frame widget before adding elements
        for widget in frame.winfo_children():
            widget.destroy()
        if not self.pendingUsers:
            label = tk.Label(frame, text="No new pending requests", width=50)
            label.grid(row=0, column=0, padx=5, pady=5)
        else:
            # Add elements and buttons to the Frame widget
            for i, element in enumerate(self.pendingUsers):
                label = tk.Label(frame, text=element, width=50)
                label.grid(row=i, column=0, padx=5, pady=5)
                button1 = tk.Button(frame, text='reject', command=lambda element=element: self.delete_element(element))
                button1.grid(row=i, column=1, padx=5, pady=5)
                button2 = tk.Button(frame, text='accept', command=lambda element=element: self.move_element(element))
                button2.grid(row=i, column=2, padx=5, pady=5)
                
    def add_search_elements(self, frame):
        # Clear the Frame widget before adding elements
        for widget in frame.winfo_children():
            widget.destroy()
        # Create and add the search label and text box widgets
        search_label = tk.Label(frame, text="")
        search_label.grid(row=0, column=0, padx=5, pady=5)
        self.search_textbox = tk.Entry(frame, width=50)
        self.search_textbox.grid(row=0, column=1, padx=5, pady=5)
        # Create and add the search button widget
        search_button = tk.Button(frame, text="Search", command=self.search)
        search_button.grid(row=0, column=2, padx=5, pady=5)
        # Add back button
        backButton = tk.Button(frame, text="Back", command=lambda: self.controller.show_frame("ApplicationWindow"))
        backButton.grid(row=len(self.results)+1, column=0, padx=5, pady=5)

    def search(self):
        # Get the search query from the text box
        query = self.search_textbox.get()
        # Clear the Frame widget before adding elements
        for widget in self.search_frame.winfo_children():
            #if widget != self.search_textbox:
            widget.destroy()
        # Execute the search query
        cursor = self.conn.execute(f"SELECT u.USERNAME, u.FIRSTNAME, u.LASTNAME, p.University, p.Major FROM USER_DATA u LEFT JOIN PROFILE_DATA p ON u.USERNAME = p.USERNAME WHERE (u.LASTNAME LIKE '%{query}%' OR p.University LIKE '%{query}%' OR p.Major LIKE '%{query}%')")
        self.results = cursor.fetchall()
        if not self.results:
            label = tk.Label(self.search_frame, text="No results found", width=50)
            label.grid(row=0, column=0, padx=5, pady=5)
        else:
            # Add elements and buttons to the Frame widget
            for i, element in enumerate(self.results):
                # Check if the user is already a friend
                cursor = self.conn.execute("SELECT * FROM FRIENDS WHERE USER_ID = ? AND FRIEND_FIRST = ? AND FRIEND_LAST = ?",
                (self.userid, element[1], element[2]))
                if not cursor.fetchone() and loginUsername != element[0]:
                    label = tk.Label(self.search_frame, text=f"{element[0]} {element[1]} {element[2]} {element[3]} {element[4]}",width=50)
                    university = element[3] if element[3] is not None else " "
                    major = element[4] if element[4] is not None else " "
                    label = tk.Label(self.search_frame, text=f"{element[0]} {element[1]} {element[2]} {university} {major}", width=50)                
                    label.grid(row=i, column=0, padx=5, pady=5)
                    button = tk.Button(self.search_frame, text='add', command=lambda element=element: self.add_friend(element))
                    button.grid(row=i, column=1, padx=5, pady=5)
            cursor = self.conn.execute(f"SELECT USER_ID FROM USER_DATA WHERE USERNAME = '{element[0]}'")
            self.pendingId = cursor.fetchone()[0]
        backButton = tk.Button(self.search_frame, text="Back", command=lambda: self.controller.show_frame("ApplicationWindow"))
        backButton.grid(row=len(self.results)+1, column=0, padx=5, pady=5)

    def add_friends_elements(self, frame):
        # Clear the Frame widget before adding elements
        for widget in frame.winfo_children():
            widget.destroy()
        cursor = self.conn.execute(f"SELECT F.FRIEND_FIRST, F.FRIEND_LAST, P.University, P.Major FROM FRIENDS F LEFT JOIN PROFILE_DATA P ON F.FRIEND_USER = P.USERNAME WHERE F.USER_ID = '{self.userid}'")
        self.friendUsers = cursor.fetchall()
        if not self.friendUsers:
            label = tk.Label(frame, text="Don't have any friends yet", width=50)
            label.grid(row=0, column=0, padx=5, pady=5)
        else:
            # Add elements and buttons to the Frame widget
            for i, element in enumerate(self.friendUsers):
                university = element[2] if element[2] is not None else ""
                major = element[3] if element[3] is not None else ""
                label = tk.Label(frame, text=f"{element[0]} {element[1]} {university} {major}", width=50)
                label.grid(row=i, column=0, padx=5, pady=5)
                button1 = tk.Button(frame, text='disconnect', command=lambda element=element: self.disconnect_element(element))
                button1.grid(row=i, column=1, padx=5, pady=5)

    #delete request from pending table
    def delete_element(self, element):
        self.conn.execute(f"DELETE FROM PENDING WHERE USER_ID = {self.userid} AND PENDING_FIRST = '{element[0]}' AND PENDING_LAST = '{element[1]}'")
        self.conn.commit()
        self.pendingUsers.remove(element)
        self.update_frame()
        #move user to friends table
    def move_element(self, element):
        self.conn.execute(f"INSERT INTO FRIENDS (USER_ID, FRIEND_FIRST, FRIEND_LAST,FRIEND_USER) VALUES ({self.userid}, '{element[0]}', '{element[1]}','{element[2]}')")
        self.conn.execute(f"DELETE FROM PENDING WHERE USER_ID = {self.userid} AND PENDING_FIRST = '{element[0]}' AND PENDING_LAST = '{element[1]}'")
        self.conn.commit()   
        self.pendingUsers.remove(element)
        self.friendUsers.append((element[0], element[1]))
        cursor = self.conn.execute(f"SELECT USER_ID FROM USER_DATA WHERE FIRSTNAME = '{element[0]}' AND LASTNAME = '{element[1]}'")
        friend_userid = cursor.fetchone()[0]
        self.conn.execute(f"INSERT INTO FRIENDS (USER_ID, FRIEND_FIRST, FRIEND_LAST, FRIEND_USER) VALUES ({friend_userid}, '{self.myfirst}', '{self.mylast}','{loginUsername}')")
        self.conn.commit()
        self.update_frame()

    def add_friend(self, element):
        # Check if the friend request already exists
        cursor = self.conn.execute("SELECT * FROM PENDING WHERE USER_ID = ? AND PENDING_FIRST = ? AND PENDING_LAST = ?",
                                (self.pendingId, self.myfirst, self.mylast))
        if not cursor.fetchone():
            # Friend request doesn't exist, add it
            self.conn.execute("INSERT INTO PENDING (USER_ID, PENDING_FIRST, PENDING_LAST, PENDING_USER) VALUES (?, ?, ?, ?)",
                            (self.pendingId, self.myfirst, self.mylast, loginUsername))
            self.conn.commit()
            self.update_frame()
        else:
            # Friend request already exists, show message box
            messagebox.showinfo("Friend Request Sent", "You have already sent a friend request to this user.")

    #remove user from friends table
    def disconnect_element(self, element):
        #delete my friend
        self.conn.execute(f"DELETE FROM FRIENDS WHERE USER_ID = {self.userid} AND FRIEND_FIRST = '{element[0]}' AND FRIEND_LAST = '{element[1]}'")
        self.conn.commit()
        #delete friend's friend(me)
        cursor = self.conn.execute(f"SELECT USER_ID FROM USER_DATA WHERE FIRSTNAME = '{element[0]}' AND LASTNAME = '{element[1]}'")
        friend_userid = cursor.fetchone()[0]
        self.conn.execute(f"DELETE FROM FRIENDS WHERE USER_ID = {friend_userid} AND FRIEND_FIRST = '{self.myfirst}' AND FRIEND_LAST = '{self.mylast}'")       
        self.conn.commit()
        self.friendUsers.remove(element)
        self.update_frame()

    def update_frame(self):
        self.add_pending_elements(self.pending_frame)
        self.add_friends_elements(self.friends_frame)
        self.add_search_elements(self.search_frame)
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def add_elements(self):
        # Clear the Frame widget before adding elements
        for widget in self.frame.winfo_children():
            widget.destroy()
        # Add pending requests label frame and elements
        pendingFrame = tk.LabelFrame(self.frame, text="Pending Requests")
        pendingFrame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5, expand=True)
        self.add_pending_elements(pendingFrame)
        # Add friends label frame and elements
        friendsFrame = tk.LabelFrame(self.frame, text="Friends")
        friendsFrame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5, expand=True)
        self.add_friends_elements(friendsFrame)
        searchFrame = tk.LabelFrame(self.frame, text="search a friend by last name, university, or major")
        searchFrame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5, expand=True)
        self.add_friends_elements(searchFrame)
        # Allow the Canvas widget to automatically adjust its size
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

class MessageFrame(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    self.bind("<<ShowFrame>>", self.on_show_frame)
    
    #widgets for initial screen in MessageFrame
    self.selectOptionLabel = tk.Label(self, text="Please select an option below:")
    self.selectUserButton = tk.Button(self, text="Send Message", command=self.select_user)
    self.inboxButton = tk.Button(self, text="Inbox", command=self.inbox)
    self.backButton = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("ApplicationWindow"))

    #widgets for inbox function in message frame
    self.noMessagesLabel = tk.Label(self, text="You currently have no messages.")
    self.backButton2 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("MessageFrame"))

    

  def on_show_frame(self, event):
    global loginUsername

    self.conn = sqlite3.connect('database.db')  
    self.cursor = self.conn.cursor() 

    self.user_id = self.cursor.execute(f'SELECT USER_ID FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]
    self.tier = self.cursor.execute(f'SELECT TIER FROM USER_DATA WHERE USERNAME = "{loginUsername}"').fetchone()[0]
    self.messages = self.conn.execute(f'SELECT SENDER, MESSAGE FROM MESSAGES WHERE RECEIVER = "{loginUsername}"').fetchall()
    self.friends = self.cursor.execute(f"SELECT FRIEND_FIRST, FRIEND_LAST FROM FRIENDS WHERE USER_ID = {self.user_id}").fetchall()
    self.usersList = self.cursor.execute(f"SELECT * FROM USER_DATA WHERE USER_ID != {self.user_id}").fetchall()
    self.names = self.cursor.execute(f"SELECT FIRSTNAME, LASTNAME FROM USER_DATA WHERE USER_ID != {self.user_id}").fetchall()

    self.selectOptionLabel.grid(padx=5, pady=5)
    self.selectUserButton.grid(padx=5, pady=5)
    self.inboxButton.grid(padx=5, pady=5)
    self.backButton.grid(padx=5, pady=5)

    self.remove_widgets2()

  

  def select_user(self):
    self.remove_widgets()
    self.remove_widgets2()
    try:
      self.typeMessageLabel.grid_remove()
      self.messageText.grid_remove()
      self.sendMessageButton.grid_remove()
      self.backButton5.grid_remove()
    except AttributeError:
      pass
    

    if len(self.usersList) == 0:
      self.noUsersLabel = tk.Label(self, text="There are no other registered users.")
      self.noUsersLabel.grid(padx=5, pady=5)

      self.backButton4 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("MessageFrame"))
      self.backButton4.grid(padx=5, pady=5)

    else:
      self.selectFriendLabel = tk.Label(self, text="Please select user to send a message to.")
      self.selectFriendLabel.grid(padx=5, pady=5)

      self.clicked = StringVar()
      self.clicked.set(self.names[0])
      self.dropdown = tk.OptionMenu(self, self.clicked, *self.names)
      self.dropdown.grid(padx=5, pady=5)

      self.selectButton = tk.Button(self, text="Send A Message", command= self.check_if_friend)
      self.selectButton.grid(padx=5, pady=5)

      self.backButton4 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("MessageFrame"))
      self.backButton4.grid(padx=5, pady=5)

  def check_if_friend(self):
    self.value = re.sub("[('),]", "", self.clicked.get())
    self.value = self.value.split(' ')
    
    valid = False

    if self.tier == "Premium":
      self.type_message()
    else:
      for i in range(0, len(self.friends)):
        if self.value[0] in self.friends[i] and self.value[1] in self.friends[i]:
          valid = True
          break
      if valid == False:
        messagebox.showerror("Error", "You cannot send a message to a user who is not in your friends list. Please select another user.")
        self.select_user()
      else:
        self.type_message()
          

  def type_message(self):
    self.remove_widgets2()

    self.typeMessageLabel = tk.Label(self, text="Please type your message:")
    self.typeMessageLabel.grid(padx=5, pady=5)

    self.messageText = tk.Text(self, height=5)
    self.messageText.grid(padx=5, pady=5)

    self.sendMessageButton = tk.Button(self, text="Send Message", command= self.send_message)
    self.sendMessageButton.grid(padx=5, pady=5)

    self.backButton5 = tk.Button(self, text="Back", command=self.select_user)
    self.backButton5.grid(padx=5, pady=5)

  def send_message(self):
    sender = loginUsername
    receiver = self.cursor.execute(f'SELECT USERNAME FROM USER_DATA WHERE FIRSTNAME = "{self.value[0]}" AND LASTNAME = "{self.value[1]}"').fetchone()[0]
    message = self.messageText.get("1.0", 'end-1c')

    message_query = ('''INSERT INTO MESSAGES(
                    SENDER, RECEIVER, MESSAGE) VALUES
                    (?, ?, ?)
                    ''')
    
    message_insert_tuple = (sender, receiver, message)

    self.cursor.execute(message_query, message_insert_tuple)
    self.conn.commit()

    messagebox.showinfo("Message Sent.", "Your message has been sent.")
    self.controller.show_frame("MessageFrame")


  def inbox(self):
    self.remove_widgets()
    self.remove_widgets2()
    
    if len(self.messages) == 0:
      self.noMessagesLabel.grid(padx=5, pady=5)
      self.backButton2.grid(padx=5, pady=5)

    else:
      for i in range(0, len(self.messages)):
        messageList = []
        messageList.append(f'"{self.messages[i][0]}": "{self.messages[i][1]}"')
      

      self.inboxLabel = tk.Label(self, text="Inbox:")
      self.inboxLabel.grid(padx=5, pady=5)

      self.clicked = StringVar()
      self.clicked.set(messageList[0])
      self.dropdown = tk.OptionMenu(self, self.clicked, *messageList)
      self.dropdown.grid(padx=5, pady=5)

      self.deleteButton = tk.Button(self, text="Delete Message", command=self.delete_message)
      self.deleteButton.grid(padx=5, pady=5)
      self.backButton3 = tk.Button(self, text="Back", command=lambda: self.controller.show_frame("MessageFrame"))
      self.backButton3.grid(padx=5, pady=5)

  def delete_message(self):
    message = re.sub(r'"', '', self.clicked.get())
    message = re.sub(":", "", message)
    message = message.split(" ", 1)

    self.cursor.execute(f'DELETE FROM MESSAGES WHERE SENDER = "{message[0]}" AND MESSAGE = "{message[1]}"')
    self.conn.commit()

    messagebox.showinfo("Message Deleted.", "You have successfully deleted the message.")
    self.controller.show_frame("MessageFrame")

  def remove_widgets(self):
    try:
      self.selectOptionLabel.grid_remove()
      self.selectUserButton.grid_remove()
      self.inboxButton.grid_remove()
      self.backButton.grid_remove()
    except AttributeError:
      pass
      

  def remove_widgets2(self):
    try:
      self.noMessagesLabel.grid_remove()
      self.backButton2.grid_remove()
    except AttributeError:
      pass
    try:
      self.inboxLabel.grid_remove()
      self.dropdown.grid_remove()
      self.deleteButton.grid_remove()
      self.backButton3.grid_remove()
    except AttributeError:
      pass
    try:
      self.selectFriendLabel.grid_remove()
      self.dropdown.grid_remove()
      self.selectButton.grid_remove()
      self.backButton4.grid_remove()
    except AttributeError:
      pass
    try:
      self.noUsersLabel.grid_remove()
      self.backButton4.grid_remove()
    except AttributeError:
      pass
    try:
      self.typeMessageLabel.grid_remove()
      self.messageText.grid_remove()
      self.sendMessageButton.grid_remove()
      self.backButton5.grid_remove()
    except AttributeError:
      pass


     

class ProfileFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.conn = sqlite3.connect('database.db')  
        self.cursor = self.conn.cursor()

        # create label for title
        self.title_label = Label(self, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        # create entry for title
        self.title_entry = Entry(self)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)
        # create label for major
        self.major_label = Label(self, text="Major:")
        self.major_label.grid(row=1, column=0, padx=10, pady=10)
        # create entry for major
        self.major_entry = Entry(self)
        self.major_entry.grid(row=1, column=1, padx=10, pady=10)
        # create label for university
        self.university_label = Label(self, text="University:")
        self.university_label.grid(row=2, column=0, padx=10, pady=10)
        # create entry for university
        self.university_entry = Entry(self)
        self.university_entry.grid(row=2, column=1, padx=10, pady=10)
        # create label for about
        self.about_label = Label(self, text="About:")
        self.about_label.grid(row=3, column=0, padx=10, pady=10)
        # create text box for about
        self.about_text = Text(self, height=5, width=50)
        self.about_text.grid(row=3, column=1, padx=10, pady=10)
        # create label for experience
        self.experience_label = Label(self, text="Experience:")
        self.experience_label.grid(row=4, column=0, padx=10, pady=10)

        #create label for experience title
        self.experience_title_label = Label(self, text="Title:")
        self.experience_title_label.grid(row=5, column=0, padx=10, pady=10)

        #create entry for experience title
        self.experience_title_entry = Entry(self)
        self.experience_title_entry.grid(row=5, column=1, padx=10, pady=10)

        #create label for experience employer
        self.experience_employer_label = Label(self, text="Employer:")
        self.experience_employer_label.grid(row=6, column=0, padx=10, pady=10)

        #create entry for experience employer
        self.experience_employer_entry = Entry(self)
        self.experience_employer_entry.grid(row=6, column=1, padx=10, pady=10)

        #create label for experience start date
        self.experience_startdate_label = Label(self, text="Start Date:")
        self.experience_startdate_label.grid(row=7, column=0, padx=10, pady=10)

        #create entry for experience start date
        self.experience_startdate_entry = Entry(self)
        self.experience_startdate_entry.grid(row=7, column=1, padx=10, pady=10)

        #create label for experience end date
        self.experience_enddate_label = Label(self, text="End Date:")
        self.experience_enddate_label.grid(row=8, column=0, padx=10, pady=10)

        #create entry for experience end date
        self.experience_enddate_entry = Entry(self)
        self.experience_enddate_entry.grid(row=8, column=1, padx=10, pady=10)

        #create label for experience location
        self.experience_location_label = Label(self, text="Location:")
        self.experience_location_label.grid(row=9, column=0, padx=10, pady=10)

        #create entry for experience location
        self.experience_location_entry = Entry(self)
        self.experience_location_entry.grid(row=9, column=1, padx=10, pady=10)

        #create label for experience description
        self.experience_description_label = Label(self, text="Job Description:")
        self.experience_description_label.grid(row=10, column=0, padx=10, pady=10)

        # create text box entry for experience description
        self.experience_description_entry = Text(self, height=5, width=50)
        self.experience_description_entry.grid(row=10, column=1, padx=10, pady=10)
        # create label for education
        self.education_label = Label(self, text="Education:")
        self.education_label.grid(row=11, column=0, padx=10, pady=10)
        # create label for school name
        self.school_name_label = Label(self, text="School Name:")
        self.school_name_label.grid(row=12, column=0, padx=10, pady=10)
        # create entry for school name
        self.school_name_entry = Entry(self)
        self.school_name_entry.grid(row=12, column=1, padx=10, pady=10)
        # create label for degree
        self.degree_label = Label(self, text="Degree:")
        self.degree_label.grid(row=13, column=0, padx=10, pady=10)
        # create entry for degree
        self.degree_entry = Entry(self)
        self.degree_entry.grid(row=13, column=1, padx=10, pady=10)
        # create label for years attended
        self.years_attended_label = Label(self, text="Years Attended:")
        self.years_attended_label.grid(row=14, column=0, padx=10, pady=10)
        # create entry for years attended
        self.years_attended_entry = Entry(self)
        self.years_attended_entry.grid(row=14, column=1, padx=10, pady=10)
        self.saveButton = tk.Button(self, text="Save", command = self.submit_profile )
        self.saveButton.grid(row=15,column=1)
        self.backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("ApplicationWindow"))
        self.backButton.grid(row=16,column=1)
    # function to handle submit button click
    def submit_profile(self):
        # get values from input fields
        
        title = self.title_entry.get()
        major = self.major_entry.get().lower().title()  # convert to title case
        university = self.university_entry.get().lower().title()
        about = self.about_text.get("1.0", END)

        experience_title = self.experience_title_entry.get()
        experience_employer = self.experience_employer_entry.get()
        experience_startdate = self.experience_startdate_entry.get()
        experience_enddate = self.experience_enddate_entry.get()
        experience_location = self.experience_location_entry.get()

        experience = f"Title: {experience_title}\nEmployer: {experience_employer}\nStart Date: {experience_startdate}\nEnd Date {experience_enddate}\nLocation: {experience_location}"
                      
        school_name = self.school_name_entry.get()
        degree = self.degree_entry.get()
        years_attended = self.years_attended_entry.get()
        education = f"{degree} at {school_name}, {years_attended} years"
        #inserting into database
        #database = sqlite3.connect('database.db')
        data_insert_query = ('''INSERT INTO PROFILE_DATA (USERNAME, Title, Major, University, About, Experience, Education) VALUES (?,?,?,?,?,?,?) ON CONFLICT (USERNAME) DO UPDATE SET 
        Title = excluded.Title,
        Major = excluded.Major,
        University = excluded.University,
        About = excluded.About,
        Experience = excluded.Experience,
        Education = excluded.Education;''')
        global loginUsername
        data_insert_tuple = (loginUsername, title, major, university, about, experience, education)
        self.cursor.execute(data_insert_query, data_insert_tuple)
        self.conn.commit()
        self.controller.show_frame("ApplicationWindow")
        


class DisplayProfileFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # connect to the database
        database = sqlite3.connect('database.db')
        self.cursor = database.cursor()
        global loginUsername
        self.profUsername = loginUsername

        self.profile = {'title': '',
            'major': '',
            'university': '',
            'info': '',
            'about': '',
            'experience': '',
            'education': ''}

        self.bind("<<ShowFrame>>", self.on_show_frame)

        self.name_label = tk.Label(self, text=f""+self.profUsername)
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.title_label = tk.Label(self, text=f"Title: {self.profile['title']}")
        self.title_label.grid(row=1, column=0, padx=10, pady=10)

        self.major_label = tk.Label(self, text=f"Major: {self.profile['major']}")
        self.major_label.grid(row=2, column=0, padx=10, pady=10)

        self.university_label = tk.Label(self, text=f"University: {self.profile['university']}")
        self.university_label.grid(row=3, column=0, padx=10, pady=10)

        self.info_label = tk.Label(self, text=f"Info: {self.profile['info']}")
        self.info_label.grid(row=4, column=0, padx=10, pady=10)

        self.experience_label = tk.Label(self, text="Experience:")
        self.experience_label.grid(row=5, column=0, padx=10, pady=10)
        for experience in self.profile['experience']:
            experience_line_label = tk.Label(self, text=f"- {experience}")
            experience_line_label.grid(row=6, column=0, padx=10, pady=10)

        self.education_label = tk.Label(self, text="Education:")
        self.education_label.grid(row=7, column=0, padx=10, pady=10)
        for education in self.profile['education']:
            education_line_label = tk.Label(self, text=f"- {education}")
            education_line_label.grid(row=8, column=0, padx=10, pady=10)
        
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("ApplicationWindow"))
        backButton.grid(row=9,column=1)
    

    def on_show_frame(self, event):
        # retrieve the profile information from the database

        global loginUsername
        profile_data_query=("SELECT * FROM PROFILE_DATA WHERE USERNAME='"+ loginUsername +"'")

        self.cursor.execute(profile_data_query)
        profile_data = self.cursor.fetchone()
        #print(profile_data)
        #profile_data = array('i', profile_data_tup)
        # convert the retrieved data to a dictionary
        profUsername = profile_data[0]
        self.profile = {
            'title': profile_data[1],
            'major': profile_data[2],
            'university': profile_data[3],
            'about': profile_data[4],
            'experience': profile_data[5].split('\n') if profile_data[4] else [],
            'education': profile_data[6].split('\n') if profile_data[5] else []
        }
        # update label text
        self.profUsername = loginUsername
        self.name_label['text'] = self.profUsername
        self.title_label['text'] = f"Title: {self.profile['title']}"
        self.major_label['text'] = f"Major: {self.profile['major']}"
        self.university_label['text'] = f"University: {self.profile['university']}"
        self.info_label['text'] = f"About: {self.profile['about']}"
        self.experience_label['text'] = f"Experience: {self.profile['experience']}"
        self.education_label['text'] = f"Education: {self.profile['education']}"



class MainWindow(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    mainframe = tk.Frame()
    self.windowNum = 0
    mainframe.pack(padx = 5, pady = 5,)# fill = 'both', expand = 1)
    self.framelist = {}                 #dictionary for different pages

    for F in (MainMenu, LoginWindow, SignUpWindow,
              VideoWindow, ApplicationWindow, LearnSkillWindow,
              FindSomeoneFrame, JobSearchFrame, AddJobFrame, RemoveJobFrame,
              JobApplicationFrame, DisplayProfileFrame, ViewJobApplicationFrame, 
              ViewJobNotAppliedFrame, ViewSavedJobsFrame, ProfileFrame, IL.CopyrightNoticeFrame,
              IL.InCollegeAboutFrame, IL.AccessibilityNoticeFrame, IL.UserAgreementFrame,
              IL.PrivacyPolicyFrame, IL.CookiePolicyFrame, IL.CopyrightPolicyFrame,
              IL.BrandPolicyFrame, GuestControlsFrame, LanguageFrame,
              GeneralWindow, UL.HelpCenterFrame, UL.AboutFrame, 
              UL.PressFrame, UnderConstruction, FriendFrame, MessageFrame):

      frame_name = F.__name__
      frame = F(parent = mainframe, controller = self)
      frame.grid(row = 0, column = 0, sticky = 'nsew')
      self.framelist[frame_name] = frame

    self.show_frame("MainMenu")

    #creation of sqlite database
    database = sqlite3.connect('database.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS USER_DATA(
                    USER_ID INT,
                    USERNAME TEXT, 
                    PASSWORD TEXT, 
                    FIRSTNAME TEXT, 
                    LASTNAME TEXT,
                    EMAIL_PREF INT,
                    SMS_PREF INT, 
                    TA_PREF INT,
                    LANG_PREF TEXT,
                    TIER TEXT,
                    PRIMARY KEY (USER_ID)
                    
    )'''

    database.execute(table_create_query)
    
    job_table_query = '''CREATE TABLE IF NOT EXISTS JOB_DATA(	
                        JOB_ID INT,
                        TITLE TEXT,	
                        DESCRIPTION TEXT,	
                        EMPLOYER TEXT,	
                        LOCATION TEXT,	
                        SALARY TEXT,
                        APPLIED INT,
                        POSTED_BY INT,
                        PRIMARY KEY (JOB_ID),
                        FOREIGN KEY (POSTED_BY) REFERENCES USER_DATA(USER_ID)
    )'''	
    database.execute(job_table_query)
    
    profile_table_query = '''CREATE TABLE IF NOT EXISTS PROFILE_DATA(
                        USERNAME TEXT,
                        Title TEXT, 
                        Major TEXT, 
                        University TEXT, 
                        About TEXT,
                        Experience INT,
                        Education INT,
                        PRIMARY KEY (USERNAME),
                        FOREIGN KEY (USERNAME) REFERENCES USER_DATA(USERNAME)
    )'''
    
    database.execute(profile_table_query)



    friends_query = '''CREATE TABLE IF NOT EXISTS FRIENDS(
                    USER_ID INT,
                    FRIEND_FIRST TEXT,
                    FRIEND_LAST TEXT,
                    FRIEND_USER TEXT,
                    FOREIGN KEY (USER_ID) REFERENCES USER_DATA(USER_ID),
                    FOREIGN KEY (FRIEND_USER) REFERENCES PROFILE_DATA(USERNAME)
    )'''

    database.execute(friends_query)
    
    messaging_query = '''CREATE TABLE IF NOT EXISTS MESSAGES(
                      SENDER TEXT,
                      RECEIVER TEXT,
                      MESSAGE TEXT,
                      TIMESTAMP TEXT
    )'''

    database.execute(messaging_query)
    



    pending_query = '''CREATE TABLE IF NOT EXISTS PENDING(
                    USER_ID INT,
                    PENDING_FIRST TEXT,
                    PENDING_LAST TEXT,
                    PENDING_USER TEXT,
                    FOREIGN KEY(PENDING_USER) REFERENCES PROFILE_DATA(USERNAME),
                    FOREIGN KEY (USER_ID) REFERENCES USER_DATA(USER_ID)
    )'''

    database.execute(pending_query)

    job_applications = '''CREATE TABLE IF NOT EXISTS APPLICATIONS(
                      JOB_ID INT,
                      USER_ID INT,
                      TITLE TEXT, 
                      EMPLOYER TEXT, 
                      DESCRIPTION TEXT, 
                      GRADUATION_DATE DATE, 
                      START_DATE DATE,
                      WHY TEXT,
                      PRIMARY KEY (USER_ID, JOB_ID),
                      FOREIGN KEY (USER_ID) REFERENCES USER_DATA(USER_ID),
                      FOREIGN KEY (JOB_ID) REFERENCES JOB_DATA(JOB_ID),
                      FOREIGN KEY(TITLE) REFERENCES JOB_DATA (TITLE),
                      FOREIGN KEY(EMPLOYER) REFERENCES JOB_DATA (EMPLOYER),
                      FOREIGN KEY(DESCRIPTION) REFERENCES JOB_DATA (DESCRIPTION)
    )'''

    database.execute(job_applications)

    saved_jobs = '''CREATE TABLE IF NOT EXISTS SAVED_JOBS(
                      JOB_ID INT, 
                      USER_ID INT,
                      TITLE TEXT, 
                      EMPLOYER TEXT, 
                      DESCRIPTION TEXT, 
                      PRIMARY KEY (USER_ID, JOB_ID),
                      FOREIGN KEY (JOB_ID) REFERENCES JOB_DATA(JOB_ID),
                      FOREIGN KEY (USER_ID) REFERENCES USER_DATA(USER_ID),
                      FOREIGN KEY(TITLE) REFERENCES JOB_DATA (TITLE),
                      FOREIGN KEY(EMPLOYER) REFERENCES JOB_DATA (EMPLOYER),
                      FOREIGN KEY(DESCRIPTION) REFERENCES JOB_DATA (DESCRIPTION)
    )'''

    database.execute(saved_jobs)

  def show_frame(self, frame_name):
    frame = self.framelist[frame_name]
    frame.event_generate("<<ShowFrame>>")
    frame.tkraise()

  
if __name__ == '__main__':
  window = MainWindow()
  window.mainloop()

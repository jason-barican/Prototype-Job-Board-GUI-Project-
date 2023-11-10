#This module allows the user to create a profile and also allow users to view profiles

from tkinter import *
import sqlite3

class ProfileFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Create Profile")
        self.master = master
        master.title("Create Profile")

        # create label for title
        title_label = Label(master, text="Title:")
        title_label.grid(row=0, column=0, padx=10, pady=10)

        # create entry for title
        title_entry = Entry(master)
        title_entry.grid(row=0, column=1, padx=10, pady=10)

        # create label for major
        major_label = Label(master, text="Major:")
        major_label.grid(row=1, column=0, padx=10, pady=10)

        # create entry for major
        major_entry = Entry(master)
        major_entry.grid(row=1, column=1, padx=10, pady=10)

        # create label for university
        university_label = Label(master, text="University:")
        university_label.grid(row=2, column=0, padx=10, pady=10)

        # create entry for university
        university_entry = Entry(master)
        university_entry.grid(row=2, column=1, padx=10, pady=10)

        # create label for about
        about_label = Label(master, text="About:")
        about_label.grid(row=3, column=0, padx=10, pady=10)

        # create text box for about
        about_text = Text(master, height=5, width=50)
        about_text.grid(row=3, column=1, padx=10, pady=10)


        # create label for experience
        experience_label = Label(master, text="Experience:")
        experience_label.grid(row=4, column=0, padx=10, pady=10)

        # create text box for experience
        experience_text = Text(master, height=5, width=50)
        experience_text.grid(row=4, column=1, padx=10, pady=10)


        # create label for education
        education_label = Label(master, text="Education:")
        education_label.grid(row=5, column=0, padx=10, pady=10)

        # create label for school name
        school_name_label = Label(master, text="School Name:")
        school_name_label.grid(row=6, column=0, padx=10, pady=10)

        # create entry for school name
        school_name_entry = Entry(master)
        school_name_entry.grid(row=6, column=1, padx=10, pady=10)

        # create label for degree
        degree_label = Label(master, text="Degree:")
        degree_label.grid(row=7, column=0, padx=10, pady=10)

        # create entry for degree
        degree_entry = Entry(master)
        degree_entry.grid(row=7, column=1, padx=10, pady=10)

        # create label for years attended
        years_attended_label = Label(master, text="Years Attended:")
        years_attended_label.grid(row=8, column=0, padx=10, pady=10)

        # create entry for years attended
        years_attended_entry = Entry(master)
        years_attended_entry.grid(row=8, column=1, padx=10, pady=10)

    # function to handle submit button click
    def submit_profile(self):
        # get values from input fields
        title = self.title_entry.get()
        major = self.major_entry.get().lower().title()  # convert to title case
        university = self.university_entry.get().lower().title()
        about = self.about_text.get("1.0", END)
        experience = self.experience_text.get("1.0", END)
        school_name = self.school_name_entry.get()
        degree = self.degree_entry.get()
        years_attended = self.years_attended_entry.get()
        education = f"{degree} at {school_name}, {years_attended} years"

        #inserting into database
        database = sqlite3.connect('database.db')

        database.execute('''CREATE TABLE IF NOT EXISTS PROFILE_DATA(
                        USERNAME TEXT,
                        Title TEXT, 
                        Major TEXT, 
                        University TEXT, 
                        About TEXT,
                        Experience INT,
                        Education INT,
                        PRIMARY KEY (USERNAME),
                        FOREIGN KEY (USERNAME) REFERENCES USER_DATA(USERNAME)
        )''')

        data_insert_query = ("INSERT INTO PROFILE_DATA (Title, Major, University, About, Experience, Education) \
        VALUES (?,?,?,?,?,?)")

        data_insert_tuple = (title, major, university, about, experience, education)

        database.execute(data_insert_query, data_insert_tuple)
        database.commit()

        database.close()
        
        # create submit button
        submit_button = Button(self.root, text="Save", command=self.submit_profile)
        submit_button.grid(row=6, column=1, padx=10, pady=10)

        self.root.mainloop()

def retrieve_profile(username):
    # connect to the database
    database = sqlite3.connect('database.db')
    cursor = database.cursor()

    # retrieve the profile information from the database
    profile_data_query=("SELECT * FROM PROFILE_DATA WHERE USERNAME='?'")

    #cursor.execute(profile_data_query, username)
    profile_data = cursor.fetchone()

    # close the database connection
    database.close()

    # convert the retrieved data to a dictionary
    profile = {
        'title': profile_data[0],
        'major': profile_data[1],
        'university': profile_data[2],
        'about': profile_data[3],
        'experience': profile_data[4].split('\n') if profile_data[4] else [],
        'education': profile_data[5].split('\n') if profile_data[5] else []
    }

    return profile

import tkinter as tk

def display_profile():

    profile = retrieve_profile()

    window = tk.Tk()
    window.title("Profile")
    
    title_label = tk.Label(window, text=f"Title: {profile['title']}")
    title_label.pack()
    
    major_label = tk.Label(window, text=f"Major: {profile['major']}")
    major_label.pack()
    
    university_label = tk.Label(window, text=f"University: {profile['university']}")
    university_label.pack()
    
    info_label = tk.Label(window, text=f"Info: {profile['info']}")
    info_label.pack()
    
    experience_label = tk.Label(window, text="Experience:")
    experience_label.pack()
    for experience in profile['experience']:
        experience_line_label = tk.Label(window, text=f"- {experience}")
        experience_line_label.pack()
    
    education_label = tk.Label(window, text="Education:")
    education_label.pack()
    for education in profile['education']:
        education_line_label = tk.Label(window, text=f"- {education}")
        education_line_label.pack()
    
    window.mainloop()

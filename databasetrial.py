import sqlite3
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

class Student:
    def __init__(self, name, SID):
        self.name = name
        self.SID = SID

class CourseRegistrationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin can add/remove/update students and courses")
        self.master.geometry('900x600')
        self.master.configure(bg='#292929')

        # Initialize list to store student records
        self.students = []
        self.courses = []
        
       # Create frames
        self.frameM = ctk.CTkFrame(master, fg_color='#8dcbf2', corner_radius=12)
        self.frameL = ctk.CTkFrame(self.frameM, fg_color='white', corner_radius=12)
        self.frameR = ctk.CTkFrame(self.frameM, fg_color='white', corner_radius=12)

        self.frameM.pack(fill='both',expand=True, padx=20, pady=20)
        self.frameL.pack(side='left',fill='both',padx=20, pady=20, expand=True)
        self.frameR.pack(side='left',fill='y', padx=20, pady=20)

        # Create tabs (stu_tab and cou_tab is students' credentials and courses' credentials respectively)
        self.creds = ctk.CTkTabview(self.frameL)
        self.creds.pack(fill='both', expand=True, padx=10, pady=10)

        self.stu_tab = self.creds.add("Students")
        self.cou_tab = self.creds.add("Courses")


        # Create labels and entry widgets for student information
        self.label_name = ctk.CTkLabel(self.frameR, text="Name:",bg_color='transparent')
        self.entry_name = ctk.CTkEntry(self.frameR,bg_color='transparent')

        self.label_SID = ctk.CTkLabel(self.frameR, text="Student ID:",bg_color='transparent')
        self.entry_SID = ctk.CTkEntry(self.frameR,bg_color='transparent')

        # Create buttons for actions
        self.button_add = ctk.CTkButton(self.frameR, text="Add Student", command=self.add_student,bg_color='transparent')
        self.button_remove = ctk.CTkButton(self.frameR, text="Remove Student", command=self.remove_student,bg_color='transparent')
        self.button_update = ctk.CTkButton(self.frameR, text="Update Student", command=self.update_student,bg_color='transparent')

        # Place widgets in the grid
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_SID.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_SID.grid(row=1, column=1, padx=10, pady=10)

        self.button_add.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_remove.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_update.grid(row=4, column=0, columnspan=2, pady=10)

    def add_student(self):
        name = self.entry_name.get()
        namecaps = name.upper()
        SID = self.entry_SID.get()

        if namecaps and SID:
            student = Student(namecaps, SID)
            self.students.append(student)
            messagebox.showinfo("Success", f"Student {name} added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill everything in.")

    def remove_student(self):
        SID = self.entry_SID.get()

        for student in self.students:
            if student.SID == SID:
                self.students.remove(student)
                messagebox.showinfo("Success", f"Student with ID {SID} removed successfully!")
                self.clear_entries()
                return

        messagebox.showwarning("Warning", f"No student found with ID {SID}.")

    def update_student(self):
        SID = self.entry_SID.get()

        for student in self.students:
            if student.SID == SID:
                new_name = self.entry_name.get()
                student.name = new_name
                messagebox.showinfo("Success", f"Student information updated successfully!")
                self.clear_entries()
                return

        messagebox.showwarning("Warning", f"No student found with ID {SID}.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_SID.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseRegistrationApp(root)
    root.mainloop()

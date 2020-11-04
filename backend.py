from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import os, csv, sys
import pygal
import sqlite3

mydata = []

con = sqlite3.connect('questioner.db')
cur = con.cursor()


class Backend():
    def __init__(self):


        # Statistic 
        def exam_taken():
            num_students = cur.execute("SELECT count(student_id) FROM student_questioner").fetchone()[0]
            return num_students

        def max_score():
            max_sco = cur.execute("SELECT MAX(student_score) FROM student_questioner").fetchone()[0]
            return max_sco


        def low_score():
            low_sco = cur.execute("SELECT MIN(student_score) FROM student_questioner").fetchone()[0]
            return low_sco

        def avg_score():
            try:
                avg_sco = cur.execute("SELECT AVG(student_score) FROM student_questioner").fetchone()[0]
                return int(avg_sco)
            except:
                print('Some Error')

        
        def clear():
            query = "SELECT student_id, student_name, student_surname, student_card, student_score FROM student_questioner"
            cur.execute(query)
            rows = cur.fetchall()
            update(rows)

        def update(rows):
            global mydata
            mydata = rows
            self.treeview.delete(*self.treeview.get_children())
            for i in rows:
                self.treeview.insert('', 'end', values = i, tags = 'unchecked')

        def search():
            q2 = qsearch.get()
            query = "SELECT student_id, student_name, student_surname, student_card FROM student_questioner WHERE student_name LIKE '%"+q2+"%' OR student_surname LIKE '%"+q2+"%'"
            cur.execute(query)
            rows = cur.fetchall()
            update(rows)

        def update_student():
            studid = t1.get()
            fname = t2.get()
            surname = t3.get()
            idc = t4.get()
            if messagebox.askyesno('Please Confirm', 'Are you sure you want to update student data?'):
                query = "UPDATE student_questioner SET student_name = ?, student_surname = ?, student_card = ? WHERE student_id = ?"
                cur.execute(query,(fname, surname, idc, studid))

                con.commit()
                clear()
            else:
                return True

        def delete_student():
            student_id = t1.get()
            if messagebox.askyesno('Please Confirm', 'Are you sure you want to delete this student?'):
                try:
                    query = "DELETE FROM student_questioner WHERE student_id = ?"
                    cur.execute(query, (student_id,))
                    con.commit()
                    clear()
                except EOFError as e:
                    print(e)
            else:
                return True

        def add_new():
            studentid = t1.get()
            fname = t2.get()
            lname = t3.get()
            idc = t4.get()
            try:
                query = "INSERT INTO student_questioner( student_name, student_surname, student_card) VALUES (?, ?, ?)"
                cur.execute(query, (fname, lname, idc))
                con.commit()
                clear()
                messagebox.showinfo('Success','New student has been added into the Database!')
            except EOFError as e:
                print(e)


        def export():
            if len(mydata) < 1:
                messagebox.showerror('No Data', 'No Data available to export')
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = 'Save CSV', filetypes = (("CSV File", "*.csv"), ("All Files", "*.*")), defaultextension=True)
            with open(fln, mode = 'w') as myfile:
                exp_writer = csv.writer(myfile, delimiter = ',', lineterminator='\n')
                for i in mydata:
                    exp_writer.writerow(i)
            messagebox.showinfo('Data Exported', 'Your data has been exported to ' + os.path.basename(fln)+' Successfully')

        def importcsv():
            mydata.clear()
            fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Open CSV', filetypes = (("CSV File", "*.csv"), ("All Files", "*.*")))
            with open(fln, mode = 'r') as myfile:
                csvread = csv.reader(myfile, delimiter = ',')
                for i in csvread:
                    mydata.append(i)
            update(mydata)


        def savedb():
            if messagebox.askyesno('Confirm', 'Are you sure you want to save the data into the Database?'):
                try:
                    
                    for i in mydata:
                        zid = i[0]
                        fname = i[1]
                        surname = i[2]
                        idc = i[3]
                        score = i[4]
                        query = "INSERT INTO student_questioner(student_id, student_name, student_surname, student_card, student_score) VALUES (NULL, ?, ?, ?, ?) "
                        cur.execute(query, ( fname, surname, idc, score))
                    con.commit()
                    clear()
                    messagebox.showinfo('Data Saved', 'Data has been saved to the database!')
                except EOFError as a:
                    messagebox.showerror(a)
            else:
                return False



        def getrow(event):
            try:
                rowid = self.treeview.identify_row(event.y)
                item = self.treeview.item(self.treeview.focus())
                t1.set(item['values'][0])
                t2.set(item['values'][1])
                t3.set(item['values'][2])
                t4.set(item['values'][3])
            except EOFError as e:
                print(e)
                
        # Main Frame
        statistic = Frame(root)
        statistic.grid(row = 0, column = 1, sticky = 'W')

        header = Frame(root)
        header.grid(row=1, column = 1, sticky='W', pady = 10, padx = 10)

        content = Label(root)
        content.grid(row=2,column = 1, sticky='N', padx = 420)

        footer = LabelFrame(root, text = '     Student Info', pady = 20, padx = 40, bd = 0)
        footer.grid(row=2, column = 1, sticky='W')

        root.columnconfigure(0, weight=1) # 100% 

        root.rowconfigure(0, weight=7) # 10%
        root.rowconfigure(1, weight=2) # 80%
        root.rowconfigure(2, weight=1) # 10%


        # TREE VIEW 
        self.treeview = ttk.Treeview(header, columns = (1, 2, 3, 4, 5))
        self.treeview = ttk.Treeview(header, columns = (1, 2, 3, 4, 5), show = 'headings', height = 10)
        style = ttk.Style(self.treeview)

        self.vsb = ttk.Scrollbar(header, orient = 'vertical', command = self.treeview)
        self.vsb.configure(command = self.treeview.yview)
        self.vsb.grid(row = 0, rowspan = 5, column = 1, sticky = 'NS')

        style.configure('Treeview', rowheight = 30, yscrollcommand = self.vsb.set)
        self.treeview.grid(row = 0, column = 0)




        self.treeview.heading('#0', text = '')
        self.treeview.heading('#1', text = 'Database ID')
        self.treeview.column('#1', width = 100, stretch = NO)
        self.treeview.heading('#2', text = 'Student Name')
        self.treeview.column('#2', width = 200, stretch = NO)
        self.treeview.heading('#3', text = 'Student Surname')
        self.treeview.heading('#4', text = 'Student ID Card')
        self.treeview.heading('#5', text = 'Student Score')
        self.treeview.column('#5', width = 100, stretch = NO)

        self.treeview.bind('<Double 1>', getrow)
        #self.treeview.bind('<Button-1>', getrow) -> for 1 click

        # Export CSV, Import CSV, Save Data, Exit  | SEARCH
        expbtn = Button(content, text = 'Export CSV', command = export, padx = 10, pady = 4)
        expbtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)

        impbtn = Button(content, text = 'Import CSV', command = importcsv, padx = 10, pady = 4)
        impbtn.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)

        savebtn = Button(content, text = 'Save Data', command = savedb, padx = 10, pady = 4)
        savebtn.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = W)


        query = "SELECT student_id, student_name, student_surname, student_card, student_score FROM student_questioner"
        cur.execute(query)
        rows = cur.fetchall()
        update(rows)        


        # Search BOX
        self.lbl_search = Label(content, text = 'Search')
        self.lbl_search.grid(row = 2, column = 0, padx = 5, pady = 30)

        qsearch = StringVar()
        self.entSearch = Entry(content, textvariable = qsearch)
        self.entSearch.grid(row = 2, column = 1, padx = 5, pady = 30)


        self.btnSearch = Button(content, text = 'Search', command = search, padx = 10, pady = 4)
        self.btnSearch.grid(row = 3, column = 0)

        self.btnClear = Button(content, text = 'Clear', command = clear, padx = 10, pady = 4)
        self.btnClear.grid(row = 3, column = 1)



        # STUDENT DATA SECTION

        # Student DB ID
        self.lbl_studID = Label(footer, text = 'Student DB ID')
        self.lbl_studID.grid(row = 0, column = 0, padx = 5, pady = 3, sticky = W)
        
        t1 = StringVar()
        self.ent_studID = Entry(footer, textvariable = t1)
        self.ent_studID.grid(row = 0, column = 1, padx = 5, pady = 3)

        # Student Name
        self.lbl_studName = Label(footer, text = 'Student Name')
        self.lbl_studName.grid(row = 1, column = 0, padx = 5, pady = 3, sticky = W)

        t2 = StringVar()
        self.ent_studName = Entry(footer, textvariable = t2)
        self.ent_studName.grid(row = 1, column = 1, padx = 5, pady = 3)

        # StudentSurname
        self.lbl_studSurname = Label(footer, text = 'Student Surname')
        self.lbl_studSurname.grid(row = 2, column = 0, padx = 5, pady = 3, sticky = W)

        t3 = StringVar()
        self.ent_studSurname = Entry(footer, textvariable = t3)
        self.ent_studSurname.grid(row = 2, column = 1, padx = 5, pady = 3)

        # Student ID Card
        self.lbl_studIdCard = Label(footer, text = 'Student idCard')
        self.lbl_studIdCard.grid(row = 3, column = 0, padx = 5, pady = 3, sticky = W)

        t4 = StringVar()
        self.ent_studIdCard = Entry(footer, textvariable = t4)
        self.ent_studIdCard.grid(row = 3, column = 1, padx = 5, pady = 3)


        # Buttons
        update_btn = Button(footer, text = 'Update', command = update_student, padx = 10, pady = 4)
        update_btn.grid(row = 4, column = 0, padx = 5, pady = 3)

        add_btn = Button(footer, text = 'Add New', command = add_new, padx = 10, pady = 4)
        add_btn.grid(row = 4, column = 1, padx = 5, pady = 3)

        delete_btn = Button(footer, text = 'Delete', command = delete_student, padx = 10, pady = 4)
        delete_btn.grid(row = 4, column = 2, padx = 5, pady = 3)

        #### STATISTIC ####
        self.lbl_studentCounter = Label(statistic, text = 'Taken by ' + str (exam_taken()) + ' students,')
        self.lbl_studentCounter.grid(row = 1, column = 0, padx = 5)

        self.lbl_avgscore = Label(statistic, text = 'Average Score is '+ str(avg_score())+ (', '))
        self.lbl_avgscore.grid(row = 1, column = 1)

        self.lbl_lowestScore = Label(statistic, text = 'Lowest Score is '+ str(low_score())+ (' and the'))
        self.lbl_lowestScore.grid(row = 1, column = 2)

        self.lbl_highestScore = Label(statistic, text = 'Highest Score '+ str(max_score()))
        self.lbl_highestScore.grid(row = 1, column = 3, pady = 5)


root = Tk()
app = Backend()
root.geometry('830x600+500+200')
root.resizable(False, False)
root.title('Admin Panel')
root.iconbitmap('icon.ico')


root.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import sqlite3
from typing import Counter
from time import perf_counter
import time
import pygal



# Creating DB - (questioner.db)
con = sqlite3.connect('questioner.db')
cur = con.cursor()

# Global Variables

counter = 0
mistake = 0
num_questions = 16

# Statistic Counter

def start_counter():
   tic = time.perf_counter()
   return tic

def end_counter():
    toc = time.perf_counter()
    return toc


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



class Questionnaire:

    def __init__(self, root):

        def answers():

            global counter
            global mistake
            # Q1
            if self.Radio_Value1.get() == 'Archie':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q2
            if self.Radio_Value2.get() == '32 bit':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q3
            if self.Radio_Value3.get() == 'Nexus':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q4
            if self.Radio_Value4.get() == 'Creeper Virus':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q5
            if self.Radio_Value5.get() == '128 Byte':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q6
            if self.Radio_Value6.get() == 'COBOL':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q7
            if self.Radio_Value7.get() == 'C':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q8
            if self.Radio_Value8.get() == 'Security':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q9
            if self.Radio_Value9.get() == 'Apple':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q10
            if self.Radio_Value10.get() == 'Image File':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q11
            if self.Radio_Value11.get() == 'Linux':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q12
            if self.Radio_Value12.get() == 'IBM':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q13
            if self.Radio_Value13.get() == 'Malware':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q14
            if self.Radio_Value14.get() == 'NodeJS':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q15
            if self.Radio_Value15.get() == 'SMTP':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')
            # Q16
            if self.Radio_Value16.get() == 'Security':
                counter += 1
                print('Correct Answer')
            else:
                mistake += 1
                print('Incorrect Answer')

            p = counter
            print(p)
            m = mistake
            print(m)
  

            mistakes = mistake
            score = counter
            name =  self.entStudentname.get()
            surname = self.entStudentsurname.get()
            card = self.entStudentId.get()
            if (name, surname, card != ''):
                try:
                    query = "INSERT INTO 'student_questioner'(student_name, student_surname, student_card, student_score, student_mistakes) VALUES (?, ?, ?, ?, ?)"
                    cur.execute(query, (name, surname, card, score, mistakes))
                    con.commit()
                    messagebox.showinfo('Success','End of the quiz! The results are subbmited!')
                    results()
                    end_counter()
                    print(end_counter())
                except sqlite3.Error as e:
                    print(e)
                    messagebox.showerror('Error', 'Fatal Error')
            else:
                messagebox.showwarning('Warning', 'Fields can NOT be empty!')

            #### Score to Pie Chart ####
            def pie():
            
                data = [['Correct : ', counter],
                        ['Mistakes: ', mistakes],
                        ['Total questions: ', num_questions]]
                pie_chart = pygal.HorizontalBar()
                pie_chart.title = "Correct answers, Mistakes and Total Questions:"
                for label, data_points in data:
                    pie_chart.add(label, data_points)
                # Render the chart    
                pie_chart.render_to_png('ScoreChart')
            pie()
            # Convert SVG to PNG


            ########### END OF STATISTIC

        def results():
            frame3 = Frame(root, bg = '#f0f0f0')
            frame3.place(x = 0, y = 0, height = 640, width = 800)

            self.lbl_section = Label(frame3, text = 'Results')
            self.lbl_section.place(x = 370, y = 10)

            self.CheckScore = StringVar()
            self.CheckScore.set(counter)
            self.lbl_score = Label(frame3, text = 'Score: ')
            self.lbl_score.place(x = 50, y = 50)
            self.score = Label(frame3, textvariable = self.CheckScore)
            self.score.place(x = 120, y = 50)

            

            self.CheckMistake = StringVar()
            self.CheckMistake.set(mistake)
            self.lbl_mistakes = Label(frame3, text = 'Mistakes: ')
            self.lbl_mistakes.place(x = 50, y = 100)
            self.mistakes = Label(frame3, textvariable = self.CheckMistake)
            self.mistakes.place(x = 120, y = 100)

            self.count = Label(frame3, text = 'Ended in: ' + (str(int(end_counter())/60)) + str(' minutes'))
            self.count.place(x = 50, y = 200)

            if mistake < 8 and mistake > 0:
                self.lbl_pass = Label(frame3, text = 'The student pass the exam!', fg = '#047817', padx = 10, pady = 10)
                self.lbl_pass.place(x = 50, y = 130)
            elif mistake > 8:
                self.lbl_pass = Label(frame3, text = 'The student did not pass the exam',  fg = '#f72525', padx = 10, pady = 10)
                self.lbl_pass.place(x = 50, y = 130)



        def check_start():
                thename = self.entStudentname.get()
                thesurname = self.entStudentsurname.get()
                theid = self.entStudentId.get()
                if (thename and thesurname != '') and (theid.isdigit() == True):
                    start_counter()
                    page1()
                else:
                    messagebox.showinfo('Warning','Name, Surname and ID card are required.\n    ID card must be Integer Value')


        def page1():
            frame1 = Frame(root, bg = '#f0f0f0')
            frame1.place(x = 0, y = 0, height = 640, width = 800)

            self.lbl_section = Label(frame1, text = 'Section 1')
            self.lbl_section.place(x = 370, y = 10)

            # First Question
            self.lbl_q1 = Label(frame1, text = '1. Which one is the first search engine in internet')
            self.lbl_q1.place(x = 20, y = 50)

            self.Radio_Value1 = StringVar()
            self.Radio_Value1.set('Google')
            self.radb = Radiobutton(frame1, value = 'Google', text = 'Google', padx = 9, pady = 3, variable = self.Radio_Value1)
            self.radb.place(x = 20, y = 80)
            self.radb2 = Radiobutton(frame1, value = 'Archie', text = 'Archie', padx = 9, pady = 3, variable = self.Radio_Value1)
            self.radb2.place(x = 20, y = 100)
            self.radb3 = Radiobutton(frame1, value = 'WAIS', text = 'WAIS', padx = 9, pady = 3, variable = self.Radio_Value1)
            self.radb3.place(x = 20, y = 120)
            self.radb4 = Radiobutton(frame1, value = 'Altvista', text = 'Altvista', padx = 9, pady = 3, variable = self.Radio_Value1)
            self.radb4.place(x = 20, y = 140)

            # Second Question
            self.lbl_q2 = Label(frame1, text = '2. Number of bit used by the IPv6 address')
            self.lbl_q2.place(x = 20, y = 180)

            self.Radio_Value2 = StringVar()
            self.Radio_Value2.set('32 bit')
            self.radbq2 = Radiobutton(frame1, value = '32 bit', text = '32 bit', padx = 9, pady = 3, variable = self.Radio_Value2)
            self.radbq2.place(x = 20, y = 200)
            self.radb2q2 = Radiobutton(frame1, value = '64 bit', text = '64 bit', padx = 9, pady = 3, variable = self.Radio_Value2)
            self.radb2q2.place(x = 20, y = 220)
            self.radb3q2 = Radiobutton(frame1, value = '128 bit', text = '128 bit', padx = 9, pady = 3, variable = self.Radio_Value2)
            self.radb3q2.place(x = 20, y = 240)
            self.radb4q2 = Radiobutton(frame1, value = '256 bit', text = '256 bit', padx = 9, pady = 3, variable = self.Radio_Value2)
            self.radb4q2.place(x = 20, y = 260)

            # Third Question
            self.lbl_q3 = Label(frame1, text = '3. Which one is the first web browser invented in 1990')
            self.lbl_q3.place(x = 20, y = 290)

            self.Radio_Value3 = StringVar()
            self.Radio_Value3.set('Internet Explorer')
            self.radbq3 = Radiobutton(frame1, value = 'Internet Explorer', text = 'Internet Explorer', padx = 9, pady = 3, variable = self.Radio_Value3)
            self.radbq3.place(x = 20, y = 310)
            self.radb2q3 = Radiobutton(frame1, value = 'Mosaic', text = 'Mosaic', padx = 9, pady = 3, variable = self.Radio_Value3)
            self.radb2q3.place(x = 20, y = 330)
            self.radb3q3 = Radiobutton(frame1, value = 'Mozilla', text = 'Mozilla', padx = 9, pady = 3, variable = self.Radio_Value3)
            self.radb3q3.place(x = 20, y = 350)
            self.radb4q3 = Radiobutton(frame1, value = 'Nexus', text = 'Nexus', padx = 9, pady = 3, variable = self.Radio_Value3)
            self.radb4q3.place(x = 20, y = 370)

            # Fourth Question
            self.lbl_q4 = Label(frame1, text = '4. First computer virus is known as?')
            self.lbl_q4.place(x = 20, y = 400)

            self.Radio_Value4 = StringVar()
            self.Radio_Value4.set('Rabbit')
            self.radbq4 = Radiobutton(frame1, value = 'Rabbit', text = 'Rabbit', padx = 9, pady = 3, variable = self.Radio_Value4)
            self.radbq4.place(x = 20, y = 420)
            self.radb2q4 = Radiobutton(frame1, value = 'Creeper Virus', text = 'Creeper Virus', padx = 9, pady = 3, variable = self.Radio_Value4)
            self.radb2q4.place(x = 20, y = 440)
            self.radb3q4 = Radiobutton(frame1, value = 'Elk Cloner', text = 'Elk Cloner', padx = 9, pady = 3, variable = self.Radio_Value4)
            self.radb3q4.place(x = 20, y = 460)
            self.radb4q4 = Radiobutton(frame1, value = 'SCA Virus', text = 'SCA Virus', padx = 9, pady = 3, variable = self.Radio_Value4)
            self.radb4q4.place(x = 20, y = 480)

            # Fifth Question
            self.lbl_q5 = Label(frame1, text = '5. 1024 bit is equal to how many byte')
            self.lbl_q5.place(x = 420, y = 50)

            self.Radio_Value5 = StringVar()
            self.Radio_Value5.set('1 Byte')
            self.radbq4 = Radiobutton(frame1, value = '1 Byte', text = '1 Byte', padx = 9, pady = 3, variable = self.Radio_Value5)
            self.radbq4.place(x = 420, y = 80)
            self.radb2q4 = Radiobutton(frame1, value = '128 Byte', text = '128 Byte', padx = 9, pady = 3, variable = self.Radio_Value5)
            self.radb2q4.place(x = 420, y = 100)
            self.radb3q4 = Radiobutton(frame1, value = '32 Byte', text = '32 Byte', padx = 9, pady = 3, variable = self.Radio_Value5)
            self.radb3q4.place(x = 420, y = 120)
            self.radb4q4 = Radiobutton(frame1, value = '64 Byte', text = '64 Byte', padx = 9, pady = 3, variable = self.Radio_Value5)
            self.radb4q4.place(x = 420, y = 140)

            # Sixth Question
            self.lbl_q6 = Label(frame1, text = '6. Which of the following is not database management software')
            self.lbl_q6.place(x = 420, y = 180)

            self.Radio_Value6 = StringVar()
            self.Radio_Value6.set('MySQL')
            self.radbq6 = Radiobutton(frame1, value = 'MySQL', text = 'MySQL', padx = 9, pady = 3, variable = self.Radio_Value6)
            self.radbq6.place(x = 420, y = 200)
            self.radb2q6 = Radiobutton(frame1, value = 'Oracle', text = 'Oracle', padx = 9, pady = 3, variable = self.Radio_Value6)
            self.radb2q6.place(x = 420, y = 220)
            self.radb3q6 = Radiobutton(frame1, value = 'Sybase', text = 'Sybase', padx = 9, pady = 3, variable = self.Radio_Value6)
            self.radb3q6.place(x = 420, y = 240)
            self.radb4q6 = Radiobutton(frame1, value = 'COBOL', text = 'COBOL', padx = 9, pady = 3, variable = self.Radio_Value6)
            self.radb4q6.place(x = 420, y = 260)

            # Seventh Question
            self.lbl_q7 = Label(frame1, text = '7. Which of the following is not an operating system')
            self.lbl_q7.place(x = 420, y = 290)

            self.Radio_Value7 = StringVar()
            self.Radio_Value7.set('DOS')
            self.radbq7 = Radiobutton(frame1, value = 'DOS', text = 'DOS', padx = 9, pady = 3, variable = self.Radio_Value7)
            self.radbq7.place(x = 420, y = 310)
            self.radb2q7 = Radiobutton(frame1, value = 'MAC', text = 'MAC', padx = 9, pady = 3, variable = self.Radio_Value7)
            self.radb2q7.place(x = 420, y = 330)
            self.radb3q7 = Radiobutton(frame1, value = 'C', text = 'C', padx = 9, pady = 3, variable = self.Radio_Value7)
            self.radb3q7.place(x = 420, y = 350)
            self.radb4q7 = Radiobutton(frame1, value = 'Linux', text = 'Linux', padx = 9, pady = 3, variable = self.Radio_Value7)
            self.radb4q7.place(x = 420, y = 370)

            # Eighth Question
            self.lbl_q8 = Label(frame1, text = '8. Firewall in computer is used for')
            self.lbl_q8.place(x = 420, y = 400)

            self.Radio_Value8 = StringVar()
            self.Radio_Value8.set('Security')
            self.radbq8 = Radiobutton(frame1, value = 'Security', text = 'Security', padx = 9, pady = 3, variable = self.Radio_Value8)
            self.radbq8.place(x = 420, y = 420)
            self.radb2q8 = Radiobutton(frame1, value = 'Data Transmission', text = 'Data Transmission', padx = 9, pady = 3, variable = self.Radio_Value8)
            self.radb2q8.place(x = 420, y = 440)
            self.radb3q8 = Radiobutton(frame1, value = 'Authentication', text = 'Authentication', padx = 9, pady = 3, variable = self.Radio_Value8)
            self.radb3q8.place(x = 420, y = 460)
            self.radb4q8 = Radiobutton(frame1, value = 'Monitoring', text = 'Monitoring', padx = 9, pady = 3, variable = self.Radio_Value8)
            self.radb4q8.place(x = 420, y = 480)

            self.btnSectionTwo = Button(frame1, text = 'Section 2', command = lambda : page2())
            self.btnSectionTwo.place(x = 700, y = 550)

        def page2():
            frame2 = Frame(root, bg = '#f0f0f0')
            frame2.place(x = 0, y = 0, height = 640, width = 800)

            self.lbl_section = Label(frame2, text = 'Section 2')
            self.lbl_section.place(x = 370, y = 10)

            # 9 Question
            self.lbl_q9 = Label(frame2, text = '9. Mac Operating System is developed by which company')
            self.lbl_q9.place(x = 20, y = 50)

            self.Radio_Value9 = StringVar()
            self.Radio_Value9.set('IBM')
            self.radb9 = Radiobutton(frame2, value = 'IBM', text = 'IBM', padx = 9, pady = 3, variable = self.Radio_Value9)
            self.radb9.place(x = 20, y = 80)
            self.radb9 = Radiobutton(frame2, value = 'Apple', text = 'Apple', padx = 9, pady = 3, variable = self.Radio_Value9)
            self.radb9.place(x = 20, y = 100)
            self.radb9 = Radiobutton(frame2, value = 'Microsoft', text = 'Microsoft', padx = 9, pady = 3, variable = self.Radio_Value9)
            self.radb9.place(x = 20, y = 120)
            self.radb9 = Radiobutton(frame2, value = 'Altvista', text = 'Altvista', padx = 9, pady = 3, variable = self.Radio_Value9)
            self.radb9.place(x = 20, y = 140)

            # 10 Question
            self.lbl_q10 = Label(frame2, text = '10. .gif is an extension of')
            self.lbl_q10.place(x = 20, y = 180)

            self.Radio_Value10 = StringVar()
            self.Radio_Value10.set('Image File')
            self.radbq10 = Radiobutton(frame2, value = 'Image File', text = 'Image File', padx = 9, pady = 3, variable = self.Radio_Value10)
            self.radbq10.place(x = 20, y = 200)
            self.radb2q10 = Radiobutton(frame2, value = 'Video File', text = 'Video File', padx = 9, pady = 3, variable = self.Radio_Value10)
            self.radb2q10.place(x = 20, y = 220)
            self.radb3q10 = Radiobutton(frame2, value = 'Audio File', text = 'Audio File', padx = 9, pady = 3, variable = self.Radio_Value10)
            self.radb3q10.place(x = 20, y = 240)
            self.radb4q10 = Radiobutton(frame2, value = 'Word File', text = 'Word File', padx = 9, pady = 3, variable = self.Radio_Value10)
            self.radb4q10.place(x = 20, y = 260)

            # 11 Question
            self.lbl_q11 = Label(frame2, text = '11. Which one is the first fully supported 64-bit system')
            self.lbl_q11.place(x = 20, y = 290)

            self.Radio_Value11 = StringVar()
            self.Radio_Value11.set('Windows Vista')
            self.radbq11 = Radiobutton(frame2, value = 'Windows Vista', text = 'Windows Vista', padx = 9, pady = 3, variable = self.Radio_Value11)
            self.radbq11.place(x = 20, y = 310)
            self.radb2q11 = Radiobutton(frame2, value = 'Mac', text = 'Mac', padx = 9, pady = 3, variable = self.Radio_Value11)
            self.radb2q11.place(x = 20, y = 330)
            self.radb3q11 = Radiobutton(frame2, value = 'Linux', text = 'Linux', padx = 9, pady = 3, variable = self.Radio_Value11)
            self.radb3q11.place(x = 20, y = 350)
            self.radb4q11 = Radiobutton(frame2, value = 'Windows XP', text = 'Windows XP', padx = 9, pady = 3, variable = self.Radio_Value11)
            self.radb4q11.place(x = 20, y = 370)

            # 12 Question
            self.lbl_q12 = Label(frame2, text = '12. Computer Hard Disk was first introduced in 1956 by')
            self.lbl_q12.place(x = 20, y = 400)

            self.Radio_Value12 = StringVar()
            self.Radio_Value12.set('Dell')
            self.radbq12 = Radiobutton(frame2, value = 'Dell', text = 'Dell', padx = 9, pady = 3, variable = self.Radio_Value12)
            self.radbq12.place(x = 20, y = 420)
            self.radb2q12 = Radiobutton(frame2, value = 'Apple', text = 'Apple', padx = 9, pady = 3, variable = self.Radio_Value12)
            self.radb2q12.place(x = 20, y = 440)
            self.radb3q12 = Radiobutton(frame2, value = 'Microsoft', text = 'Microsoft', padx = 9, pady = 3, variable = self.Radio_Value12)
            self.radb3q12.place(x = 20, y = 460)
            self.radb4q12 = Radiobutton(frame2, value = 'IBM', text = 'IBM', padx = 9, pady = 3, variable = self.Radio_Value12)
            self.radb4q12.place(x = 20, y = 480)
            #IBM

            # 13 Question
            self.lbl_q13 = Label(frame2, text = '13. In computer world, Trojan refer to')
            self.lbl_q13.place(x = 420, y = 50)

            self.Radio_Value13 = StringVar()
            self.Radio_Value13.set('Virus')
            self.radbq13 = Radiobutton(frame2, value = 'Virus', text = 'Virus', padx = 9, pady = 3, variable = self.Radio_Value13)
            self.radbq13.place(x = 420, y = 80)
            self.radb2q13 = Radiobutton(frame2, value = 'Malware', text = 'Malware', padx = 9, pady = 3, variable = self.Radio_Value13)
            self.radb2q13.place(x = 420, y = 100)
            self.radb3q13 = Radiobutton(frame2, value = 'Worm', text = 'Worm', padx = 9, pady = 3, variable = self.Radio_Value13)
            self.radb3q13.place(x = 420, y = 120)
            self.radb4q13 = Radiobutton(frame2, value = 'Spyware', text = 'Spyware', padx = 9, pady = 3, variable = self.Radio_Value13)
            self.radb4q13.place(x = 420, y = 140)
            #Malware

            # 14 Question
            self.lbl_q14 = Label(frame2, text = '14. Which on of the followings is a programming language')
            self.lbl_q14.place(x = 420, y = 180)

            self.Radio_Value14 = StringVar()
            self.Radio_Value14.set('HTTP')
            self.radbq14 = Radiobutton(frame2, value = 'HTTP', text = 'HTTP', padx = 9, pady = 3, variable = self.Radio_Value14)
            self.radbq14.place(x = 420, y = 200)
            self.radb2q14 = Radiobutton(frame2, value = 'HTML', text = 'HTML', padx = 9, pady = 3, variable = self.Radio_Value14)
            self.radb2q14.place(x = 420, y = 220)
            self.radb3q14 = Radiobutton(frame2, value = 'NodeJS', text = 'NodeJS', padx = 9, pady = 3, variable = self.Radio_Value14)
            self.radb3q14.place(x = 420, y = 240)
            self.radb4q14 = Radiobutton(frame2, value = 'FTP', text = 'FTP', padx = 9, pady = 3, variable = self.Radio_Value14)
            self.radb4q14.place(x = 420, y = 260)

            # 15 Question
            self.lbl_q15 = Label(frame2, text = '15. Which protocol is used to send e-mail')
            self.lbl_q15.place(x = 420, y = 290)

            self.Radio_Value15 = StringVar()
            self.Radio_Value15.set('HTTP')
            self.radbq15 = Radiobutton(frame2, value = 'HTTP', text = 'HTTP', padx = 9, pady = 3, variable = self.Radio_Value15)
            self.radbq15.place(x = 420, y = 310)
            self.radb2q15 = Radiobutton(frame2, value = 'POP3', text = 'POP3', padx = 9, pady = 3, variable = self.Radio_Value15)
            self.radb2q15.place(x = 420, y = 330)
            self.radb3q15 = Radiobutton(frame2, value = 'SMTP', text = 'SMTP', padx = 9, pady = 3, variable = self.Radio_Value15)
            self.radb3q15.place(x = 420, y = 350)
            self.radb4q15 = Radiobutton(frame2, value = 'SSH', text = 'SSH', padx = 9, pady = 3, variable = self.Radio_Value15)
            self.radb4q15.place(x = 420, y = 370)

            # 16 Question
            self.lbl_q16 = Label(frame2, text = '16. Firewall in computer is used for')
            self.lbl_q16.place(x = 420, y = 400)

            self.Radio_Value16 = StringVar()
            self.Radio_Value16.set('Security')
            self.radbq16 = Radiobutton(frame2, value = 'Security', text = 'Security', padx = 9, pady = 3, variable = self.Radio_Value16)
            self.radbq16.place(x = 420, y = 420)
            self.radb2q16 = Radiobutton(frame2, value = 'Data Transmission', text = 'Data Transmission', padx = 9, pady = 3, variable = self.Radio_Value16)
            self.radb2q16.place(x = 420, y = 440)
            self.radb3q16 = Radiobutton(frame2, value = 'Authentication', text = 'Authentication', padx = 9, pady = 3, variable = self.Radio_Value16)
            self.radb3q16.place(x = 420, y = 460)
            self.radb4q16 = Radiobutton(frame2, value = 'Monitoring', text = 'Monitoring', padx = 9, pady = 3, variable = self.Radio_Value16)
            self.radb4q16.place(x = 420, y = 480)

            self.btnSectionOne = Button(frame2, text = 'Section 1', command = lambda : page1())
            self.btnSectionOne.place(x = 700, y = 550)


            self.btnFinish = Button(frame2, text = 'Finish', command = lambda : answers(), padx = 50)
            self.btnFinish.place(x = 530, y = 550)

########################################################################################################

        # Main Frame
        header = Frame(root)
        header.grid(row=0, sticky='news',pady = 50, padx = 25)

        content = Frame(root)
        content.grid(row=1, sticky='N', pady = 50, padx = 25)

        footer = Frame(root)
        footer.grid(row=2, sticky='news', pady = 50, padx = 25)

        root.columnconfigure(0, weight=1) # 100% 

        root.rowconfigure(0, weight=2) # 10%
        root.rowconfigure(1, weight=7) # 80%
        root.rowconfigure(2, weight=1) # 10%


        # Student Name
        self.lbl_studetname = Label(header, text = 'Student Name: ')
        self.lbl_studetname.grid(row = 0, column = 1, sticky = W)

        self.entStudentname = Entry(header, width = 20)
        self.entStudentname.grid(row = 0, column = 2, sticky = W)

        # Student Surname
        self.lbl_studetsurname = Label(header, text = 'Student Surname: ')
        self.lbl_studetsurname.grid(row = 0, column = 3, padx = (20,0), sticky = W)

        self.entStudentsurname = Entry(header, width = 20)
        self.entStudentsurname.grid(row = 0, column = 4, sticky = W)

        # Student ID Card
        self.lbl_studetId = Label(header, text = 'Student ID card: ')
        self.lbl_studetId.grid(row = 0, column = 5, padx = (20,0), sticky = W)

        self.entStudentId = Entry(header, width = 20)
        self.entStudentId.grid(row = 0, column = 6, sticky = W)

        # Quistioner Guide
        self.lbl_guide = Label(content, text = 'Please read the questions carefully, you have 45 minutes to finish the quiz. \n Any questions regarding the quiz please raise your hand and do not disturb your colleagues!')
        self.lbl_guide.grid(row = 1, column = 2, columnspan = 4)

        # Start Button
        self.startButton = Button(content, text = 'START', padx = 20, command = lambda : check_start())
        self.startButton.grid(row = 3, column = 4, pady = 50, sticky = W)

        # Statistic
        self.lbl_studentCounter = Label(footer, text = 'Taken by ' + str (exam_taken()) + (' students'))
        self.lbl_studentCounter.grid(row = 0, column = 0, padx = 5)


        #self.lbl_avgscore = Label(footer, text = 'Average Score: '+ str(avg_score()))
        #self.lbl_avgscore.grid(row = 0, column = 1, padx = 5)

        #self.lbl_lowestScore = Label(footer, text = 'Lowest Score: '+ str(low_score()))
        #self.lbl_lowestScore.grid(row = 0, column = 2, padx = 5)

        #self.lbl_highestScore = Label(footer, text = 'Highest Score: '+ str(max_score()))
        #self.lbl_highestScore.grid(row = 0, column = 3, padx = 5)




root = Tk()
app = Questionnaire(root)
root.title('Student Qustioner Quiz')
root.geometry("800x600+600+200")
root.iconbitmap('icon.ico')
root.resizable(False, False)
root.mainloop()


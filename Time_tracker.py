from tkinter import *
from datetime import *
import time
import json



root = Tk()
root.title("This is an app")
root.geometry("400x300")
t_frame = Frame(root,bd=10,bg="purple")
t_frame.place(x=100,y=70)
btn_frame = Frame(root)
btn_frame.grid(row=1,column=1)

#-------------------------------------------------------------------------------
# Creates the table, use only once!!!!


'''
employee_name text,
employee_title,
employee_number integer,
date text,
clocked_in text,
clocked_out text,
total_days_hours integer,
total_week_hours integer
'''
#-------------------------------------------------------------------------------
def clocked_in():
    global current_in_time

    btn_start["state"] = DISABLED
    btn_stop["state"] = NORMAL


    current_in_time = datetime.now()

    with open("test.json" , "a") as cl_in:
        cl_in.write("\n" + "Clocked in at : " + str(current_in_time))
        cl_in.close()

    print("Clocked in at: " + str(current_in_time))


#------------------------------------------------------------------------------
def clock_out():
    global current_out_time
    btn_start["state"] = NORMAL
    btn_stop["state"] = DISABLED


    current_out_time = datetime.now()


    with open("test.json" , "a") as cl_ot:
        cl_ot.write("\n" + "Clocked out at : " + str(current_out_time) + "\n")
        cl_ot.close()

    print("Clocked out at : " + str(current_out_time))
    print(current_out_time - current_in_time)

#-------------------------------------------------------------------------------
def time_sheet():
    time_sheet = open("test.json" , "r",encoding="UTF8").read()
    time_label = Label(t_frame,text=time_sheet)
    time_label.grid(row=2,column=1)


#-------------------------------------------------------------------------------


timer_box = Label(root,text= "Timer goes here")
timer_box.grid(row=0,column=0)


btn_start= Button(root,text="Clock-in",command=clocked_in,bg="green")
btn_start.grid(row=1,column=1)

btn_stop= Button(root,text="Clock-out",command = clock_out,bg="red")
btn_stop.grid(row=1,column=2)

btn_timesheet= Button(root,text="Time Sheet",command = time_sheet,bg="blue")
btn_timesheet.grid(row=1,column=3)


btn_stop["state"] = DISABLED


root.mainloop()

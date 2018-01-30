from tkinter import *
import tkinter.scrolledtext
import tkinter.filedialog
import datetime
import tkinter.messagebox
import os



# global variable to prevent resaving of a saved file when save function is called multiple time or a file is opened through open command
count = 0
filename = "Untitled"

# root window
root = Tk()
root.title(filename + " - Easy Text")
root.iconphoto(root,PhotoImage(file ="tarwayimage.png"))
root.geometry('500x600+700+100')

#-----------------------------------------------creating About menu-------------------------------------------------------------------------------------------
def easy_text():
    temp_frame = Toplevel(root)
    temp_frame.title("Easy Text")
    temp_frame.geometry('350x200+800+150')
    label1 = Label(temp_frame,text = "Easy Text is an user friendly open-source\n text editor for writing code, markup and prose.\n You'll love the slick user interface,\n extraordinary features and amazing performance.",bg= "gold",fg= "Black",font =("Times New Roman","12",""))
    label1.pack(side=TOP,fill=BOTH,expand =1)

def developer_menu():
    temp_frame = Toplevel(root)
    temp_frame.title("Easy Text")
    temp_frame.geometry('350x200+800+150')
    label1 = Label(temp_frame,
                   text="Ankit Tarway\n B.Tech Pre-final year(in year 2018)\n IIT(ISM),Dhanbad\n ankittarway.iitdhn@gmail.com\n\n\n Shobhit Mathur\n B.Tech Pre-final year(in year 2018)\n IIT(ISM),Dhanbad\n  beingmathur@gmail.com",
                   bg="gold", fg="black", font=("Times New Roman", "12", ""))
    label1.pack(side=TOP, fill=BOTH, expand=1)



#-----------------------------------------------creating format menu-------------------------------------------------------------------------------------------
def formate_menu():
    def save_font():
        temp_str =""
        try :
            if v2.get() != "Regular" :
                temp_str = v2.get()
            textPad.tag_add("bt", "sel.first", "sel.last")
            textPad.tag_config("bt", font=(v3.get(), v1.get(), temp_str))
            frame1.destroy()
        except :
            frame1.destroy()
            pass
    frame1 = Toplevel(root)
    frame1.geometry('370x200+800+150')
    frame1.title("Font")
    v3 = StringVar(frame1)
    v3.set("Arial")
    v2 = StringVar(frame1)
    v2.set("Regular")
    v1 = StringVar(frame1)
    v1.set("10")
    font = Label(frame1,text= "Font")
    font_style =Label(frame1,text = "Font Style")
    size = Label(frame1,text = "Size")
    font_drop = OptionMenu(frame1,v3,"Arial", "Courier", "Times New Roman", "Georgia","Edwardian Script ITC")
    font_drop.config(bg = "white")
    font_style_drop = OptionMenu(frame1,v2,"Regular","bold", "italic", "underline", "bold italic","bold underline")
    font_style_drop.config(bg="white")
    size_drop  = OptionMenu(frame1,v1,"10", "11", "12", "14","16","18","20","22","24")
    size_drop.config(bg="white")
    button1 = Button(frame1,text = "Save",command = save_font)
    font.grid(row =1 ,column= 1)
    font_style.grid(row = 1,column = 10)
    size.grid(row = 1,column =18)
    font_drop.grid(row = 2,column =1,columnspan =9)
    font_style_drop.grid(row = 2,column =10,columnspan =7)
    size_drop.grid(row= 2, column =18,columnspan =2)
    button1.grid(row =10 ,column = 7)



#------------------------------------creating file menu-----------------------------------------------------------------

# function to get name of file

def get_name(s):
    temp = ''
    for i in s:
        temp = i + temp
    fstring = ''
    for i in temp:
        if (i == '/'):
            break
        else:
            fstring = i + fstring
    return fstring


def exit_menu():
    response = tkinter.messagebox.askquestion("EXIT", "Do you want to save this file ?")
    if response == 'yes':
        save_menu()
    root.destroy()


# code to ask do you want to save file on click on "X" on top bar
root.protocol("WM_DELETE_WINDOW", exit_menu)




# creating command for new
def new_menu():
    response = tkinter.messagebox.askquestion("EXIT", "Do you want to save this file ?")
    if response == 'yes':
        save_menu()

    textPad.delete(1.0, END)










# creating command for  save
def save_as_menu():
    global filename
    filename = tkinter.filedialog.asksaveasfilename()
    if filename:
        alltext = textPad.get(1.0, END)
        open(filename, 'w').write(alltext)
        root.title(get_name(str(filename)) + " - Easy Text")


def save_menu():
    global count
    global filename
    if (count == 0):
        filename = tkinter.filedialog.asksaveasfilename()
        count += 1
    else:
        alltext = textPad.get(1.0, END)
        open(filename, 'w').write(alltext)

    if filename:
        alltext = textPad.get(1.0, END)
        open(filename, 'w').write(alltext)
    root.title(get_name(str(filename)) + " - Easy Text")

#rename command
def rename_menu():

    global filename
    if filename != "Untitled" :

        def do_rename():
            global filename
            str_temp = filename.replace(get_name(filename),str(entry1.get()))
            os.rename( str(filename) ,str(str_temp))
            filename= str_temp
            root.title(get_name(str(filename)) + " - Easy Text")
            temp_frame.destroy()

        temp_frame = Toplevel(root)
        temp_frame.title("Rename")
        temp_frame.geometry('250x100+800+150')
        label1 = Label(temp_frame, text ="New Name:")

        entry1 = Entry(temp_frame)

        label1.grid( row=0, column=0)

        entry1.grid(row=0, column=1,columnspan=5)

        Button(temp_frame, text ="Ok",command = do_rename).grid(row=4, column=3,padx =10,ipadx = 10 ,pady =10)
    else :
        return

# creating command for open
def open_menu():
    global count
    global filename
    count += 1
    textPad.delete(1.0, END)
    filename = tkinter.filedialog.askopenfilename()
    file = open(filename, 'r')

    if file != '':

        txt = file.read()

        textPad.insert(INSERT, txt)

    else:

        pass
    root.title(get_name(str(filename)) + " - Easy Text")


##-----------------------------------------------------------------------------------------------------------------------------------------
# replace command
def replace_menu():
    def do_replacement():
       try:
           str_temp = textPad.get(1.0, END)
           str_temp = str_temp.replace(str(entry1.get()), str(entry2.get()))
           textPad.delete(1.0, END)
           textPad.insert(INSERT, str_temp)
           temp_frame.destroy()
       except :
           temp_frame.destroy()
           pass

    temp_frame = Toplevel(root)
    temp_frame.title("Replace")
    temp_frame.geometry('250x300+800+150')
    label1 = Label(temp_frame, text ="Find What :")
    label2 = Label(temp_frame, text = "Replace With :")
    entry1 = Entry(temp_frame)
    entry2 = Entry(temp_frame)
    label1.grid( row=0, column=0)
    label2.grid(row=1, column=0 )
    entry1.grid(row=0, column=1,columnspan=4)
    entry2.grid(row=1, column=1,columnspan=4)
    Button(temp_frame, text ="Ok",command = do_replacement).grid(row=4, column=3,padx =10,ipadx = 10 ,pady =10)

# creating command for  copy and paste
def copy_menu():
    try:
        textPad.clipboard_clear()
        textPad.clipboard_append(textPad.selection_get())
    except:
        tkinter.messagebox.showerror("Error", "Nothing Selected to copy")


def paste_menu():
    try:
        mem = textPad.selection_get(selection='CLIPBOARD')
        textPad.insert(INSERT, mem)
    except:
        tkinter.messagebox.showerror("Error", "Nothing to paste")


def cut_menu():
    copy_menu()
    textPad.delete(SEL_FIRST, SEL_LAST)


def del_menu():
    try:
        textPad.delete(SEL_FIRST, SEL_LAST)
    except:
        pass


def undo_menu():
    textPad.event_generate("<<Undo>>")


def redo_menu():
    textPad.event_generate("<<Redo>>")
    return


def selectall_menu():
    textPad.tag_add("sel", '1.0', 'end')

# creating command for date/time
def date_menu():
    data = datetime.date.today()
    import time
    time_ = time.strftime('%H:%M:%S')
    textPad.insert(INSERT, data)
    textPad.insert(INSERT, " " + time_)



##--------------------------------------------------------------------------------------------------------------------------------------------


# creating menu of texteditior
mymenu = Menu(root)
root.config(menu=mymenu)
file_menu = Menu(mymenu)
edit_menu = Menu(mymenu)
format_menu = Menu(mymenu)

about_menu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=file_menu)
mymenu.add_cascade(label="Edit", menu=edit_menu)
mymenu.add_cascade(label="Format", menu=format_menu)

mymenu.add_cascade(label="About", menu=about_menu)

# configuring file menu i.e file_menu
file_menu.add_command(label="New    CTRL + N", command=new_menu)
file_menu.add_command(label="Open   CTRL + O", command=open_menu)
file_menu.add_command(label="Save    CTRL + S", command=save_menu)
file_menu.add_command(label="Save As.. ", command=save_as_menu)
file_menu.add_separator()
file_menu.add_command(label="Rename ", command=rename_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_menu)

# configuring edit_menu
edit_menu.add_command(label="Undo     CTRL + Z", command=undo_menu)
edit_menu.add_command(label="Redo     CTRL + Y", command=redo_menu)
edit_menu.add_separator()
edit_menu.add_command(label="Cut   CTRL + X", command=cut_menu)
edit_menu.add_command(label="Copy     CTRL + C", command=copy_menu)
edit_menu.add_command(label="Paste    CTRL + V", command=paste_menu)
edit_menu.add_command(label="Delete   Del", command=del_menu)
edit_menu.add_separator()
edit_menu.add_command(label="Replace",command= replace_menu)
edit_menu.add_separator()
edit_menu.add_command(label="Select All   CTRL + A", command=selectall_menu)
edit_menu.add_command(label="Time/Date    F5", command=date_menu)

# configuring format_menu

format_menu.add_command(label = "Font",command =formate_menu)


# Configuring About_menu
about_menu.add_command(label="Developer",command= developer_menu)
about_menu.add_command(label="About Easy Text" ,command = easy_text)

# adding Text section
# import ScrolledText # Because Tkinter textarea does not provide scrolling
#  abilities, we use this additional library
frame = Frame(root)
textPad = Text(frame)
textPad.pack(expand=1, fill=BOTH)
frame.pack(expand=1, fill=BOTH)
scroll = Scrollbar(textPad, command=textPad.yview)
scroll.config(command=textPad.yview)
textPad.config(yscrollcommand=scroll.set, wrap=NONE)
scroll.pack(side=RIGHT, fill=Y)

scrollx = Scrollbar(textPad, command=textPad.xview, orient=HORIZONTAL)
scrollx.config(command=textPad.xview)
textPad.config(xscrollcommand=scrollx.set, font=("Arial", 10))
scrollx.pack(side=BOTTOM, fill=X)

root.mainloop()

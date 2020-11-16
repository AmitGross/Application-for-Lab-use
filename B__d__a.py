from tkinter import *

from tkinter import *
def change_i_window_B_d_a(window_name, back, next):



    root=Tk()

    Label(root, text= window_name,fg="blue").pack()
    #Label(root, text= "choose what to do").pack()
    #Label(root, text = "last window was: "+str(back)).pack()
    #Label(root, text="next window: " + str(next)).pack()
    projectname_entry=Entry(root)
    projectname_entry.pack()
    def ok_button():
            global v
            v=int(next)
            global project_name
            project_name=projectname_entry.get()
            root.destroy()

    def back_button():
            global v
            v=int(back)
            global project_name
            project_name=""
            root.destroy()


    Button(root, text= "ok", command = ok_button,width=17,bg="grey").pack()
    Button(root, text="back", command=back_button,width=17,bg="grey").pack()

    root.mainloop()
    global v
    global project_name
    return v , project_name
from tkinter import *

def change_i_window_B(window_name, back, next, username):
    root=Tk()


    Label(root, text= window_name, fg= "blue").pack()
    if username!="":
        Label(root, text= "hello "+str(username)).pack()
    #Label(root, text = "last window was: "+str(back)).pack()
    #Label(root, text="next window: " + str(next)).pack()

    def my_projects():
            global v
            v=int(next[0])
            root.destroy()
    def search():
            global v
            v=int(next[1])
            root.destroy()
    def new_project():
            global v
            v=int(next[2])
            root.destroy()
    def calculators():
            global v
            v=int(next[3])
            root.destroy()


    def back_button():
            global v
            v=int(back)
            root.destroy()


    Button(root, text= "my projects", command = my_projects, width=17, bg="grey").pack()
    Button(root, text= "search", command = search, width=17, bg="grey").pack()
    Button(root, text= "new project", command = new_project, width=17, bg="grey").pack()
    Button(root, text= "calculators", command = calculators, width=17, bg="grey").pack()
    Button(root, text="back", command=back_button, width=17, bg="grey").pack()

    root.mainloop()
    return v
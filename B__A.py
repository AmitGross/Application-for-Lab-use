from tkinter import *
from B__A__a import change_i_window_B_A_a
def change_i_window_B_A(window_name, back, next):
    root=Tk()
    Label(root, text= "Calculators Menu", fg= "blue").pack()


    root.title("Calculaors")
    #Label(root, text= "choose what to do").pack()
    #Label(root, text = "last window was: "+str(back)).pack()
    #Label(root, text="next window: " + str(next)).pack()

    def poweder_to_solution():
        change_i_window_B_A_a("poweder to solution")
    def cal_two():
            pass
    def cal_three():
            pass

    def back_button():
            global v
            v=int(back)
            root.destroy()


    Button(root, text= "poweder to solution", command = poweder_to_solution, width=17, bg="grey").pack()
    Button(root, text= "cal_two", width=17, bg="grey", command = cal_two).pack()
    Button(root, text= "cal_three", width=17, bg="grey", command = cal_three).pack()
    Button(root, text="back", width=17, bg="grey", command=back_button).pack()

    root.mainloop()
    global v
    return v
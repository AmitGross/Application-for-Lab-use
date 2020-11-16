from tkinter import *
def change_i_window_B_d_B_b_b(window_name, back, next):
    root=Tk()
    PAb_data={}

    frame_one = Frame(root)
    frame_one.grid(column=0, row=0)
    Label(frame_one, text="1°Ab").pack()
    Label(frame_one, text="first 1°Ab").pack()
    Label(frame_one, text="second 1°Ab").pack()
    Label(frame_one, text="third 1°Ab").pack()

    frame_two = Frame(root)
    frame_two.grid(column=1, row=0)
    Label(frame_two, text="protein of interest").pack()
    first_PAb_entry = Entry(frame_two)
    first_PAb_entry.pack()
    second_PAb_entry = Entry(frame_two)
    second_PAb_entry.pack()
    third_PAb_entry = Entry(frame_two)
    third_PAb_entry.pack()

    frame_third = Frame(root)
    frame_third.grid(column=2, row=0)
    Label(frame_third, text="animal").pack()
    first_PAb_animal_entry = Entry(frame_third)
    first_PAb_animal_entry.pack()
    second_PAb_animal_entry = Entry(frame_third)
    second_PAb_animal_entry.pack()
    third_PAb_animal_entry = Entry(frame_third)
    third_PAb_animal_entry.pack()

    frame_third = Frame(root)
    frame_third.grid(column=3, row=0)
    Label(frame_third, text="ratio").pack()
    Label(frame_third, text="1:").pack()
    Label(frame_third, text="1:").pack()
    Label(frame_third, text="1:").pack()

    frame_four = Frame(root)
    frame_four.grid(column=4, row=0)
    Label(frame_four, text="ratio").pack()
    first_PAb_ratio_entry = Entry(frame_four)
    first_PAb_ratio_entry.pack()
    second_PAb_ratio_entry = Entry(frame_four)
    second_PAb_ratio_entry.pack()
    third_PAb_ratio_entry = Entry(frame_four)
    third_PAb_ratio_entry.pack()

    def ok_button():
        first_PAb=first_PAb_entry.get()
        PAb_data.update(first_PAb=first_PAb)
        first_PAb_animal=first_PAb_animal_entry.get()
        PAb_data.update(first_PAb_animal=first_PAb_animal)
        first_PAb_ratio=first_PAb_ratio_entry.get()
        PAb_data.update(first_PAb_ratio=first_PAb_ratio)
        second_PAb=second_PAb_entry.get()
        PAb_data.update(second_PAb=second_PAb)
        second_PAb_animal=second_PAb_animal_entry.get()
        PAb_data.update(second_PAb_animal=second_PAb_animal)
        second_PAb_ratio=second_PAb_ratio_entry.get()
        PAb_data.update(second_PAb_ratio=second_PAb_ratio)
        third_PAb=third_PAb_entry.get()
        PAb_data.update(third_PAb=third_PAb)
        third_PAb_animal=third_PAb_animal_entry.get()
        PAb_data.update(third_PAb_animal=third_PAb_animal)
        third_PAb_ratio=third_PAb_ratio_entry.get()
        PAb_data.update(third_PAb_ratio=third_PAb_ratio)

        global v
        v = (int(next), PAb_data)
        root.destroy()

    def back_button():

        global v
        v=(int(back),None)
        root.destroy()

    frame_zero=Frame(root)
    frame_zero.grid(column=0, row=1)
    Button(frame_zero, text= "ok", width=30,bg="tan2", command = ok_button).pack()
    Button(frame_zero, text="back",width=30,bg="tan2", command=back_button).pack()

    root.mainloop()
    global v
    return v
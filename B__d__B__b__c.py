from tkinter import *
def change_i_window_B_d_B_b_c(window_name, back, next,PAb_data):
    PAb_data=PAb_data
    def menu_tk(root):
        menubar = Menu(root)

        def hello():
            global v
            v = 1
            global username
            username = ""
            root.destroy()

        root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="mainmenu", command=hello)
        filemenu.add_command(label="Save", command=hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="go to", menu=filemenu)

    root=Tk()
    menu_tk(root)
    last_dic={}
    frame_Ab_name = Frame(root)
    frame_Ab_name.grid(column=0, row=0)

    Label(frame_Ab_name, text="  ").pack()
    Label(frame_Ab_name,
          text=str(PAb_data.get("first_PAb")) + ":   α " + str(PAb_data.get("first_PAb_animal") + "  Cy")).pack()
    Label(frame_Ab_name,
          text=str(PAb_data.get("second_PAb")) + ":   α " + str(PAb_data.get("second_PAb_animal") + "  Cy")).pack()
    Label(frame_Ab_name,
          text=str(PAb_data.get("third_PAb")) + ":   α " + str(PAb_data.get("third_PAb_animal") + "  Cy")).pack()

    frame_Ab_Ratio_entry = Frame(root)
    frame_Ab_Ratio_entry.grid(column=1, row=0)

    Label(frame_Ab_Ratio_entry, text="").pack()
    entry_first_second_Ab = Entry(frame_Ab_Ratio_entry)
    entry_first_second_Ab.pack()
    entry_second_second_Ab = Entry(frame_Ab_Ratio_entry)
    entry_second_second_Ab.pack()
    entry_third_second_Ab = Entry(frame_Ab_Ratio_entry)
    entry_third_second_Ab.pack()

    frame_ratio_label = Frame(root)
    frame_ratio_label.grid(column=2, row=0)

    Label(frame_ratio_label, text="").pack()
    Label(frame_ratio_label, text="1: ").pack()
    Label(frame_ratio_label, text="1: ").pack()
    Label(frame_ratio_label, text="1: ").pack()

    frame_ratio_entry = Frame(root)
    frame_ratio_entry.grid(column=3, row=0)

    Label(frame_ratio_entry, text="").pack()
    first_second_Ab_ratio_entry = Entry(frame_ratio_entry)
    first_second_Ab_ratio_entry.pack()
    second_second_Ab_ratio_entry = Entry(frame_ratio_entry)
    second_second_Ab_ratio_entry.pack()
    third_second_Ab_ratio_entry = Entry(frame_ratio_entry)
    third_second_Ab_ratio_entry.pack()

    frame_zero = Frame(root)
    frame_zero.grid(column=0, row=1)

    def ok_button():
        first_second_Ab=entry_first_second_Ab.get()
        second_second_Ab=entry_second_second_Ab.get()
        third_second_Ab=entry_third_second_Ab.get()
        first_second_Ab_ratio=first_second_Ab_ratio_entry.get()
        second_second_Ab_ratio=second_second_Ab_ratio_entry.get()
        third_second_Ab_ratio=third_second_Ab_ratio_entry.get()

        last_dic.update(first_second_Ab=first_second_Ab)
        last_dic.update(second_second_Ab=second_second_Ab)
        last_dic.update(third_second_Ab=third_second_Ab)
        last_dic.update(first_second_Ab_ratio=first_second_Ab_ratio)
        last_dic.update(second_second_Ab_ratio=second_second_Ab_ratio)
        last_dic.update(third_second_Ab_ratio=third_second_Ab_ratio)
        global v
        v=(int(next),last_dic)
        root.destroy()

    def back_button():
            global v
            v=(int(back),None)
            root.destroy()


    Button(frame_zero, text= "ok", command = ok_button).pack()
    Button(frame_zero, text="back", command=back_button).pack()

    root.mainloop()
    return v
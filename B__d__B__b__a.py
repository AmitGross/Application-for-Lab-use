from tkinter import *
from tkinter.ttk import Combobox
def change_i_window_B_d_B_b_a(window_name, back, next):
    root=Tk()
    root.configure(bg="burlywood1")
    root.geometry("392x200")
    conditions={}
    slides_frame=Frame(root, bg="burlywood1")

    slides_frame.pack()
    Label(slides_frame, text="number of slides", width=31, anchor=E, bg="burlywood1").grid(column=0, row=0)
    slides_entry=Entry(slides_frame,  width=25)
    slides_entry.grid(column= 1, row=0)


    Triton_frame=Frame(root)
    Triton_frame.pack()
    Label(Triton_frame, text="percent of Triton", width=30, anchor=E, bg="burlywood1").grid(column=0, row=0)
    triton_combobox=Combobox(Triton_frame, values= [None,0.1,0.2,0.3,0.5], width=25)
    triton_combobox.grid(column=1, row=0)


    AR_frame=Frame(root)
    AR_frame.pack()
    Label(AR_frame, text="choose AR",width=30, anchor=E, bg="burlywood1").grid(column=0, row=0)
    AR_combobox=Combobox(AR_frame, values= [None,"TE","CA"], width=25)
    AR_combobox.grid(column=1, row=0)

    AR_time=Frame(root)
    AR_time.pack()
    Label(AR_time, text="AR time", width=30, anchor=E, bg="burlywood1").grid(column=0, row=0)
    AR_time_combobox=Combobox(AR_time, values= ["10 minutes","20 minutes","25 minutes"], width=25)
    AR_time_combobox.grid(column=1, row=0)


    AB_block=Frame(root)
    AB_block.pack()
    Label(AB_block, text="A/B time",width=30, anchor=E, bg="burlywood1").grid(column=0, row=0)
    AB_combobox=Combobox(AB_block, values= [None,"15 minutes","30 minutes"], width=25)
    AB_combobox.grid(column=1, row=0)


    PAb_frame=Frame(root)
    PAb_frame.pack()
    Label(PAb_frame, text="to stain", width=30, anchor=E, bg="burlywood1").grid(column=0, row=0)
    PAb_combobox=Combobox(PAb_frame, values= [None,1,2,3], width=25)
    PAb_combobox.grid(column=1, row=0)




    amp_frame=Frame(root)
    amp_frame.pack()
    Label(amp_frame, text="amplification", width=30, anchor=E, bg="burlywood1").grid(column=0, row=0)
    amp_combobox = Combobox(amp_frame, values=[None, "yes"], width=25)
    amp_combobox.grid(column=1, row=0)


    def ok_button():
        slides = slides_entry.get()
        conditions.update(slides=slides)
        triton = triton_combobox.get()
        conditions.update(triton=triton)
        AR = AR_combobox.get()
        conditions.update(AR=AR)
        AR_time = AR_time_combobox.get()
        conditions.update(AR_time=AR_time)
        AB = AB_combobox.get()
        conditions.update(AB=AB)
        PAb = PAb_combobox.get()
        conditions.update(PAb=PAb)
        amp = amp_combobox.get()
        conditions.update(amp=amp)
        global v
        v = (int(next), conditions)
        root.destroy()

    def back_button():
        global v
        v=(int(back),None)
        root.destroy()


    Button(root, text= "ok",width=20, bg="tan4",command = ok_button).pack()
    Button(root, text="back",width=20,bg="tan4", command=back_button).pack()

    root.mainloop()
    return v
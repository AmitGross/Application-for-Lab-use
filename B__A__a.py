from tkinter import *
def change_i_window_B_A_a(window_name):
    root=Tk()
    root.geometry("178x200")




    def back_button():
            root.destroy()
    def ok_button():
        substance=entry_substance.get()
        volume=int(entry_volume.get())
        molarity=int(entry_molarity.get())
        substance_Mw=int(element_reader(substance))
        answer= substance_Mw*molarity*volume
        Label(root, text = "weigh "+str(answer)+" grams of "+ str(substance)).pack()
    Label(root, text ="write substance in capital letters").pack()
    entry_substance=Entry(root,width=28)
    entry_substance.pack()
    Label(root, text = "write volume in litters").pack()
    entry_volume=Entry(root,width=28)
    entry_volume.pack()
    Label(root, text = "write Molarity").pack()
    entry_molarity=Entry(root,width=28)
    entry_molarity.pack()

    Button(root, text="ok",width=28,bg="grey", command=ok_button).pack()
    Button(root, text="back",width=28,bg="grey", command=back_button).pack()

    root.mainloop()




def element_reader(Input_of_formula):
    elements_in_dict = \
        {
            "C": 12, \
            "O": 16, \
            "H": 1 \
            }
    # string_of_2_to_9="23456789"
    string_of_2_to_9 = [2, 3, 4, 5, 6, 7, 8, 9]
    # print(elements_in_dict.get("C"))
    listIcontainingthe_input = []
    sum = 0
    i=0

    for letter in Input_of_formula:
        i+=1

        listIcontainingthe_input.append(letter)

        letters_wight= elements_in_dict.get(letter)
        if letters_wight ==None:
            #print("i is: " + str(i))

            for number in string_of_2_to_9:
                if int(number)== int(letter):
                    #print(letter)
                    element_to_multiply_by_number= elements_in_dict.get(listIcontainingthe_input[i-2])
                    sum_to_add_but_need_to_subtract_once=int(element_to_multiply_by_number)*(int(number))
                    sum_to_add=(sum_to_add_but_need_to_subtract_once-element_to_multiply_by_number)
                    #print(sum_to_add)
                    sum+=sum_to_add

            continue

        sum+=letters_wight
    return sum


from tkinter import *

def change_i_window_B_d_B_a(project_name,list_of_treatments):

    root=Tk()
    Label(root, text=project_name)
    i=0
    print(list_of_treatments)

    for item in list_of_treatments:
        Label(root, text= "Treatment").grid(column= 0, row=i)
        i+=1


        for condition in item.conditions:
            Label(root, text=condition).grid(column=0, row=i)
            i+=1


        for data in item.PAb_data:
            Label(root, text=data).grid(column=0, row=i)
            i+=1


        for data_l in item.last_dictionary:
            Label(root, text=data_l).grid(column=0, row=i)
            i+=1
        break








    x=1
    for item in list_of_treatments:
        y=0
        Label(root, text= item.treatment_num).grid(column=x, row=y)
        y+=1

        for condition in item.conditions:
            Label(root, text=item.conditions.get(str(condition)) ).grid(column=x, row=y)
            y+=1
        for data in item.PAb_data:
            Label(root, text=item.PAb_data.get(str(data)) ).grid(column=x, row=y)
            y+=1
        for data_1 in item.last_dictionary:
            Label(root, text=item.last_dictionary.get(str(data_1)) ).grid(column=x, row=y)
            y+=1
        x+=1

    root.mainloop()



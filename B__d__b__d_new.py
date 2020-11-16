import json
from tkinter import *
import time
from tkinter.ttk import Combobox


def open_notebook():
    openfile = open(str("notebook") + str(".json"))
    str_dic = json.load(openfile)

    dic = json.loads(str_dic)
    return dic


def turn_treatment_instance_to_json(day,month,year,list_of_treatments):






    name_of_file=str(year)+str(month)
    def openfile(jasonfilename):
        try:
            openjson=open(str(jasonfilename + str(".json")))
            data = json.load(openjson)





            return json.loads(data)
        except:
            openjson= open(str(jasonfilename)+str(".json"), "w")

            return {}

    var_dic=openfile(name_of_file)



    #var_dic = {}
    var_dict = {}

    # print(all_treatmebts_instance.conditions)
    # print(all_treatmebts_instance.PAb_data)
    # print(all_treatmebts_instance.last_dictionary)
    #print(list_of_treatments)
    for treat in list_of_treatments:
        if var_dic.get(str(day)) == None:
            var_dic[day] = [[{"main_data": treat.main_data},
                            {"conditions": treat.conditions},
                            {"P_Ab_data": treat.PAb_data},
                            {"last_dictionary": treat.last_dictionary}]]

        else:
            var_dic.get(str(day)).append([{"main_data": treat.main_data},
                                          {"conditions": treat.conditions},
                                          {"P_Ab_data": treat.PAb_data},
                                          {"last_dictionary": treat.last_dictionary}])
            #print(var_dic.get(str(day)))

    jsonvar=json.dumps(var_dic)
    print(jsonvar)

    with open(str(name_of_file) + str(".json"), "w") as name_of_file:
        json.dump(jsonvar, name_of_file)









global list_of_dates
list_of_dates = []

a = time.asctime()
dic_time = a.split()
current_day = dic_time[0]
current_month = dic_time[1]
current_day_in_month = dic_time[2]
current_hour = dic_time[3]
current_year = dic_time[4]
list_of_months = ["january", "feburary", "march", "april", "may", "june", "july", "august", "september", "october",
                  "november", "december"]

list_of_days = []

def save_treatments(list_of_treatments):


    for i in range(31):
        list_of_days.append(i)
    root = Toplevel()
    upper_frame=Frame(root)
    upper_frame.grid(column=0,row=0, sticky= W)
    day_combo_box = Combobox(upper_frame, values=list_of_days);
    day_combo_box.grid(column=1, row=1, sticky= W)
    month_combobox = Combobox(upper_frame, values=list_of_months);
    month_combobox.grid(column=2, row=1, sticky= W)
    year_box = Combobox(upper_frame, values=[2017, 2018, 2019]);
    year_box.grid(column=3, row=1, sticky= W)
    v = StringVar()





    def var_fun():

       #these 4 lines are possibly not in the right place, therefore there are saving problems/?
        chosen_day = day_combo_box.get()
        chosen_month = month_combobox.get()
        chosen_year = year_box.get()
        chosen_date = str(str(chosen_day) + " " + str(chosen_month) + " " + str(chosen_year))
        if v.get() == "other_date":
            list_of_dates.append(chosen_date.split())
            day = str(list_of_dates[0][0])
            month = list_of_dates[0][1]
            year = str(list_of_dates[0][2])
            turn_treatment_instance_to_json(day, month, year,list_of_treatments)
            root.destroy()
        else:
            var = v.get()

            list_of_dates.append(var.split())
            day = str(list_of_dates[0][0])
            month = list_of_dates[0][1]
            year = str(list_of_dates[0][2])
            turn_treatment_instance_to_json(day, month, year,list_of_treatments)
            root.destroy()


    current_date_button = Radiobutton(upper_frame, variable=v, value=str(
        str(current_day_in_month) + " " + str(current_month) + " " + str(current_year)), indicatoron=0,
                                      text="current date", bg="grey");
    current_date_button.grid(column=0, row=0)

    different_date_button = Radiobutton(upper_frame, variable=v, value="other_date", indicatoron=0, text="other date");
    different_date_button.grid(column=0, row=1)



    Label(upper_frame, text=current_month + " / " + current_day_in_month + " / " + current_year, fg="blue", width=18).grid(column=1, row=0)
    #Label(upper_frame, text="",width=70, bg="grey").grid(columnspan=5, row=4, sticky= W)

    notebook_frame=Frame(root) ; notebook_frame.grid(column=0, row=2, sticky= W)
    notebook_header_frame=Frame(root)
    notebook_header_frame.grid(column=0, row=1)
    Label(notebook_header_frame, text= "notebook information", bg="grey", width=70).grid(column=0, row=0)
    noteb_var=StringVar()

    data_note=open_notebook()

    current_notebook=data_note.get("current")
    older_notebooks=data_note.get("old")
    older_notebooks_arr=[]
    for item in older_notebooks:
        older_notebooks_arr.append("{}    {} - {}".format(item[0],item[1],item[2]))

    #print(older_notebooks)

    current_notebook_radiobutton=Radiobutton(notebook_frame, variable=noteb_var, value="current_note") ; current_notebook_radiobutton.grid(column= 1, row=0, sticky= E)
    Label(notebook_frame, text=current_notebook, fg="blue").grid(column= 3, row=0)

    Label(notebook_frame, text=  "old").grid(column= 2, row=1)
    other_notebook_radiobutton=Radiobutton(notebook_frame, variable=noteb_var, value="old_note") ; other_notebook_radiobutton.grid(column= 1, row=1, sticky= E)
    current_notebook_radiobutton.select()
    current_date_button.select()

    old_notebooks = Combobox(notebook_frame, value=older_notebooks_arr, width=28)

    old_notebooks.grid(column=3, row=1, sticky=W)

    Label(notebook_frame, text="current").grid(column= 2, row=0)
    Label(notebook_frame, text="current").grid(column= 2, row=0)
    Label(notebook_frame, text="pages :", bg="light pink").grid(column= 0, row=0)
    entry_days=Entry(notebook_frame, width= 7, bg="light pink"); entry_days.grid(column=0, row=1, sticky= N)

    save_button = Button(notebook_frame, text="save project", command=var_fun, width=23, height= 3, bg="LightPink4").grid(column=4,row=0, rowspan=4, sticky=E)












    root.mainloop()


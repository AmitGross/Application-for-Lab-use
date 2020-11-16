import json
from tkinter import *
from tkinter.ttk import Combobox


def change_i_window_B_B(window_name, back):
    list_of_months = ["january", "feburary", "march", "april", "may", "june", "july", "august", "september", "october",
                      "november", "december"]

    dic_of_month_num_to_str = {1: "january", 2: "feburary", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july",
                               8: "august", 9: "september", 10: "october",
                               11: "november", 12: "december"}
    dic_of_month_str_to_num = {"january": 1, "feburary": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
                               "august": 8, "september": 9, "october": 10,
                               "november": 11, "december": 12}

    def openfile(jasonfilename):
        try:

            with open(str(jasonfilename + str(".json"))) as x:
                data = json.load(x)
        except:
            # print("no such file : "+str(jasonfilename))
            return
        # print("there is there file" + str(jasonfilename))

        return json.loads(data)

    def open_months_from_to(from_month, to_month, year):
        from_month_value = dic_of_month_str_to_num.get(from_month)

        to_month_value = dic_of_month_str_to_num.get(to_month)
        list_of_months_var = []
        for month in range(from_month_value, to_month_value + 1):
            list_of_months_var.append(dic_of_month_num_to_str.get(month))

        return [list_of_months_var, year]

    var_list = open_months_from_to("march", "september", 2018)

    # print(var_list)

    def year_to_year(start_year, month_start, end_year, month_end):
        list_of_month_to_open = []

        difference = end_year - start_year
        if difference < 0:
            return

        if difference == 0:
            list_of_month_to_open.append(open_months_from_to(month_start, month_end, start_year))
        if difference == 1:
            list_of_month_to_open.append((open_months_from_to(month_start, "december", start_year)))
            list_of_month_to_open.append(open_months_from_to("january", month_end, end_year))

        if difference > 1:

            list_of_month_to_open = []
            for i in range(difference + 1):

                if i == 0:
                    list_of_month_to_open.append(open_months_from_to(month_start, "december", start_year))

                if i == difference:
                    list_of_month_to_open.append(open_months_from_to("january", month_end, end_year))

                else:
                    current_year = i + start_year
                    if current_year == start_year:
                        pass
                    else:

                        list_of_month_to_open.append(open_months_from_to("january", "december", current_year))

        return list_of_month_to_open

    def input_fromtomonth_output_eachproject():
        entered_username = entry_username.get()
        entered_protein = entry_protein.get()
        if from_year_box.get() == "":
            if to_year_box.get() == "":
                # laster change min and max year
                list_with_months_and_year = year_to_year(2017, "january", 2020, "december")

        else:
            from_year = int(from_year_box.get())
            from_month = str(from_month_combobox.get())
            to_year = int(to_year_box.get())
            to_month = str(to_month_combobox.get())
            list_with_months_and_year = year_to_year(from_year, from_month, to_year, to_month)

        # from_year= 2017
        # from_month="january"
        # to_year=   2020
        # to_month=  "december"

        # here later need to put accual input dates#####
        # list_with_months_and_year=year_to_year(2017,"january",2020,"december")

        list_of_all_files_opend = []

        for item in list_with_months_and_year:
            # print(item)
            # print(item)
            months_var_year = item[0]
            current_var_year = item[1]
            for month in months_var_year:
                # print(str(current_var_year)+str(month))

                name_of_file_to_open = str(current_var_year) + str(month)
                dic = openfile(name_of_file_to_open)
                if dic == None:
                    pass
                else:
                    list_of_all_files_opend.append((str(current_var_year), str(month), dic))
                    # print(dic)

        # print(list_of_all_files_opend)

        i = 1

        for project in list_of_all_files_opend:

            project_year = project[0]
            project_month = project[1]
            project_data = project[2]
            # print(project_data)
            for day in project_data:
                for a_project in project_data.get(day):

                    # for details in a_project:
                    #    print(details)
                    projectlist = []

                    # print(project)
                    # print(project_month)
                    # print(project_year)
                    # print(day)
                    date_str = " {}  {}  {}".format(day, project_month, project_year)

                    main_data_dic = a_project[0].get("main_data")

                    conditions_dic = a_project[1].get("conditions")
                    P_Ab_data_dic = a_project[2].get("P_Ab_data")
                    last_dictionary_dic = a_project[3].get("last_dictionary")

                    projectname = main_data_dic.get("project_name")
                    proteins = main_data_dic.get("list_of_proteins")
                    username = main_data_dic.get("username")

                    # print(username)
                    # print(entered_username)
                    # print(proteins)
                    # print(entered_protein)
                    if entered_username == "":
                        if entered_protein == "":
                            main_data_str = "                       {}                                          {}                    {}   ".format(
                                date_str, username, proteins)
                            listbox.insert(i, main_data_str)

                        else:
                            if entered_protein == proteins[0]:
                                main_data_str = "                       {}                                          {}                    {}   ".format(
                                    date_str, username, proteins)
                                listbox.insert(i, main_data_str)

                            if entered_protein == proteins[1]:
                                main_data_str = "                       {}                                          {}                    {}   ".format(
                                    date_str, username, proteins)
                                listbox.insert(i, main_data_str)
                    else:
                        if entered_username == username:
                            if entered_protein == "":
                                main_data_str = "                       {}                                          {}                    {}   ".format(
                                    date_str, username, proteins)
                                listbox.insert(i, main_data_str)
                            else:
                                if entered_protein == proteins[0]:
                                    main_data_str = "                       {}                                          {}                    {}   ".format(
                                        date_str, username, proteins)
                                    listbox.insert(i, main_data_str)

                                if entered_protein == proteins[1]:
                                    main_data_str = "                       {}                                          {}                    {}   ".format(
                                        date_str, username, proteins)
                                    listbox.insert(i, main_data_str)

            i += 1

    root=Tk()
    root.configure(bg="LightSkyBlue3")
    frame_back=Frame(root)
    frame_back.grid(column=0, row=3)

    def back_button():
            global v
            v=int(back)
            global project_name
            project_name=""
            root.destroy()


    Button(frame_back, text="back", command=back_button, width= 50, height=2, bg="SlateGray2").pack()
    root.geometry("560x400")

    search_frame = Frame(root, bg="LightSkyBlue1")
    search_frame.grid(column=0, row=0)

    Label(search_frame, text="username",bg="LightSkyBlue1").grid(column=0, row=0)
    entry_username = Entry(search_frame, width=23);
    entry_username.grid(column=0, row=1)

    Label(search_frame, text="protein",bg="LightSkyBlue1").grid(column=1, row=0)
    entry_protein = Entry(search_frame, width=23, );
    entry_protein.grid(column=1, row=1)

    Label(search_frame, text="from",bg="LightSkyBlue1").grid(columnspan=2, row=2)

    from_month_combobox = Combobox(search_frame, values=list_of_months);
    from_month_combobox.grid(column=0, row=3)

    from_year_box = Combobox(search_frame, values=[2017, 2018, 2019, 2020]);
    from_year_box.grid(column=1, row=3)

    Label(search_frame, text="to",bg="LightSkyBlue3").grid(columnspan=2, row=4)
    to_month_combobox = Combobox(search_frame, values=list_of_months);
    to_month_combobox.grid(column=0, row=5)
    to_year_box = Combobox(search_frame, values=[2017, 2018, 2019, 2020]);
    to_year_box.grid(column=1, row=5)

    header_frame = Frame(root, bg="LightSkyBlue3")
    header_frame.grid(column=0, row=1)
    Label(header_frame, text="", bg="LightSkyBlue3").grid(column=0, row=2)
    Label(header_frame, text="date                                   user name                     1°Ab",bg="LightSkyBlue3").grid(column=0,
                                                                                                               row=3)

    listbox_frame = Frame(root ,bg="LightSkyBlue3")
    listbox_frame.grid(column=0, row=2)

    def data_fetch():
        listbox.delete(0, END)
        selected_project = listbox.get(ACTIVE)
        # print(selected_project)
        selected_project_i = listbox.index(ACTIVE)
        # print(selected_project_i)
        # messagebox.showinfo("data"," you selected "+ selected_project)
        input_fromtomonth_output_eachproject()

    listbox = Listbox(listbox_frame,bg="SlateGray2", width=80)
    listbox.pack(side=LEFT, fill="both", expand=True)


    buttonone = Button(header_frame, width=40,  text="search", command=data_fetch, bg="SlateGray2")
    buttonone.grid(column=0, row=1)
    i = 0
    # print(dic)

    scroll = Scrollbar(listbox_frame,bg="LightSkyBlue3")
    scroll.pack(side=RIGHT, fill="y")

    # allows me to scroll the scroll bar
    scroll.config(command=listbox.yview)

    # lets the scroll bar stay in a position, rather then jump th ethe top when left
    listbox.config(yscrollcommand=scroll.set)

    root.mainloop()
    global v
    return v

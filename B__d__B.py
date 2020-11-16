from tkinter import *
from B__d__b__d_new import save_treatments




def change_i_window_B_d_B(window_name, back, next, projectname,list_of_treatments):


    root=Tk()
    Label(root, text= window_name, fg="blue").pack()
    if projectname!="":
        Label(root, text= projectname, fg="blue").pack()
    #Label(root, text = "last window was: "+str(back)).pack()
    #Label(root, text="next window: " + str(next)).pack()


    def matrix():
            global v
            v=int(next[0])
            root.destroy()
    def protocol():
            global v
            v=int(next[1])
            root.destroy()
    def treatment():
            global v
            v=int(next[2])
            root.destroy()


    def back_button():
            global v
            v=int(back)
            root.destroy()
    def save_button():
            global v
            v=int(back)

            save_treatments(list_of_treatments)
            root.destroy()



    Button(root, text= "matrix", command = matrix, width=17, bg="grey").pack()
    Button(root, text= "protocol", command = protocol, width=17, bg="grey").pack()
    Button(root, text= "add treatment", command = treatment, width=17, bg="grey").pack()
    Button(root, text= "save project", command = save_button, width=17, bg="grey").pack()
    Button(root, text="back", command=back_button, width=17, bg="grey").pack()

    root.mainloop()
    global v
    return v




"""
def turn_treatment_instance_to_json(list_of_treatments, year,month, day):

    print("--------------------")


    print(list_of_treatments)
    print("---------------------")

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


"""
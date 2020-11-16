from tkinter import *


from tkinter import *


class Treatments:
    def __init__(self,treatment_num, deparaffinization,ACT,AR_time,AR,AB_time,P_Ab_one,P_Ab_one_Animal,P_Ab_one_ratio,Triton,Slides,P_Ab_two, P_Ab_two_Animal, P_Ab_two_ratio, P_Ab_three, P_Ab_three_Animal, P_Ab_three_ratio, secondary_Ab_one_cy,  secondary_Ab_two_cy, secondary_Ab_three_cy, secondary_Ab_one_ratio, secondary_Ab_two_ratio, secondary_Ab_three_ratio,biotin_ratio  ):
        self.treatment_num=treatment_num
        self.deparaffinization = deparaffinization
        self.ACT = ACT
        self.AR_time = AR_time
        self.AR = AR
        self.AB_time = AB_time
        self.P_Ab_one = P_Ab_one
        self.P_Ab_one_Animal = P_Ab_one_Animal
        self.P_Ab_one_ratio = P_Ab_one_ratio
        self.Triton = Triton
        self.Slides = Slides
        self.P_Ab_two=P_Ab_two
        self.P_Ab_two_Animal=P_Ab_two_Animal
        self.P_Ab_two_ratio=P_Ab_two_ratio
        self.P_Ab_three=P_Ab_three
        self.P_Ab_three_Animal=P_Ab_three_Animal
        self.P_Ab_three_ratio=P_Ab_three_ratio
        self.secondary_Ab_one_cy=                   secondary_Ab_one_cy
        self.secondary_Ab_two_cy=                   secondary_Ab_two_cy
        self.secondary_Ab_three_cy=                   secondary_Ab_three_cy
        self.secondary_Ab_one_ratio=                   secondary_Ab_one_ratio
        self.secondary_Ab_two_ratio=                   secondary_Ab_two_ratio
        self.secondary_Ab_three_ratio=                   secondary_Ab_three_ratio
        self.biotin_ratio=                   biotin_ratio
















def change_i_window_B_d_B_c(project_name,list_of_treatments):

    list_for_info = []

    class protocol_class:
        def __init__(self,):
            GUI=Tk()

            maintreatmentsframe = Frame(GUI)
            maintreatmentsframe.grid(column=0, row=0)

            # deparafinization

            Deparaffinizationframe = Frame(GUI)
            Deparaffinizationframe.grid(column=1, row=1)

            Deparaffinizationframe_label = Label(Deparaffinizationframe, text="Deparaffinization:", background="green2")
            Deparaffinizationframe_label.grid(column=0, row=0)

            Deparaffinizationframe_wash_label = Label(Deparaffinizationframe, text="wash", background="pink")
            Deparaffinizationframe_wash_label.grid(column=1, row=1)

            # treatments  DEPAF
            deparaffinization_counter = 1
            for item in list_for_info:
                if item.deparaffinization == "yes":
                    Label(Deparaffinizationframe, text=item.treatment_num).grid(column=deparaffinization_counter, row=0)
                deparaffinization_counter += 1

                # ACT
            ACTframe = Frame(GUI)
            ACTframe.grid(column=1, row=2)

            ACT_label = Label(ACTframe, text="ACT:", background="green2")
            ACT_label.grid(column=0, row=0)

            # treatments  ACT
            ACT_counter = 1
            for item in list_for_info:
                if item.ACT == "yes":
                    Label(ACTframe, text=item.treatment_num).grid(column=ACT_counter, row=0)
                    Label(ACTframe, text=item.treatment_num).grid(column=ACT_counter, row=1)

                ACT_counter += 1

            ACT_wash_label = Label(ACTframe, text="wash", background="pink")
            ACT_wash_label.grid(column=1, row=1)

            # AR
            ARframe = Frame(GUI)
            ARframe.grid(column=1, row=3)

            ARlabel = Label(ARframe, text="AR", background="green2")
            ARlabel.grid(column=0, row=0)

            CAlabel = Label(ARframe, text="CA")
            CAlabel.grid(column=1, row=1)

            CA_tenlabel = Label(ARframe, text="10", background="yellow")
            CA_tenlabel.grid(column=2, row=2)

            CA_twentylabel = Label(ARframe, text="20", background="yellow")
            CA_twentylabel.grid(column=2, row=3)

            TElabel = Label(ARframe, text="TE")
            TElabel.grid(column=1, row=4)

            TE_tenlabel = Label(ARframe, text="10", background="yellow")
            TE_tenlabel.grid(column=2, row=5)

            TE_twentylabel = Label(ARframe, text="20", background="yellow")
            TE_twentylabel.grid(column=2, row=6)

            AR_wash_label = Label(ARframe, text="60' Cooldown --> wash", background="pink")
            AR_wash_label.grid(column=0, row=7)

            # treatments
            CAten_counter = 3
            CAtwenty_counter = 3

            TEten_counter = 3
            TEtwenty_counter = 3

            for item in list_for_info:
                if item.AR == "CA":
                    if item.AR_time =="10 minutes":
                        Label(ARframe, text=item.treatment_num).grid(column=CAten_counter, row=2)
                        CAten_counter += 1
                    if item.AR_time =="20 minutes":
                        Label(ARframe, text=item.treatment_num).grid(column=CAtwenty_counter, row=3)
                        CAtwenty_counter += 1
                if item.AR == "TE":
                    if item.AR_time =="10 minutes":
                        Label(ARframe, text=item.treatment_num).grid(column=TEten_counter, row=5)
                        TEten_counter += 1
                    if item.AR_time =="20 minutes":
                        Label(ARframe, text=item.treatment_num).grid(column=TEtwenty_counter, row=6)
                        TEtwenty_counter += 1

                    # BLOck
            Blockframe = Frame(GUI)
            Blockframe.grid(column=1, row=4)

            Blockframelabel = Label(Blockframe, text="Block", background="green2")
            Blockframelabel.grid(column=1, row=0)

            PBS_label_block = Label(Blockframe, text="PBSx1 80%")
            PBS_label_block.grid(column=0, row=1)

            NHS_label_block = Label(Blockframe, text="NHS 20%")
            NHS_label_block.grid(column=1, row=1)

            Triton_label_block = Label(Blockframe, text="Triton")
            Triton_label_block.grid(column=2, row=1)

            Triton_label_block = Label(Blockframe, text="0.2% Triton: ")
            Triton_label_block.grid(column=3, row=2)

            Triton_label_block = Label(Blockframe, text="0.3% Triton: ")
            Triton_label_block.grid(column=3, row=3)

            Triton_label_block = Label(Blockframe, text="0.5% Triton: ")
            Triton_label_block.grid(column=3, row=4)

            Triton_two_per = 0
            Triton_three_per = 0
            Triton_five_per = 0
            Triton_two_per_slides = 0
            Triton_three_per_slides = 0
            Triton_five_per_slides = 0
            for secitem in list_for_info:
                #print("fdfd")
                #print(secitem)
                #print(secitem.Triton)
                #print("fdfdfd")
                if secitem.Triton == "0.2":
                    Label(Blockframe, text=secitem.treatment_num).grid(column=int(4 + Triton_two_per), row=2)
                    Triton_two_per += 1
                    Triton_two_per_slides += int(secitem.Slides)
                    Label_PBS_Triton_two_per = Label(Blockframe, text=str(125 * 0.8 * Triton_two_per_slides) + "µL")
                    Label_PBS_Triton_two_per.grid(column=0, row=2)

                    Label_NHS_Triton_two_per = Label(Blockframe, text=str(125 * 0.2 * Triton_two_per_slides) + "µL")
                    Label_NHS_Triton_two_per.grid(column=1, row=2)

                    Label_Triton_Triton_two_per = Label(Blockframe, text=str(125 * 0.02 * Triton_two_per_slides) + "µL")
                    Label_Triton_Triton_two_per.grid(column=2, row=2)

                if secitem.Triton == "0.3":
                    Label(Blockframe, text=secitem.treatment_num).grid(column=int(4 + Triton_three_per), row=3)
                    Triton_three_per += 1
                    Triton_three_per_slides += int(secitem.Slides)

                    ##
                    Label_PBS_Triton_three_per = Label(Blockframe, text=str(125 * 0.8 * Triton_three_per_slides) + "µL")
                    Label_PBS_Triton_three_per.grid(column=0, row=3)

                    Label_NHS_Triton_three_per = Label(Blockframe, text=str(125 * 0.2 * Triton_three_per_slides) + "µL")
                    Label_NHS_Triton_three_per.grid(column=1, row=3)

                    Label_Triton_Triton_three_per = Label(Blockframe,
                                                          text=str(125 * 0.03 * Triton_three_per_slides) + "µL")
                    Label_Triton_Triton_three_per.grid(column=2, row=3)
                    ##

                if secitem.Triton == "0.5":
                    Label(Blockframe, text=secitem.treatment_num).grid(column=int(4 + Triton_five_per), row=4)
                    Triton_five_per += 1
                    Triton_five_per_slides += int(secitem.Slides)

                    Label_PBS_Triton_five_per = Label(Blockframe, text=str(125 * 0.8 * Triton_five_per_slides) + "µL")
                    Label_PBS_Triton_five_per.grid(column=0, row=4)

                    Label_NHS_Triton_five_per = Label(Blockframe, text=str(125 * 0.2 * Triton_five_per_slides) + "µL")
                    Label_NHS_Triton_five_per.grid(column=1, row=4)

                    Label_Triton_Triton_five_per = Label(Blockframe,
                                                         text=str(125 * 0.05 * Triton_five_per_slides) + "µL")
                    Label_Triton_Triton_five_per.grid(column=2, row=4)

                # AB_Block

            ABframe = Frame(GUI)
            ABframe.grid(column=1, row=5)

            ABlabel = Label(ABframe, text="AB_Block")
            ABlabel.grid(column=0, row=0)

            ABlabel_fifth = Label(ABframe, text="15", background="yellow")
            ABlabel_fifth.grid(column=1, row=1)

            ABlabel_thrd = Label(ABframe, text="30", background="yellow")
            ABlabel_thrd.grid(column=1, row=2)

            AB_counter_fifth = 1
            AB_counter_thrd = 1
            for secitem in list_for_info:
                if secitem.AB_time =="15 minutes":
                    AB_counter_fifth += 1
                    Label(ABframe, text=secitem.treatment_num).grid(column=AB_counter_fifth, row=1)

                if secitem.AB_time =="30 minutes":
                    AB_counter_thrd += 1
                    Label(ABframe, text=secitem.treatment_num).grid(column=AB_counter_thrd, row=2)

            list_of_relavent_Ab_treats = []
            for item in list_for_info:
                list_of_relavent_Ab_treats.append(
                    {"treatment_num": item.treatment_num, "Triton": item.Triton, "slides": item.Slides,
                     "P_Ab_one": item.P_Ab_one, "P_Ab_one_Animal": item.P_Ab_one_Animal,
                     "P_Ab_one_ratio": item.P_Ab_one_ratio, "P_Ab_two": item.P_Ab_two,
                     "P_Ab_two_Animal": item.P_Ab_two_Animal, "P_Ab_two_ratio": item.P_Ab_two_ratio})

            # for item in list_of_relavent_Ab_treats:
            # print(item)

            def compare_function(a, b):


                if a.get("Triton") == b.get("Triton"):
                    if a.get("P_Ab_one") == b.get("P_Ab_one"):
                        if a.get("P_Ab_one_Animal") == b.get("P_Ab_one_Animal"):
                            if a.get("P_Ab_one_ratio") == b.get("P_Ab_one_ratio"):
                                if a.get("P_Ab_two") == b.get("P_Ab_two"):
                                    if a.get("P_Ab_two_Animal") == b.get("P_Ab_two_Animal"):
                                        if a.get("P_Ab_two_ratio") == b.get("P_Ab_two_ratio"):
                                            return True
                return False

            grouplist = []

            for item in list_of_relavent_Ab_treats:
                flag = 0
                for group in grouplist:

                    if compare_function(group[0], item):
                        group.append(item)
                        flag = 1
                        break
                if flag == 0:
                    grouplist.append([item])
            # i=1
            # for group in grouplist:
            #     print(str(i)+": ")
            #     i+=1
            #     for item in group:
            #         print("-----------------------------")
            #        print(item)

            # P_Ab

            P_Abframe = Frame(GUI)
            P_Abframe.grid(column=1, row=6)

            P_Abframelabel = Label(P_Abframe, text="1°Ab", background="green2")
            P_Abframelabel.grid(column=1, row=0)

            PBS_label_PAb = Label(P_Abframe, text="PBSx1 100%")
            PBS_label_PAb.grid(column=0, row=1)

            NHS_label_PAb = Label(P_Abframe, text="NHS 2%")
            NHS_label_PAb.grid(column=1, row=1)

            Triton_label_PAb = Label(P_Abframe, text="Triton")
            Triton_label_PAb.grid(column=2, row=1)

            label_PAb = Label(P_Abframe, text="1°Ab")
            label_PAb.grid(column=3, row=1)

            label_PAb_sec = Label(P_Abframe, text="1°Ab")
            label_PAb_sec.grid(column=4, row=1)

            Ab_counter = 2
            count = 2
            for similar_treatments_list in grouplist:
                treat_num_list=[]

                slides=0
                for group in similar_treatments_list:
                    var=group.get("slides")
                    slides+=int(var)




                    group_len = len(group)
                    Triton_Ab_str = group.get("Triton")
                    Triton_Ab_float=float(Triton_Ab_str)

                    first_Ab = group.get("P_Ab_one")
                    first_Ab_ratio = int(group.get("P_Ab_one_ratio"))
                    first_Ab_animal = group.get("P_Ab_one_Animal")

                    second_Ab = group.get("P_Ab_two")
                    second_Ab_ratio = int(group.get("P_Ab_two_ratio"))
                    second_Ab_animal = group.get("P_Ab_two_Animal")
                    treat_num_list.append(group.get("treatment_num"))

                triton_result_float=slides*12.5*Triton_Ab_float
                triton_result=round(triton_result_float,2)
                NHS_result_float=float(slides*0.02*125)
                NHS_result=round(NHS_result_float,2)
                PBS_result=slides*125
                first_Ab_ratio_result=(PBS_result/first_Ab_ratio)
                second_Ab_ratio_result = (PBS_result / second_Ab_ratio)







                Label(P_Abframe, text=str(triton_result)+"µL").grid(column=2, row=count)
                Label(P_Abframe, text=str(NHS_result)+"µL").grid(column=1, row=count)
                Label(P_Abframe, text=str(PBS_result)+"µL").grid(column=0, row=count)
                varx=5
                for item in treat_num_list:
                    Label(P_Abframe,text=item).grid(column=varx, row=count)
                    varx+=1


                text_for_first_PAb_name_and_amount=" {}µL (1: {}) of {} ({})".format(first_Ab_ratio_result,first_Ab_ratio,first_Ab, first_Ab_animal)
                text_for_second_PAb_name_and_amount=" {}µL (1: {}) of {} ({})".format(second_Ab_ratio_result,second_Ab_ratio,second_Ab, second_Ab_animal)


                Label(P_Abframe, text=text_for_first_PAb_name_and_amount).grid(column=3,row=count)
                Label(P_Abframe, text=text_for_second_PAb_name_and_amount).grid(column=4, row=count)
                count += 1






            Biotinframe = Frame(GUI)
            Biotinframe.grid(column=1, row=7)

            Secondary_Abframe = Frame(GUI)
            Secondary_Abframe.grid(column=1, row=8)

            blockframe = Frame(GUI)

            GUI.mainloop()

    x=1
    v=x-1

    for item in list_of_treatments:

        list_for_info.append(Treatments(item.treatment_num, "yes", None, item.conditions.get("AR_time"), item.conditions.get("AR"), item.conditions.get("AB"), item.PAb_data.get("first_PAb"), item.PAb_data.get("first_PAb_animal"),item.PAb_data.get("first_PAb_ratio"), item.conditions.get("triton"), item.conditions.get("slides"), item.PAb_data.get("second_PAb"), item.PAb_data.get("second_PAb_animal"),item.PAb_data.get("second_PAb_ratio"), None, None, None,None, None, None, None, None, None, None))


    protocol_class()





"""

    list_for_info.append(
        Treatments("a", "yes", None, "10 minutes", "CA", "15 minutes", "mac2", "Rt", 100, "0.2", 1, "cd3", "Rb", 25, None, None, None,
                   None, None, None, None, None, None, None))
    list_for_info.append(
        Treatments("c", "yes", "yes", "20 minutes", "TE", "15 minutes", "mac2", "Rt", 100, "0.2", 2, "cd3", "m", 25, None, None, None,
                   None, None, None, None, None, None, None))
    list_for_info.append(
        Treatments("b", None, "yes", "10 minutes", "CA", "30 minutes", "mac2", "Rt", 100, "0.3", 3, "GFP", "Gt", 100, None, None, None,
                   None, None, None, None, None, None, None))
    list_for_info.append(
        Treatments("d", None, "yes", "20 minutes", "CA", "30 minutes", "mac2", "Rt", 100, "0.3", 1, "GFP", "Gt", 100, None, None, None,
                   None, None, None, None, None, None, None))
    list_for_info.append(
        Treatments("e", None, "yes", "10 minutes", "CA", "30 minutes", "mac2", "Rt", 100, "0.3", 2, "", "Gt", 100, None, None, None,
                   None, None, None, None, None, None, None))

"""
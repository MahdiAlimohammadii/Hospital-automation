from Patient import Patient
from Doctor import Doctor
import colorama as clr

while True:
    print(clr.Back.LIGHTWHITE_EX,
          clr.Style.BRIGHT,
          clr.Fore.BLACK,
          "           Welcome!\n\n",
          "         Menu of Hospital\n\n",
          "1_Patients\n",
          "2_Doctors\n",
          "3_Exit\n")
    print(clr.Back.RESET)
    choose_operate = input(clr.Back.LIGHTWHITE_EX +
                           " Please enter the operation you need : ")
    print(clr.Style.RESET_ALL)
    while choose_operate == "1":
        print(clr.Back.BLUE,
              clr.Fore.LIGHTWHITE_EX,
              clr.Style.BRIGHT,
              "           Manage of Patients\n\n",
              "1_Create New Patient\n",
              "2_Remove Patient\n",
              "3_Edit Patient Info\n",
              "4_Show Patients of a Doctor\n",
              "5_Show All of Patient\n",
              "6_exit\n")
        print(clr.Back.RESET)
        patient_operate = input(clr.Back.BLUE +
                                " Please enter the operation you need : ")
        print(clr.Style.RESET_ALL)
        if patient_operate == "1":
            NewPatient = Patient(input(clr.Back.YELLOW +
                                       clr.Fore.BLACK +
                                       clr.Style.BRIGHT +
                                       " Please enter your serial code (must be 10 number!): " +
                                       clr.Style.RESET_ALL +
                                       "\n"),
                                 input(clr.Back.YELLOW +
                                       clr.Fore.BLACK +
                                       clr.Style.BRIGHT +
                                       " Please enter your name : " +
                                       clr.Style.RESET_ALL +
                                       "\n"),
                                 input(clr.Back.YELLOW +
                                       clr.Fore.BLACK +
                                       clr.Style.BRIGHT +
                                       " Please enter your doctors code (with tow space between codes): " +
                                       clr.Style.RESET_ALL +
                                       "\n"))
            Patient.new_patient(NewPatient, False)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Patients " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Patients " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif patient_operate == "2":
            PatientCode = input(clr.Back.YELLOW +
                                clr.Fore.BLACK +
                                clr.Style.BRIGHT +
                                " Please enter your serial code : " +
                                clr.Style.RESET_ALL +
                                "\n")
            Patient.remove_patient(PatientCode, False)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Patients " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Patients " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif patient_operate == "3":
            PatientCode = input(clr.Back.YELLOW +
                                clr.Fore.BLACK +
                                clr.Style.BRIGHT +
                                " Please enter your serial code : " +
                                clr.Style.RESET_ALL +
                                "\n")
            Patient.edit_info(PatientCode)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Patients " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Patients " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif patient_operate == "4":
            DrCode = input(clr.Back.YELLOW +
                           clr.Fore.BLACK +
                           clr.Style.BRIGHT +
                           " Please enter dr code : " +
                           clr.Style.RESET_ALL +
                           "\n")
            Patient.show_patient_from_dr_code(DrCode)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Patients " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Patients " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif patient_operate == "5":
            Patient.show_all_patient()
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Patients " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Patients " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif patient_operate == "6":
            break
        else:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Your insert is wrong!" +
                  clr.Style.RESET_ALL +
                  "\n")
    while choose_operate == "2":
        print(clr.Back.LIGHTGREEN_EX,
              clr.Fore.LIGHTWHITE_EX,
              clr.Style.BRIGHT,
              "           Manage of Doctors\n\n",
              "1_Create New Doctor\n",
              "2_Remove Doctor\n",
              "3_Edit Doctor Info\n",
              "4_Search Doctor\n",
              "5_Show Doctor List\n",
              "6_Show Doctors By Expertise\n",
              "7_exit\n")
        print(clr.Back.RESET)
        doctor_operate = input(clr.Back.LIGHTGREEN_EX +
                               " Please enter the operation you need : ")
        print(clr.Style.RESET_ALL)
        if doctor_operate == "1":
            NewDoctor = Doctor(input(clr.Back.YELLOW +
                                     clr.Fore.BLACK +
                                     clr.Style.BRIGHT +
                                     " Please enter your code : " +
                                     clr.Style.RESET_ALL +
                                     "\n"),
                               input(clr.Back.YELLOW +
                                     clr.Fore.BLACK +
                                     clr.Style.BRIGHT +
                                     " Please enter your name : " +
                                     clr.Style.RESET_ALL +
                                     "\n"),
                               input(clr.Back.YELLOW +
                                     clr.Fore.BLACK +
                                     clr.Style.BRIGHT +
                                     " Please enter your phone number (must be 11 number): " +
                                     clr.Style.RESET_ALL +
                                     clr.Fore.GREEN +
                                     "\n 09" +
                                     clr.Style.RESET_ALL),
                               input(clr.Back.YELLOW +
                                     clr.Fore.BLACK +
                                     clr.Style.BRIGHT +
                                     " Please enter your expertise (among : Eye, Pediatric, General and Heart): " +
                                     clr.Style.RESET_ALL +
                                     "\n"))
            Doctor.new_doctor(NewDoctor, False)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Doctors " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Doctors " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif doctor_operate == "2":
            code = input(clr.Back.YELLOW +
                         clr.Fore.BLACK +
                         clr.Style.BRIGHT +
                         " Please enter your doctor code : " +
                         clr.Style.RESET_ALL +
                         "\n")
            Doctor.remove_doctor(code, False)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Doctors " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Doctors " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif doctor_operate == "3":
            code = input(clr.Back.YELLOW +
                         clr.Fore.BLACK +
                         clr.Style.BRIGHT +
                         " Please enter your doctor code : " +
                         clr.Style.RESET_ALL +
                         "\n")
            Doctor.edit_info(code)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Doctors " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Doctors " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif doctor_operate == "4":
            code = input(clr.Back.YELLOW +
                         clr.Fore.BLACK +
                         clr.Style.BRIGHT +
                         " Please enter your doctor code : " +
                         clr.Style.RESET_ALL +
                         "\n")
            Doctor.search_doctor(code)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Doctors " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Doctors " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif doctor_operate == "5":
            Doctor.show_all_doctors()
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Doctors " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Doctors " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif doctor_operate == "6":
            expertise = input(clr.Back.YELLOW +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              " Please enter expertise : " +
                              clr.Style.RESET_ALL +
                              "\n")
            Doctor.show_doctor_list_by_expertise(expertise)
            condition = input(clr.Back.MAGENTA +
                              clr.Fore.BLACK +
                              clr.Style.BRIGHT +
                              "Press enter to return Manage Doctors " +
                              "(otherwise, Please enter 'exit' to return main page) : " +
                              clr.Style.RESET_ALL +
                              "\n")
            if condition == "":
                continue
            elif condition == "exit":
                break
            else:
                while condition != "" and condition != "exit":
                    print(clr.Back.RED +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          "Your insert is wrong!" +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = input(clr.Back.MAGENTA +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      "Press enter to return Manage Doctors " +
                                      "(otherwise, Please enter 'exit' to return main page) : " +
                                      clr.Style.RESET_ALL +
                                      "\n")
                if condition == "":
                    continue
                elif condition == "exit":
                    break
        elif doctor_operate == "7":
            break
        else:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Your insert is wrong!" +
                  clr.Style.RESET_ALL +
                  "\n")
    if choose_operate == "3":
        print(clr.Fore.LIGHTWHITE_EX +
              clr.Back.BLACK +
              clr.Cursor.BACK(1) +
              " Thank you for your visit!\n",
              "Good Luck :)")
        break
    elif choose_operate not in ["1", "2", "3"]:
        print(clr.Back.RED +
              clr.Fore.LIGHTWHITE_EX +
              clr.Style.BRIGHT +
              "Your insert is wrong!" +
              clr.Style.RESET_ALL +
              "\n")
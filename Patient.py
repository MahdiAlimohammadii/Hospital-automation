import colorama as clr


class Patient:
    def __init__(self, serial, name, Dr_code):
        self.serial = serial
        self.name = name
        self.Dr_code = Dr_code

    def new_patient(self, edit_mode):
        condition = True
        cond2 = True
        patient_file = open("Patients.txt", "r")
        patient_list = patient_file.readlines()
        patient_file.close()
        # check for unique code
        patient_file = open("Patients.txt", "a")
        doctor_file = open("Doctors.txt", "r")
        doctor_list = doctor_file.readlines()
        for patient in patient_list:
            for doctor in doctor_list:
                if self.serial in patient:
                    condition = False
                elif self.serial in doctor:
                    condition = False
        # for capitalize name
        list_name = str(self.name).split(" ")
        n_list = []
        for name in list_name:
            n_list.append(name.capitalize())
        self.name = "".join(n_list)
        # for possible error
        list_number = str(self.Dr_code).split("  ")
        for num in list_number:
            for doctor in doctor_list:
                if num in doctor:
                    break
            else:
                condition = False
                cond2 = False
                print(clr.Back.RED +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT +
                      f" Error: The doctor with this code {num} not found!" +
                      clr.Style.RESET_ALL +
                      "\n")
        try:
            int(self.serial)
            for num in list_number:
                int(num)
        except:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: your number of serial code or Dr code is wrong!" +
                  clr.Style.RESET_ALL +
                  "\n")
            condition = False
            cond2 = False
        if not (len(str(self.serial).strip()) == 10):
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: your serial code must be 10 character!" +
                  clr.Style.RESET_ALL +
                  "\n")
            condition = False
            cond2 = False
        if not (str(self.name).isalpha()):
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: Your name don't have number and special character!" +
                  clr.Style.RESET_ALL +
                  "\n")
            condition = False
            cond2 = False
        # optimize
        self.name = " ".join(n_list)
        # append patient to patient file
        if condition:
            patient_file.write("serial : " + str(self.serial).strip() +
                               ", name : " + self.name +
                               ", Dr code : " + str(self.Dr_code) + "\n")
            if not edit_mode:
                print(clr.Back.GREEN +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT +
                      " Patient Created!" +
                      clr.Style.RESET_ALL +
                      "\n")
            if edit_mode:
                return True
        elif cond2:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: Someone exist with your serial code!" +
                  clr.Style.RESET_ALL +
                  "\n")
            if edit_mode:
                return False
        patient_file.close()
        doctor_file.close()

    @staticmethod
    def remove_patient(serial, edit_mode):
        enter = False if serial == "" else True
        condition = True
        patient_file = open("Patients.txt", "r")
        patient_list = patient_file.readlines()
        patient_file.close()
        patient_file = open("Patients.txt", "w")
        for patient in patient_list:
            if serial in patient[9:20] and enter:
                if not edit_mode:
                    print(clr.Back.GREEN +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          " Patient Deleted!" +
                          clr.Style.RESET_ALL +
                          "\n")
                condition = False
                pass
            else:
                patient_file.write(patient)
        patient_file.close()
        if edit_mode and not condition:
            return True
        if condition:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: The patient with serial code not found!" +
                  clr.Style.RESET_ALL +
                  "\n")
            if edit_mode:
                return False

    @staticmethod
    def edit_info(serial):
        condition = Patient.remove_patient(serial, True)
        if condition:
            new_patient = Patient(serial,
                                  input(clr.Back.YELLOW +
                                        clr.Fore.BLACK +
                                        clr.Style.BRIGHT +
                                        " Please enter Patient's name : " +
                                        clr.Style.RESET_ALL +
                                        "\n"),
                                  input(clr.Back.YELLOW +
                                        clr.Fore.BLACK +
                                        clr.Style.BRIGHT +
                                        " Please enter Dr code : " +
                                        clr.Style.RESET_ALL +
                                        "\n"))
            condition2 = Patient.new_patient(new_patient, True)
            if condition2:
                print(clr.Back.GREEN +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT +
                      " Your info has been edited!" +
                      clr.Style.RESET_ALL +
                      "\n")
            elif not condition2:
                while not condition2:
                    new_patient2 = Patient(serial,
                                           input(clr.Back.YELLOW +
                                                 clr.Fore.BLACK +
                                                 clr.Style.BRIGHT +
                                                 " Please enter Patient's name : " +
                                                 clr.Style.RESET_ALL +
                                                 "\n"),
                                           input(clr.Back.YELLOW +
                                                 clr.Fore.BLACK +
                                                 clr.Style.BRIGHT +
                                                 " Please enter Dr code : " +
                                                 clr.Style.RESET_ALL +
                                                 "\n"))
                    condition2 = Patient.new_patient(new_patient2, True)
                else:
                    print(clr.Back.GREEN +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          " Your info has been edited!" +
                          clr.Style.RESET_ALL +
                          "\n")

    @staticmethod
    def show_patient_from_dr_code(Dr_code):
        condition = True
        patient_file = open("Patients.txt", "r")
        patient_list = patient_file.readlines()
        patient_list = sorted(patient_list)
        for patient in patient_list:
            dr_code_patient = patient.split(",")
            if Dr_code in dr_code_patient[2]:
                print(clr.Back.LIGHTBLACK_EX +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT + " " +
                      patient +
                      clr.Style.RESET_ALL +
                      "\n")
                condition = False
        patient_file.close()
        if condition:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " The patient with this doctor code not found!" +
                  clr.Style.RESET_ALL +
                  "\n")

    @staticmethod
    def show_all_patient():
        patient_file = open("Patients.txt", "r")
        patient_list = patient_file.readlines()
        name_list = []
        for patient in patient_list:
            patient = patient.split(", ")
            family = patient[1].split(" ")
            name_list.append(family[-1])
        name_list = set(name_list)
        name_list = list(name_list)
        name_list = sorted(name_list)
        for name in name_list:
            for patient in patient_list:
                if name in patient:
                    print(clr.Back.LIGHTBLACK_EX +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT + " " +
                          patient +
                          clr.Style.RESET_ALL +
                          "\n")
        patient_file.close()

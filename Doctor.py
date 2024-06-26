import colorama as clr


class Doctor:
    def __init__(self, code, name, phone_number, expertise):
        self.code = code
        self.name = name
        self.phone_number = phone_number
        self.expertise = expertise

    def new_doctor(self, edit_mode):
        condition = True
        cond2 = True
        doctor_file = open("Doctors.txt", "r")
        doctor_list = doctor_file.readlines()
        doctor_file.close()
        # check for unique code
        doctor_file = open("Doctors.txt", "a")
        patient_file = open("Patients.txt", "r")
        patient_list = patient_file.readlines()
        for patient in patient_list:
            for doctor in doctor_list:
                if self.code in patient and not edit_mode:
                    condition = False
                elif self.code in doctor:
                    condition = False
        # for capitalize expertise and name
        self.expertise = str(self.expertise).capitalize()
        expertise_list = ["Heart", "Eye", "Pediatric", "General"]
        list_name = str(self.name).split(" ")
        n_list = []
        for name in list_name:
            n_list.append(name.capitalize())
        self.name = "".join(n_list)
        # check possible error
        try:
            int(self.code)
            int(self.phone_number)
        except:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: Your code or phone number is wrong!" +
                  clr.Style.RESET_ALL +
                  "\n")
            condition = False
            cond2 = False
        if not (len(str(self.phone_number).strip()) == 9):
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: your phone number must be 11 character!" +
                  clr.Style.RESET_ALL +
                  "\n")
            condition = False
            cond2 = False
        if not (str(self.name).isalpha() and str(self.expertise).isalpha()):
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: your name and expertise don't have number and special characters!" +
                  clr.Style.RESET_ALL +
                  "\n")
            condition = False
            cond2 = False
        if not (self.expertise in expertise_list):
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: Your expertise must among Heart, Eye, Pediatric, General!" +
                  clr.Style.RESET_ALL +
                  "\n")
            condition = False
            cond2 = False
        # optimize
        self.name = " ".join(n_list)
        # append doctor to doctor file
        if condition:
            doctor_file.write("code : " + str(self.code).strip() +
                              ", name : " + self.name +
                              ", phone number : " + "09" + str(self.phone_number).strip() +
                              ", expertise : " + self.expertise + "\n")
            if not edit_mode:
                print(clr.Back.GREEN +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT +
                      " Doctor Created!" +
                      clr.Style.RESET_ALL +
                      "\n")
            if edit_mode:
                return True
        elif cond2:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: Someone exist with your code!" +
                  clr.Style.RESET_ALL +
                  "\n")
            if edit_mode:
                return False
        doctor_file.close()
        patient_file.close()

    @staticmethod
    def remove_doctor(code, edit_mode):
        enter = False if code == "" else True
        condition = False
        doctor_file = open("Doctors.txt", "r")
        doctor_list = doctor_file.readlines()
        doctor_file.close()
        doctor_file = open("Doctors.txt", "w")
        for doctor in doctor_list:
            dr_code = doctor.split(",")
            if code in dr_code[0] and enter:
                if not edit_mode:
                    print(clr.Back.GREEN +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          " Doctor deleted!" +
                          clr.Style.RESET_ALL +
                          "\n")
                condition = True
                pass
            else:
                doctor_file.write(doctor)
        doctor_file.close()
        if not condition:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Error: The doctor with this code not found!" +
                  clr.Style.RESET_ALL +
                  "\n")
            if edit_mode:
                return False
        elif condition:
            if not edit_mode:
                patient_file = open("Patients.txt", "r")
                patient_list = patient_file.readlines()
                patient_file.close()
                patient_file = open("Patients.txt", "w")
                for patient in patient_list:
                    if code in patient:
                        patient = patient.partition(code)
                        patient = list(patient)
                        patient.remove(code)
                        patient = " ".join(patient)
                        patient_file.write(patient)
                    else:
                        patient_file.write(patient)
                patient_file.close()
            if edit_mode:
                return True

    @staticmethod
    def edit_info(code):
        condition = Doctor.remove_doctor(code, True)
        if condition:
            new_doctor = Doctor(code,
                                input(clr.Back.YELLOW +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      " Please enter doctor's name : " +
                                      clr.Style.RESET_ALL +
                                      "\n"),
                                input(clr.Back.YELLOW +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      " Please enter doctor's phone number (must 11 numbers): " +
                                      clr.Style.RESET_ALL +
                                      clr.Fore.GREEN +
                                      "\n 09" +
                                      clr.Style.RESET_ALL),
                                input(clr.Back.YELLOW +
                                      clr.Fore.BLACK +
                                      clr.Style.BRIGHT +
                                      " Please enter your expertise (must among Heart, Eye, Pediatric and General): " +
                                      clr.Style.RESET_ALL +
                                      "\n"))
            condition2 = Doctor.new_doctor(new_doctor, True)
            if condition2:
                print(clr.Back.GREEN +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT +
                      " Your info has been edited!" +
                      clr.Style.RESET_ALL +
                      "\n")
            elif not condition2:
                while not condition2:
                    new_doctor2 = Doctor(code,
                                         input(clr.Back.YELLOW +
                                               clr.Fore.BLACK +
                                               clr.Style.BRIGHT +
                                               " Please enter doctor's name : " +
                                               clr.Style.RESET_ALL +
                                               "\n"),
                                         input(clr.Back.YELLOW +
                                               clr.Fore.BLACK +
                                               clr.Style.BRIGHT +
                                               " Please enter doctor's phone number : " +
                                               clr.Style.RESET_ALL +
                                               "\n 09"),
                                         input(clr.Back.YELLOW +
                                               clr.Fore.BLACK +
                                               clr.Style.BRIGHT +
                                               " Please enter your expertise : " +
                                               clr.Style.RESET_ALL +
                                               "\n"))
                    condition2 = Doctor.new_doctor(new_doctor2, True)
                else:
                    print(clr.Back.GREEN +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT +
                          " Your info has been edited!" +
                          clr.Style.RESET_ALL +
                          "\n")

    @staticmethod
    def search_doctor(code):
        condition = True
        doctor_file = open("Doctors.txt", "r")
        doctor_list = doctor_file.readlines()
        for doctor in doctor_list:
            dr_code = doctor.split(",")
            if code in dr_code[0]:
                print(clr.Back.LIGHTBLACK_EX +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT + " " +
                      doctor +
                      clr.Style.RESET_ALL +
                      "\n")
                condition = False
        doctor_file.close()
        if condition:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " The doctor with this code not found!" +
                  clr.Style.RESET_ALL +
                  "\n")

    @staticmethod
    def show_all_doctors():
        doctor_file = open("Doctors.txt", "r")
        doctor_list = doctor_file.readlines()
        name_list = []
        for doctor in doctor_list:
            doctor = doctor.split(", ")
            family = doctor[1].split(" ")
            name_list.append(family[-1])
        name_list = set(name_list)
        name_list = list(name_list)
        name_list = sorted(name_list)
        for name in name_list:
            for doctor in doctor_list:
                if name in doctor:
                    print(clr.Back.LIGHTBLACK_EX +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT + " " +
                          doctor +
                          clr.Style.RESET_ALL +
                          "\n")

    @staticmethod
    def show_doctor_list_by_expertise(expertise):
        condition = True
        expertise = str(expertise).capitalize()
        expertise_list = ["Heart", "Eye", "Pediatric", "General"]
        if expertise in expertise_list:
            doctor_file = open("Doctors.txt", "r")
            doctor_list = doctor_file.readlines()
            for doctor in doctor_list:
                expertise_doctor = doctor.split(",")
                if expertise in expertise_doctor[3]:
                    print(clr.Back.LIGHTBLACK_EX +
                          clr.Fore.LIGHTWHITE_EX +
                          clr.Style.BRIGHT + " " +
                          doctor +
                          clr.Style.RESET_ALL +
                          "\n")
                    condition = False
            doctor_file.close()
            if condition:
                print(clr.Back.RED +
                      clr.Fore.LIGHTWHITE_EX +
                      clr.Style.BRIGHT +
                      " Your wanted expertise not found!" +
                      clr.Style.RESET_ALL +
                      "\n")
        else:
            print(clr.Back.RED +
                  clr.Fore.LIGHTWHITE_EX +
                  clr.Style.BRIGHT +
                  " Your insert is wrong!" +
                  clr.Style.RESET_ALL +
                  "\n")

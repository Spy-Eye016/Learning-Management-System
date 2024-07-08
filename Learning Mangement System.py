def UserName():
    Name=input("Enter the Name: ")
    return Name
    # print(f"User Name is ------------>{User_Name}.")
def CNIC():
    while (True):
        try:
            CNIC_Number=input("Enter your CNIC without Dashes: ")
            assert (CNIC_Number.isdigit())
            try:
                assert(len(CNIC_Number)==13)
                return CNIC_Number
                # print(f"Your Phone Number is ----------->{int(CNIC_Number)}")
                break
            except Exception as msg:
                print("Phone Number must be of Eleven Characters !")
                continue
        except Exception as msg:
            print("Please, Enter your Phone Number in this format 12345678923 !")
            continue
def Email():
    while (True):
        Mail=input("Enter your E-Mail: ")
        if (len(Mail)<7):
            print("Please, Enter Email having at least 7 Characters !")
            continue
        else:
            if ("@" in Mail):
                if (Mail[0].isalpha()):
                    if ("." in Mail):
                        return (Mail.lower())
                        # print(f"Your E-Mail is ------------>{Mail.lower()}")
                        break
                    else:
                        print("Incorrect E-Mail !")
                        continue
                else:
                    print("Incorrect E-Mail, First Character of Email should be An Alphabet !")
                    continue
            else:
                print("Please, Enter the Correct E-Mail, @ is not present in E-Mail !")
                continue
def Password():
    import random
    while (True):
        Password=input("Do You want the Strong Password?(Y/N): ")
        if (Password.upper()=="Y"):
            Number=random.randint(8,20)
            Pin=""
            for i in range (Number):
                Pin+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?/|<>~")
            print(f"Your Strong Password is ------------>{Pin}")
            return Pin
            break
        elif(Password.upper()=="N"):
            Lock=input("Enter your password: ")
            if (len(Lock)<8):
                print("Please, Enter the Password having at least 8 Charaters !")
                continue
            else:
                return Lock
                # print(f"Your Password is ------------>{Lock}")
                break
        else:
            print("Please, Enter inly Y or N !")
            continue
def Country():
    Country="Pakistan"
    return Country
    # print(Country)
def PhoneNumber():
    while (True):
        try:
            Number=input("Enter your Phone Number without Dashes: ")
            assert (Number.isdigit())
            try:
                assert(len(Number)==11)
                return Number
                # print(f"Your Phone Number is ----------->{int(Number)}")
                break
            except Exception as msg:
                print("Phone Number must be of Eleven Characters !")
                continue
        except Exception as msg:
            print("Please, Enter your Phone Number in this format 12345678923 !")
            continue
def NumberFunc():
    while (True):
        try:
            Number=int(input("Enter the Number of Students: "))
            assert (type(Number)==int)
            try:
                assert (Number>0)
                return Number
                break
            except Exception as msg:
                print("Enter the Positive Number only !")
                continue
        except Exception as msg:
            print("Enter the Number not Strings !")
            continue
def StudentGrade():
    while (True):
        try:
            grade=input("Enter the Grade of Student: ")
            assert (len(grade)==1 or len(grade)==2)
            return (grade.title())
            break
        except Exception as msg:
            print("Enter only Alphabets !")
            continue
def CreditHours():
    while (True):
        try:
            Credit_Hours=int(input("Enter the Credit Hours: "))
            assert (type(Credit_Hours)==int)
            try:
                assert (Credit_Hours>0 and Credit_Hours<4)
                return (Credit_Hours)
                break
            except Exception as msg:
                print("Credit Hours must be between zero and 4 !")
                continue
        except Exception as msg:
            print("Please,Enter only Digits not Strings !")
            continue
def StudentGradePoints(X):
    while (True):
        if (X.title()=="A+"):
            return ("4.0")
        elif (X.title()=="A"):
            return ("4.0")
        elif (X.title()=="A-"):
            return ("3.7")
        elif (X.title()=="B+"):
            return ("3.3")
        elif (X.title()=="B"):
            return ("3.0")
        elif (X.title()=="B-"):
            return ("2.7")
        elif (X.title()=="C+"):
            return ("2.3")
        elif (X.title()=="C"):
            return ("2.0")
        elif (X.title()=="C-"):
            return ("1.7")
        elif (X.title()=="D+"):
            return ("1.3")
        elif (X.title()=="D"):
            return ("1.0")
        elif (X.title()=="F"):
            return ("0.7")       
def ChallanNumber():
    import random
    Challan_Number=""
    for i in range(15):
        Random_Number=random.randint(0,9)
        Challan_Number=Challan_Number+str(Random_Number)
    return Challan_Number
def Sem():
    while (True):
        try:
            Semester=int(input("Enter the Semester: "))
            assert (type(Semester)==int)
            return ("Semester "+str(Semester))
            break
        except Exception as msg:
            print("Enter the Digits only not Strings !")
            continue
def DueDate():
    print("Enter the Date like this formate xx/xx/xxxx !")
    while (True):
        try:
            Due_Date=input("Enter the Due Date: ")
            assert(len(Due_Date)==8  or len(Due_Date)==9  or len(Due_Date)==10)
            return (Due_Date)
            break
        except Exception as msg:
            print("Enter the Due Date according to above given format.")
            continue
def ClassRegistration():
    print("Enter the Registration Number Like This formate 2000ce.")
    while (True):
        try:
            RegNumber=input("Enter the Registration Number: ")
            assert (len(RegNumber)==6 or len(RegNumber)==7)
            try:
                assert (RegNumber[:4].isdigit())
                try:
                    assert (RegNumber[4:].isalpha())
                    return (RegNumber.lower())
                except Exception as msg:
                    print("There msut be Aplhebets at 5th and 6th Place !")
                    continue
            except Exception as msg:
                print("Enter the Registraion According to Given Formate !")
                continue
        except Exception as msg:
            print("Length of Registartion Number must be 6 or 7 !")
            continue
    
class ScholarshipClass:
    """ This Class is generated which takes some
      necessary Student Data for Any Schoalrship.
    """
    def ScholarName(self):
        while (True):
            self.Name=input("Enter the Student Name: ")
            if (" " in self.Name):
                self.Actual_Name=self.Name.split(" ")
                self.name=""
                Count=0
                for i in self.Actual_Name:
                    if (i.isalpha()):
                        self.name+=i
                        Count+=1
                        if (Count>0):
                            self.name+=" "
                return (self.name.title())
                break
            else:
                if (self.Name.isalpha()):
                    return (self.Name.capitalize())
                    break
                else:
                    print("Please, Enter Your Actual Name not Digits in Name !")
                    continue
    def ScholarCNIC(self):
        while (True):
            try:
                self.CNIC_Number=input("Enter your CNIC without Dashes: ")
                assert (self.CNIC_Number.isdigit())
                try:
                    assert(len(self.CNIC_Number)==13)
                    return (self.CNIC_Number)
                    # print(f"Your Phone Number is ----------->{int(CNIC_Number)}")
                    break
                except Exception as msg:
                    print("Phone Number must be of Thirteen Characters !")
                    continue
            except Exception as msg:
                print("Please, Enter your Phone Number in this format 12345678923 !")
                continue
    def ScholarFatherName(self):
        while (True):
            self.Name=input("Enter the Student's Father Name: ")
            if (" " in self.Name):
                self.Actual_Name=self.Name.split(" ")
                self.name=""
                Count=0
                for i in self.Actual_Name:
                    if (i.isalpha()):
                        self.name+=i
                        Count+=1
                        if (Count>0):
                            self.name+=" "
                return (self.name.title())
                break
            else:
                if (self.Name.isalpha()):
                    return (self.Name.capitalize())
                    break
                else:
                    print("Please, Enter Your Actual Name not Digits in Name !")
                    continue
    def ScholarFatherCNIC(self):
        while (True):
            try:
                self.CNIC_Number=input("Enter the Student's Father CNIC without Dashes: ")
                assert (self.CNIC_Number.isdigit())
                try:
                    assert(len(self.CNIC_Number)==13)
                    return (self.CNIC_Number)
                    # print(f"Your Phone Number is ----------->{int(CNIC_Number)}")
                    break
                except Exception as msg:
                    print("CNIC must be of Thirteen Characters !")
                    continue
            except Exception as msg:
                print("Please, Enter your Phone Number in this format 12345678923 !")
                continue
    def ScholarPhoneNumber(self):
        while (True):
            try:
                self.Number=input("Enter the Student Phone Number without Dashes: ")
                assert (self.Number.isdigit())
                try:
                    assert(len(self.Number)==11)
                    return (self.Number)
                    # print(f"Your Phone Number is ----------->{int(Number)}")
                    break
                except Exception as msg:
                    print("Phone Number must be of Eleven Characters !")
                    continue
            except Exception as msg:
                print("Please, Enter your Phone Number in this format 12345678923 !")
                continue
    def ScholarFatherPhoneNumber(self):
        while (True):
            try:
                self.Number=input("Enter the Student's Father Phone Number without Dashes: ")
                assert (self.Number.isdigit())
                try:
                    assert(len(self.Number)==11)
                    return (self.Number)
                    # print(f"Your Phone Number is ----------->{int(Number)}")
                    break
                except Exception as msg:
                    print("CNIC must be of Thirteen Characters !")
                    continue
            except Exception as msg:
                print("Please, Enter your Phone Number in this format 12345678923 !")
                continue
    def FamilyMembers(self):
        while (True):
            try:
                self.Members=int(input("How many Family Members are you?: "))
                assert (type(self.Members)==int)
                try:
                    assert(0<(self.Members)<30)
                    return (self.Members)
                    break
                except Exception as msg:
                    print("Family Members must be greater than zero and less than 30 !")
                    continue
            except Exception as msg:
                print("Please, Enter the Number of Your Family Members !")
                continue
    def FatherSalary(self):
        while (True):
            try:
                self.FatherSalary=int(input("Enter your Father Salary: "))
                assert (type(self.FatherSalary)==int)
                try:
                    assert(0<self.FatherSalary)
                    try:
                        assert (self.FatherSalary<60000)
                        return (self.FatherSalary)
                        break
                    except Exception as msg:
                        return "You are not Eligible for Scholarship."
                        break
                except Exception as msg:
                    print ("Do not Enter Negative Numbers.")
                    continue
            except Exception as msg:
                print("Enter the Salary in Digits not including Strings !")
                continue
    def GuardianSalary(self):
        while (True):
            try:
                self.GuardianSalary=int(input("Enter your Guardian Salary: "))
                assert (type(self.GuardianSalary)==int)
                try:
                    assert(0<self.GuardianSalary)
                    try:
                        assert (self.GuardianSalary<60000)
                        return (self.GuardianSalary)
                        break
                    except Exception as msg:
                        return "You are not Eligible for Scholarship."
                        break
                except Exception as msg:
                    print ("Do not Enter Negative Numbers.")
                    continue
            except Exception as msg:
                print("Enter the Salary in Digits not including Strings !")
                continue
    def Province(self):
        print("For khaber Pakhtunkhwa enter only kp.")
        while (True):
            try:
                self.ProvinceName=input("Enter the Province: ")
                assert (self.ProvinceName.isalpha())
                try:
                    assert (((self.ProvinceName).capitalize())=="Punjab" or (self.ProvinceName.capitalize())=="Sindh" or (self.ProvinceName.capitalize())=="Balochistan" or (self.ProvinceName.capitalize())=="Kp")
                    return (self.ProvinceName.capitalize())
                    break
                except Exception as msg:
                    print("Enter the Name of Provinces !")
                    continue
            except Exception as msg:
                print("Enter, only Strings not Alphabets !")
                continue
        pass
    def District(self):
        while (True):
            self.DistrictName=input("Enter the District: ")
            if (" " in self.DistrictName):
                self.Actual_District_Name=self.DistrictName.split(" ")
                self.Disrictname=""
                Count=0
                for i in self.Actual_District_Name:
                    if (i.isalpha()):
                        self.Disrictname+=i
                        Count+=1
                        if (Count>0):
                            self.Disrictname+=" "
                return (self.Disrictname.title())
                break
            else:
                if (self.DistrictName.isalpha()):
                    return (self.DistrictName.capitalize())
                    break
                else:
                    print("Please, Enter Your Actual Name not Digits in Name !")
                    continue
    def City(self):
        while (True):
            self.CityName=input("Enter the City Name: ")
            if (" " in self.CityName):
                self.Actual_City_Name=self.CityName.split(" ")
                self.Cityname=""
                Count=0
                for i in self.Actual_City_Name:
                    if (i.isalpha()):
                        self.Cityname+=i
                        Count+=1
                        if (Count>0):
                            self.Cityname+=" "
                return (self.Cityname.title())
                break
            else:
                if (self.CityName.isalpha()):
                    return (self.CityName.capitalize())
                    break
                else:
                    print("Please, Enter Your Actual Name not Digits in Name !")
                    continue
    def Transport(self):
        while (True):
            try:
                self.Vehicle=input("Do you have any Vehicle?(Y/N): ")
                assert(self.Vehicle.isalpha())
                try:
                    assert (self.Vehicle.upper()=="Y" or "N")
                    if (self.Vehicle.upper()=="Y"):
                        try:
                            self.Trans=input("Which you have,Motorbike(M) or Car(C): ")
                            assert  (self.Trans.upper()=="M"or "C")
                            if (self.Trans.upper()=="M"):
                                BikeModel=input("Enter the bike Model: ")
                                return ("Bike "+BikeModel)
                            elif (self.Trans.upper()=="C"):
                                CarModel=input("Enter the Car Model: ")
                                return ("Car "+CarModel)    
                        except Exception as Message:
                            print("Please, Enter only M or C !")
                            continue
                    elif (self.Vehicle.upper()=="N"):
                        return "User Has no Transport !"
                        break
                except Exception as Link:
                    print("Enter only Y or N !")
                    continue
            except Exception as msg:
                print("Please, Enter only Alphabets !")
                continue
    def MatricMarks(self):
        while (True):
            try:
                self.Matric_Marks=input("Enter the obtained Marks of Matric: ")
                assert (self.Matric_Marks.isdigit())
                try:
                    assert (len(self.Matric_Marks)==4)
                    try:
                        assert(int(self.Matric_Marks)>0)
                        try:
                            assert(int(self.Matric_Marks)<1100)
                            return (int(self.Matric_Marks))
                            break
                        except Exception as msg:
                            print("Obtained Marks should be less than 1100 !")
                            continue
                    except Exception as msg:
                        print("Number must be Positive !")
                        continue
                except Exception as msg:
                    print("Marks should be of 4 digits !")
                    continue
            except Exception as msg:
                print("Please, Enter the Marks that must be digits not Strings !")
                continue
    def TotalMatricMarks(self):
        while (True):
            try:
                self.Total_Matric_Marks=input("Enter the Total Marks of Matric: ")
                assert (self.Total_Matric_Marks.isdigit())
                try:
                    assert (len(self.Total_Matric_Marks)==4)
                    try:
                        assert(int(self.Total_Matric_Marks)>0)
                        try:
                            assert(int(self.Total_Matric_Marks)==1100)
                            return (int(self.Total_Matric_Marks))
                            break
                        except Exception as msg:
                            print("Obtained Marks should be equal to 1100 !")
                            continue
                    except Exception as msg:
                        print("Number must be Positive !")
                        continue
                except Exception as msg:
                    print("Marks should be of 4 digits !")
                    continue
            except Exception as msg:
                print("Please, Enter the Marks that must be digits not Strings !")
                continue
    def InterMarks(self):
        while (True):
            try:
                self.Inter_Marks=input("Enter the obtained Marks of Intermediate: ")
                assert (self.Inter_Marks.isdigit())
                try:
                    assert (len(self.Inter_Marks)==4)
                    try:
                        assert(int(self.Inter_Marks)>0)
                        try:
                            assert(int(self.Inter_Marks)<1100)
                            return (int(self.Inter_Marks))
                            break
                        except Exception as msg:
                            print("Obtained Marks should be less than 1100 !")
                            continue
                    except Exception as msg:
                        print("Number must be Positive !")
                        continue
                except Exception as msg:
                    print("Marks should be of 4 digits !")
                    continue
            except Exception as msg:
                print("Please, Enter the Marks that must be digits not Strings !")
                continue
    def TotalInterMarks(self):
        while (True):
            try:
                self.Total_Inter_Marks=input("Enter the Total Marks of Intermediate: ")
                assert (self.Total_Inter_Marks.isdigit())
                try:
                    assert (len(self.Total_Inter_Marks)==4)
                    try:
                        assert(int(self.Total_Inter_Marks)>0)
                        try:
                            assert(int(self.Total_Inter_Marks)==1100)
                            return (int(self.Total_Inter_Marks))
                            break
                        except Exception as msg:
                            print("Obtained Marks should be equal to 1100 !")
                            continue
                    except Exception as msg:
                        print("Number must be Positive !")
                        continue
                except Exception as msg:
                    print("Marks should be of 4 digits !")
                    continue
            except Exception as msg:
                print("Please, Enter the Marks that must be digits not Strings !")
                continue
    def PayRent(self):
        while (True):
            try:
                Rent=input("Enter the Rent Of Your House: ")
                assert (Rent.isdigit())
                try:
                    assert (Rent>=0)
                    return Rent
                    break
                except Exception as msg:
                    print("Rent Money Must be Positive !")
                    continue
            except Exception as msg:
                print("Please, Enter the Money in digits not Strings !")
                continue
    def HarvestLand(self):
        while (True):
            try:
                Harvest_Land=input("Enter the Total Land: ")
                assert (Harvest_Land.isdigit())
                try:
                    assert (Harvest_Land>=0)
                    return (Harvest_Land)
                    break
                except Exception as msg:
                    print("Must be Positive !")
                    continue
            except Exception as msg:
                print("Do not involve Strings in Land !")
                continue
    def HouseLand(self):
        while (True):
            try:
                House_Land=input("Enter the Total Land: ")
                assert (House_Land.isdigit())
                try:
                    assert (House_Land>=0)
                    return (House_Land)
                    break
                except Exception as msg:
                    print("Must be Positive !")
                    continue
            except Exception as msg:
                print("Do not involve Strings in Land !")
                continue
    def DOB(self):
        print("Enter the Date of Birth like this formate xx/xx/xxxx !")
        while (True):
            try:
                self.DateofBirth=input("Enter the Date of Birth: ")
                assert(len(self.DateofBirth)==8 or len(self.DateofBirth)==9 or len(self.DateofBirth)==10)
                return (self.DateofBirth)
                break
            except Exception as msg:
                print("Enter the Date of Borth according to above given format.")
                continue
    def RegistrationNumber(self):
        print("Enter the Registration Number Like This formate 2000ce39.")
        while (True):
            try:
                self.RegNumber=input("Enter the Registration Number: ")
                assert (len(self.RegNumber)==7 or len(self.RegNumber)==8)
                try:
                    assert (self.RegNumber[:4].isdigit())
                    try:
                        assert (self.RegNumber[4:6].isalpha())
                        try:
                            assert (self.RegNumber[6:].isdigit())
                            return (self.RegNumber.lower())
                            break
                        except Exception as msg:
                            print ("Enter the Roll Number means digits at Last Places !")
                            continue
                    except Exception as msg:
                        print("There msut be Aplhebets at 5th and 6th Place !")
                        continue
                except Exception as msg:
                    print("Enter the Registraion According to Given Formate !")
                    continue
            except Exception as msg:
                print("Length of Registartion Number must be 7 or 8 !")
                continue
       
class RegistrationClass(ScholarshipClass):
    """ This Class is helpful in Registration 
        of Studenst and takes some necessary details 
        that can be helpful in Registration.This
        Class is inherited from Scholarship Class.
    """
    def Category(self):
        self.AdmissionCategory=input("Enter the Admission Category: ")
        return (self.AdmissionCategory.upper())
    def Department(self):
        while (True):
            self.DepartmentName=input("Enter the Department: ")
            if (" " in self.DepartmentName):
                self.Actual_Department_Name=self.DepartmentName.split(" ")
                self.Departmentname=""
                Count=0
                for i in self.Actual_Department_Name:
                    if (i.isalpha()):
                        self.Departmentname+=i
                        Count+=1
                        if (Count>0):
                            self.Departmentname+=" "
                return (self.Departmentname.title())
                break
            else:
                if (self.DepartmentName.isalpha()):
                    return (self.DepartmentName.capitalize())
                    break
                else:
                    print("Please, Enter Your Actual Name not Digits in Name !")
                    continue
    def Degree(self):
        while (True):
            self.DegreeName=input("Enter the Degree: ")
            if (" " in self.DegreeName):
                self.Actual_Degree_Name=self.DegreeName.split(" ")
                self.Degreename=""
                Count=0
                for i in self.Actual_Degree_Name:
                    if (i.isalpha()):
                        self.Degreename+=i
                        Count+=1
                        if (Count>0):
                            self.Degreename+=" "
                return (self.Degreename.title())
                break
            else:
                if (self.DegreeName.isalpha()):
                    return (self.DegreeName.capitalize())
                    break
                else:
                    print("Please, Enter Your Actual Name not Digits in Name !")
                    continue
    def UniversityMail(self):
        while (True):
            self.Mail=input("Enter the Student's University E-Mail: ")
            if (len(self.Mail)<7):
                print("Please, Enter Email having at least 7 Characters !")
                continue
            else:
                if ("@" in self.Mail):
                        if ("." in (self.Mail)):
                            return (self.Mail.lower())
                            # print(f"Your E-Mail is ------------>{Mail.lower()}")
                            break
                        else:
                            print("Incorrect E-Mail !")
                            continue
                else:
                    print("Please, Enter the Correct E-Mail, @ is not present in E-Mail !")
                    continue
    def Campus(self):
        self.CampusName=input("Enter the Campus Name: ")
        return (self.CampusName.title())
    def Status(self):
        print("1.Day Scholar\n2.Hostellite")
        while (True):
            try:
                self.UserStatus=input("Enter the Status: ")
                assert ((self.UserStatus).isdigit())
                try:
                    assert ((self.UserStatus)=="1" or (self.UserStatus)=="2")
                    if ((self.UserStatus)=="1"):
                        return ("Day Scholar")
                        break
                    elif ((self.UserStatus)=="2"):
                        return ("Hostellite")
                        break
                except Exception as msg:
                    print("Enter only 1 or 2 !")
                    continue
            except Exception as msg:
                print("Enter only Digits !")
                continue
    def Aggregate(self):
        while (True):
            try:
                Number=float(input("Enter the Aggregate of Student: "))
                assert (type(Number)==float)
                try:
                    assert (Number>0 and Number<100)
                    return Number
                    break
                except Exception as msg:
                    print("Enter the Positive Number only !")
                    continue
            except Exception as msg:
                print("Enter the Number not Strings !")
                continue
                    
class ChallanClass(RegistrationClass):
    """ This Class will used in generating Challans
        of Students.It is inherited from Registration Class."""
    def TutionFee(self):
        while (True):
            try:
                self.Tution_Fee=float(input("Enter the Tution Fee: "))
                assert (type(self.Tution_Fee)==float)
                return (self.Tution_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def FacilitiesFee(self):
        while (True):
            try:
                self.Facilities_Fee=float(input("Enter the Facilities Fee: "))
                assert (type(self.Facilities_Fee)==float)
                return (self.Facilities_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def SportsFee(self):
        while (True):
            try:
                self.Sports_Fee=float(input("Enter the Sports Fee: "))
                assert (type(self.Sports_Fee)==float)
                return (self.Sports_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def MagazineFee(self):
        while (True):
            try:
                self.Magazine_Fee=float(input("Enter the Magazine Fee: "))
                assert (type(self.Magazine_Fee)==float)
                return (self.Magazine_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def InternetCharges(self):
        while (True):
            try:
                self.Internet_Charges=float(input("Enter the Internet Charges: "))
                assert (type(self.Internet_Charges)==float)
                return (self.Internet_Charges)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def ExaminationFee(self):
        while (True):
            try:
                self.Examination_Fee=float(input("Enter the Examination Fee: "))
                assert (type(self.Examination_Fee)==float)
                return (self.Examination_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def LabFee(self):
        while (True):
            try:
                self.Lab_Fee=float(input("Enter the Lab Fee: "))
                assert (type(self.Lab_Fee)==float)
                return (self.Lab_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def MedicalFee(self):
        while (True):
            try:
                self.Medical_Fee=float(input("Enter the Medical Fee: "))
                assert (type(self.Medical_Fee)==float)
                return (self.Medical_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def TutorialFee(self):
        while (True):
            try:
                self.Tutorial_Fee=float(input("Enter the Tutorial Fee: "))
                assert (type(self.Tutorial_Fee)==float)
                return (self.Tutorial_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def InterUniFee(self):
        while (True):
            try:
                self.Inter_Uni_Fee=float(input("Enter the Inter Uni Fee: "))
                assert (type(self.Inter_Uni_Fee)==float)
                return (self.Inter_Uni_Fee)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue

class HostelChallan(ChallanClass):
    """This Class will used in generating Hostel Challans
        of Students.It is inherited from Challan Class.
    """
    def RoomRent(self):
        while (True):
            try:
                self.Room_Rent=float(input("Enter the Room rent: "))
                assert (type(self.Room_Rent)==float)
                return (self.Room_Rent)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def GasBill(self):
        while (True):
            try:
                self.Gas_Bill=float(input("Enter the Gas Bill: "))
                assert (type(self.Gas_Bill)==float)
                return (self.Gas_Bill)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def FanBill(self):
        while (True):
            try:
                self.Fan_Bill=float(input("Enter the Fan Bill: "))
                assert (type(self.Fan_Bill)==float)
                return (self.Fan_Bill)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue
    def ElectricityBill(self):
        while (True):
            try:
                self.Electricity_Bill=float(input("Enter the Electricity Bill: "))
                assert (type(self.Electricity_Bill)==float)
                return (self.Electricity_Bill)
                break
            except Exception as msg:
                print("Enter only Digits mean integers not Strings !")
                continue

import os,time,pyfiglet,datetime,msvcrt,pyttsx3
from tkinter import *
print("\nPress any key to Start....")
msvcrt.getch()
os.system("cls")
Text1="<-----  Welocme to LMS  ----->"
Text2="<-{ Admin Mode }->"
Text3="<-{ User Mode }->"
Text4="~~(  Thanks for Visiting Here  )~~"
Text5="~~( Ok, Thanks ! )~~"
Big_Text1=pyfiglet.figlet_format(Text1,font="Big")
Big_Text2=pyfiglet.figlet_format(Text2,font="Small")
Big_Text3=pyfiglet.figlet_format(Text3,font="Small")
Big_Text4=pyfiglet.figlet_format(Text4,font="Small")
Big_Text5=pyfiglet.figlet_format(Text5,font="Small")
time.sleep(2)
print(Big_Text1)
Date=datetime.datetime.now()
Date1=Date.strftime("%d-%m-%Y")
Time=Date.strftime("%H-%M-%S")
while (True):
    try:
        time.sleep(2)
        print("\n|1| For Admin Mode\n|2| For User Mode\n|3| For Exit\n")
        Choice=input("Enter Your Choice: ")
        os.system("cls")
        assert (Choice.isdigit())
        try:
            assert (Choice=="1" or  Choice=="2" or Choice=="3")
            if (Choice=="1"):   # Admin Mode
                while (True):
                    try: 
                        print("\n")
                        print(Big_Text2)
                        time.sleep(2)
                        print("\n1.Register The Students\n2.Result\n3.Attendance\n4.Offered Courses\n5.Scholarships\n6.Generate Challan\n7.Exit\n")
                        Option=input("Choose your Option: ")
                        os.system("cls")
                        assert (Option.isdigit())
                        if (Option=="1"):   # Here is Code for the Registration of Students
                            Number=NumberFunc()
                            for i in range(Number):
                                StudentName=UserName()
                                Directory="c:/Users/Admin/Desktop"
                                File_Name=f"{StudentName.title()}_Registration.txt"
                                if File_Name in os.listdir(Directory):
                                    print(f"\nThis {StudentName.title()} file already exists.\n")
                                    continue
                                else:
                                    StudentRegistration=RegistrationClass()
                                    StudentCNIC=StudentRegistration.ScholarCNIC()
                                    StudentFatherName=StudentRegistration.ScholarFatherName()
                                    StudentFatherCNIC=StudentRegistration.ScholarFatherCNIC()
                                    StudentDOB=StudentRegistration.DOB()
                                    StudentNumber=StudentRegistration.ScholarPhoneNumber()
                                    StudentFatherNumber=StudentRegistration.ScholarFatherPhoneNumber()
                                    StudentCategory=StudentRegistration.Category()
                                    StudentDepartment=StudentRegistration.Department()
                                    StudentDegree=StudentRegistration.Degree()
                                    StudentAggregate=StudentRegistration.Aggregate()
                                    StudentStatus=StudentRegistration.Status()
                                    StudentCampus=StudentRegistration.Campus()
                                    StudentRegistrationNumber=StudentRegistration.RegistrationNumber()
                                    StudentUniversityEmail=StudentRegistration.UniversityMail()
                                    StudentCity=StudentRegistration.City()
                                    StudentDistrict=StudentRegistration.District()
                                    StudentProvince=StudentRegistration.Province()
                                    StudentMail=Email()
                                    f=open(f"{StudentName.title()}_Registration.txt","a")
                                    f.write("Name: "+StudentName+"\n"+"Student CNIC: "+StudentCNIC+"\n"+"Date Of Birth: "+StudentDOB+"\n"+"Father Name: "+StudentFatherName+"\n"+"Father CNIC: "+StudentFatherCNIC+"\n"+"Contact 1: "+StudentNumber+"\n"+"Contact 2: "+StudentFatherNumber+"\n"+"Aggregate: "+str(StudentAggregate)+"\n"+"Category: "+StudentCategory+"\n"+"Registration Number: "+StudentRegistrationNumber+"\n"+"Degree: "+StudentDegree+"\n"+"Department: "+StudentDepartment+"\n"+"Campus: "+StudentCampus+"\n"+"Status: "+StudentStatus+"\n"+"University Mail: "+StudentUniversityEmail+"\n"+"Student Mail: "+StudentMail+"\n"+"City: "+StudentCity+"\n"+"District: "+StudentDistrict+"\n"+"Province: "+StudentProvince+"\n")
                                    f.close()
                                    # print(f"{Name.title()} is successfully registered.")
                        elif (Option=="2"):    # Here is the Code for DMC
                            Number2=NumberFunc()
                            for i in range(Number2):
                                Name1=UserName()
                                Directory="c:/Users/Admin/Desktop"
                                File_Name=f"{Name1.title()}_Result.txt"
                                if (File_Name) in os.listdir(Directory):
                                    print(f"\nThis {Name1.title()} file is already present.\n")
                                    continue
                                else:
                                    Fazul=RegistrationClass()
                                    Roll_Number=Fazul.RegistrationNumber()
                                    Credit_Hours=CreditHours()
                                    Course_Code=input("Enter the Course Code: ")
                                    Grade=StudentGrade()
                                    GPA=StudentGradePoints(Grade)
                                    GPA=float(GPA)
                                    Grade_Points=(Credit_Hours*GPA)
                                    f=open(f"{Name1.title()}_Result.txt","a")
                                    f.write("Name: "+Name1+"\n"+"Reg No: "+str(Roll_Number)+"\n"+"Course Code: "+Course_Code.upper()+"\n"+"Credit Hours: "+str(Credit_Hours)+"\n"+"Grade Points: "+str(Grade_Points)+"\n"+"GPA: "+str(GPA)+"\n")
                                    f.close()
                                    print(f"\n{Name1.title()} result is ready.\n")
                        elif (Option=="3"):     # Here is the code for Attendance
                            while (True):
                                try:
                                    Number5=int(input("Enter the Strength of Class: "))
                                    assert (type(Number5)==int)
                                    ClassCode=ClassRegistration()
                                    for i in range (Number5):
                                        Attendance=input(f"{ClassCode}{i+1} is present or not?(Y/N): ")
                                        if (Attendance.upper()=="Y"):
                                            with open(f"Attendance{Date1}.txt","a") as f:
                                                f.write("Date: "+Date1+"\n"+"Time: "+Time+"\n"+f"{ClassCode}{i+1}"+"\t"+"P"+"\n")
                                        else:
                                            with open(f"Attendance{Date1}.txt","a") as f:
                                                f.write("Date: "+Date1+"\n"+"Time: "+Time+"\n"+f"{ClassCode}{i+1}"+"\t"+"A"+"\n")
                                    break
                                except Exception as msg:
                                    print("\nEnter only Number not Strings !\n")
                                    continue
                        elif (Option=="4"):    # Here is the Code for Offered Subjects
                            while (True):
                                try:
                                    Number1=int(input("Enter the Number of Offered Subjects: "))
                                    assert (type(Number1)==int)
                                    for i in range (Number1):
                                        Offered_Subjects=input("Enter the Offered Subjects: ")
                                        with open("Offered Subjects.txt","a") as f:
                                            f.write(Offered_Subjects.upper()+"\n")
                                    break        
                                except Exception as msg:
                                    print("\nEnter only Digits not Strings !\n")
                                    continue
                        elif (Option=="5"):     # Here is the Code for Scholarship Form
                            while (True):
                                try:
                                    Scholarship=input("Is any ScholarShip is avialable?(Y/N): ")
                                    assert (Scholarship.upper()=="Y" or Scholarship.upper()=="N")
                                    if (Scholarship.upper()=="Y"):
                                        with open (f"Scholarship.txt","a") as f:
                                            f.write(Scholarship.title())
                                        while (True):
                                            try:
                                                Need_Base=input("Is Need base Scholarship available?(Y/N): ")
                                                assert (Need_Base.upper()=="Y" or Need_Base.upper()=="N")
                                                if (Need_Base.upper()=="Y"):
                                                    with open (f"Need_Base.txt","a") as f:
                                                        f.write(Need_Base.title())
                                                        break
                                                else:
                                                    print("Ok, Thanks !")
                                                    break
                                            except Exception as msg:
                                                print("Enter only 'Y' or 'N' !")
                                                continue
                                        while (True):
                                            try:
                                                Merit_Base=input("Is Merit base Scholarship available?(Y/N): ")
                                                assert (Merit_Base.upper()=="Y" or Merit_Base.upper()=="N")
                                                if (Merit_Base.upper()=="Y"):
                                                    with open (f"Merit_Base.txt","a") as f:
                                                        f.write(Merit_Base.title())
                                                        break
                                                else:
                                                    print("Ok, Thanks !")
                                                    break
                                            except Exception as msg:
                                                print("\nEnter only 'Y' or 'N' !\n")
                                                continue
                                        break
                                    else:
                                        print("\nOk, Thanks !\n")
                                        break
                                except Exception as msg:
                                    print("\nEnter only 'Y' or 'N' !\n")
                                    continue
                        elif (Option=="6"):     # Here is the Code for Generating Challan
                            Number3=NumberFunc()
                            for i in range (Number3):
                                Name2=UserName()
                                Directory="c:/Users/Admin/Desktop"
                                File_Name=f"{Name2.title()}_Challan.txt"
                                if (File_Name) in os.listdir(Directory):
                                    print(f"\nA Challan of {Name2.title()} Name is already present.\n")
                                    continue
                                else:
                                    University=" Univeristy of Engineering and Technology, Lahore "
                                    Semester=Sem()
                                    Due_Date=DueDate()
                                    Nan=RegistrationClass()
                                    RollNumber=Nan.RegistrationNumber()
                                    Challan_Number=ChallanNumber()
                                    StudentChallan=ChallanClass()
                                    Tution_Fee=StudentChallan.TutionFee()
                                    Facilities_Fee=StudentChallan.FacilitiesFee()
                                    Sports_Fee=StudentChallan.SportsFee()
                                    Magazine_Fee=StudentChallan.MagazineFee()
                                    Internet_Fee=StudentChallan.InternetCharges()
                                    Exam_Fee=StudentChallan.ExaminationFee()
                                    Lab_Fee=StudentChallan.LabFee()
                                    Medical_Fee=StudentChallan.MedicalFee()
                                    Tutorial_Fee=StudentChallan.TutorialFee()
                                    Inter_Uni_Fee=StudentChallan.InterUniFee()
                                    Total_Amount=(Tution_Fee+Facilities_Fee+Sports_Fee+Magazine_Fee+Internet_Fee+Exam_Fee+Lab_Fee+Medical_Fee+Tutorial_Fee+Inter_Uni_Fee)
                                    f=open(f"{Name2.title()}_Challan.txt","a")
                                    f.write(University+"\n"+"Semester: "+Semester+"\n"+"Challan Number: "+Challan_Number+"\n"+"Due Date: "+Due_Date+"\n"+"Reg No: "+str(RollNumber)+"\n"+"Name: "+Name2+"\n"+"Tutorial Fee: "+str(Tutorial_Fee)+"\n"+"Inter Uni Fee: "+str(Inter_Uni_Fee)+"\n"+"Magazine Fee: "+str(Magazine_Fee)+"\n"+"Medical Fee: "+str(Medical_Fee)+"\n"+"Tution Fee: "+str(Tution_Fee)+"\n"+"Lab Fee: "+str(Lab_Fee)+"\n"+"Examination Fee: "+str(Exam_Fee)+"\n"+"Sports Fee: "+str(Sports_Fee)+"\n"+"Internet Charges: "+str(Internet_Fee)+"\n"+"Facilities Fee: "+str(Facilities_Fee)+"\n"+"\n"+"Total Amount: "+str(Total_Amount)+"\n")
                                    f.close()
                                    print(f"\n{Name2.title()} Fee Challan is Genrated.\n")
                                    while (True):
                                        try:
                                            Status=input(f"Is {Name2} hostelite?(Y/N): ")
                                            assert ((Status.upper()=="Y") or (Status.upper()=="N"))
                                            if (Status.upper()=="Y"):
                                                Challan_NO=ChallanNumber()
                                                Hostelite=HostelChallan()
                                                Room_Rent=Hostelite.RoomRent()
                                                Gas_Bill=Hostelite.GasBill()
                                                Fan_Bill=Hostelite.FanBill()
                                                Electricity_Bill=Hostelite.ElectricityBill()
                                                Total_Hostel_Amount=(Room_Rent+Gas_Bill+Fan_Bill+Electricity_Bill)
                                                f=open(f"{Name2.title()}_Hostel_Challan.txt","a")
                                                f.write(University+"\n"+"Semester: "+Semester+"\n"+"Challan Number: "+Challan_Number+"\n"+"Due Date: "+Due_Date+"\n"+"Reg No: "+str(RollNumber)+"\n"+"Name: "+Name2+"\n"+"Room Rent: "+str(Room_Rent)+"\n"+"Gas Bill: "+str(Gas_Bill)+"\n"+"Fan Bill: "+str(Fan_Bill)+"\n"+"Electricity Bill: "+str(Electricity_Bill)+"\n"+"\n"+"Total Amount: "+str(Total_Hostel_Amount)+"\n")
                                                f.close()
                                                print(f"\n{Name2.title()} Hostel Challan is generated.\n")
                                                break
                                            else:
                                                print("\nOk, Thanks !\n")
                                                break
                                        except Exception as msg:
                                            print("\nEnter only 'Y' or 'N' !\n")
                                            continue
                        elif (Option=="7"):     # Here is the code for Exit
                            break
                        else:
                            print("\nEnter the Digits from 1 to 7!\n")
                            continue
                    except Exception as msg:
                        print("Please, Enter only Digits !")
                        continue
            elif (Choice=="2"):  # User Mode
                print("\n")
                print(Big_Text3)
                print("\nFirst Sign up then go for Login.")
                while (True):
                    Desicion=input(f"Sign Up(s) or login(l) or exit(e): ")
                    os.system("cls")
                    if (Desicion.lower()=="s"):     # Here is the code for sign up
                        time.sleep(2)
                        User_Name=UserName()
                        Directory="c:/Users/Admin/Desktop"
                        File_Name=f"{User_Name}.txt"
                        File_Path=os.path.join(Directory,File_Name)
                        if os.path.exists(File_Path):
                            print(f"A File of {User_Name} is already exist.")
                            continue
                        else:
                            User_CNIC=CNIC()
                            E_Mail=Email()
                            Pin=Password()
                            country=Country()
                            Phone_Number=PhoneNumber()  
                            f=open(f"{User_Name}.txt","a")
                            f.write("Name:"+User_Name+"\n"+"CNIC:"+User_CNIC+"\n"+"E-Mail:"+E_Mail+"\n"+"Password:"+Pin+"\n"+"Country:"+country+"\n"+"Phone Number: "+Phone_Number+"\n")
                            f.close()
                            time.sleep(2)
                            os.system("cls")
                            print("You are Successfully Signed Up.")
                            continue
                    elif (Desicion.lower()=="l"):       # Here is the codde for log in
                        time.sleep(2)
                        Name=input("Ente your Name: ")
                        Directory="c:/Users/Admin/Desktop"
                        File_Name=f"{Name}.txt"
                        File_Path=os.path.join(Directory,File_Name)
                        if os.path.exists(File_Path):
                            Mail=Email()
                            Locked=input("Enter your Password: ")
                            with open (f"{Name}.txt","r") as f:
                                Content=f.read()
                            if ((Mail in Content) and (Locked in Content)):
                                print("\nYou are successfully logged in.\n")
                                while (True):
                                    try:
                                        time.sleep(2)
                                        print("\n1.Student Profile\n2.Current Courses\n3.Result\n4.Attendence\n5.Challan\n6.Hostel Comment\n7.Scholarship\n8.Exit\n")
                                        User_Option=input("Enter your Choice: ")
                                        os.system("cls")
                                        assert (User_Option.isdigit())
                                        if (User_Option=="1"):      # Here is the Code to Show Student Profile
                                            Directory="c:/Users/Admin/Desktop"
                                            File_Name=f"{Name.title()}_Registration.txt"
                                            if (File_Name) in os.listdir(Directory):
                                                with open(f"{Name.title()}_Registration.txt","r") as f:
                                                    Content=f.read()
                                                time.sleep(1)
                                                print("\n\n"+Content+"\n\n")
                                            else:
                                                print("\nNo Record Found !\n")
                                        elif (User_Option=="2"):        # Here is the Code to Register Courses
                                            while (True):
                                                try:
                                                    Number4=int(input("Enter the Number of Courses: "))
                                                    assert (type(Number4)==int)
                                                    for i in range(Number4):
                                                        Course_Name=input("Enter the Course Code: ")
                                                        Directory="c:/Users/Admin/Desktop"
                                                        File_Name=f"Offered Subjects.txt"
                                                        if (File_Name) in os.listdir(Directory):
                                                            with open("Offered Subjects.txt","r") as f:
                                                                Subject_Content=f.read()
                                                            if (Course_Name.upper() in Subject_Content): 
                                                                print("\nCourse Successfully Registered !\n")
                                                            else:
                                                                print("\nCourse is not present in offered Subjects !\n")
                                                        else:
                                                            print("\nOffered Subjects File is Missing !\n")
                                                    break
                                                except Exception as msg:
                                                    print("\nEnter only Numbers not Strings !\n")
                                                    continue
                                        elif (User_Option=="3"):        # here is the Code to Show Result of Student
                                            Directory="c:/Users/Admin/Desktop"
                                            File_Name=f"{Name.title()}_Result.txt"  
                                            if (File_Name) in os.listdir(Directory):
                                                with open (f"{Name.title()}_Result.txt","r") as f:
                                                    Result_Content=f.read()
                                                print("\n\n"+Result_Content+"\n\n")
                                            else:
                                                print("\nNo Record Found !\n")                                          
                                        elif (User_Option=="4"):        # Here is the Code to Show Attendance 
                                            print("Enter the Date according to this format xx-xx-xxxx !")
                                            date=input("Enter the Date: ")
                                            if (len(date)==10):
                                                Directory="c:/Users/Admin/Desktop"
                                                File_Name=f"Attendance{date}.txt"
                                                if (File_Name) in os.listdir(Directory):
                                                    Khatam=RegistrationClass()
                                                    Reg_Number=Khatam.RegistrationNumber()
                                                    P=True
                                                    with open (f"Attendance{date}.txt","r") as f:
                                                        Attendance_Content=f.read()
                                                    if Reg_Number in Attendance_Content:
                                                        Index=Attendance_Content.find(f"{Reg_Number}")
                                                        print(f"{Reg_Number} attendance is {Attendance_Content[Index:Index+10]}\n")
                                                    else:
                                                        P=False
                                                        print("\nYour Attendance is missing !\n")
                                                else:
                                                    print("\nNo Attendance Record !\n")
                                            else:
                                                print("Date format is wrong !")
                                        elif (User_Option=="5"):        # Here is the Code to Show Challan 
                                            Directory="c:/Users/Admin/Desktop"
                                            File_Name=f"{Name.title()}_Challan.txt"
                                            if (File_Name) in os.listdir(Directory):
                                                with open(f"{Name.title()}_Challan.txt","r") as f:
                                                    Challan_Content=f.read()
                                                time.sleep(1)
                                                print("\n\n"+Challan_Content+"\n\n")
                                            else:
                                                print("\nNo Record Found !\n")
                                            while (True):
                                                try:
                                                    Checking=input("Is you Hostelite?(Y/N): ")
                                                    assert (Checking.upper()=="Y" or Checking.upper()=="N")
                                                    if (Checking.upper()=="Y"):
                                                        Directory="c:/Users/Admin/Desktop"
                                                        File_Name=f"{Name.title()}_Hostel_Challan.txt"
                                                        if (File_Name) in os.listdir(Directory):
                                                            with open (f"{Name.title()}_Hostel_Challan.txt","r") as f:
                                                                Hostel_Challan_Content=f.read()
                                                            time.sleep(1)
                                                            print("\n\n"+Hostel_Challan_Content+"\n\n")
                                                            break
                                                        else:
                                                            print("\nNo Record Found !\n")
                                                            break
                                                    else:
                                                        print("Ok,Thanks !")
                                                        break
                                                except Exception as msg:
                                                    print("Enter only 'Y' or 'N' !")
                                                    continue
                                        elif (User_Option=="6"):        # Here is the Code for Hostel Comment 
                                            Hostel_Comment=input("Enter your Comment about Hostel: ")
                                            with open (f"{Name.title()}_Hostel_Comment.txt","a") as f:
                                                f.write(Hostel_Comment.capitalize())
                                        elif (User_Option=="7"):        # Here is the code for Scholarship Apply
                                            Directory="c:/Users/Admin/Desktop"
                                            File_Name=f"Scholarship.txt"
                                            if (File_Name) in os.listdir(Directory):
                                                while (True):
                                                    try:
                                                        print("\n|1| for Need Base Sholarship\n|2| for Merit Base Scholarship\n")
                                                        Scholarship_Option=input("Enter your Choice: ")
                                                        assert (Scholarship_Option=="1" or Scholarship_Option=="2")
                                                        if (Scholarship_Option=="1"):
                                                            Directory="c:/Users/Admin/Desktop"
                                                            File_Name=f"Need_Base.txt"
                                                            if (File_Name) in os.listdir(Directory):
                                                                Name3=UserName()
                                                                Directory="c:/Users/Admin/Desktop"
                                                                File_Name=f"{Name3.title()}_Scholarship.txt"
                                                                if (File_Name) in os.listdir(Directory):
                                                                    print(f"\nA File of {Name3.title()} name is already Present.\n")
                                                                else:
                                                                    Stipened=ScholarshipClass()
                                                                    Scholar_CNIC=Stipened.ScholarCNIC()
                                                                    Scholar_Father_Name=Stipened.ScholarFatherName()
                                                                    Scholar_Father_CNIC=Stipened.ScholarFatherCNIC()
                                                                    Scholar_Number=Stipened.ScholarPhoneNumber()
                                                                    Scholar_Father_Number=Stipened.ScholarFatherPhoneNumber()
                                                                    Scholar_Family_Members=Stipened.FamilyMembers()
                                                                    Scholar_Father_Salary=Stipened.FatherSalary()
                                                                    Scholar_Guardian_Salary=Stipened.GuardianSalary()
                                                                    Scholar_City=Stipened.City()
                                                                    Scholar_District=Stipened.District()
                                                                    Scholar_Province=Stipened.Province()
                                                                    Scholar_Matric_Marks=Stipened.MatricMarks()
                                                                    Scholar_Total_Matric_Marks=Stipened.TotalMatricMarks()
                                                                    Scholar_Inter_Marks=Stipened.InterMarks()
                                                                    Scholar_Total_Inter_Marks=Stipened.TotalInterMarks()
                                                                    Scholar_Transport=Stipened.Transport()
                                                                    Scholar_DOB=Stipened.DOB()
                                                                    Scholar_RegNo=Stipened.RegistrationNumber()
                                                                    Scholar_PayRent=Stipened.PayRent()
                                                                    Scholar_House_Land=Stipened.HouseLand()
                                                                    Scholar_Harvest_Land=Stipened.HarvestLand()
                                                                    f=open(f"{Name3.title()} Need Base.txt","a")
                                                                    f.write("Name:"+Name3.title()+"\n"+"CNIC: "+str(Scholar_CNIC)+"\n"+"Father Name: "+str(Scholar_Father_Name)+"\n"+"Father CNIC: "+str(Scholar_Father_CNIC)+"\n"+"Date of Birth: "+str(Scholar_DOB)+"\n"+"Contact No.1: "+str(Scholar_Number)+"\n"+"Conatct No.2: "+str(Scholar_Father_Number)+"\n"+"Reg Number: "+str(Scholar_RegNo)+"\n"+"Family Members: "+str(Scholar_Family_Members)+"\n"+"Fahter Salary: "+str(Scholar_Father_Salary)+"\n"+"Guardian Salary: "+str(Scholar_Guardian_Salary)+"\n"+"Matric Marks: "+str(Scholar_Matric_Marks)+"\n"+"Total Matric Marks: "+str(Scholar_Total_Matric_Marks)+"\n"+"Inter Marks: "+str(Scholar_Inter_Marks)+"\n"+"Total Inter Marks: "+str(Scholar_Total_Inter_Marks)+"\n"+"City: "+Scholar_City+"\n"+"District: "+Scholar_District+"\n"+"Province: "+Scholar_Province+"\n"+"Transport: "+Scholar_Transport+"\n"+"Rent: "+Scholar_PayRent+"\n"+"\n"+"House Land: "+Scholar_House_Land+"\n"+"Harvest Land: "+Scholar_Harvest_Land+"\n")
                                                                    f.close()
                                                                break
                                                            else:
                                                                print("\nNo Need Base Scholarship Available !\n")
                                                                break
                                                        else:
                                                            Directory="c:/Users/Admin/Desktop"
                                                            File_Name=f"Merit_Base.txt"
                                                            if (File_Name) in os.listdir(Directory):
                                                                Name4=UserName()
                                                                Directory="c:/Users/Admin/Desktop"
                                                                File_Name=f"{Name4.title()}_Scholarship.txt"
                                                                if (File_Name) in os.listdir(Directory):
                                                                    print(f"\nA File of {Name4.title()} name is already Present.\n")
                                                                else:
                                                                    Stipened=ScholarshipClass()
                                                                    Scholar_CNIC=Stipened.ScholarCNIC()
                                                                    Scholar_Father_Name=Stipened.ScholarFatherName()
                                                                    Scholar_Father_CNIC=Stipened.ScholarFatherCNIC()
                                                                    Scholar_Number=Stipened.ScholarPhoneNumber()
                                                                    Scholar_Father_Number=Stipened.ScholarFatherPhoneNumber()
                                                                    Scholar_Family_Members=Stipened.FamilyMembers()
                                                                    Scholar_Father_Salary=Stipened.FatherSalary()
                                                                    Scholar_Guardian_Salary=Stipened.GuardianSalary()
                                                                    Scholar_City=Stipened.City()
                                                                    Scholar_District=Stipened.District()
                                                                    Scholar_Province=Stipened.Province()
                                                                    Scholar_Matric_Marks=Stipened.MatricMarks()
                                                                    Scholar_Total_Matric_Marks=Stipened.TotalMatricMarks()
                                                                    Scholar_Inter_Marks=Stipened.InterMarks()
                                                                    Scholar_Total_Inter_Marks=Stipened.TotalInterMarks()
                                                                    Scholar_Transport=Stipened.Transport()
                                                                    Scholar_DOB=Stipened.DOB()
                                                                    Scholar_RegNo=Stipened.RegistrationNumber()
                                                                    Scholar_PayRent=Stipened.PayRent()
                                                                    Scholar_House_Land=Stipened.HouseLand()
                                                                    Scholar_Harvest_Land=Stipened.HarvestLand()
                                                                    f=open(f"{Name4.title()} Merit Base.txt","a")
                                                                    f.write("Name:"+Name4.title()+"\n"+"CNIC: "+str(Scholar_CNIC)+"\n"+"Father Name: "+str(Scholar_Father_Name)+"\n"+"Father CNIC: "+str(Scholar_Father_CNIC)+"\n"+"Date of Birth: "+str(Scholar_DOB)+"\n"+"Contact No.1: "+str(Scholar_Number)+"\n"+"Conatct No.2: "+str(Scholar_Father_Number)+"\n"+"Reg Number: "+str(Scholar_RegNo)+"\n"+"Family Members: "+str(Scholar_Family_Members)+"\n"+"Fahter Salary: "+str(Scholar_Father_Salary)+"\n"+"Guardian Salary: "+str(Scholar_Guardian_Salary)+"\n"+"Matric Marks: "+str(Scholar_Matric_Marks)+"\n"+"Total Matric Marks: "+str(Scholar_Total_Matric_Marks)+"\n"+"Inter Marks: "+str(Scholar_Inter_Marks)+"\n"+"Total Inter Marks: "+str(Scholar_Total_Inter_Marks)+"\n"+"City: "+Scholar_City+"\n"+"District: "+Scholar_District+"\n"+"Province: "+Scholar_Province+"\n"+"Transport: "+Scholar_Transport+"\n"+"Rent: "+Scholar_PayRent+"\n"+"\n"+"House Land: "+Scholar_House_Land+"\n"+"Harvest Land: "+Scholar_Harvest_Land+"\n")
                                                                    f.close()
                                                                break
                                                            else:
                                                                print("\nNo Merit Base Scholarship Available !\n")
                                                                break
                                                    except Exception as msg:
                                                        print("\nEnter only '1' or '2' !\n")
                                                        continue
                                            else:
                                                print("\nNo Sholarship Available !\n")
                                        elif (User_Option=="8"):        # here is the Code for Exit
                                            break
                                        else:
                                            print("\nEnter the Digits from 1 to 8 !\n")
                                            continue
                                    except Exception as msg:
                                        print("\nPlease, Enter the only digits !\n")
                                        continue
                                #   Here to insert all functionality of LMS given to user
                                break
                            else:
                                if not (Mail in Content):
                                    print("\nIncorrect E-Mail.\n")
                                    continue
                                else:
                                    print("\nIncorrect Password.\n")
                                    continue
                        else:
                                print(f"\nSorry, {Name} file is not Present.\n")    
                    elif (Desicion.lower()=="e"):       # Here is the code for exit
                        print("\nThanks for Visiting Here.\n")
                        break   
                    else:       # Here is the code when not of any condition is chosen
                        print("\nPlease, Enter s or l or e !\n")
                        continue
            elif (Choice=="3"):
                print("\n")
                print(Big_Text4)
                break
        except Exception as msg:
            print("\nEnter Only 1 or 2  or 3!\n")
            continue
    except Exception as msg:
        print("\nPlease, Enter only Integers !\n")
        continue


while (True):
    try:
        Audio_Option=input("Do you want to Listen  Any File Content?(Y/N): ")
        assert (Audio_Option.upper()=="Y" or Audio_Option.upper()=="N")
        if (Audio_Option.upper()=="Y"):
            root=Tk()
            root.title("Audio Book")
            def Read():
                file = open(f"{File_Name.get().title()}.txt")
                file_txt=file.readlines()
                engine=pyttsx3.init()
                Rate=engine.getProperty("rate")
                engine.setProperty("rate",Rate+50)
                Volume=engine.getProperty("volume")
                engine.setProperty("volume",Volume+150)
                for i in file_txt:
                    engine.say(i)
                    engine.runAndWait()
            root.geometry("355x400")
            root.minsize(300,350)
            F1=Frame(root,bg="Pale Green",borderwidth=15,relief=GROOVE)
            F1.pack(fill=BOTH)
            FileName=Label(F1,text="File Name",bg="Blue",fg="White").grid(row=1,column=2)
            File_Name=StringVar()
            File_Name_Entry=Entry(F1,textvariable=File_Name).grid(row=1,column=3)
            Button(F1,text="Apply",bg="White",fg="Black",command=Read).grid(row=2,column=3)
            root.mainloop()
        else:
            print("\n")
            print(Big_Text5)
            break
    except Exception as msg:
        print("Enter only 'Y' or 'N' !")
        continue



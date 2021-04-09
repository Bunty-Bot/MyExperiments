#This code is made by Shreyas Bapat
#Making a better version of Receptionist

#Information about Hospital and staff
info = 'Welcome to Med4U Hospital. This Hospital was Established by Shreyas Swanand Bapat.\n' \
       'Our Hospital has 3 floors and it is well ventilated. The patients are happy with our service.\n' \
       'Also we have Rosie. She is a robot and our receptionist too.\n' \
       'She is excellent at her work and set a very good example of use of AI in healthcare industry.\n' \
       'Every doctor in our Hospital is dedicated to their work and they are very friendly.\n' \
       'We have a choice of doctors for you.\n' \
       'We have both MD and BHMS doctors in our Hospital.\n' \
       'We consider every doctor and patient as our family.\n' \
       'We are also awarded with many awards like "Best Multi-speciality Hospital",\n' \
       '"Best Hospital - Emergency","Best Hi-Tech Hospital",etc.\n' \
       'We all thank you for choosing our Hospital. Thank you so much!!! '

Sujata = 'Name - Dr.Sujata Mahesh Mali.(MD)\n' \
         'Contact no. - 8643489823\n' \
         'Email ID - sujata.mali12@gmail.com\n' \
         'Education - MBBS from JHSD medical college.\n' \
         'MD in Trauma.\n' \
         'Achievements - Receive “Gold Medal” in All Indian health care group in 2010-2011\n' \
         'Give many speeches for general precautions in many villages.\n' \
         'Provide free medical help to many poor people in villages during camps.\n' \
         'Attended many seminars as chief guest.\n' \
         'Technical skills - Well versed with the basic use of computer.\n' \
         'Familiar with all the surgical equipment of the operation theater.\n' \
         'Internet savvy.'

Neeraj = 'Name - Dr.Neeraj Sanket Ponkshe.(BHMS)\n' \
         'Contact no. - 9831429740\n' \
         'Email ID - raj.33ponkshe@gmail.com\n' \
         'Education - BHMS in Anandi Bai Joshi college.\n' \
         'Achievements - Secretary of Dhondumama Sathe Hospital from 2 years\n' \
         'Wrote a book on care after the education\n' \
         'Won football match in hospital tournament.'

Sarvesh = 'Name - Sarvesh Lalit Abhyankar.(OD)\n' \
          'Contact no. - 9881537284\n' \
          'Email ID - sarvesh.11abhya@gmail.com\n' \
          'Education - Bachelor of science:History/Library media science\n' \
          'Southern Utah University - city state, USA\n' \
          'Opthalmic specialist 2012.\n' \
          'Achievments - Gold medalist at Southern Utah University.\n' \
          'Also 10th rank in MCI Screening Test.\n' \
          'Skills - Contact lens fitting and training\n' \
          'OCT and Standard Opthalmic Pre-exam test.'

Anushka = 'Name - Anushka Ramesh Kulkarni.(Dermatologist)\n' \
          'Contact No. - 6892828832\n' \
          'Email ID - anushka.123k@gmail.com\n' \
          'Education - Medical Esthetician - (Southeastern college - Jacksonville, FL)\n' \
          'Skills - Medical, Healthcare, Nurse.'

Misba = 'Name - Misba Satish Sathe.(DM)\n' \
          'Contact No. - 8839103910\n' \
          'Email ID - megha.sathe00@gmail.com\n' \
          'Education - MBBS from MIMER College\n' \
          'MD from JHSD medical college\n' \
          'DM from University of Russia\n' \
          'Skills - Interpersonal skills, Medical administrations.'

Varsha = 'Name - Varsha Sahil Khamkar.(MBBS)\n' \
         'Contact No. - 9035835824\n' \
         'Email ID - varsha123.k@gmail.com\n' \
         'Education - MBBS from Maulana Azad college.\n' \
         'Skills - Interpersonal skills, Social, Friendly.'

Anvay = 'Name - Anvay Makaranda Shastri(MD)\n' \
        'Contact No. - 6928439638\n' \
        'Email ID - anvay6.s@gmail.com\n' \
        'Education - MBBS from JHSD medical college.\n' \
         'MD in Trauma.\n' \
        'Skills - Strong communication, Great knowledge of Human anatomy and nervous system.'

Pankaj = 'Name - Pankaj Girish Mahajan(MD)\n' \
         'Contact No. - 9473859295\n' \
         'Email ID - pankaj14.maha@gmail.com\n' \
         'Education - MBBS from AIIMS Delhi.\n' \
         'MD from Apollo college\n' \
         'Skills - Friendly, Interpersonal skills, Good practice.'

Bhushan = 'Name - Bhushan Anil Sutar(MD)\n' \
          'Contact No. - 9248929492\n' \
          'Email ID - bhushan.28s@gmail.com\n' \
          'Education - MBBS from AIIMS Delhi.\n' \
         'MD from Apollo college\n' \
          'Skills - Interpersonal skills, Friendly.'

Rahul = 'Name - Rahul Ganesh Waghmare(BSRT)' \
        'Contact No. - 4926582258\n' \
        'Email ID - rahul.waghmare1@gmail.com\n' \
        'Education - BSRT from APJ school of medical sciences\n' \
        'Skills - Interpersonal skills, Social, Good at work.'

#All functions
def greetings():
    print("Hello!!!\n"
          "I'm Rosie a virtual artificial intelligence and I'm here to help you in our Hospital.\n"
          "I'm here to help patients with their difficulties.\n"
          "My job is to assist everyone in this hospital and help them as much as I can.\n"
          "I'm available for you 24 by 7 and 7 days of week.")
    return "Stay Home Stay Safe"

def information():
    print("Do you want to know some information about our Hospital?\n"
          "Press y for YES and n for NO.")
    bore = input()
    if bore=='y':
        print(info)
        print("Do you want more information about our doctors?\n"
              "Press y for YES and n for NO.")
        ugach = input()
        if ugach=='y':
            print("Please select the name of the doctor.\n"
                  "Press 1 for Dr. Sujata.\n"
                  "press 2 for Dr. Neeraj.\n"
                  "Press 3 for Dr. Sarvesh.\n"
                  "Press 4 for Dr. Anushka.\n"
                  "Press 5 for Dr. Misba.\n"
                  "Press 6 for Dr. Varsha.\n"
                  "Press 7 for Dr. Anvay.\n"
                  "Press 8 for Dr. Pankaj.\n"
                  "Press 9 for Dr. Bhushan.\n"
                  "Press 0 for Dr. Rahul.")
            name1 = int(input())
            if name1==1:
                print(Sujata)
            elif name1==2:
                print(Neeraj)
            elif name1==3:
                print(Sarvesh)
            elif name1==4:
                print(Anushka)
            elif name1==5:
                print(Misba)
            elif name1==6:
                print(Varsha)
            elif name1==7:
                print(Anvay)
            elif name1==8:
                print(Pankaj)
            elif name1==9:
                print(Bhushan)
            else:
                print(Rahul)
        else:
            pass
    else:
        pass
    return "Stay Home Stay Safe"

def questions():
    print("What is your full name?")
    name = input()
    print("What is your age?")
    age = int(input())
    print("Do you have allergy of any chemical or something? If not pls type none.")
    prob = input()
    print("What is the name of you family doctor?")
    Dr = input()
    print(f"name - {name}\n"
          f"age - {age}\n"
          f"Any allergies - {prob}\n"
          f"Family doctor - {Dr}\n")
    print("Thank you for your information!!!")
    return "Stay Home Stay Safe"

def appointment():
    print("Do you have an appointment with any doctor?\n"
          "Press y for YES and n for NO.")
    bol = input()
    if bol=='y':
        print("OK. Please tell me the name of your doctor\n"
              "Press 1 for Dr. Sujata.\n"
              "press 2 for Dr. Neeraj.\n"
              "Press 3 for Dr. Sarvesh.\n"
              "Press 4 for Dr. Anushka.\n"
              "Press 5 for Dr. Misba.\n"
              "Press 6 for Dr. Varsha.\n"
              "Press 7 for Dr. Anvay.\n"
              "Press 8 for Dr. Pankaj.\n"
              "Press 9 for Dr. Bhushan.\n"
              "Press 0 for Dr. Rahul.")
        app = int(input())
        if app==1:
            print("OK. Dr. Sujata is on the Ground floor Room no.1\n"
                  "Thank you and Get well soon!!")
        elif app==2:
            print("OK. Dr. Neeraj is on Ground floor Room no.2\n"
                  "Thank you and Get well soon!!")
        elif app==3:
            print("OK. Dr. Sarvesh is on Ground floor Room no.3\n"
                  "Thank you and Get well soon!!")
        elif app==4:
            print("OK. Dr. Anushka is on Second floor Room no.2\n"
                  "Thank you and Get well soon!!")
        elif app==5:
            print("OK. Dr.Misba is on Second floor Room no.1\n"
                  "Thank you and Get well soon.")
        elif app==6:
            print("OK. Dr. Varsha is on Second floor Room no.3\n"
                  "Thank you and Get well soon!!")
        elif app==7:
            print("OK. Dr. Anvay is on Third floor Room no.1\n"
                  "Thank you and Get well soon!!")
        elif app==9:
            print("OK. Dr. Bhushan is on Third floor Room no.2\n"
                  "Thank you and Get well soon!!")
        elif app==8:
            print("OK. Dr. Pankaj is on First floor\n"
                  "Thank you and Get well soon!!")
        else:
            print("OK. Dr. Rahul is on Third floor Room no.3\n"
                  "Thank you and Get well soon!!")
        repeat()

    else:
        print("OK. So please answer some basic questions.\n"
              "Don't worry these are just for our records.")
        questions()
    return "Stay Home Stay Safe"

def rate():
    print("Which test is recommended by the doctor?\n"
          "Press 1 for CT scan.\n"
          "Press 2 for CAT scan.\n"
          "Press 3 for MRI.\n"
          "Press 4 for MRA.\n"
          "Press 5 for X-RAY.\n"
          "Press 6 for PET scan.\n"
          "Press 7 for PET-CT scan.\n"
          "Press 8 for Ultrasound.\n"
          "Press 9 for EEG.\n"
          "Press 0 for ECG.")
    c = int(input())
    if c==1:
        print("OK. So your total bill is 3000 Rs.\n"
              "This includes,\n"
              "Doctor fee - 200 Rs.\n"
              "CT scan fee - 2740 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==2:
        print("OK. So your total bill is 3250 Rs.\n"
              "This includes,\n"
              "Doctor fee - 200 Rs.\n"
              "CAT scan fee - 2990 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==3:
        print("OK. So your total bill is 7560 Rs.\n"
              "This includes,\n"
              "Doctor fee - 500 Rs.\n"
              "MRI fee - 7000 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==4:
        print("OK. So your total bill is 10320 Rs.\n"
              "This includes,\n"
              "Doctor fee - 200 Rs.\n"
              "MRA fee - 10,060 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==5:
        print("OK. So your total bill is 760 Rs.\n"
              "This includes,\n"
              "Doctor fee - 200 Rs.\n"
              "X-RAY fee - 500 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==6:
        print("OK. So your total bill is 15560 Rs.\n"
              "This includes,\n"
              "Doctor fee - 500 Rs.\n"
              "PET scan fee - 15000 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==7:
        print("OK. So your total bill is 22560 Rs.\n"
              "This includes,\n"
              "Doctor fees - 500 Rs.\n"
              "PET-CT scan - 22000 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==8:
        print("OK. So your total bill is 1360 Rs.\n"
              "This includes,\n"
              "Doctor fee - 200 Rs.\n"
              "Ultrasound fee - 1100 Rs.\n"
              "Taxes - 60 Rs.")
    elif c==9:
        print("OK. So your total bill is 3960 Rs.\n"
              "This includes,\n"
              "Doctor fee - 400 Rs.\n"
              "EEG fee - 3500 Rs.\n"
              "Taxes - 60 Rs.")
    else:
        print("OK. So your bill is 960 Rs.\n"
              "This includes,\n"
              "Doctor fee - 400 Rs.\n"
              "ECG fee - 500 Rs.\n"
              "Taxes - 60 Rs.")
    print("Thank you!! It was nice meeting you. Get well soon!!!")
    repeat()
    return "Stay Home Stay Safe"

def bill():
    print("You are now at billing stage so please answer the question given below.")
    print("Under which doctor you take the treatment?\n"
          "Press 1 for Dr. Sujata.\n"
          "press 2 for Dr. Neeraj.\n"
          "Press 3 for Dr. Sarvesh.\n"
          "Press 4 for Dr. Anushka.\n"
          "Press 5 for Dr. Misba.\n"
          "Press 6 for Dr. Varsha.\n"
          "Press 7 for Dr. Anvay.\n"
          "Press 8 for Dr. Pankaj.\n"
          "Press 9 for Dr. Bhushan.\n"
          "Press 0 for Dr. Rahul.")
    a = int(input())
    if a==1:
        print("OK. Did Dr. Sujata advised any test?\n"
              "Press y for YES and n for NO.")
        b = input()
        if b=='y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==2:
        print("OK. Did Dr. Neeraj advised any test?\n"
              "Press y for YES and n for NO.")
        d = input()
        if d == 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==3:
        print("OK. Did Dr. Sravesh advised any test?\n"
              "Press y for YES and n for NO.")
        e = input()
        if e == 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==4:
        print("OK. Did Dr. Anushka advised any test?\n"
              "Press y for YES and n for NO.")
        f = input()
        if f=='y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==5:
        print("OK. Did Dr. Misba advised any test?\n"
              "Press y for YES and n for NO.")
        g = input()
        if g == 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==6:
        print("OK. Did Dr. Varsha advised any test?\n"
              "Press y for YES and n for NO.")
        h = input()
        if h == 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==7:
        print("OK. Did Dr. Anvay advised any test?\n"
              "Press y for YES and n for NO.")
        h = input()
        if h == 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==8:
        print("OK. Did Dr. Pankaj advised any test?\n"
              "Press y for YES and n for NO.")
        i = input()
        if i== 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    elif a==9:
        print("OK. Did Dr. Bhushan advised any test?\n"
              "Press y for YES and n for NO.")
        j = input()
        if j == 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    else:
        print("OK. Did Dr. Rahul advised any test?\n"
             "Press y for YES and n for NO.")
        k = input()
        if k == 'y':
            rate()
        else:
            print("OK. So your bill is 350 Rs.\n"
                  "This includes,\n"
                  "Doctor fee - 290 Rs.\n"
                  "Taxes - 60 Rs.")
            repeat()
    return "Stay Home Stay Safe"

def clinic():
    print("What difficulties are you facing?\n"
          "Press 1 for Basic(Fever,Cough,Cold,Headache,Body Pain,First Aid,etc.\n"
          "Press 2 for Eye(Eye checkup, Change in spectacle number, eye disease,etc.\n"
          "Press 3 for Skin and Hair(Skin problems, hair problems,etc.\n"
          "Press 4 for Blood and Cardiovascular problems,etc.\n"
          "Press 5 for Neurological problems(Brain, mental health related problems)\n"
          "Press 6 for Vaccination\n"
          "Press 7 for COVID problems\n"
          "Press 8 for Radiology(Different types of scans and techniques)\n"
          "Press 9 for Orthopedic problems(Bone related problems)")
    diff = int(input())
    if diff==1:
        print("OK.\n"
              "Press 1 for Fever.\n"
              "Press 2 for Cough.\n"
              "Press 3 for Cold.\n"
              "Press 4 for Headache.\n"
              "Press 5 for Body pain.\n"
              "Press 6 for First Aid.\n"
              "Press 7 for other.")
        tp = int(input())
        print("OK.\n"
              "Press 1 for Allopathic treatment.\n"
              "Press 2 for Ayurvedic treatment.")
        main = int(input())
        if main==1:
            print("OK. Dr. Sujata will diagnose you. She is on the ground floor Room no.1\n"
                  "Thank you and Get well soon!!")
        else:
            print("OK. Dr. Neeraj will diagnose you. He is on the Ground floor Room no.2\n"
                  "Thank you and Get well soon!!")
    elif diff==2:
        print("OK.\n"
              "Press 1 for eye checkup.\n"
              "Press 2 for spectacle's number checkup.\n"
              "Press 3 for Eye disease.\n"
              "Press 4 for Other.")
        eye = int(input())
        print("OK. So our Dr. Sarvesh will diagnose you. He is on the ground floor Room no.3\n"
              "Thank you and Get well soon!!")
    elif diff==3:
        print("OK.\n"
              "Press 1 for Skin Problems.\n"
              "Press 2 for Hair problems.")
        skin = int(input())
        print("OK. So our Dr. Anushka will diagnose you. She is on Second floor Room no.2\n"
              "Thank you and Get well soon!!")
    elif diff==4:
        print("OK.\n"
              "Press 1 for Blood related problems.\n"
              "Press 2 for Heart related problems.\n"
              "Press 3 for BP checkup.\n"
              "Press 4 for sugar checkup.\n"
              "Press 5 for other")
        heart = int(input())
        print("OK. So our Dr. Misba will diagnose you. She is on Second floor Room no.1\n"
              "Thank you and Get well soon!!")
    elif diff==6:
        print("OK.\n"
              "Press 1 for Polio.\n"
              "Press 2 for Rabies.\n"
              "Press 3 for AIDS.\n"
              "Press 4 for Tetanus.\n"
              "Press 5 for Covishield.\n"
              "Press 6 for Covaccine.\n"
              "Press 7 for Measles.\n"
              "Press 8 for Hepatitis.")
        vaccine = int(input())
        print("OK. So for your selected vaccine our Dr. Varsha will take care of you.\n "
              "She is on second floor Room no.3\n"
              "Thank you and Get well soon!!")
    elif diff==5:
        print("OK. Please meet Dr. Anvay. He will diagnose you. He is on Third floor Room no.1\n"
              "Thank you and Get well soon.")
    elif diff==7:
        print("OK. Please don't get panic we are here to diagnose you.\n"
              "Please meet Dr. Pankaj. He is on First floor.\n"
              "Entire floor is secured for covid treatments so you will be safe there.")
    elif diff==8:
        print("OK.\n"
              "Press 1 for CT scan.\n"
              "Press 2 for CAT scan.\n"
              "Press 3 for MRI scan.\n"
              "Press 4 for MRA scan.\n"
              "Press 5 for X-Ray.\n"
              "Press 6 for PET scan.\n"
              "Press 7 for PET-CT.\n"
              "Press 8 for Ultrasound.\n"
              "Press 9 for EEG.\n"
              "Press 0 for ECG.")
        scan = int(input())
        print("OK. please meet our Dr. Rahul.\n"
              "He is on Third floor Room no.3. He will diagnose you.\n"
              "Thank you and Get well soon.")
    else:
        print("OK. Please meet Dr. Bhushan for your bone problems. He will diagnose you.\n"
              "He is on Third floor room no.2\n"
              "Thank you and Get well soon.")
    return "Stay Home Stay Safe"

def repeat():
    print("Press y to start the procedure for next patient and n to exit the process.")
    s = input()
    if s=='y':
        greetings()
        information()
        appointment()
        clinic()
        bill()
    else:
        pass
    return "Stay Home Stay Safe"

#Real Code
greetings()
information()
appointment()
clinic()
bill()
repeat()












    






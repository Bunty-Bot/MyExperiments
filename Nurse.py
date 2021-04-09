#This code is made by Shreyas Bapat

z = {'Dr. Sujata': 'Her cabin is on Ground floor Room no.1','Dr.Neeraj': 'His cabin is on Ground floor Room no.2',
     'Dr.Sarvesh':'His cabin is on Ground floor Room 3',
     'Dr.Anushka': 'She is on First floor',
     'Dr.Meghana':'Her cabin is on Second floor Room no.1','Dr.Varsha':'Her cabin is on Second floor Room no.2',
     'Dr.Anvay' : 'His cabin is on Second floor Room no.3','Dr.Pankaj' : 'His cabin is on Second floor Room no.4',
     'Dr.Bhushan' : 'His cabin is on Second floor Room no.5',
     'Dr.Rahul' : 'He is on Third floor'}

print("Hello!! We are here to diagnose you.")




def clinic():
    print("What difficulties are you facing?")
    print("Press 1 for basic(Headache,Fever, Cough, Cold)\n"
          "Press 2 for Heart(BP)\n"
          "Press 3 for Covid\n"
          "Press 4 for Major(Swine Flu, Dengue, Malaria, AIDS, Polio)\n"
          "Press 5 for Techniques(X-Ray, EEG, ECG)\n")
    n = int(input())
    if n==1:
        print("OK. Please select your disease;\n"
              "Press 1 for Headache.\n"
              "Press 2 for Fever,Cough and Cold.")
        a = int(input())
        if a==1:
            print("Since when you have this Headache?\n"
                  "Please enter the number of days:")
            b = int(input())
            if b<=2:
                print("OK. Please consult to our Doctor.\n"
                      "Please meet Dr. Sujata.\n"
                      "Her cabin is on ground floor. Room No.1")
            if b>2:
                print("You should come here within 2 days since the headache starts.\n"
                      "This advice is for your health.\n"
                      "Now please consult to our Doctor.\n"
                      "Please meet Dr. Sujata.\n"
                      "Her cabin is on ground floor. Room No.1")
        if a==2:
            print("Since when you are suffering from Fever/Cough/Cold?\n"
                  "Please enter the number of days:")
            c = int(input())
            if c<=2:
                print("OK. Please consult to our Doctor.\n"
                      "Please meet Dr. Neeraj.\n"
                      "His cabin is on ground floor. Room No.2")
            if c>2:
                print("You should come here within 2 days when you fell ill.\n"
                      "This advice is for your health.\n"
                      "Now please consult to our Doctor.\n"
                      "Please meet Dr. Neeraj.\n"
                      "His cabin is on ground floor. Room No.2")

    if n==2:
        print("OK. So you want to check your Blood Pressure.\n"
              "Please meet Dr. Sarvesh. He will consult you for the same.\n"
              "His cabin is on ground floor. Room No.6")
    if n==3:
        print("OK.\n"
              "Press 1 if you are affected by covid for thr first time.\n"
              "Press 2 if it is not the first time.")
        j = int(input())
        if j==1:
            print("OK. Don't get panic. We are here to help you.\n"
                  "You will be absolutely fine.\n"
                  "Please consult to our Doctor.\n"
                  "Please meet Dr. Anushka.\n"
                  "Her cabin is on first floor.\n"
                  "Entire floor is reserved for covid treatment.")
        else:
            print("OK. Our Doctors will do your check up.\n"
                  "Don't get panic.\n"
                  "Meet Dr. Anushka. She is on first floor.\n"
                  "Entire floor is reserved for covid treatment.")
    if n==4:
        print("OK. What difficulties are you facing?\n"
              "Press 1 for Swine-Flu.\n"
              "Press 2 for Malaria.\n"
              "Press 3 for Dengue.\n"
              "Press 4 for AIDS.\n"
              "Press 5 for Polio.")
        k = int(input())
        if k==1:
            print("OK. We have a vaccine for that.\n"
                  "But before that please consult to our Doctors.\n"
                  "Please meet Dr. Meghana.\n"
                  "Her cabin is on 2nd floor. Room No.1")
        if k==2:
            print("OK. We have a vaccine for that.\n"
                  "But before that please consult to our Doctors.\n"
                  "Please meet Dr. Varsha.\n"
                  "Her cabin is on 2nd floor. Room No.2")
        if k==3:
            print("OK. We have a vaccine for that.\n"
                  "But before that please consult to our Doctors.\n"
                  "Please meet Dr. Anvay.\n"
                  "His cabin is on 2nd floor. Room No.3")
        if k==4:
            print("OK. Don't get panic.\n"
                  "Please consult to our Doctor\n"
                  "Meet Dr. Pankaj\n"
                  "His cabin is on 2nd floor. Room No. 4")
        if k==5:
            print("OK. We have a vaccine for that.\n"
                  "But before that please consult to our Doctors.\n"
                  "Please meet Dr. Bhushan.\n"
                  "His cabin is on 2nd floor. Room No.5")
    if n==5:
        print("OK. Which technique is advised for you by the Doctor?\n"
              "Press 1 for X-Ray.\n"
              "Press 2 for EEG.\n"
              "Press 3 for ECG.\n"
              "Press 4 for MRI.")
        l = int(input())
        if l==1:
            print("OK. The X-Ray room is on 3rd floor. Room No.1")
        if l==2:
            print("OK. The EEG room is on 3rd floor. Room No.2")
        if l==3:
            print("OK. The ECG room is on 3rd floor. Room No.3")
        if l==4:
            print("OK. The MRI room is on 3rd floor. Room No.4")

    return("Thank you for visiting our clinic!!\n"
         "please come again after 5 days for routine checkup.\n"
         "Get well soon!!!")
def basic():
    print("Press y to start the procedure for next patient.\n"
          "and n to exit the process.")
    s = input()
    if s=='y':
        clinic()
        basic()
    else:
        pass
    return ("Stay Home!!! Stay safe!!")
clinic()
basic()
print("Thank you for your support!!")
print("Thank you for visiting our clinic!!\n"
      "please come again after 5 days for routine checkup.\n"
      "Get well soon!!!")



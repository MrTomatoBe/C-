o = input("How many minutes do you study everyday?:" \
"")
given = int(o)
hour = (given // 60)
minutes = (given % 60)


def option(): 
    Chosen_subject = [] #this is the storage
        
    Subjects = { 
        1: "math",
        2: "Science",
        3: "History",
        4: "Physical education",
        5: "Finance"
        } # this is the correlation of numbers that will be chosen in the input
                    
    while True: 
          
            print("1. Math")
            print("2. Science")
            print("3. History")
            print("4. Physical education")
            print("5. Finance")
            S = int(input("What subjects you have studied today?: ")) 
            if S in Subjects:
                Chosen_subject.append(Subjects[S])
            else:
                print("meh")
            M = input("Is there more? (Y/N):")
            if M == "Y":
                continue
            if M == "N":
                return Chosen_subject
            else: 
             print("huh") 
        
chosen = option()
list = ", ".join(chosen)

print (f"Congrats in {hour} Hours and {minutes} minutes you have studied, {list}")

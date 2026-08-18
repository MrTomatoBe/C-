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
                        
    print("1. Math")
    print("2. Science")
    print("3. History")
    print("4. Physical education")
    print("5. Finance")
             
    while True:
                try: 
                    Answer_int = int(input("What subjects you have studied today (1-5)?: ")) 
                except ValueError:
                    print("Enter a number please")
                    continue
                if Answer_int in Subjects:
                 Chosen_subject.append(Subjects[Answer_int])

                M = input("Is there more? (Y/N):")
                if M == "Y":
                 continue
                if M == "N":
                 return Chosen_subject
                else:
                    print("Choose between N or Y, please")
                    continue
    
        
chosen = option()
list = ", ".join(chosen)

print (f"Congrats in {hour} Hours and {minutes} minutes you have studied, {list}")

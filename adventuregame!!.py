print("\t\tWelcome to the Haunted Mansion!\n\n\
\t\tYou are a distant family member of a rich millionaire who has just passed away,leaving this mansion to you.\n\n\
\t\tAs the newfound owner,you decide to pay a visit to the mansion.\n\n\
\t\tHouse is dated,creaky.You walk in the front door.\n\n\
\t\tTHIS HOUSE SEEMS TO LOOK CREEPY AND HORRIFYING!!!!!\n\n\
\t\tSO DO YOU REALLY WANT TO ENTER THE HOUSE?!!!!!")

enterChoice= input("\t\t>>> ")
if(enterChoice.lower().strip()=="no"):
    print("\t\t ..........\n\n\
\t\tYOU CHANGED YOUR MIND TO NOT ENTER THE HOUSE")
    exit()



elif(enterChoice.lower().strip()=="yes"):
    print("\t\tYOU ENTER IN THE HOUSE\n\n\
\t\tWHEN YOU ENTER IN THE HOUSE YOU SAW TWO DOORS \n\n\
\t\tONE OPENS IN THE LIVING ROOM AND THE OTHER IN THE DINING ROOM\n\n\
\t\tIN WHICH ROOM WOULD YOU LIKE TO ENTER LIVING ROOM OR THE DINING ROOM?")
    

    roomChoice = input("\t\t>>> ")

    if(roomChoice.lower().strip()== "living room"):
        print("\t\tYOU ENTER IN THE LIVING ROOM\n\n\
\t\tAS YOU WALK IN, YOU SEE A SLEEPING HYENA WHO'S GUARDING SOME GOLD COINS.\n\n\
\t\tDO YOU WANT TO STEAL THESE GOLD COINS FROM THE HYENA?")

        hyenaChoice = input("\t\t>>> ")
        if(hyenaChoice.lower().strip()== "yes"):
            print("\t\tYOU ATTEMPT TO STEAL THE COINS ,\n\n\
\t\tBUT\n\n\
\t\t..................\n\n..................\n\n..................\n\n..................\n\n\
\t\tTHE HYENA WALKS UP AND TEARS YOU TO SHREDS\n\n\
\t\tYOU ARE DEAD NOW ")
            
        elif(hyenaChoice.lower().strip()== "no"):
            print("\t\tYOU DECIDE TO NOT STEAL THE COINS \n\n\
\t\tAND AS YOU TURN AROUND \n\n\
\t\tYOU SEE THE HYENA HAS WOKE UP\n\n\
\t\t.................\n\n\
\t\tTHE HYENA WALKS UP AND TEARS YOU TO SHREDS\n\n\
\t\tYOU ARE DEAD NOW ")
            
        
        else:
            print("\t\tInvalid choice.Please TRY AGAIN")
    elif(roomChoice.lower().strip() == "dining room"):
        print("\t\tYou chose to go into the dining room.\n\n\
\t\tAs you walk in, you see a pearl box on the table.\n\n\
\t\tDo you want to open the box?")

        boxChoice = input("\t\t>>> ")

        if(boxChoice.lower().strip()  == "yes"):
            print("\t\tYOU OPEN THE BOX AND FINDS A PEARL NECKLACE!\n\n \
\t\tDO YOU WANT TO WEAR THIS NECKLACE")
            necklacechoice = input("\t\t>>>")
            if (necklacechoice.lower().strip() == "yes"):
                print("\t\tYOU FELT A HEAVY SHOCKWAVE IN YOUR BODY \n\n\
\t\tTHEN \n\
\t\t.................\n\n\
\t\tYOU WOKE UP AND REALISED IT WAS ALL A DREAM")
                
            elif(necklacechoice.lower().strip() == "no"):
                print("\t\tA DARK FIGURE WITH GLOWING RED EYES LAUNCHES AT YOU AND KNOCKS YOU UNCONCIOUS \n\n \
\t\tTHEN \n\
\t\t.................\n\n\
\t\tYOU WOKE UP AND REALISED IT WAS ALL A DREAM")
                
            else:
                print("\t\tInvalid choice,TRY AGAIN")
               


        elif(boxChoice.lower().strip()  == "no"):
            print("\t\tAS YOU TURN TO LEAVE,YOU  HEAR A CRACKING SOUND COMING FROM THE CORNER\n\n\
\t\tA DARK FIGURE WITH GLOWING RED EYES LAUNCHES AT YOU AND KNOCKS YOU UNCONCIOUS \n\n\
\t\tYOU WOKE UP AND REALISED IT WAS ALL A DREAM.")
            


        else:
            print("\t\tInvalid choice. TRY AGAIN!")
    else:
            print("\t\tInvalid choice,TRY AGAIN")
else:
    print("\t\tINVALID CHOICE  , TRY AGAIN!")


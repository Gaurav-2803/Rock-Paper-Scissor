import random,os                            

'''Clear Function'''
clear=lambda:os.system("cls")
clear()

'''Color Functions'''
color_brwhite=lambda:os.system("color 0f")  #Default        #Bright_White_Color_Fn
color_aqua=lambda:os.system("color 0b")     #Round Win      #Aqua_Color_Fn
color_red=lambda:os.system("color 0c")      #Round Lose     #Red_Color_Fn
color_yellow=lambda:os.system("color 0e")   #TIE            #Yellow_Color_Fn
color_ligreen=lambda:os.system("color 0a")  #WIN            #ligreen_Color_Fn
color_purple=lambda:os.system("color 0d")   #LOSE           #Purple_Color_Fn

'''MAIN'''                             
color_brwhite()
print("\t\t<|Rock Paper Scissor|>\n")
clear()
name=input("Enter Your Name : ")
print("===============================\nWelcome",name,"\n===============================\n#Rules :\n1]Use 1st Letter Of Word(R/P/S)\n2]Player With 3 Point's Will Win\n===============================")
x=['R','P','S']
tie=0
win=0
lose=0
input("Hit Enter To Begin With Game")
clear()
while win<3 and lose<3:
    print("\t   |Score|\n",name,":",win,"Tie :",tie,"Computer :",lose,"\n=================================")
    print()
    comp=x[random.randint(0,2)]
    player=input("Your Choice (R/P/S) : ")
    print("============================================")
    player=player.upper()
    if player==comp:
        clear()
        tie+=1
        color_yellow()
        print("\t'This One Is Tie'\nSame Things Can't Harm Each Other\n=================================")
    elif player=='R':
        if comp=='P':
            lose+=1
            clear()
            color_red()
            print("\t'You Lose This Round'\nComputer Wrapped Your Rock With Paper\n=====================================")
        else:
            win+=1
            clear()
            color_aqua()
            print("\t'You Win This Round'\nYou Smash The Computer's Scissor With Rock\n==========================================")
    elif player=='P':
        if comp=='S':
            lose+=1
            clear()
            color_red()
            print("\t'You Lose This Round'\nComputer Cut Your Paper With Scissor\n=====================================")
        else:
            win+=1
            clear()
            color_aqua()
            print("\t'You Win This Round'\nYou Wrapped Computer's Rock With Paper\n======================================")
    elif player=='S':
        if comp=='R':
            lose+=1
            clear()
            color_red()
            print("\t'You Lose This Round'\nComputer Smashes Your Scissor With Rock\n========================================")
        else:
            win+=1
            clear()
            color_aqua()
            print("\t'You Win This Round'\nYou Cut Computer's Paper With Scissor\n=====================================")
    else:
        clear()
        color_red()
        print("That's Not A Valid Play\nCheck Your Spellings & Try Again\n============================================")
else:
    if win==3:
        color_ligreen()
        print("\t<Final Score>\n\t | Tie :",tie,"|\n|",name,":",win,"\tComputer :",lose,end="")
        print("|\n=====================================")
        print("Congrats",name,"You Won Rock Paper Scissor\n=====================================")
    elif lose==3:
        color_purple()
        print("\t<Final Score>\n\t | Tie :",tie,"|\n|",name,":",win,"\tComputer :",lose,end="")
        print("|\n=====================================")
        print(name,"You Lose Rock Paper Scissor\n=====================================")

input("Hit Enter To Exit")        

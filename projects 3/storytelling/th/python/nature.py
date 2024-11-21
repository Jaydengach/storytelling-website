#welcom our users
print("Welcome to our nature walk center . What would you like to do?")
#set an inital choices value
choices=''
#start a loop until presses q to quit
while choices!= q:
#display all choices
print("[1]Enter 1 to go for a bicycle ride\n")
print("[2]Enter 2 to go for a run\n")
print("[3]Enter 3 to climb a mountain\n")
print("[q]Enter q to quit")

#ask for the choices
choices=input("what would you like to do")

#check choices
if choices==1:
    print("Here is a bicycle , have fun\n")

elif choices==2:
    print("Here are some running shoes run very fast\n")

elif choices==3:
    print("Here is a map ,Climb to the peak\n")

elif choices==q
    print("Thanks for stopping by , Have a good day")
     
else:
    print("I dont understand that choice,please try again")

# print a message that we are all finished
print("Thanks again , bye now")
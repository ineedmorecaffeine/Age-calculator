# This is just for practice.
import datetime

while True:
 print('Type your birthday \nex)20020428 \n')
 Birthday = input()

 present = datetime.datetime.now()
 year = present.year
 month = present.month
 day = present.day
 age = 0


 tempyr = int(year) - int(Birthday[:4]) 

 if int(Birthday[4:6]) > int(month):
     age = tempyr - 1

 elif int(Birthday[4:6]) < int(month):
     age = tempyr 

 elif int(Birthday[4:6]) == int(month):

     if int(Birthday[6:8]) <= int(day):
         age = tempyr 
    
     elif int(Birthday[6:8]) > int(day):
         age = tempyr - 1

    


# Print area

 print("Your age is", age, "\n")




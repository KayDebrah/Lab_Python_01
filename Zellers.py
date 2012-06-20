#Excercise 5#
Firstname=raw_input("What is your Firsname:")
Lastname=raw_input("What is your Lastname:")

#Display Month Options
print "March=1\nApril=2\nMay=3\nJune=4\nJuly=5\nAugust=6\nSeptember=7\nOctober=8\nNovember=9\nDecember=10\nJanuary=11\nFebraury=12\n"

#Accepting Date Values
month=raw_input("Month of Birth:")
day=raw_input("Day of Birth:")
year=raw_input("Year of Century:")
century=raw_input("Century:")

#Converting INouts to Integers
A=int(month)
B=int(day)
C= int(year)
D=int (century)

#Comparing the 11th and 12th Month
if A==11:
   C=C-1
   
elif A==12:
   C=C-1
   
elif A>12:
   print "Value out of range"
elif A<1:
   print "Value out of range"
   


W=(13*A-1)/5
X=C/4
Y=D/4
Z=W+X+Y+B+C-2*D
R=Z%7

#Selecting Day
if R<0:
   R=R+7
if R==0:
   Day="Sunday"
elif R==1:
   Day="Monday"
elif R==2:
   Day="Tuesday"
elif R==3:
   Day="Wednesday"
elif R==4:
   Day="Thursday"
elif R==5:
   Day="Friday"
elif R==6:
   Day="Saturday"

#Display
print Firstname+' '+Lastname+" was born on", Day ,A,'/',B,'/',D,C


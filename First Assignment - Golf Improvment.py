#program 1       September 09, 2020       Lorenzo Celiento

#Second version

#Introduction messages
print("this program is going to calculate the golfer’s handicap")
print()
print("________________________________________________________")
print()

#inizialization of variables start ************

Par = 0
Slope = 0
Score = 0

SumForAver = 0.0
AverDiff = 0.0
handicap = 0.0

counter = 0      #to make the average
condRound = "y"  #to go out of the round's while 

GoOut = "y"      #to go out of the player's while

#Inizialization of variables end **************

#while to insert more than one name*************************************

while (GoOut.lower() == "y"):

	NameGolfer = str(input("Enter the Golfer's name: "))
	print()
	print("All right " + NameGolfer)

	#While which count all th 3 rounds and calculates the Sum for the average

	while (condRound.lower() == "y"):

		print("_______________________________")

		counter += 1    #to make the correct average
		print("this is the ", counter  ,"° round")
		Par = int(input("Enter the Par: "))
		Slope = int(input("Enter Slope: "))
		Score = int(input("Enter Score: "))

		SumForAver += ((Score - Par) * 113) / Slope   #calculation necessary for the handicap
		
		condRound = input("did you play another round? y/n")

	#End of the while********************************************************

	AverDiff = SumForAver / counter    #Average calculation
	handicap = AverDiff / 0.96         #Handicap calculation

	handicap2dec = "{:.2f}".format(handicap)   #shows only the firsts tow decimal number

	print("The handicap of ", NameGolfer , " is ", handicap2dec)
        
	print()
	GoOut = input("Do you have another Golfer? y/n")
	counter = 0
	condRound = "y"

print()
GoOut = print("Bye")

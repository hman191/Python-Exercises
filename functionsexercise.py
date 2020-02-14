def overall(hw,ass,fe):
	overallscore=hw+ass+fe
	overallperc=(overallscore/175)*100
	return overallperc

def overallgrade(overallperc):
	if overallperc>=80:
		overallgrade="A"
	elif 70<=overallperc<=79:
		overallgrade="B"
	elif 60<=overallperc<=69:
		overallgrade="C"
	else:
		overallgrade="Fail"
	return overallgrade

hw=int(input("Please enter your homework mark out of 25:"))
while hw>25:
	hw=int(input("Please enter a number from 0-25 for your homework mark:"))
ass=int(input("Please enter your assessment score out of 50:"))
while ass>50:
	ass=int(input("Please enter a number from 0-50 for your assessment score:"))
fe=int(input("Please enter your final exam score out of 100:"))
while fe>100:
	fe=int(input("Please enter a number between 0-100 for your final exam score:"))

user_perc = overall(hw,ass,fe)
print("Your overall percentage was -", ("%.2f" % user_perc), "%," + " so your grade works out to " + overallgrade(user_perc))

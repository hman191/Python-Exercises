	# <QUESTION 1>

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

	# <EXAMPLES>

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False

	# <HINT>

	# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
        input = input.lower()
        if input.endswith("py"):
                return True
        else:
                return False


if endsPy("ilovepy") == True:
        print("Pass")
if endsPy("welovepy") == True:
        print("Pass")
if endsPy("welovepyforreal") == False:
        print("Pass")
if endsPy("pyiscool") == False:
        print("Pass")

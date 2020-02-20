def getBert(input):
    input = input.lower()
    if input.count("bert") != 2:
        return ("")
    else:
        split_input = input.split("bert")
        word = split_input[1]
        rev_word = word[::-1]
        return rev_word

getBert("xxbertfridgebertyy")

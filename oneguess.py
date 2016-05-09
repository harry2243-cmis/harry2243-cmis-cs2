import random

def numberRange(minimum, maximum):
    return random.randint(minimum, maximum)

def output(result, PlayerGuess, wrong):
    if result == PlayerGuess:
        print """The target was {}
Your guess was {}
That's correct!""".format(result, PlayerGuess)
    else:
        print """The target was {}
Your guess was {}
{}""".format(result, PlayerGuess, wrong)

def PlayerResult(result, PlayerGuess):
    if result > PlayerGuess:
        sub = abs(PlayerGuess - result)
        return "That is under by {}".format(sub)
    else:
        add = abs(PlayerGuess - result)
        return "That is over by {}".format(add)

def main():
    minimum = int(raw_input("What is the minimum number? "))
    maximum = int(raw_input("What is the maximum number? "))
    print "I am thinking of a number from {} to {}".format(minimum, maximum)
    PlayerGuess = int(raw_input("What do you think it is?: "))
    result = int(numberRange(minimum, maximum))
    wrong = PlayerResult(result, PlayerGuess)
    return output(result, PlayerGuess, wrong)

main()

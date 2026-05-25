def rps(fist1, fist2):
    if fist1 == "rock": 
        return "paper" if fist2 == "paper" else "rock" # return paper cause it wins rock, if not rock wins
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper" # return scissors
    else:
        return "rock" if fist2 == "rock" else "scissors"
    

print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# 1. paper, rock -> paper rock 
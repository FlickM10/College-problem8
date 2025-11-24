import random

N = int(input("Enter the number of rounds to play : "))

Initial_roll = random.randint(1, 6)
print(f"The initial Roll was {Initial_roll}.")

Wins = 0

for i in range(N):
    Pred = input("Enter the Prediction for the next roll (High, Tie, Low) : ")
    Roll = random.randint(1, 6)
    if Roll > Initial_roll:
        Pred_real = 'High'
    if Roll == Initial_roll:
        Pred_real = 'Tie'
    if Roll < Initial_roll:
        Pred_real = 'Low'
    if Pred_real == Pred:
        print("Correct!!!!")
        Wins = Wins + 1
    else:
        print("Incorrect :( ")
    print(f"The dice value was {Roll}.")
    
print(f"The number of rounds played = {N}")

Win_percent = (Wins * 100) / N
print(f"Percent Wins : {Win_percent}")


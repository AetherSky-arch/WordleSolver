with open("dict", "r") as file:
    words = file.read().split('\n')

lenof_dict = len(words)

forbidden1 = []
forbidden2 = []
forbidden3 = []
forbidden4 = []
forbidden5 = []

somewhere = []

counter = 0

solution = ['-', '-', '-', '-', '-']
guess = input("Input initial guess. \"slate\" is a recommended starting word.\n>>> ")

def is_working(guess):
    for letter in somewhere:
        if not letter in guess:
            return False
    i = 0
    while i < 5:
        if solution[i] != '-':
            if solution[i] != guess[i]:
                return False
        i += 1
    if guess[0] in forbidden1 or (guess[0] != solution[0] and solution[0] != '-'):
        return False
    if guess[1] in forbidden2 or (guess[1] != solution[1] and solution[1] != '-'):
        return False
    if guess[2] in forbidden3 or (guess[2] != solution[2] and solution[2] != '-'):
        return False
    if guess[3] in forbidden4 or (guess[3] != solution[3] and solution[3] != '-'):
        return False
    if guess[4] in forbidden5 or (guess[4] != solution[4] and solution[4] != '-'):
        return False
    return True

feed = "-----"

while (counter < lenof_dict):
    feed = input("Input Wordle feedback :\n (-) for nonexistent letter\n (x) for misplaced letter\n (o) for correctly placed letter\n>>> ")
    if feed == "ooooo":
        break
    i = 0
    while i < 5:
        if feed[i] == '-':
            forbidden1.append(guess[i])
            forbidden2.append(guess[i])
            forbidden3.append(guess[i])
            forbidden4.append(guess[i])
            forbidden5.append(guess[i])
        if feed[i] == 'x':
            if (i == 0):
                forbidden1.append(guess[i])
            if (i == 1):
                forbidden2.append(guess[i])
            if (i == 2):
                forbidden3.append(guess[i])
            if (i == 3):
                forbidden4.append(guess[i])
            if (i == 4):
                forbidden5.append(guess[i])
            somewhere.append(guess[i])
        if feed[i] == 'o':
            solution[i] = guess[i]
        i += 1
    while not is_working(words[counter]):
        counter += 1
    guess = words[counter]
    print("\nguess : " + words[counter])

if counter >= lenof_dict:
    print("No solutions found in given dictionary.")
else:
    print("Success !")

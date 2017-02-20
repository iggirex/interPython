f = open("scores.txt", "w")

while True:
    participant = raw_input("Parcticipant name > ")

    if participant == "quit":
        print("Quitting...")
        break

    score = input("Score for " + participant + "> ")
    f.write(participant + "," + str(score) + "\n")

f.close()
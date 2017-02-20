capitals_dic={
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfurt",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "South Dakota": "Pierre",
    "Tennesse": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Seattle",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

import random
correct = 0
wrong = 0

states = list(capitals_dic.keys())
print(states)

for i in range(5):
    state = random.choice(states)
    capital = capitals_dic[state]
    guess = raw_input("What is the capital of " + str(state) + "?")
    if guess == capital:
        print("You're Correct!")
        correct+=1
    else:
        print("You missed this one! The right answer is " + capital)
        wrong+=1
if(correct == 5):
    print("You're AMAZEBALLS! You got all 5 correct!")
elif( 2 < correct < 5):
    print("You did well, you got " + str(correct) + " right." )
elif(correct == 2):
    print("You did not do well you got 2 right.")
else:
    print("wow you suck you got 1 right")
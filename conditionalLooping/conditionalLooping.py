for i in [1,2,3,4,5]:
    print("Helloworld %s" % str(i) )

counter = 0
while counter < 5:
    print("YoYoYo %s" % counter)
    counter += 1

counter2 = 0
while True:
    print "yoDIGGITYY"
    counter2 +=1
    if counter2 >= 5:
        break

print("Hello Human!!")

while True:
    user_input = raw_input("> ")
    if user_input == "quit":
        print("Goodyby human!")
        break
    else:
        print(user_input)
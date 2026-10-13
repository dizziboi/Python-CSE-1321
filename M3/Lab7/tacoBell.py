def notEat(word,num):
    for i in range(1,num):
        print("I will not eat to", word)
food = input("what will you not eat: ")
times = int(input("How many times: "))

notEat(food,times)
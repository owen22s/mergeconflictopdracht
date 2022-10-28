import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():
    return ["On a day in spring. We saw a hawk descending"]

#zet hier je haiku functie neer, zie https://github.com/progsen/haikugitopdracht voor ideeen

haikus = [
    basicHaiku()
]

def randomHaiku():
    return random.choice(haikus)

def start():
    print("starting main")
    
    print(randomHaiku())

    pass


start()
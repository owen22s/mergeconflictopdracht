import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():
<<<<<<< HEAD
    return ["Toward those short trees","we saw a big bird","On a day in spring."]
=======
    return ["On a day in spring. We saw a hawk descending"]
>>>>>>> feuture

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

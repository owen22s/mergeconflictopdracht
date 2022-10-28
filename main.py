import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():
<<<<<<< HEAD
<<<<<<< HEAD
    return ["Toward those short trees","we saw a big bird","On a day in spring."]
=======
    return ["On a day in spring. We saw a hawk descending"]
>>>>>>> feuture
=======
    return ["Toward those short trees","We saw a hawk descending","On a day in spring."]
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

import art
import details
import random
print(art.art1)
score=0
print("welcome to higher lower game ! guess the fame of the persons\n")

while(True):
    rand_per=random.choice(details.persons)
    print(f"compare a :{rand_per["name"]} is {rand_per["job"]}")
    f1=int(rand_per["followers"])
    print(art.vs)
    rand_per=random.choice(details.persons)
    print(f"compare b :{rand_per["name"]} is {rand_per["job"]}")
    f2=int(rand_per["followers"])
    print("who has more followers\n")
    ans=input()
    if ans=='a':
        if f1>f2:
            score=score+1
            print("\n"*100)
            print(f"your score is {score}")
        else:
            print("you lost!!!!!!")
            print(f"your score is {score}")
            exit(0)
    elif ans=='b':
        if f2>f1:
            score=score+1
            print("\n"*100)
            print(f"your score is {score}") 
        else:
            print("you lost!!!!!!")
            print(f"your score is {score}")
            exit(0)   
    else:
        raise Exception("incorrect value!!!!")
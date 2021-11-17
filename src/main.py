import game_data
import random

print("Welcome to higher/lower game")

gameFinished=False

def GetRandom():
    ranChoice=random.randint(0,len(game_data.data)-1)
    return ranChoice
def GetPerson():
    person=[]
    data_person=game_data.data[GetRandom()]
    person.append(data_person["name"])
    person.append(data_person["follower_count"])
    person.append(data_person["description"])
    person.append(data_person["country"])
    return person
    # print(game_data.data[ranChoice]["name"]+","
    #       +game_data.data[ranChoice]["description"]+","+game_data.data[ranChoice]["country"])
    
def game():
    global gameFinished
    first=GetPerson()
    print(f"First person is {first[0]},{first[2]},{first[3]}")
    second=GetPerson()
    print("VS")
    print(f"Second person is {second[0]},{second[2]},{second[3]}")
    choice = int(input("Select the pereson with the highest follower count\ntype 1 for the first and 2 for the second:"))
    if int(first[1])>int(second[1]) and choice==2:
        gameFinished=True
        print(f"Wrong {first[0]} has {first[1]} followers and {second[0]} has {second[1]} followers")
    elif int(first[1])>int(second[1]) and choice==1:
        game()
        print(f"{first[0]}:{first[1]}\n{second[0]}:{second[1]}")
        print("\n\n\n")
    elif int(first[1])<int(second[1]) and choice==1:
        gameFinished=True
        print(f"Wrong {first[0]} has {first[1]} followers and {second[0]} has {second[1]} followers")
    elif int(first[1])>int(second[1]) and choice==2:
        game()
        print(f"{first[0]}:{first[1]}\n{second[0]}:{second[1]}")
        print("\n\n\n")
while gameFinished==False: 
    game()

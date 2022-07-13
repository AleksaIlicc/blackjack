import random

def showcards(players_list, sumoflist, computers_first_card):
    print(f"    Your cards: {players_list}, current score: {sumoflist} ")
    print(f"    Computer's first card: {computers_first_card}")

def finalhands(your_list, computers_list, sum_of_your_cards, sum_of_computers_cards):
    print(f"    Your final hand:{your_list}, final score: {sum_of_your_cards}")
    print(
        f"    Computer's final hand:{computers_list}, final score: {sum_of_computers_cards}")

def summinglist(list):
    sumofcards = 0
    for card in list:
        sumofcards += card
    return sumofcards

def aces(list):
    exist_count = list.count(11)
    if exist_count >0:
        first_index = list.index(11)
        list[first_index] = 1

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end_of_game = False
while end_of_game == False:
    playagame = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if playagame == "y":
        listofcards = [random.choice(cards), random.choice(cards)]
        sumofmycards = summinglist(listofcards)

        computerslist = [random.choice(cards), random.choice(cards)]
        sumofcomputerscards = summinglist(computerslist)

        while sumofcomputerscards < 17:
            computerslist.append(random.choice(cards))         
            sumofcomputerscards = summinglist(computerslist)
        if summinglist(computerslist)>21:
                aces(computerslist)

        showcards(listofcards, sumofmycards, computerslist[0])  

        if sumofmycards == 21:
            print("You win, it's a Blackjack!")                
            another_card = "random"                                   
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        while another_card == "y":
            listofcards.append(random.choice(cards))
            if summinglist(listofcards)>21:
                aces(listofcards)
            sumofmycards = summinglist(listofcards)             
            showcards(listofcards, sumofmycards, computerslist[0])  
            if sumofmycards < 21:
                another_card = input(
                    "Type 'y' to get another card, type 'n' to pass: ")
            else:
                finalhands(listofcards, computerslist,
                           sumofmycards, sumofcomputerscards)
                print("You went over. You lose")
                another_card="random"
        if another_card == "n":
            finalhands(listofcards, computerslist,
                       sumofmycards, sumofcomputerscards)
            if sumofcomputerscards > 21:
                print("Computer went over. You win")
            if sumofmycards == sumofcomputerscards:
                print("It's a draw.")
            computercheck = 21-sumofcomputerscards
            mycheck = 21-sumofmycards
            if computercheck < mycheck:
                print("You lose.")
            else:
                print("You win.")
    else:
        end_of_game = True

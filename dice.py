import random
import time

auth_user = ["User0", "User1", "User2"]
password = "1234"
j = 0
i = 0
while i == 0:
    user1 = input("Enter username for player 1: ")
    user2 = input("Enter username for player 2: ")
    if user1 and user2 in auth_user:
        while j == 0:
            pass1 = input("Enter password for player 1 and 2: ")
            if pass1 == password:
                print("Access granted to play the game")
                j = 1
            else:
                print("Try again")
                j = 0
        print("-----------------------------------------------------------------------\n")
        print("Game Begins")
        time.sleep(2)

        tscore1 = 0
        tscore2 = 0
        users = [user1, user2]
        even = [2, 4, 6, 8, 10, 12]
        odd = [1, 3, 5, 7, 9, 11]
        for r in range(1, 6):
            print("-----------------------------------------------------------------------\n")
            print("Round", r, "begins")
            # time.sleep(1)
            dice1 = random.randint(0, 6)
            dice2 = random.randint(0, 6)
            print("You have rolled", dice1, ",", dice2)
            tdice1 = dice1 + dice2
            print("The total dice score is", tdice1)
            # time.sleep(1)
            score2 = 0
            if tdice1 in even:
                score1 = tdice1 + 10
                print("You have gained 10 bonus points because your number is even. Your score now is:", score1)
            elif tdice1 in odd:
                score1 = tdice1 - 5
                print("You have lost 5 points because your number is odd. Your score now is:", score1)
            elif dice1 == dice2:
                print("You have got the same numbers so you have a second throw. ")
                # time.sleep(1)
                dice3 = random.randint(0, 6)
                dice4 = random.randint(0, 6)
                print("You have rolled", dice3, "and", dice4, "on your second throw")
                score1 = tdice1 + dice3 + dice4
                if tdice1 in even:
                    score1 = score1 + 10
                elif tdice1 in odd:
                    score1 = score1 - 5
                else:
                    print("You have gained no bonus points")
                print("You have gained points. Your score now is:", score1)
            else:
                print("You have gained no bonus points")
            if score1 < 0:
                score1 = 0
            else:
                print("You have a positive score")
            tscore1 = score1 + tscore1
            print("The total score for", user1, "is", tscore1)
            time.sleep(1)
            Rest1 = input("Press Enter to continue")
            print("-----------------------------------------------------------------------\n")
            print("Round", r, "continues")
            # time.sleep(1)
            dice5 = random.randint(0, 6)
            dice6 = random.randint(0, 6)
            print("You have rolled", dice5, ",", dice6)
            tdice2 = dice5 + dice6
            print("The total dice score is", tdice2)
            # time.sleep(1)
            score2 = 0
            if tdice2 in even:
                score2 = tdice2 + 10
                print("You have gained 10 bonus points because your number is even. Your score now is:", score2)
            elif tdice2 in odd:
                score2 = tdice2 - 5
                print("You have lost 5 points because your number is odd. Your score now is:", score2)
            elif dice5 == dice6:
                print("You have got the same numbers so you have a second throw. ")
                # time.sleep(1)
                dice7 = random.randint(0, 6)
                dice8 = random.randint(0, 6)
                print("You have rolled", dice7, "and", dice8, "on your second throw")
                score2 = tdice2 + dice7 + dice8
                if tdice2 in even:
                    score2 = score2 + 10
                elif tdice2 in odd:
                    score2 = score2 - 5
                else:
                    print("You have gained no bonus points")
                print("You have gained points. Your score now is:", score2)
            else:
                print("You have gained no bonus points")
            if score2 < 0:
                score2 = 0
            else:
                print("You have a positive score")
            tscore2 = score2 + tscore2
            print("The total score for", user2, "is", tscore2)
            time.sleep(1)
        if tscore1 > tscore2:
            print(user1, "has won with", tscore1, "points.", user2, "had", tscore2, "points")
            f = open("test.txt", "a")
            f.write("\n")
            f.write(user1)
            f.write(" 's score: ")
            f.write(str(tscore1))
            f.close()
        elif tscore1 < tscore2:
            print(user2, "has won with", tscore2, "points.", user1, "had", tscore1, "points")
            f = open("test.txt", "a")
            f.write("\n")
            f.write(user2)
            f.write(" 's score: ")
            f.write(str(tscore2))
            f.close()
        elif tscore1 == tscore2:
            print("Both players have", tscore1, "so to decide the winner, both players will roll the dice once.")
            p = 0
            while p == 1:
                dice9 = random.randint(0, 6)
                dice10 = random.randint(0, 6)
                print(user1, "has rolled", dice9)
                time.sleep(1)
                print(user2, "has rolled", dice10)
                if dice9 > dice10:
                    print(user1, "has won")
                    p = 1
                elif dice9 < dice10:
                    print(user2, "has won")
                    p = 1
                else:
                    print("Both users have the same value, so roll again")
                    p = 0
        print("-----------------------------------------------------------------------\n")
        print("The Top 5 scores of all time: ")
        time.sleep(1)

        file1 = open('test.txt', 'r')
        ls = file1.readlines()
        scores = {}
        count = 1
        for line in ls:
            scores[int(line.split(':')[1].strip())] = line.split("'")[0].strip()
        scores_items = scores.items()
        sorted_scores = sorted(scores_items, reverse=True)
        for y in sorted_scores:
            print(count, y[1], ":", y[0])
            count += 1
            if count > 5:
                break
            else:
                continue

        i = 1
    else:
        i = 0
        print("Try Again\n-----------------------------------------------------------------------\n")
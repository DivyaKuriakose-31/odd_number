def stick_game():
    print("Welcome to the stick game!!")
    print("Rules of the game are")
    print("You can pick 1,2, or 3 sticks in one turn")
    print("The player who picks the last stick lose")
    no_of_sticks=16
    player1=input("Enter the name of first player:")
    player2=input("Enter the name of second player:")
    print("Game started!!")
    remaining_sticks=no_of_sticks
    while(remaining_sticks>0):
        input_value_1=int(input(f"{player1},Pick 1,2,or 3 sticks:"))
        if (input_value_1 > 3):
            print("You can't choose more than 3 sticks")
        else:
            remaining_sticks-=input_value_1
            print(f"Remaining sticks are:{remaining_sticks}")
        input_value_2=int(input(f"{player2},pick 1,2, or 3 sticks:"))
        if(input_value_2>3):
            print("You can't choose sticks more than 3")
        else:
            remaining_sticks-=input_value_2
            print(f"Remaining sticks are:{remaining_sticks}")
    if(remaining_sticks<=1):
        print("You lose")



stick_game()








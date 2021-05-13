import random

options = ("1", "2", "3")


def select_option():
    option_selected = input("""
    Choose your weapon:
    1) Rock
    2) Papper
    3) Scissors
    
    Choose: """
                            )
    return option_selected


def battle():

    pc_count = 0
    player_count = 0
    while pc_count <= 2 and player_count <= 2:
        pc = random.choice(options)
        player = select_option()
        if pc == "1" and player == "1":
            print("TIE")
        elif pc == "1" and player == "2":
            player_count += 1
        elif pc == "1" and player == "3":
            pc_count += 1
        elif pc == "2" and player == "1":
            pc_count += 1
        elif pc == "2" and player == "2":
            print("TIE")
        elif pc == "2" and player == "3":
            player_count += 1
        elif pc == "3" and player == "1":
            player_count += 1
        elif pc == "3" and player == "2":
            pc_count += 1
        elif pc == "3" and player == "3":
            print("TIE")
        else:
            print("Select a valid option")
        print(f"""
        Score:
        Pc: {pc_count}
        Player: {player_count}""")
    if pc_count > 2:
        print("PC Win!")
    elif player_count > 2:
        print("Player Win!")


def run():
    battle()


if __name__ == "__main__":
    run()

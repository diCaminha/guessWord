def play():
    secret_word = "banana"

    status = ["_", "_", "_", "_", "_", "_"]

    win = False
    game_over = False
    turn = 0

    while (not win and not game_over):
        turn += 1
        letter = input("guess a letter in the word: ")
        index = 0
        for i in secret_word:
            if i == letter:
                status[index] = letter
            index += 1
        print("turn: ", turn)
        print("status: ", status)
        win = "_" not in status
        game_over = turn == 10 and not win

if(__name__ == "__main__"):
    play()
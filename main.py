import random


def play():

    file = open("bucket_words.txt", "r")
    words = []
    for row in file:
        words.append(row.strip())

    print(words)

    position = random.randrange(0, len(words))
    secret_word = words[position].upper()

    status = ["_", "_", "_", "_", "_", "_"]

    win = False
    game_over = False
    turn = 0

    while (not win and not game_over):
        turn += 1
        guess = input("guess a letter in the word: ")
        guess = guess.strip()
        index = 0
        for letter in secret_word:
            if (guess.upper() == letter.upper()):
                status[index] = guess
            index += 1
        print("turn: ", turn)
        print("status: ", status)
        win = "_" not in status
        game_over = turn == 10

    if win:
        print ("end of game. You win")
    else:
        print ("end of game. You lost")

    file.close()


if __name__ == "__main__":
    play()

def minion_game(string):
    vowels = 'AEIOU'
    player1_score = 0
    player2_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            player1_score += length - i
        else:
            player2_score += length - i

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Example usage
word = input("Enter a word: ")
minion_game(word)

'''
Output
Enter a word: BANANA
Player 2 wins!
'''
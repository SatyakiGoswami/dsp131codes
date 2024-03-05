from collections import Counter

def find_winner(votes):
    vote_count = Counter(votes)
    winner = vote_count.most_common(1)[0][0]

    return winner
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie']
winner = find_winner(votes)
print("The winner of the election is:", winner)
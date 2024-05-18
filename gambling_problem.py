import random

def play_game():
    heads = 0
    tails = 0
    flips = 0
    sequence = []
    
    while abs(heads - tails) < 3:
        flip = random.randint(0, 9)
        if flip < 5:
            heads += 1
            sequence.append('H')
        else:
            tails += 1
            sequence.append('T')
        flips += 1

    return flips, sequence

def simulate_games(num_games):
    total_flips = 0
    total_cost = 0
    total_return = 0
    results = []

    for game in range(num_games):
        flips, sequence = play_game()
        total_flips += flips
        cost = flips  # 1 Re. per flip
        if flips <= 8:
            return_money = 8
        else:
            return_money = 0
        total_cost += cost
        total_return += return_money
        results.append((game + 1, flips, cost, return_money, ''.join(sequence)))

    return results, total_flips, total_cost, total_return

def main():
    num_games = 20  # Number of games to simulate
    results, total_flips, total_cost, total_return = simulate_games(num_games)

    # Display the results in tabular form
    print(f"{'Game':<10} {'Flips':<10} {'Cost (Rs)':<10} {'Return (Rs)':<12} {'Sequence':<20}")
    print("-" * 70)
    for result in results:  # Displaying all results
        game, flips, cost, return_money, sequence = result
        print(f"{game:<10} {flips:<10} {cost:<10} {return_money:<12} {sequence:<20}")
    
    print("\nSummary:")
    print(f"Total games played: {num_games}")
    print(f"Total flips: {total_flips}")
    print(f"Total cost: Rs. {total_cost}")
    print(f"Total return: Rs. {total_return}")
    print(f"Average flips per game: {total_flips / num_games:.2f}")
    print(f"Net gain/loss: Rs. {total_return - total_cost}")

if __name__ == "__main__":
    main()

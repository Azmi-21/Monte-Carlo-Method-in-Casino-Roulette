from logic import compute_init_odds, compute_next_spin_odds

def main():
    print("Hello and welcome to the Monte Carlo Method implementation in the context of Casino Roulette!\n \n")
    print("This program is made for fun and research purposes only. Its goal is to discover and understand the famous Monte Carlo Method. This system predicts the modified odds of landing each of the colors in the classical European casino roulette based on the previous results.\n \n")  
    
    results = []

    # Initial input validation
    while True:
        init_results = input("Please enter the latest results of the roulette game separated by a space: ")
        init_results = init_results.split()

        processed = []
        invalid = []

        for val in init_results:
            try:
                num = int(val)
                if 0 <= num <= 36:
                    processed.append(num)
                else:
                    invalid.append(val)
            except ValueError:
                invalid.append(val)

        if invalid:
            print("Invalid input(s):", invalid)
            print("Please try again.\n")
        else:
            print("All outcomes are valid")
            break
    
    results.extend(processed)
   
    # Compute & display initial odds
    (green_odds, black_odds, red_odds), counts, n = compute_init_odds(processed)
    
    print(f"Based on your last {n} spins:")
    print(f"  Green odds: {green_odds:.4f}")
    print(f"  Black odds: {black_odds:.4f}")
    print(f"  Red odds:   {red_odds:.4f}\n")

    # ask user how many future spins to project -- This is the first version where the system relied on 
    # the expected future spins to rebalance the odds. 
    '''
    while True:
        try:
            m = int(input("Enter the number of future spins you want to project to rebalance (e.g., 50): "))
            if m > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Compute new odds
    q_green, q_black, q_red = compute_next_spin_odds(counts, n)
    
    print(f"\nTo converge to perfect odds after {m} more spins, the required future odds would be:")
    print(f"  Green: {q_green:.4f}")
    print(f"  Black: {q_black:.4f}")
    print(f"  Red:   {q_red:.4f}\n")
    '''

    # ask user for the next spin -- This is the second version where the system relies on 
    # the next spin to rebalance the odds (spin by spin rebalance)
    while True:
        spin = input("Enter the next roulette outcome (0–36), or 'q' to quit: ")

        if spin.lower() == 'q':
            print("Exiting... Hopefully you did not lose the house! 🙏")
            break

        try:
            num = int(spin)
            if 0 <= num <= 36:
                results.append(num)
            else:
                print("Invalid number. Please enter between 0 and 36.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
            continue

        # recompute odds with new results
        (green_odds, black_odds, red_odds), counts, n = compute_init_odds(results)

        print(f"\nAfter {n} spins:")
        print(f"  Green odds: {green_odds:.4f}")
        print(f"  Black odds: {black_odds:.4f}")
        print(f"  Red odds:   {red_odds:.4f}")

        # compute required probabilities for the NEXT spin (m = 1)
        q_green, q_black, q_red = compute_next_spin_odds(counts, n)

        print("\nFor the NEXT spin to help rebalance toward perfect odds:")
        print(f"  Green required prob: {q_green:.4f}")
        print(f"  Black required prob: {q_black:.4f}")
        print(f"  Red required prob:   {q_red:.4f}\n")    

    

if __name__ == "__main__":
    main()

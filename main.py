from logic import compute_init_odds

def main():
    print("Hello and welcome to the Monte Carlo Method implementation in the context of Casino Roulette!\n \n")
    print("This program is made for fun and research purposes only. Its goal is to discover and understand the famous Monte Carlo Method. This system predicts the modified odds of landing each of the colors in the classical European casino roulette based on the previous results.\n \n")  
    
    
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

        green_perfect_odds = 1/38
        black_perfect_odds = 19/38
        red_perfect_odds = 19/38
        
        green = [0]
        black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

    green_odds, black_odds, red_odds = compute_init_odds(processed)
    
    
    

    

if __name__ == "__main__":
    main()

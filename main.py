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

        


    

    

if __name__ == "__main__":
    main()

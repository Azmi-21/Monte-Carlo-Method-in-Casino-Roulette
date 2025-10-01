def compute_init_odds(init_results):
    # define number categories
    green = [0]
    black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    
    # initialize counters
    green_count = 0
    black_count = 0
    red_count = 0
    
    # count occurrences of each color
    for num in init_results:
        if num in green:
            green_count += 1
        elif num in black:
            black_count += 1
        elif num in red:
            red_count += 1

    # compute number of spins
    n = len(init_results)
    if n == 0:  # avoid division by zero
        return (0,0,0), (0,0,0), (0,0,0)

    # compute current game odds based on user input
    green_odds = green_count / n
    black_odds = black_count / n
    red_odds = red_count / n
    
    # return computed odds, counts, and number of spins
    return (green_odds, black_odds, red_odds), (green_count, black_count, red_count), n


def compute_next_spin_odds(counts, n):
    # Perfect odds
    green_p = 1/37
    black_p = 18/37
    red_p = 18/37

    # Current odds
    c_green, c_black, c_red = counts

    # formula for q_i (modified odds) with m = 1 (very next spin)
    q_green = green_p * (n + 1) - c_green
    q_black = black_p * (n + 1) - c_black
    q_red   = red_p   * (n + 1) - c_red

    # return modified odds
    return q_green, q_black, q_red
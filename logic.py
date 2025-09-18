def compute_init_odds(init_results):
    green = [0]
    black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    
    green_count = 0
    black_count = 0
    red_count = 0
    
    for num in init_results:
        if num in green:
            green_count += 1
        elif num in black:
            black_count += 1
        elif num in red:
            red_count += 1
        
    green_odds = green_count / len(init_results)
    black_odds = black_count / len(init_results)
    red_odds = red_count / len(init_results)
    
    return green_odds, black_odds, red_odds
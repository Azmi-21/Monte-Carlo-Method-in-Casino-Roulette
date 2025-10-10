# Monte-Carlo-Method-in-Casino-Roulette
## Overview
This project explores the Monte Carlo Method in the context of European casino roulette, focusing on color-based outcomes (Red, Black, Green).
It is designed for educational and research purposes only, to simulate and visualize how probabilities evolve based on previous results.

**DISCLAIMER**: This program does not guarantee prediction accuracy. Roulette spins are statistically independent events and any perceived “pattern” is an illusion often called the Gambler’s Fallacy.

## Project Goal
The goal of this system is to:
* Compute the current odds of each roulette color (green, red, black) based on past spins.
* Continuously update and display new adjusted odds after each additional spin.
* Demonstrate how the Monte Carlo principle and law of large numbers apply to random systems like roulette.

## Core Concepts
1. Monte Carlo Method

The Monte Carlo method relies on repeated random sampling to estimate numerical results.
In this project, it’s used to illustrate how observed outcomes (past spins) are supposed to approach theoretical probabilities as more spins are recorded.

2. Law of Large Numbers

As the number of samples N increases, the observed proportions of outcomes converge to their theoretical values:
* Green → 1/37
* Red → 18/37
* Black → 18/37

3. Gambler’s Fallacy

The mistaken belief that past results influence future outcomes.
Example: believing “Red is due” after a long streak of Black.
While the program updates odds for educational purposes, it’s crucial to remember that each roulette spin remains independent.

## How It Works

This project simulates **roulette odds estimation** using a simplified interpretation of the **Monte Carlo method**.

1. **Initial Data Entry**  
   - The user starts by entering as many previous roulette outcomes as possible (numbers between 0–36).  
   - Each number corresponds to a color.

2. **Initial Odds Calculation**  
   - The program counts how many times each color appeared in the input.  
   - It then divides these counts by the total number of spins to compute the *current empirical odds*.
   - These odds represent what the roulette currently “looks like” based on your provided history.

3. **Monte Carlo Adjustment (Rebalancing)**  
   - The program assumes that in the long run, odds should converge to their theoretical values:
     - Green = **1/37**
     - Red = **18/37**
     - Black = **18/37**
   - Given your current observed odds and total spins `n`, the system computes **adjusted probabilities** that would bring the long-term distribution closer to the ideal odds after more spins.

4. **Iterative Updates**  
   - After each new spin, the user inputs the latest result.  
   - The program recalculates the updated odds instantly, showing how the new outcome affects convergence toward the theoretical balance.


### **Please do not bet your house on red**

Author: Azmi Abidi

Language: Python

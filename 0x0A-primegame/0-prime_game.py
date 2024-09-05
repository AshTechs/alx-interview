#!/usr/bin/python3
"""This implements the Prime Game function"""

def sieve_of_eratosthenes(n):
    """Uses the Sieve of Eratosthenes to find all primes <= n."""
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return is_prime

def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    
    Parameters:
    x: number of rounds
    nums: list of n for each round
    
    Returns:
    Name of the player with the most wins or None if no clear winner
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + (1 if primes[i] else 0)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_moves[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

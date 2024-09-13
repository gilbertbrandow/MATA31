import numpy as np

def main():
    N = error_approximation(1/1000)
    print(logarithm_of_2_estimate(N))

def compute_lower_bound(N: int) -> float: 
    return sum(1/denominator for denominator in range(N+1, 2*N))
        
def compute_upper_bound(N: int) -> float:
    return sum(1/denominator for denominator in range(N-1, 2*N - 1)) 

def logarithm_of_2_estimate(N: int) -> float: 
    return (compute_upper_bound(N=N) + compute_lower_bound(N=N)) / 2

def error_approximation(error_margin: float) -> int: 
    return int(1 / (2 * error_margin)) + 1

if __name__ == "__main__":
    main()
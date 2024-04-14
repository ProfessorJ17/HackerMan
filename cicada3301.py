import time
import threading

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime(number):
    """Print a number with a tab space."""
    print(f"\t{number}", end="")

def loading_sequence():
    print("Loading Cicada3301.iso..")
    print(2, end="") # Print the first prime number
    for i in range(3, 3302):
        if i == 1039:
            time.sleep(7) # Stop for 7 seconds at 1033
        if is_prime(i):
            print_prime(i)
        time.sleep(0.01033) # Wait for 0.01033 seconds before printing the next number

    time.sleep(11) # Wait for 11 seconds before ending
    print("\nCicada3301.iso LOADED.") # Print the loading completion message
    print("\nDone.")

# Run the loading sequence in a separate thread to allow for non-blocking execution
threading.Thread(target=loading_sequence).start()

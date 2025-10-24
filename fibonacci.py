#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)


def get_user_input():
    """Ask the user for how many Fibonacci terms to generate and validate it."""
    while True:
        try:
            n = int(input("How many terms of the Fibonacci sequence do you want? "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_fibonacci(n):
    """Generate a list containing n terms of the Fibonacci sequence."""
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence


def print_sequence(sequence):
    """Print the Fibonacci sequence in a readable format."""
    print("Fibonacci sequence:")
    print(", ".join(map(str, sequence)))


def main():
    """Main program function."""
    num_terms = get_user_input()
    fib_sequence = generate_fibonacci(num_terms)
    print_sequence(fib_sequence)


if __name__ == "__main__":
    main()

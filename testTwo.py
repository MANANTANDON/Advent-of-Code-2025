import os

# Define the path to the input file relative to the script's execution
# You will need to change this path to point to your actual file location.
# Example: INPUT_FILE_PATH = "input.txt" if the file is in the same directory.
INPUT_FILE_PATH = "file2.txt" 
# NOTE: The original C++ path was: "/Users/rob/projects/robvanderleek/adventofcode/2025/01/input.txt"
# If you are running this in a different environment, you must update the path below.

def load_input(filename: str) -> list[tuple[str, int]]:
    """
    Loads instructions from a file. Each line is expected to be
    a direction ('L' or 'R') followed immediately by a distance (integer).
    Example: L10, R50, L123
    """
    instructions: list[tuple[str, int]] = []
    
    # Check if the file exists before attempting to open it
    if not os.path.exists(filename):
        print(f"Error: Input file not found at '{filename}'")
        # Returning an empty list or raising an error would be appropriate
        return instructions

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                direction = line[0]
                # The remaining part of the string is the distance
                distance = int(line[1:])
                instructions.append((direction, distance))
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        # Depending on the desired behavior, you might want to stop execution here
        
    return instructions

def calculate_zeros(instructions: list[tuple[str, int]], count_pass_zero: bool = False) -> int:
    """
    Simulates rotating a dial (0-99) and counts the number of times the dial
    lands on or passes through 0 (or 100, which is 0).

    :param instructions: A list of (direction, count) tuples.
    :param count_pass_zero: If True, counts a zero when the dial wraps around.
    :return: The total count of zeros.
    """
    dial: int = 50  # Initial dial position (0-99)
    zeros: int = 0
    
    for direction, count in instructions:
        # 1. Handle counts >= 100: Separate large movements into full 100 rotations
        if count >= 100:
            if count_pass_zero:
                # Full 100 rotations means passing through 0 (or landing on it)
                zeros += count // 100
            count = count % 100 # Remaining distance

        # 2. Handle 'L' (Left/Decrement) movement
        if direction == 'L':
            next_dial: int = dial - count
            
            if next_dial < 0:
                # The dial has wrapped around 0 (or 100)
                if count_pass_zero and dial > 0:
                    # If we start at > 0 and move left past 0, count a pass
                    zeros += 1
                next_dial = 100 + next_dial # Wrap around (e.g., 1 - 5 = -4. 100 + (-4) = 96)
            
            dial = next_dial

        # 3. Handle 'R' (Right/Increment) movement
        elif direction == 'R':
            next_dial: int = dial + count
            
            if next_dial >= 100:
                # The dial has wrapped around 99 back to 0
                if count_pass_zero and next_dial != 100:
                    # If we move past 100 (e.g., 90 + 20 = 110), count a pass
                    zeros += 1
                next_dial = next_dial % 100 # Wrap around (e.g., 96 + 5 = 101. 101 % 100 = 1)
            
            dial = next_dial
        
        # 4. Final check: Check if the dial lands exactly on 0
        # NOTE: 100 is treated as 0 in the dial logic (due to % 100)
        if dial == 0:
            zeros += 1
            
    return zeros

def part_one():
    """
    Executes the Part One logic (count_pass_zero=False).
    """
    instructions = load_input(INPUT_FILE_PATH)
    if not instructions:
        return
        
    result = calculate_zeros(instructions)
    print(f"Part One Result: {result}")
    
    # Assert is usually used for testing. If this fails, the code or input is wrong.
    # The expected result (1064) depends on the specific contents of the input file.
    # The original C++ code had: assert(result == 1064)

def part_two():
    """
    Executes the Part Two logic (count_pass_zero=True).
    """
    instructions = load_input(INPUT_FILE_PATH)
    if not instructions:
        return
        
    result = calculate_zeros(instructions, count_pass_zero=True)
    print(f"Part Two Result: {result}")
    
    # The expected result (6122) depends on the specific contents of the input file.
    # The original C++ code had: assert(result == 6122)

def main():
    """
    Main entry point for the script.
    """
    print(f"Attempting to load input from: {INPUT_FILE_PATH}")
    part_one()
    print("-" * 20)
    part_two()

if __name__ == "__main__":
    main()
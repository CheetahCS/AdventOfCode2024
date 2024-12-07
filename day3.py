import re

def extract_multiplications(inputfile):
    with open(inputfile, 'r') as file:
        content = file.read()

    # Regular expression to match valid `mul(x,y)` expressions
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, content)


    total = 0
    for match in matches:
        # Extract numbers and compute multiplication
        x, y = map(int, match)
        total += x * y

    return total
def with_conditional(inputfile):
    import re

import re

import re

def handle_instructions(inputfile):
    # Patterns to match instructions
    mul_pattern = r"mul\(\d+,\d+\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    with open(inputfile, 'r') as file:
        lines = file.readlines()

    total = 0
    enabled = True  # `mul` instructions are enabled by default

    for row in lines:
        # Process the entire row using regex
        instructions = re.findall(f"{mul_pattern}|{do_pattern}|{dont_pattern}", row)
        
        for instr in instructions:
            if instr == "don't()":
                enabled = False
            elif instr == "do()":
                enabled = True
            elif instr.startswith("mul(") and enabled:
                # Extract numbers and calculate the product
                x, y = map(int, instr[4:-1].split(','))
                total += x * y

    return total

# Run the function and print the result
print(handle_instructions("day3input.txt"))



print(extract_multiplications("day3input.txt"))
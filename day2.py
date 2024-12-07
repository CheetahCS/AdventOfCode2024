def calcsafe():
    with open("day2input.txt") as file:
        lines = file.readlines()
        safe = 0


        for i in range(len(lines)):
            oneNumber = True
            # Clean and split the line into integers
            line = [int(x.strip()) for x in lines[i].split()]
            
            # Skip lines with fewer than 2 numbers
            if len(line) < 2:
                continue
            
            # Compute differences
            diff = [line[j + 1] - line[j] for j in range(len(line) - 1)]
            
            # Check if all differences are increasing or decreasing
            if all(d > 0 for d in diff) or all(d < 0 for d in diff):
                # Check if all differences are within the safe range
                safeish = all(1 <= abs(d) <= 3 for d in diff)
                if safeish:
                    safe += 1
            elif oneNumber:
                oneNumber = False


        return safe


def calcsafeAdj():
    with open("day2input.txt") as file:
        lines = file.readlines()
        safe = 0

        for i in range(len(lines)):
            # Clean and split the line into integers
            line = [int(x.strip()) for x in lines[i].split()]
            
            # Skip lines with fewer than 2 numbers
            if len(line) < 2:
                continue
            
            # Function to check if a sequence is safe
            def is_safe(sequence):
                # Compute differences
                diff = [sequence[j + 1] - sequence[j] for j in range(len(sequence) - 1)]
                # Check if all differences are increasing or decreasing and within range
                return (all(d > 0 for d in diff) or all(d < 0 for d in diff)) and all(1 <= abs(d) <= 3 for d in diff)

            # Check if the original line is safe
            if is_safe(line):
                safe += 1
                continue

            # Check if removing one level makes it safe
            for j in range(len(line)):
                modified_line = line[:j] + line[j+1:]  # Remove the j-th level
                if is_safe(modified_line):
                    safe += 1
                    break  # No need to check further removals for this line

        return safe
print(calcsafeAdj())

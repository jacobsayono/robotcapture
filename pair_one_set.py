def generate_pairs():
    r_values = []
    p_values = []
    increment = 10.0 / 9  # Increment for 'r' values and 'p' values

    # Generate 'r' values for each quarter
    for quarter in range(4):
        if quarter == 0:  # -170 to -180
            start, end, step = -170, -180, -increment
        elif quarter == 1:  # 180 to 170
            start, end, step = 180, 170, -increment
        elif quarter == 2:  # 170 to 180
            start, end, step = 170, 180, increment
        else:  # -180 to -170
            start, end, step = -180, -170, increment

        while (step < 0 and start >= end) or (step > 0 and start <= end):
            r_values.append(round(start, 5))
            start += step

    # Adjusted generation of 'p' values for each quarter according to new requirements
    for quarter in range(4):
        if quarter == 0:  # 0 to -10
            start, end, step = 0, -10, -increment
        elif quarter == 1:  # -10 to 0
            start, end, step = -10, 0, increment
        elif quarter == 2:  # 0 to 10
            start, end, step = 0, 10, increment
        else:  # 10 to 0
            start, end, step = 10, 0, -increment

        while (step < 0 and start > end) or (step > 0 and start < end):
            next_value = round(start, 5)
            if not (-10 <= next_value <= 10):  # Ensure next_value does not exceed bounds
                break
            p_values.append(next_value)
            start += step
        # Ensure the final value in each range is added correctly within bounds
        final_value = round(start, 5)
        if (-10 <= final_value <= 10) and (not p_values or final_value != p_values[-1]):
            p_values.append(final_value)

    # Pair 'r' and 'p' values
    pairs = list(zip(r_values, p_values))
    return pairs

# Generate and print pairs
r_p_pairs = generate_pairs()

# Open a file named 'pairs.txt' in write mode
with open('pairing.txt', 'w') as file:
    for pair in r_p_pairs:
        # Write each pair to the file, converting the pair to a string
        # Add a newline character after each pair for readability
        file.write(f"{pair}\n")

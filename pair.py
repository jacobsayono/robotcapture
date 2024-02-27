def generate_pairs_with_dynamic_increments_adjusted_fixed():
    all_pairs = []  # List to hold all pairs for 6 loops

    for loop in range(1, 7):
        r_values = []
        p_values = []

        r_start = 180 - 10 * loop
        p_end = 10 * loop

        r_increment = (180 - r_start) / 9
        p_increment = p_end / 9

        # Adjust 'r' values generation
        for i in range(4):
            if i == 0:  # -r_start to -180
                start, end, step = -r_start, -180, -r_increment
            elif i == 1:  # 180 to r_start, avoiding duplicate 180
                start, end, step = 180, r_start, -r_increment
                if r_values[-1] == -180:  # Avoid duplicating -180 as 180
                    r_values.pop()  # Remove the last -180
            elif i == 2:  # r_start to 180
                start, end, step = r_start, 180, r_increment
            else:  # -180 to -r_start, avoiding duplicate -180
                start, end, step = -180, -r_start, r_increment
                if r_values[-1] == 180:  # Avoid duplicating 180 as -180
                    r_values.pop()  # Remove the last 180

            while (step < 0 and start > end) or (step > 0 and start < end):
                r_values.append(round(start, 5))
                start += step
            # Add the end value if not already included to ensure the range is fully covered
            if (step < 0 and end > r_values[-1]) or (step > 0 and end < r_values[-1]):
                r_values.append(round(end, 5))

        # Adjust 'p' values generation
        for i in range(4):
            if i == 0:  # 0 to -p_end
                start, end, step = 0, -p_end, -p_increment
            elif i == 1:  # -p_end to 0
                start, end, step = -p_end, 0, p_increment
            elif i == 2:  # 0 to p_end
                start, end, step = 0, p_end, p_increment
            else:  # p_end to 0
                start, end, step = p_end, 0, -p_increment

            while (step < 0 and start >= end) or (step > 0 and start <= end):
                next_value = round(start, 5)
                if p_values and next_value == p_values[-1]:
                    start += step
                    continue
                p_values.append(next_value)
                start += step

        pairs = list(zip(r_values, p_values))
        all_pairs.extend(pairs)

    return all_pairs

# Generate and print pairs with the refined logic to prevent duplication
r_p_pairs_adjusted_fixed = generate_pairs_with_dynamic_increments_adjusted_fixed()

# Write the adjusted pairs to 'coordinates.txt'
with open('pairs.txt', 'w') as file:
    for pair in r_p_pairs_adjusted_fixed:
        file.write(f"rpy = ({pair[0]}, {pair[1]}, -90)\n")

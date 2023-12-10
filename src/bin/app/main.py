def min_jumps_custom_path_user_input():
    user_input = input("Enter an array of numbers separated by spaces: ")

    if " " not in user_input or not user_input.replace(" ", "").isdigit():
        return "Error: Enter an array of numbers separated by spaces."

    try:
        arr = list(map(int, user_input.split()))
    except ValueError:
        return "Error: All elements must be numbers."

    n = len(arr)
    if n <= 1:
        return 0, []

    jumps = 0
    current = 0
    path = []

    while current < n - 1:
        path.append(arr[current])
        if arr[current] == 1:
            current += 1
            jumps += 1
            continue

        jumps += 1
        next_jump = current + arr[current]
        if next_jump >= n - 1:
            path.append(arr[n - 1])
            break

        max_reach = 0
        next_index = current
        for i in range(1, arr[current] + 1):
            if current + i < n and current + i + arr[current + i] > max_reach:
                max_reach = current + i + arr[current + i]
                next_index = current + i

        if next_index == current:
            path.append(arr[n - 1])
            break
        current = next_index

    return jumps, path

result = min_jumps_custom_path_user_input()
if isinstance(result, tuple):
    jumps, path = result
    print(f"Minimum number of jumps: {jumps}")
    print("Path: " + " -> ".join(map(str, path)))
else:
    print(result)

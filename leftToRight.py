def leftToRight(n, disks):
    # given we have n, n is the number of dark (and light) disks, so we have 2n disks total
    for i in range(n):
        # Traverse from left to right, comparing adjacent pairs
        for j in range(2 * n - 1):
            if disks[j] == 'D' and disks[j + 1] == 'L':
                # Swap dark and light disks
                disks[j], disks[j + 1] = disks[j + 1], disks[j]
        print(f"After pass {i+1}: {disks}")
    return disks


# Without creating a disk class, we can implement this using an array

n = 4  # Number of dark disks (also light disks, so 2n total)
disks = ['D', 'L', 'D', 'L', 'D', 'L', 'D', 'L']  # Alternating dark and light disks
print("Initial state:", disks)
result = leftToRight(n, disks)
print("Final state:", result)
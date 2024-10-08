def lawnmower(n, disks):
    # given we have n, n is the number of dark (and light) disks, so we have 2n disks total

    
    for i in range(n // 2):
        # Pass through, from left to right
        for j in range(2 * n - 1):
            if disks[j] == 'D' and disks[j + 1] == 'L':
                # Swap dark and light disks
                disks[j], disks[j + 1] = disks[j + 1], disks[j]
        
        print(f"After left-to-right pass {i+1}: {disks}")
        
        # Pass through, from right to left
        for j in range(2 * n - 1, 0, -1):
            if disks[j] == 'L' and disks[j - 1] == 'D':
                # Swap light and dark disks
                disks[j], disks[j - 1] = disks[j - 1], disks[j]
        
        print(f"After right-to-left pass {i+1}: {disks}")
    
    return disks

# Without creating a disk class, we can implement this using an array as well

n = 4  # Number of dark disks (also light disks, so 2n total)
disks = ['D', 'L', 'D', 'L', 'D', 'L', 'D', 'L']  # Alternating dark and light disks
print("Initial state:", disks)
result = lawnmower(n, disks)
print("Final state:", result)
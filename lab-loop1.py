for num in range(45, 211):  # 211 because range goes up to n-1
    if num == 100:
        continue  # Skip number 100
    if num == 205:
        break  # Stop the loop at 205
    print(num)
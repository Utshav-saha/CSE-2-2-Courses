# Problem 2

import numpy as np

s = int(input())
m = int(input())

matrix = np.zeros((s, m), dtype=int)

for x in range(s):
    row = input().split()
    for y in range(m):
        matrix[x][y] = int(row[y])

vector = np.zeros(m)

for i in range(m):
    vector[i] = int(input())

k = int(input())

percentage_matrix = np.zeros((s, m), dtype=int)

for x in range(s):
    for y in range(m):
        percentage_matrix[x][y] = 100 * matrix[x][y] / vector[y]
        print(percentage_matrix[x][y])
    print()  
        


# matrix[x, :] = row x, matrix[:, y] = column y
print("Salesperson Summary:")
for x in range(s):
    avg_percentage = np.mean(percentage_matrix[x])
    best_product = np.argmax(percentage_matrix[x])
    print(f"Salesperson {x}: Average Achievement = {avg_percentage:.2f}%, "
          f"Best Product = {best_product}")

print("Product Summary:")
for y in range(m):
    avg_percentage = np.mean(percentage_matrix[:,y])
    best_product = np.argmax(percentage_matrix[:,y])
    print(f"Product {y}: Average Achievement = {avg_percentage:.2f}%, "
          f"Best Salesperson = {best_product}")

# axis = 0 → column-wise operation
# axis = 1 → row-wise operation

avg_percentages = np.mean(percentage_matrix, axis=1)
top_k_ids = np.argsort(avg_percentages)[::-1]
top_k_ids = top_k_ids[:k]

print(f"Top {k} Salesperson IDs: {top_k_ids}")


conditions = [
    percentage_matrix >= 90,
    (percentage_matrix >= 75) & (percentage_matrix < 90),
    (percentage_matrix >= 60) & (percentage_matrix < 75),
    percentage_matrix < 60
]
grades = ["Excellent", "Good", "Average", "Poor"]


# np.select(conditions, grades) — element-wise: for each cell, it checks the conditions in order and picks the matching label from grades.
grade_matrix = np.select(conditions, grades, default="Unknown")

# flattens the matrix, finds each distinct grade string, and counts how many times it occurs. Returns two parallel arrays: unique (the distinct labels) and counts (their counts).
unique, counts = np.unique(grade_matrix, return_counts=True)

# zips those two arrays into {grade: count} pairs.
grade_counts = dict(zip(unique, counts))


for grade in grades:
    print(f"{grade}: {grade_counts.get(grade, 0)}")

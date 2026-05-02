import numpy as np

# 1. Create the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# 2. Calculate mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_deviation = np.std(grades)

# 3. Find maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# 4. Sort grades in ascending order
sorted_grades = np.sort(grades)

# 5. Find the index of the highest grade
index_highest = np.argmax(grades)

# 6. Count and calculate percentage of students scoring above 90
count_above_90 = np.sum(grades > 90)
percent_above_90 = (count_above_90 / grades.size) * 100

# 7. Calculate percentage of students scoring below 75
count_below_75 = np.sum(grades < 75)
percent_below_75 = (count_below_75 / grades.size) * 100

# 8. Extract high performers and passing grades into new arrays
high_performers = grades[grades > 90]
passing_grades = grades[grades > 75]

# Print all results
print("Grades Array:", grades)
print(f"Mean: {mean_grade}")
print(f"Median: {median_grade}")
print(f"Standard Deviation: {std_deviation:.2f}")
print(f"Maximum Grade: {max_grade}")
print(f"Minimum Grade: {min_grade}")
print("Sorted Grades:", sorted_grades)
print(f"Index of Highest Grade: {index_highest}")
print(f"Number of students above 90: {count_above_90}")
print(f"Percentage above 90: {percent_above_90}%")
print(f"Percentage below 75: {percent_below_75}%")
print("High Performers (>90):", high_performers)
print("Passing Grades (>75):", passing_grades)

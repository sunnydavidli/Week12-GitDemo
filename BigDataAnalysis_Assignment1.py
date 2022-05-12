import pandas as pd

students = pd.read_csv("./datasets/students.csv")

print(students.head(5))
print()


# Return the top 5 total scores with the most occurrences
print(students['G3'].value_counts().head(5))
print()


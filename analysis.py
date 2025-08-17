"""
Employee Performance Analysis
Generated with ChatGPT assistance.
Contact: 23f2001691@ds.study.iitm.ac.in
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the employee data
df = pd.read_csv("employee_performance_dataset.csv")

# Calculate frequency count for the "IT" department
it_count = (df["Department"] == "IT").sum()
print(f"IT department frequency count: {it_count}")

# Create a histogram-like bar chart showing distribution of departments
dept_counts = df["Department"].value_counts().sort_index()

plt.figure(figsize=(10,6))
plt.bar(dept_counts.index, dept_counts.values)
plt.title("Distribution of Departments")
plt.xlabel("Department")
plt.ylabel("Count of Employees")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("department_distribution.png")
# plt.show()  # Uncomment to display when running locally

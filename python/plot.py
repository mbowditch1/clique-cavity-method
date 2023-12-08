import csv
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file created by the Rust program
with open('data/output.csv', 'r') as file:
    reader = csv.reader(file)

    # Convert each row into a tuple
    data = [row for row in reader]

num_nodes = len(data[0])
num_rows = len(data)
trans = np.linspace(0, 1, num_rows)
print(trans)
node_risk = [np.zeros(len(trans)) for i in range(num_nodes)]

# Iterate through each row and add the risk to the node_risk array
for i, row in enumerate(data):
    for j in range(len(row)):
        node_risk[j][i] = row[j]

for node in node_risk:
    plt.plot(trans, node)

plt.show()


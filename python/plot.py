import csv
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file created by the Rust program
with open('data/output.csv', 'r') as file:
    reader = csv.reader(file)

    # Convert each row into a tuple
    data = [row for row in reader]

# Read the CSV file created by the Rust program
with open('data/output_cavity.csv', 'r') as file:
    reader = csv.reader(file)

    # Convert each row into a tuple
    data_cavity = [row for row in reader]

num_nodes = len(data_cavity[0])
node_to_plot = np.random.randint(0, num_nodes)
number_to_plot = 10
num_rows = len(data_cavity)
trans = np.linspace(0, 1, num_rows)
node_risk = [np.zeros(len(trans)) for i in range(num_nodes)]

# Iterate through each row and add the risk to the node_risk array
for i, row in enumerate(data_cavity):
    for j in range(len(row)):
        node_risk[j][i] = row[j]

# for node in node_risk[:number_to_plot]:
#     plt.plot(trans, node, color="grey")
plt.plot(trans, node_risk[node_to_plot], color="grey")

num_nodes = len(data[0])
num_rows = len(data)
trans = np.linspace(0, 1, num_rows)
node_risk = [np.zeros(len(trans)) for i in range(num_nodes)]

# Iterate through each row and add the risk to the node_risk array
for i, row in enumerate(data):
    for j in range(len(row)):
        node_risk[j][i] = row[j]

# for node in node_risk[:number_to_plot]:
#     plt.scatter(trans, node)

plt.scatter(trans, node_risk[node_to_plot])
plt.show()


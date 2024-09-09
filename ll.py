import pickle

# Path to your .pkl file
file_path = r'C:\Users\shubh\OneDrive\Desktop\render_demo\model.pkl'

# Open the .pkl file in read-binary mode
with open(file_path, 'rb') as file:
    # Load the data from the file
    data = pickle.load(file)

# Print or use the loaded data
print(data)

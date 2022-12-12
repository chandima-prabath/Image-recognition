import os

# Define the directory where the images are stored
image_dir = "/path/to/image/dir"

# Create a dictionary to store the image file names and their labels
dataset = {}

# Loop through all the files in the image directory
for file_name in os.listdir(image_dir):
  # Get the label for the image from the file name
  label = file_name.split("_")[0]

  # If the label is not already in the dataset, add it
  if label not in dataset:
    dataset[label] = []

  # Add the file name to the list of images for the corresponding label
  dataset[label].append(file_name)

# Print the dataset to check if it's correct
print(dataset)

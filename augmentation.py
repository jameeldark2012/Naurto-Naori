import os
from torchvision import transforms
from PIL import Image

# Define the path to your image directory
image_directory = r"dataset\naruto"
save_directory =r"dataset\naruto"

# Define the augmentation transformations
transforms = [
    transforms.RandomRotation(degrees=(30, 70)),  # Rotate between 30 and 70 degrees
    transforms.RandomHorizontalFlip(p=1.0),       # Always flip horizontally
    transforms.RandomResizedCrop(size=(96, 96), scale=(0.5, 1.0)),  # Crop with a wider scale range
    transforms.RandomAutocontrast(p=1.0),         # Always apply autocontrast
    transforms.RandomVerticalFlip(p=1.0)          # Always flip vertically
]

# Loop through all images in the directory
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_directory, filename)
        image = Image.open(image_path)
        
        image = image.convert("RGB")
        
        # Save the augmented image
        for i, transform in enumerate(transforms):
            augmented_image = transform(image)
            augmented_image = augmented_image.resize((96, 64))
            augmented_image.save(os.path.join(save_directory, f"aug_{i}_{filename}"))


print("Augmentation complete!")
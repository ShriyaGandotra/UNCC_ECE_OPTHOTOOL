# AUTHOR: SHRIYA GANDOTRA
# This script defines a machine learning model for classifying medical images as 'Positive' or 'Negative' 
# based on a pretrained ResNet-like neural network. The model architecture includes convolutional layers, 
# batch normalization, ReLU activations, and pooling layers, with a fully connected layer for classification.

# import all libraries
import os
import numpy as np
import torch.nn as nn
import torch
from torchvision import transforms
from PIL import Image

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print(f"Using device: {device}")

# Define the CNN Model
def conv3x3(in_planes, out_planes, stride=1):
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)

class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x3(in_channels, out_channels, stride)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(out_channels, out_channels)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out

class ResNet10(nn.Module):
    def __init__(self, block, num_blocks, num_classes=1000):
        super(ResNet10, self).__init__()
        self.in_channels = 64

        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        # Layers
        self.layer1 = self._make_layer(block, 64, num_blocks[0], stride=1)
        self.layer2 = self._make_layer(block, 128, num_blocks[1], stride=2)
        self.layer3 = self._make_layer(block, 256, num_blocks[2], stride=2)

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(256 * block.expansion, num_classes)

    def _make_layer(self, block, out_channels, num_blocks, stride):
        downsample = None
        if stride != 1 or self.in_channels != out_channels * block.expansion:
            downsample = nn.Sequential(
                conv3x3(self.in_channels, out_channels * block.expansion, stride),
                nn.BatchNorm2d(out_channels * block.expansion)
            )

        layers = []
        layers.append(block(self.in_channels, out_channels, stride, downsample))
        self.in_channels = out_channels * block.expansion
        for _ in range(1, num_blocks):
            layers.append(block(self.in_channels, out_channels))

        return nn.Sequential(*layers)

    def forward(self, x):
          x = self.conv1(x)
          x = self.bn1(x)
          x = self.relu(x)
          x = self.maxpool(x)

          x = self.layer1(x)
          x = self.layer2(x)
          x = self.layer3(x)

          x = self.avgpool(x)
          x = torch.flatten(x, 1)
          x = self.fc(x)

          return x

classes = ['Positive', 'Negative']
model = ResNet10(BasicBlock, [1, 1, 1, 1], 2)
model.load_state_dict(torch.load('DR_Detection_Model.pth', map_location=torch.device('cpu')))

def MLmodel():
    total_img = 0

    # Refer to OCT Volume
    folderpath = "oct_test1/raw_images"
    folder_img = sorted(os.listdir(folderpath))
    total_img = 0 # Count for total images in volume

    for image in folder_img:
        total_img += 1

    middle_img = round(total_img/2)
    imgpath = "oct_test1/raw_images/image_0_" + str(middle_img) + '.png'

    img = Image.open(imgpath)

    # Convert the image to RGB if it's not already in RGB format
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Apply transformations
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Apply transformations and add batch dimension
    input = transform(img).unsqueeze(0)

    # Move input to the appropriate device (GPU if available)
    input = input

    # Ensure model is in evaluation mode
    model.eval()

    # Perform inference
    output = model(input)

    # Get the predicted class index
    _, predicted_class_idx = torch.max(output, 1)

    # Map the class index to class label
    predicted_class = classes[predicted_class_idx]

    print("Predicted class:", predicted_class)

    return predicted_class
        

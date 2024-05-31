"""
MIT License

Copyright (c) 2024 KernFerm (Bubbles The Dev)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import onnx
from onnx2pytorch import ConvertModel
import torch

# Function to load the ONNX model
def load_onnx_model(onnx_model_path):
    try:
        onnx_model = onnx.load(onnx_model_path)
        onnx.checker.check_model(onnx_model)  # Validate the model
        return onnx_model
    except Exception as e:
        print(f"Error loading ONNX model: {e}")
        return None

# Function to convert ONNX model to PyTorch
def convert_to_pytorch(onnx_model):
    try:
        pytorch_model = ConvertModel(onnx_model)
        return pytorch_model
    except Exception as e:
        print(f"Error converting to PyTorch model: {e}")
        return None

# Function to save the PyTorch model
def save_pytorch_model(pytorch_model, pytorch_model_path):
    try:
        torch.save(pytorch_model.state_dict(), pytorch_model_path)
        print(f"Model successfully converted and saved to {pytorch_model_path}")
    except Exception as e:
        print(f"Error saving PyTorch model: {e}")

# Paths
onnx_model_path = 'path_to_your_model.onnx' ## use \\ when doing the path 
pytorch_model_path = 'path_to_save_model.pt' ## use \\ when doing the path 

# Load, convert and save the model
onnx_model = load_onnx_model(onnx_model_path)
if onnx_model:
    pytorch_model = convert_to_pytorch(onnx_model)
    if pytorch_model:
        save_pytorch_model(pytorch_model, pytorch_model_path)

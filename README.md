##  Works

----
# ONNX to PyTorch Model Conversion

This repository provides a script to convert an ONNX model to a PyTorch model. The script includes functions to load an ONNX model, convert it to a PyTorch model, and save the converted model.

## Example 
![image](https://github.com/KernFerm/onnx-pt-converter/assets/152947339/8b7374ff-cbfa-499b-96a9-b44314421f4b)

----
## Make Sure To `CD` the path of the file 
----
## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Loading the ONNX Model](#loading-the-onnx-model)
  - [Converting the ONNX Model to PyTorch](#converting-the-onnx-model-to-pytorch)
  - [Saving the PyTorch Model](#saving-the-pytorch-model)
  - [Full Script](#full-script)
- [Example](#example)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Requirements

Ensure you have the following Python libraries installed:

- `onnx`
- `onnx2pytorch`
- `torch`

## Installation

You can install the necessary libraries using pip:

```
pip install onnx onnx2pytorch torch

```
## Usage

Loading the ONNX Model

- The load_onnx_model function loads an ONNX model from the specified path and validates it.

```
import onnx

def load_onnx_model(onnx_model_path):
    try:
        onnx_model = onnx.load(onnx_model_path)
        onnx.checker.check_model(onnx_model)  # Validate the model
        return onnx_model
    except Exception as e:
        print(f"Error loading ONNX model: {e}")
        return None

```

----

## Converting the ONNX Model to PyTorch

- The convert_to_pytorch function converts the loaded ONNX model to a PyTorch model using the onnx2pytorch library.

```
from onnx2pytorch import ConvertModel

def convert_to_pytorch(onnx_model):
    try:
        pytorch_model = ConvertModel(onnx_model)
        return pytorch_model
    except Exception as e:
        print(f"Error converting to PyTorch model: {e}")
        return None
```
---

## Saving the PyTorch Model

- The save_pytorch_model function saves the converted PyTorch model to the specified path.
```
import torch

def save_pytorch_model(pytorch_model, pytorch_model_path):
    try:
        torch.save(pytorch_model.state_dict(), pytorch_model_path)
        print(f"Model successfully converted and saved to {pytorch_model_path}")
    except Exception as e:
        print(f"Error saving PyTorch model: {e}")
```

---

## Example

- Replace `'path_to_your_model.onnx'` with the path to `your ONNX model` and `'path_to_save_model.pt'` with the desired `output path` for the PyTorch model.



# YOLO Box Visualizer

## Overview

YOLO Box Visualizer is a Streamlit-based web app that allows you to:
- Upload (or drag-and-drop) images.
- Upload (or drag-and-drop) YOLO annotation files (txt).
- Parse and visualize red bounding boxes over the uploaded image.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/YOLO-Box-Visualizer.git

2.  **Navigate to the project folder**:
    
    ```bash
    cd YOLO-Box-Visualizer
    
    ```
    
3.  **Set up a virtual environment** (optional but recommended):
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    
    ```
    
4.  **Install dependencies**:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    

## Usage

Run the Streamlit application:

```bash
streamlit run src/app.py

```

Open the provided URL in your browser. You can now:

1.  Upload an image (jpg, jpeg, png).
2.  Upload a YOLO annotation file (txt).
3.  Click "Show Annotation" to see the bounding box on your image.

## Example

![Example Screenshot](https://raw.githubusercontent.com/shamspias/YOLO-Box-Visualizer/refs/heads/main/img/1.png)
![Example Screenshot](https://raw.githubusercontent.com/shamspias/YOLO-Box-Visualizer/refs/heads/main/img/2.png)
![Example Screenshot](https://raw.githubusercontent.com/shamspias/YOLO-Box-Visualizer/refs/heads/main/img/3.png)

## Contributing

1.  Fork the repository.
2.  Create a feature branch.
3.  Commit your changes.
4.  Submit a pull request.
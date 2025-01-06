import streamlit as st
from PIL import Image, ImageDraw
import io


class YOLOAnnotation:
    """
    Represents a single YOLO annotation.

    Attributes:
        class_id (int): The class ID for the annotation (e.g., 0).
        x_center (float): The x-center of the bounding box (normalized from 0 to 1).
        y_center (float): The y-center of the bounding box (normalized from 0 to 1).
        width (float): The width of the bounding box (normalized).
        height (float): The height of the bounding box (normalized).
    """

    def __init__(self, class_id: int, x_center: float, y_center: float, width: float, height: float):
        self.class_id = class_id
        self.x_center = x_center
        self.y_center = y_center
        self.width = width
        self.height = height

    def __repr__(self):
        return (f"YOLOAnnotation(class_id={self.class_id}, "
                f"x_center={self.x_center}, y_center={self.y_center}, "
                f"width={self.width}, height={self.height})")


class YOLOVisualizer:
    """
    Handles reading YOLO annotations, drawing bounding boxes onto images,
    and displaying the results in a Streamlit app.
    """

    def __init__(self):
        """Initialize the visualizer."""
        self.image = None
        self.annotations = []

    @staticmethod
    def parse_annotation_content(content: str) -> list:
        """
        Parse the content of the annotation file (YOLO format).

        Args:
            content (str): The content of the annotation file as a string.

        Returns:
            list of YOLOAnnotation: A list of parsed YOLOAnnotation objects.
        """
        lines = content.strip().split('\n')
        annotations = []

        for line in lines:
            # Typical YOLO format: class_id x_center y_center width height
            parts = line.split()
            if len(parts) == 5:
                class_id = int(parts[0])
                x_center = float(parts[1])
                y_center = float(parts[2])
                width = float(parts[3])
                height = float(parts[4])
                annotation = YOLOAnnotation(class_id, x_center, y_center, width, height)
                annotations.append(annotation)

        return annotations

    def draw_boxes_on_image(self) -> Image:
        """
        Draw the YOLO bounding boxes on the current image.

        Returns:
            Image: The PIL Image with bounding boxes drawn.
        """
        if not self.image or not self.annotations:
            return self.image

        # Convert to a drawable format
        draw = ImageDraw.Draw(self.image)

        img_width, img_height = self.image.size

        for ann in self.annotations:
            # Convert normalized coordinates to pixel values
            box_width = ann.width * img_width
            box_height = ann.height * img_height

            x_min = (ann.x_center * img_width) - (box_width / 2)
            y_min = (ann.y_center * img_height) - (box_height / 2)
            x_max = x_min + box_width
            y_max = y_min + box_height

            # Draw bounding box (outline in red, width=2)
            draw.rectangle([x_min, y_min, x_max, y_max], outline='red', width=2)

        return self.image

    def run_app(self):
        """
        Run the Streamlit app. Allows user to upload an image and an annotation file,
        then displays the image with the annotated bounding box.
        """
        st.title("YOLO Bounding Box Visualizer")
        st.write("""
        **Instructions**:  
        1. Upload or drag-and-drop an **image**.  
        2. Upload or drag-and-drop the corresponding **YOLO annotation** text file.  
        3. The script will display the image with the bounding box drawn in red.  
        """)

        # File upload widgets
        uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
        uploaded_annotation = st.file_uploader("Upload Annotation File (TXT)", type=["txt"])

        if uploaded_image is not None:
            # Read the image into PIL
            self.image = Image.open(uploaded_image).convert("RGB")

        if uploaded_annotation is not None:
            annotation_content = uploaded_annotation.read().decode("utf-8")
            self.annotations = self.parse_annotation_content(annotation_content)

        if st.button("Show Annotation") and self.image and self.annotations:
            # Draw bounding boxes and display the result
            result_image = self.draw_boxes_on_image()
            st.image(result_image, caption="Annotated Image", use_container_width=True)


def main():
    """
    Entry point for the Streamlit app.
    """
    visualizer = YOLOVisualizer()
    visualizer.run_app()


if __name__ == "__main__":
    main()

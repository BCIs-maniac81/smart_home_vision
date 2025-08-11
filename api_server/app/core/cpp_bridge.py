import os
import sys
sys.path.append(os.path.dirname(__file__))  # Add current directory to path

from core_engine import detect_from_image

def detect(image_path: str):
    """
    Call the C++ core detection function and return Python-friendly dicts.
    """
    detections_cpp = detect_from_image(image_path)
    return [
        {
            "id": d.id,
            "label": d.label,
            "bbox": d.bbox,
            "score": d.score
        }
        for d in detections_cpp
    ]

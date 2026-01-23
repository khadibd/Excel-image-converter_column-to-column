import io
from PIL import Image
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage
from converter import ConversionResult, compress_jpg

def extract_images(ws):
    images = ws._images
    img_map = {}
    for img in images:
        if img.anchor._from.col == 1:  # colonne B
            row = img.anchor._from.row + 1
            img_map[row] = img
    return img_map

def write_jpg_to_excel(ws, results):
    for res in results:
        img = XLImage(io.BytesIO(res.jpg_bytes))
        img.anchor = f"C{res.row}"
        ws.add_image(img)

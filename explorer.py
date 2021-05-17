from pathlib import Path
import fitz
import os
from config import *

def search(text, file):
    doc = fitz.open(file)
    for i, page in enumerate(doc):
        text_instances = page.searchFor(text)
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst).rect
            highlight[0] -= 10000
            highlight[1] -= 150
            highlight[2] += 10000
            highlight[3] += 150
            print(highlight)
            zoom = 2
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix = mat, clip=highlight)
            filename = str(hash(str(file) + str(i))) + ".png"
            filename = os.path.join(image_folder, filename)
            pix.save(filename)
            yield filename
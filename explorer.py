from pathlib import Path
import fitz

file = 'textbook_pdfs/Boron_fiziologija.pdf'

def search(text, file=file):
    doc = fitz.open(file)
    for i, page in enumerate(doc):
        text_instances = page.searchFor(text)
        print(i)
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst).rect
            highlight[0] -= 10000
            highlight[1] -= 150
            highlight[2] += 10000
            highlight[3] += 150
            print(highlight)
            # zoom = 2
            # mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(clip=highlight)
            filename =f"{i}.png"
            pix.save(filename)
            yield filename
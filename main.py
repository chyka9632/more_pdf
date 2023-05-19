import glob as gb
from pathlib import Path
from fpdf import FPDF
import re

# Create a list of txt filepaths
filepaths = gb.glob("files/*.txt")

# Create on pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each txt file
for filepath in filepaths:
    # Add a page to the pdf document for each txt file
    pdf.add_page()

    # Get the filename for each txt file without the extension
    filename = Path(filepath).stem
    name = filename.capitalize()

    # Add the name to the pdf
    pdf.set_font(family="Arial", style="B", size=16)
    pdf.cell(w=0, h=10, txt=name, align="L")

    with open(filepath, "r") as file:
        content = file.read()

    # Remove [1], [2], ... occurrences within sentences
    content = re.sub(r'\[(\d+)\]', '', content)

    pdf.set_font(family="Times", size=10)
    pdf.set_xy(10, 18)
    pdf.multi_cell(w=0, h=6, txt=content)


# Produce the pdf
pdf.output("output.pdf")

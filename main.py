import glob as gb
from pathlib import Path
import pandas as pd
from fpdf import FPDF

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


# Produce the pdf
pdf.output("output.pdf")

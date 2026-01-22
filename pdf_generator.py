from fpdf import FPDF
import pandas as pd

def set_footer(topic, ln):
    pdf.ln(ln)
    
    pdf.set_font(family='Arial', style='I', size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=5, text=topic, ln=1, align='R')


pdf = FPDF(orientation='P', unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

dataframe = pd.read_csv("files/pdf-topics.csv")

for index, row in dataframe.iterrows():
    pdf.add_page()
    pdf.set_font(family='Arial', style='B', size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=5, text=f"{row["Order"]}. {row["Topic"]}", ln=1, align='L')
    pdf.line(x1=10, y1=17, x2=200, y2=17)

    set_footer(topic=row["Topic"], ln=270)

    """subtracting 1 page from the mentioned pages as one page is already added above"""
    for i in range(row['Pages'] - 1):
        pdf.add_page(same=True)
        set_footer(topic=row["Topic"], ln=273)

pdf.output('output.pdf')
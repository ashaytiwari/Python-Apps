from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="mm", format="A4")

dataframe = pd.read_csv("files/pdf-topics.csv")

for index, row in dataframe.iterrows():
    pdf.add_page()
    pdf.set_font(family='Arial', style='B', size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=5, txt=f"{row["Order"]}. {row["Topic"]}", ln=1, align='L')
    pdf.line(10, 17, 200, 17)

pdf.output('output.pdf')
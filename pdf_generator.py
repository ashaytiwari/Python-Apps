from fpdf import FPDF

pdf = FPDF(orientation='P', unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family='Arial', style='B', size=16)
pdf.cell(w=0, h=5, txt="Introduction", ln=1, align='L')

pdf.set_font(family='Arial', size=10)
pdf.cell(w=0, h=10, txt="Work Stream", ln=1, align='L')

pdf.output('output.pdf')
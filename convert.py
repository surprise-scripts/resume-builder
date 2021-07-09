# Shoutout to https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f

from yaml import load
from fpdf import FPDF

class PDF(FPDF):
    
    def aboutme(self, aboutme):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 24)
        self.set_text_color(0,0,0)
        self.cell(w=210.0, h=40.0, align='C', txt=aboutme.name)
        
    pass

pdf = PDF(orientiation='P', unit='mm', format='A4')
pdf.add_page()
pdf.output('resume.pdf', 'F')
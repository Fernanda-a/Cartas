from fpdf import FPDF

class PDF(FPDF):
	def header(self):
		self.set_font('Arial', 'B', 25)
		self.cell(0, 10, 'Carta', ln=1, align='C')
		self.ln(12)

def save_carta_txt(carta, file_name):
        txt = open(file_name + ".txt", "w")
        txt.write(carta)
        txt.close()

def save_carta(file_name):
	pdf = PDF()
	pdf.add_page()

	pdf.set_font("Arial", size=20)
	carta = file_name + ".txt"
	file = open(carta)
	lines = file.readlines()

	for i in lines:
		pdf.multi_cell(200, 10, i)

	pdf.output(file_name + ".pdf")
	pdf.close()


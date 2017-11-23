'''
Author : Vikash Singh
This programme converts .txt file to Pdf,
The paragraph is separated on the basis of punctuation marks  (i.e., ? and .)
User can input any integer value (programme will ask in running time)
The prerequisite is that user need to install reportlab
'''

from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("pdf_file",
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

styles= getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

Pdf_file=[] # Name of producedPDF will be written

# take the txt file as a input
while True: 
    text_file= input ("Enter the file with .txt extention: ")
    try:
        file_open = open(text_file ,"r")
        break
    except FileNotFoundError:
        print("\nProvide the correct .txt file (or full path to the .txt file) ")

while True:
    try: 
        Choise_of_number= int( input("Number of punctuation marks(i.e. ,. and?) per paragraph (ideal 10): ") )
        break
    except ValueError:
        print("Choise should be integer\n")

Head=input("Enter the Heading: ").title()
    
Pdf_file.append(Paragraph( '<font size=20>{}</font>'.format(Head), styles["Normal"]))
Pdf_file.append(Spacer(1, 30))


my_line = file_open.readline();
ptext=""; count=0

while  my_line:
    ptext += my_line
    if "?" in my_line or "." in my_line:  # counting the number of ? and .
        count += 1
    if count == Choise_of_number: # Paragraph will be consist of 10 ? or .
        Pdf_file.append(Paragraph(ptext, styles["Justify"]))  
        Pdf_file.append(Spacer(1, 12))
        count =0; ptext=""
        
    my_line = file_open.readline();

if count > 0:  # The remaning lines yet to be appended 
    Pdf_file.append(Paragraph(ptext, styles["Justify"]))
    
doc.build(Pdf_file)
file_open.close()

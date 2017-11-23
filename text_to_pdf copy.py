'''A 4 size in inch 11.69' X 16.53'. The defult canvas is of A4 size
where 1 point = 1/72'  '''
''' https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/'''
''' A Spacer is good for adding a line of blank space,
like a paragraph break'''

''' he getSampleStyleSheet gets a set of default styles
that we can use in our PDF'''

from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


#c = canvas.Canvas("hello.pdf")
#c.drawString(100,750,"Welcome to Reportlab!")

doc = SimpleDocTemplate("pdf_file",
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

styles= getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

Pdf_file=[] # Name of producedPDF will be written

# take the txt file as a input
while True: 
    text_file= input ("Enter the file with .txt extention: ")
    if text_file.lower()[-4:] == ".txt" :
        break
    else: print("Please include .txt \n")

while True:
    try: 
        Choise_of_number= int( input("Number of punctuation marks(i.e. ,. and?) per paragraph: ") )
        break
    except ValueError:
        print("Choise should be integer\n")

Head=input("Enter the Heading: ").title()

file_open = open(text_file ,"r")

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

if count > 0:
    Pdf_file.append(Paragraph(ptext, styles["Justify"]))

##my_lines = file_open.read();
##page_break= list ( range(10, len(my_lines)+1, 10 ) )
##
##if page_break[-1] != len(my_lines):
##    page_break.append(len(my_lines))
##
##st=0; ptext=[];
##for i in page_break:
##    ptext = "".join( my_lines[st:i+1])
##    st= i+1
##    my_file.append(Paragraph(ptext, styles["Justify"]))
##    my_file.append(Spacer(1, 12))
##    ptext=[]
##       

doc.build(Pdf_file)
file_open.close()
#c.save()

import xlrd
import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Add participant name to certificate
def make_certi(name):

    img = Image.open("aaa.png")
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype("a.TTF", 140)

    if name == -1:
        return -1
    else:
        # Insert text into image template
        
        draw.text( (610,450), name, (0,0,0), font=font ) #draw.text((x, y), message, fill=color, font=font)

        if not os.path.exists( 'certificates' ) :
            os.makedirs( 'certificates' )

        # Save as a PDF
        rgb = Image.new('RGB', img.size, (255, 255, 255))  # white background
        rgb.paste(img, mask=img.split()[3])               # paste using alpha channel as mask
        
        rgb.save( 'certificates/'+str(name)+'.pdf', "PDF", resolution=100.0)
        return 'certificates/'+str(name)+'.pdf'

# Email the certificate as an attachment
def email_certi( filename, receiver, name ):
    username = "rutuuuujaaaa@gmail.com"
    password = "Password"
    sender = username + '@gmail.com'

    msg = MIMEMultipart()
    msg['Subject'] = 'Subject'
    msg['From'] = username+'@gmail.com'
    msg['Reply-to'] = username + '@gmail.com'
    msg['To'] = receiver

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'
    
    # Body
    body = "Hello {}\nHere's something for you!\nHappppyyyy Quarantine!!!!".format(name)
    part = MIMEText(body)
    msg.attach( part )

    # Attachment
    part = MIMEApplication(open(filename,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename = os.path.basename(filename))
    msg.attach( part )

    # Login
    server = smtplib.SMTP( 'smtp.gmail.com:587' )
    server.starttls()
    server.login( username, password )

    # Send the email
    server.sendmail( msg['From'], msg['To'], msg.as_string() )

if __name__ == "__main__":
    error_list = []
    error_count = 0

    os.chdir(os.path.dirname(os.path.abspath((sys.argv[0]))))

    # Read data from an excel sheet from row 2
    Book = xlrd.open_workbook('data.xlsx')
    WorkSheet = Book.sheet_by_name('Sheet1')
    
    num_row = WorkSheet.nrows - 1
    row = 0

    while row < num_row:
        row += 1
        
        name = WorkSheet.cell_value( row, 2 )
        email = WorkSheet.cell_value( row, 1 )
        
        # Make certificate and check if it was successful
        filename = make_certi(name)
        
        # Successfully made certificate
        if filename != -1:
            email_certi( filename, email, name)
            print("Sent to ", name)
        # Add to error list
        else:
            error_list.append( ID )
            error_count += 1

    # Print all failed IDs
    print(str(error_count)," Errors- List:", ','.join(error_list))

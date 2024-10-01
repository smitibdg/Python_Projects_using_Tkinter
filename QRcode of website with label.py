import qrcode
from PIL import Image, ImageDraw, ImageFont

# Define the website URL
website_url = "https://siesascs.edu.in/"

# Generate a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)

# Create a QR code image
qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load a font for the label
try:
    font = ImageFont.truetype("arial.ttf", 25)#Adjust font size as needed
except IOError:
    font = ImageFont.load_default()  #Fallback to default font if not found

# Create an image for the label
label = "SIES College Website"
img_width, img_height = qr_image.size

# Create a new image with extra space at the top for the label
total_height = img_height + 100  #Extra space for the label
new_img = Image.new('RGB', (img_width, total_height), (255, 255, 255))

# Paste the QR code into the new image
new_img.paste(qr_image, (0, 100))  #Position the QR code below the label

# Draw the label at the top
draw = ImageDraw.Draw(new_img)

# Get the bounding box of the text
text_bbox = draw.textbbox((0, 0), label, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Position the label centered at the top
position = ((img_width - text_width) // 2, 40)  #40 pixels from the top
draw.text(position, label, fill="black", font=font)

# Save the image to a file
new_img.save("sies_clg_QR.png")

# Show the image (optional for testing)
new_img.show()

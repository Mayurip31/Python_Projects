import qrcode  # Correctly import the 'qrcode' library

# Step 1: Get data and filename from the user
data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename (with .png or .jpg extension): ').strip()

# Step 2: Create a QRCode object
qr = qrcode.QRCode(box_size=10, border=4)

# Step 3: Add data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Ensures the entire data fits into the QR code

# Step 4: Generate the image for the QR code
image = qr.make_image(fill_color='black', back_color='white')

# Step 5: Save the image with the specified filename
image.save(filename)

# Step 6: Confirm the file has been saved
print(f'QR code saved as {filename}')

import os
from qrcode import QRCode, constants

def generate_qr_code(input_string, output_file="qrcode.png"):
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    qr = QRCode(
        version=1,  
        error_correction=constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4  
    )
    qr.add_data(input_string)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

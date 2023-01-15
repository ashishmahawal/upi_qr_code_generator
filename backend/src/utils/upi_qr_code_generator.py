from io import BytesIO
from flask import send_file
import qrcode
import uuid

def generateUPIQR(upi_address,amount,user_name=None,txn_note="Money"):
    # Txn Refernce Id
    try:
        tr = str(uuid.uuid4())
        qr_data = f'upi://pay?pa={upi_address}&am={amount}&tr={tr}&tn={txn_note}&pn={user_name}&tn={txn_note}'
        print(f'Generating QR code for string : {qr_data}')
        # Create the QR code object
        qr = qrcode.QRCode(version=1, box_size=4, border=4)
        # Add the QR code data
        qr.add_data(qr_data)
        # Make the QR code
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return serve_pil_image(img)
    except Exception as e:
        return {"error":f"Unable to generate QR Code ,Error: {e}"}


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
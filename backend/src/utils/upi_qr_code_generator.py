from io import BytesIO
from flask import send_file
import qrcode
import uuid
from PIL import Image
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))

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
        # add overlay to QR
        overlay = Image.open(os.path.join(script_dir, 'sample_overlay.jpg')).resize((40,40))
        overlayed_bg = addOverlayToQR(img,overlay)
        return serve_pil_image(overlayed_bg)
    except Exception as e:
        return {"error":f"Unable to generate QR Code ,Error: {e}"}

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

def addOverlayToQR(bg,overlay):
    bg = bg.convert("RGBA")
    overlay = overlay.convert("RGBA")
    ol_delta = 20
    placement_coordinates = (bg.width//2 - ol_delta,bg.height//2 - ol_delta )
    bg.paste(overlay,placement_coordinates)
    return bg
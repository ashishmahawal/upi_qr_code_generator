import qrcode
import uuid

def generateUPIQR(upi_address,amount,purpose="Ganjha",txn_note="Money"):
    # Txn Refernce Id
    try:
        tr = str(uuid.uuid4())
        qr_data = f'upi://pay?pa={upi_address}&am={amount}&pn={purpose}&tr={tr}&tn={txn_note}'
        print(f'Generating QR code for string : {qr_data}')
        # Create the QR code object
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # Add the QR code data
        qr.add_data(qr_data)
        # Make the QR code
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("./src/upi_qr.png")
        return img
    except Exception as e:
        return {"error":f"Unable to generate QR Code ,Error: {e}"}


generateUPIQR("abc","100")
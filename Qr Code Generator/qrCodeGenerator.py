#qrCodeGenerator.py
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png

def qr_code(value1):
    
    q = pyqrcode.create(value1)
    q.png('my_img.png',scale = 6)
    print("code executed properly")
    
def main():
    data = "This is Sample QR code"
    qr_code(data)

if __name__ == "__main__":
    main()
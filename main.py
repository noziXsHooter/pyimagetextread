import pytesseract
import cv2

imagem = cv2.imread(r'images\reportagem.jpg')  # Leitura da imagem

caminho = r'C:\Users\Junior\AppData\Local\Programs\Tesseract-OCR'

pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'  # Executa tesseract

texto = pytesseract.image_to_string(imagem, lang='por')  # Transforma imagem para string
print(texto)

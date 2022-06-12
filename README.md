# pyimagetextread
Este repositório é de caráter explicativo para o procedimento de implementação de leitura de texto em imagens no Python.
## Procedimento


#### Instale as bibliotecas:

pip install opencv-python

pip install pytesseract

#### Pode ocorrer um erro no windows chamado: 'TesseractNotFoundError()'.

Caso ocorra, faça o seguinte procedimento:

#### No Linux
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

#### No Mac
brew install tesseract

#### No Windows
Baixe o binário de https://github.com/UB-Mannheim/tesseract/wiki.

Instale tesseract-ocr-setupv*.exe

Dentro do código em 'caminho', coloque o local onde está o arquivo tesseract.exe no seu computador com final:

"...\Tesseract-OCR"

#### Em pytesseract.pytesseract.tesseract_cmd, ficará!
..._cmd = caminho = "...\Tesseract-OCR\tesseract.exe"


### Modo linguagem Português no Texto Final

Acesse: https://github.com/tesseract-ocr/tessdata

Faça o donwload do arquivo:
    por.traineddata

Coloque o arquivo acima no diretório: "\Tesseract-OCR\tessdata"


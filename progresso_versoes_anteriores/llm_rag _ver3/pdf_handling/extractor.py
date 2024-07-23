# Extrator de texto de PDFs
import PyPDF2
try:
    pdf_file = open('pdf_handling/entrevistas.pdf', 'rb')
except FileNotFoundError:
    print("Arquivo não encontrado")
    exit()
pdf = PyPDF2.PdfReader(pdf_file)

def extract_text_from_pdf():
    #pegando o numero de paginas
    paginas = len(pdf.pages)
    #extraindo o conteudo de cada pagina e formatando
    for i in range(paginas):
        page = pdf.pages[i]
        text = page.extract_text()
        #print(text)
        texto_formatado = ''.join(text.split('\n'))
    return texto_formatado



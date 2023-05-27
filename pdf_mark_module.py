import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time

def mark_maker(file_path, event_time):
    watermark_text = event_time

    # 워터마크 PDF 생성
    watermark_pdf = canvas.Canvas(f"{event_time}.pdf", pagesize=letter)
    watermark_pdf.setFont("Helvetica", 60)
    watermark_pdf.setFillColorRGB(0, 0, 0)
    watermark_pdf.drawString(500, 100, watermark_text)
    watermark_pdf.save()

    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    watermark_reader = PyPDF2.PdfReader(f"{event_time}.pdf")
    watermark_page = watermark_reader.pages[0]

    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    time.sleep(1)

    pdf_output = open(file_path, 'wb')
    pdf_writer.write(pdf_output)

    pdf_file.close()
    pdf_output.close()

    print('워터마크 작업이 완료되었습니다.')

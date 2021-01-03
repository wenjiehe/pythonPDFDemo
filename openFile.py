import importlib
import sys
import time

importlib.reload(sys)
time1 = time.time()

import os.path

from  pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def parse(pdf_path, txt_path):
    fp = open(pdf_path, 'rb')

    parser = PDFParser(fp)

    doc = PDFDocument()

    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize()

    if not doc.is_extractable:
        print('走了')
        raise PDFTextExtractionNotAllowed
    else:

        mgr = PDFResourceManager()

        laparams = LAParams()

        device = PDFPageAggregator(mgr, laparams=laparams)

        interpreter = PDFPageInterpreter(mgr ,device)

        for page in doc.get_pages():
            interpreter.process_page(page)

            layout = device.get_result()

            for x in layout:
                if(isinstance(x, LTTextBoxHorizontal)):
                    with open(txt_path, 'a') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + "\n")

if __name__ == '__main__':
    pdf_path = '/Users/hewenjie/Documents/书籍/iOS多线程/IOS多线程编程指南.pdf'
    txt_path = '/Users/hewenjie/Desktop/make.txt'
    parse(pdf_path,txt_path)
    time2 = time.time()
    print("总共消耗时间为:",time2-time1)


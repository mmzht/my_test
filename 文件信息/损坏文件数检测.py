# 遍历文件夹统计pdf、jpg、zip、rar损坏文件

import os
import sys
import imghdr
import zipfile
import rarfile
from pptx import Presentation  # pptx
from docx import Document  # docx
from PyPDF2 import PdfFileReader  # pdf
from openpyxl import load_workbook  # xlsx

filepath = r'E:\工作文件\欣旺达文件备份2017'  # 需要查找的目录
savefile = r'C:\Users\Kevin\Documents\python\损坏文件数量.txt'  # 结果保存文件
with open(savefile, 'w') as f:
    f.write(
        '目录|PDF|损坏PDF|PDF数|JPG|损坏JPG|JPG数|ZIP|损坏ZIP|ZIP数|RAR|损坏RAR|RAR数|PPTX|损坏PPTX|PPTX数|DOCX|损坏DOCX|DOCX数|xlsx损坏|xslx数|损坏数|总数|比例\n')

file_nums = 0  # 文件计数
for roots, dirs, files in os.walk(filepath):  # 当前根,根下目录,目录下的文件
    # ====定义各自的计数器====
    pdf_num, pdf_bad = 0, 0
    jpg_num, jpg_bad = 0, 0
    zip_num, zip_bad = 0, 0
    rar_num, rar_bad = 0, 0
    docx_num, docx_bad = 0, 0
    pptx_num, pptx_bad = 0, 0
    xlsx_num, xlsx_bad = 0, 0
    for filename in files:
        file_nums += 1  # 临时计数
        suf = os.path.splitext(filename)[1]  # 获取后缀名
        find_file = os.path.join(roots, filename)  # =>组合成文件的完整路径
        # ====pdf判断======
        if suf.lower() == '.pdf':  # 兼容大小写
            pdf_num += 1
            with open(find_file, 'rb') as pdffile:
                try:
                    PdfFileReader(pdffile)
                except:
                    pdf_bad += 1
        # ====jpg判断==============
        if suf.lower() == '.jpg':
            jpg_num += 1
            if imghdr.what(find_file) == None:
                jpg_bad += 1
        # ====zip判断=============
        if suf.lower() == '.zip':  # 兼容大小写
            zip_num += 1
            if zipfile.is_zipfile(find_file) != True:
                zip_bad += 1
        # ====zip判断==================
        if suf.lower() == '.rar':  # 兼容大小写
            rar_num += 1
            try:
                rarfile.RarFile(find_file)
            except:
                rar_bad += 1
        # ====pptx判断==================
        if suf.lower() == '.pptx':  # 兼容大小写
            pptx_num += 1
            try:
                Presentation(find_file)
            except:
                pptx_bad += 1
        # ====docx判断=================
        if suf.lower() == '.docx':  # 兼容大小写
            docx_num += 1
            try:
                Document(find_file)
            except:
                docx_bad += 1
        #  ====xlsx判断==================
        if suf.lower() == '.xlsx':  # 兼容大小写
            # print(str(file_nums))   # 临时计数
            xlsx_num += 1
            try:
                load_workbook(find_file)
            except:
                xlsx_bad += 1

    pdfinfo = '|pdf损坏数与总数:|' + str(pdf_bad) + '|' + str(pdf_num)
    jpginfo = '|jpg损坏数与总数:|' + str(jpg_bad) + '|' + str(jpg_num)
    zipinfo = '|zip损坏数与总数:|' + str(zip_bad) + '|' + str(zip_num)
    rarinfo = '|rar损坏数与总数:|' + str(rar_bad) + '|' + str(rar_num)
    pptxinfo = '|pptx损坏数与总数:|' + str(pptx_bad) + '|' + str(pptx_num)
    docxinfo = '|docx损坏数与总数:|' + str(docx_bad) + '|' + str(docx_num)
    xlsxinfo = '|xlsx损坏数与总数:|' + str(xlsx_bad) + '|' + str(xlsx_num)

    # ======结果打印与保存==============
    totalbadfile = pdf_bad + jpg_bad + zip_bad + rar_bad + pptx_bad + docx_bad + xlsx_bad
    info = roots + pdfinfo + jpginfo + zipinfo + rarinfo + pptxinfo + docxinfo + xlsxinfo
    if totalbadfile > 0:
        print(info)
        with open(savefile, 'a+') as f:
            f.write(info + '\n')

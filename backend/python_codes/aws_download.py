# import constants
import schedule
import boto3
import pdf2image
import time
import tabula
import datetime
import mysql.connector
import shutil
from pdfimage import pdf_image
from textract_python_table_parser import append_files
from hdfc import hdfc_digitization
from kotak import kotak_digitization
from sbi import sbi_digitization
from icici import icici_digitization
from axis import axis_digitization
from letest_corporation import corporation_digitization
from form_aws import form_data_itr
import os
from itrv import get_itrv_data
from form26as import get_form26as_data
from form16 import get_form16_data
from fstype_extraction_bank import bank_extraction
from bank_name_extraction import fstype_extraction
from fstype_extraction_itr import itr_extraction
import glob

# bucket = 'a3bank'  ###define bucket name
# bucket1 = 'a3itr'  ###define bucket name
# bucket2 = 'digitizedfiles'
#
# s3 = boto3.resource('s3')

# file_path = r'C:\Users\Shubham\Desktop\pdf_files'  ## Here the pdf is stored after uploading it into the web
# csv_path = r'C:\Users\Shubham\Desktop\digitized_files'  ##  Here we will store the csv after digitisation
#
# # objects_bank = s3.Bucket(bucket).objects.all()   ###get all objects in the bucket
# # objects_itr = s3.Bucket(bucket1).objects.all()   ###get all objects in the bucket
#
# objects_bank = glob.glob(file_path + '*.pdf')  # manual testing


# objects_itr = glob.glob(r'D:\s3_itr\\*')       # manual testing

def job():
    print('Digitization')
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',  ###connect to database
        password='Knowlvers@555',
        database="details"
    )

    mycursor = mydb.cursor()
    file_path = r'C:/Users/shubhamraj/Desktop/pdf_files'  ## Here the pdf is stored after uploading it into the web
    csv_path = r'C:/Users/shubhamraj/Desktop/digitized_files'  ##  Here we will store the csv after digitisation

    # objects_bank = s3.Bucket(bucket).objects.all()   ###get all objects in the bucket
    # objects_itr = s3.Bucket(bucket1).objects.all()   ###get all objects in the bucket

    objects_bank = glob.glob(file_path+'/*.pdf')
    for file in objects_bank:

            fstype = bank_extraction(file)
            if fstype == 'HDFC':
                print('hdfc')
                print("New file path is:-")
                print(file_path)
                file_path = hdfc_digitization(file)  ##SHUBHAM EDIT
                shutil.copy(file_path, csv_path)

            elif fstype == 'SBI':
                file_path = sbi_digitization(file, '')
                shutil.copy(file_path, csv_path)

            elif fstype == 'ICICI':
                file_path = icici_digitization(file)
                shutil.copy(file_path, csv_path)

            elif fstype == 'AXIS':
                file_path = axis_digitization(file, '')
                shutil.copy(file_path, csv_path)

            elif fstype == 'Corporation':
                file_path = corporation_digitization(file, '')
                shutil.copy(file_path, csv_path)

            elif fstype == 'KOTAK':
                file_path = kotak_digitization(file, '')
                shutil.copy(file_path, csv_path)

            ###  end scanned/unscanned

            ### insert document details into the table

    #         sql = "INSERT INTO received_file_details (lead_id, file_name, file_type, file_extension, scanned, uploaded_output, uploaded_datetime) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    #         lid = obj.key.split('_')[0]
    #         spl_word = '_'
    #         fname = obj.key.partition(spl_word)[2]
    #         # fname = ''.join(obj.key.split('_')[1:])
    #         ftype = 'bank'
    #
    #         extension = obj.key.split('.')[1]
    #         s = scanned_flag
    #         fswap = 'ok'
    #         hours = 5.5  ### add hours to match our local timezone
    #         hours_added = datetime.timedelta(hours=hours)
    #         uptime = str(obj.last_modified + hours_added).split('+')[0]
    #         # uptime=str(obj.last_modified).split('+')[0]
    #
    #         val = (lid, fname, ftype, extension, s, fswap, uptime)
    #
    #         mycursor.execute(sql, val)
    #
    #
    #     except Exception as e:
    #         print(e)
    #
    # mydb.commit()  ### until and unless you commit table will not be updated
    # files = glob.glob(r"C:/Users/Abhishek/Desktop/pdf_files/*.pdf")

            os.remove(file)

schedule.every(0.1).minutes.do(job)  ### frequency of code execution

while True:
    schedule.run_pending()
    time.sleep(1)


# def job():
#     print('Digitization')
#     mydb = mysql.connector.connect(
#         host='localhost',
#         user='root',  ###connect to database
#         password='Knowlvers@555',
#         database="details"
#     )
#
#     mycursor = mydb.cursor()
#     file_path = r'C:/Users/shubhamraj/Desktop/pdf_files'  ## Here the pdf is stored after uploading it into the web
#     csv_path = r'C:/Users/shubhamraj/Desktop/digitized_files'  ##  Here we will store the csv after digitisation
#
#     objects_bank = glob.glob(file_path + '/*.pdf')
#     for file in objects_bank:
#         try:
#             fstype = bank_extraction(file)
#             if fstype == 'HDFC':
#                 print('hdfc')
#                 print("New file path is:-")
#                 print(file_path)
#                 file_path = hdfc_digitization(file)  ##SHUBHAM EDIT
#                 shutil.copy(file_path, csv_path)
#
#             elif fstype == 'SBI':
#                 file_path = sbi_digitization(file, '')
#                 shutil.copy(file_path, csv_path)
#
#             elif fstype == 'ICICI':
#                 file_path = icici_digitization(file)
#                 shutil.copy(file_path, csv_path)
#
#             elif fstype == 'AXIS':
#                 file_path = axis_digitization(file, '')
#                 shutil.copy(file_path, csv_path)
#
#             elif fstype == 'Corporation':
#                 file_path = corporation_digitization(file, '')
#                 shutil.copy(file_path, csv_path)
#
#             elif fstype == 'KOTAK':
#                 file_path = kotak_digitization(file, '')
#                 shutil.copy(file_path, csv_path)
#
#             ###  end scanned/unscanned
#
#             ### insert document details into the table
#             sql = "INSERT INTO received_file_details (lead_id, file_name, file_type, file_extension, scanned, uploaded_output, uploaded_datetime) VALUES (%s, %s, %s, %s, %s, %s, %s);"
#             lid = file.key.split('_')[0]
#             spl_word = '_'
#             fname = file.key.partition(spl_word)[2]
#             ftype = 'bank'
#             extension = file.key.split('.')[1]
#             s = 0
#             fswap = 'ok'
#             hours = 5.5  ### add hours to match our local timezone
#             hours_added = datetime.timedelta(hours=hours)
#             uptime = str(file.last_modified + hours_added).split('+')[0]
#             # uptime=str(obj.last_modified).split('+')[0]
#
#             val = (lid, fname, ftype, extension, s, fswap, uptime)
#
#             mycursor.execute(sql, val)
#             mydb.commit()  ### until and unless you commit table will not be updated
#             os.remove(file)
#
#         except Exception as e:
#             print(e)


schedule.every(0.1).minutes.do(job)  ### frequency of code execution

while True:
    schedule.run_pending()
    time.sleep(1)


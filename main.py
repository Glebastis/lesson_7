
import time
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

with open('data','w') as f:
    f.write('Toyota,Corolla,9,1.3')

with open('data') as f:
    data = f.read()
    data_ = data.split(',')

def parce_args(list):
    arguments = ['brand', 'model', 'consumption', 'price']
    return dict(zip(arguments, list))

def from_template(template, signature):

    template = DocxTemplate(template)
    args = parce_args(data_)

    img_size = Cm(15)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    args['acc'] = acc  # adds the InlineImage object to the context
    template.render(args)

    template.save('Output_report.docx')

def generate_report():
    start_time = time.time()
    template = 'Doc.docx'
    signature = 'acc.jpg'
    document = from_template(template, signature)
    print('Время генерации отчета:', time.time() - start_time)
generate_report()

import csv

start_time = time.time()
with open('csv_data.csv', 'w') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(data_)
print('Время генерации csv файла:', time.time() - start_time)

import json

start_time = time.time()
json_data= json.dumps(parce_args(data_))
with open('json_data.json', 'w') as f:
    f.write(json_data)
print('Время генерации json файла:', time.time() - start_time)
import os
import shutil
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')

os.chdir(r'C:\Users\haize\OneDrive\Desktop\data')

for i in os.listdir():
    if '.' not in i:
        continue
    extension = '.' + i.split('.')[-1]
    if extension in doc_types:
        shutil.move(i, 'mis_txts')
    elif extension in img_types:
            shutil.move(i, 'mis_img')
    elif extension in software_types:
                shutil.move(i, 'mis_software')
    else:
           shutil.move(i, 'otros/')
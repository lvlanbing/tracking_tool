import os
import xml.dom.minidom
root = r'G:\my_data\ILSVRC2015_VID\ILSVRC2015'
print(root)
img_root = os.path.join(root,r'Data\VID\train\\')
annotations_root = os.path.join(root,r'Annotations\VID\train\\')
subfile1_ann = os.listdir(annotations_root)
subfile1_img = os.listdir(img_root)
count = 0


for subpath in subfile1_ann:
    #subpath = 'TIR_training_003'
    PATH = os.path.join(annotations_root , subpath)
    PATH = PATH + '\\'
    imgsub_path = os.path.join(img_root,subpath) + '\\'
    path = os.listdir(os.path.join(annotations_root , subpath))
    for p in path:
        xml_path = os.path.join(PATH,p) + '\\'
        img_path = os.path.join(imgsub_path,p) +'\\'
        file = os.listdir(os.path.join(PATH,p))
        f = open(img_path+'groundtruth.txt','wb')
        #with open(img_path+'groundtruth_rect.txt','wb+') as f:
        print(xml_path)
        for i in range(len(file)):
            file_xml = os.path.join(xml_path,file[i])
            print(xml_path)

            print(file_xml)
            dom = xml.dom.minidom.parse(file_xml)

            Element = dom.documentElement

            xmin_body = Element.getElementsByTagName('xmin')
            xmin = float(xmin_body[0].firstChild.data)
            ymin_body = Element.getElementsByTagName('ymin')
            ymin = float(ymin_body[0].firstChild.data)
            xmax_body = Element.getElementsByTagName('xmax')
            xmax = float(xmax_body[0].firstChild.data)
            ymax_body = Element.getElementsByTagName('ymax')
            ymax = float(ymax_body[0].firstChild.data)
            douhao = ','

            xmin = str(xmin)
            ymin = str(ymin)
            xmax = str(xmax)
            ymax = str(ymax)
            f.write(xmin.encode())
            f.write(douhao.encode())
            f.write(ymin.encode())
            f.write(douhao.encode())
            f.write(xmax.encode())
            f.write(douhao.encode())
            f.write(ymax.encode())
            huanghang = '\n'
            f.write(huanghang.encode())

            count += 1
            print(count)
        f.close()



print(subfile1_ann)


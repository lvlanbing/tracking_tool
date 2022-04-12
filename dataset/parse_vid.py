from os.path import join
from os import listdir
import json
import glob
import xml.etree.ElementTree as ET

VID_base_path = '/media/upup/d6c7e0e6-efe4-4f7b-9f42-bfcc4fe51fee/lv_dataset/LSOTB-TIR/Training_Dataset/LSOTB-TIR_TrainingData'
ann_base_path = join(VID_base_path, 'Annotations/')
img_base_path = join(VID_base_path, 'TrainingData/')
sub_sets = sorted({'TIR_training_001', 'TIR_training_002' , 'TIR_training_003', 'TIR_training_004'})

vid = []
for sub_set in sub_sets:
    sub_set_base_path = join(ann_base_path, sub_set)
    videos = sorted(listdir(sub_set_base_path))
    s = []
    for vi, video in enumerate(videos):
        print('subset: {} video id: {:04d} / {:04d}'.format(sub_set, vi, len(videos)))
        v = dict()
        v['base_path'] = join(sub_set, video)
        v['frame'] = []
        video_base_path = join(sub_set_base_path, video)
        xmls = sorted(glob.glob(join(video_base_path, '*.xml')))
        print(video)
        for xml in xmls:
            print(xml)
            f = dict()
            xmltree = ET.parse(xml)
            size = xmltree.findall('size')[0]
            frame_sz = [int(it.text) for it in size]
            objects = xmltree.findall('object')
            objs = []
            for object_iter in objects:
                trackid = int(object_iter.find('trackid').text)
                name = (object_iter.find('name')).text
                bndbox = object_iter.find('bndbox')
                occluded = int(object_iter.find('occluded').text)
                o = dict()
                o['c'] = name
                o['bbox'] = [int(bndbox.find('xmin').text), int(bndbox.find('ymin').text),
                             int(bndbox.find('xmax').text), int(bndbox.find('ymax').text)]
                o['trackid'] = trackid
                o['occ'] = occluded
                objs.append(o)
            f['frame_sz'] = frame_sz
            f['img_path'] = xml.split('/')[-1].replace('xml', 'JPEG')
            f['objs'] = objs
            v['frame'].append(f)
        s.append(v)
    vid.append(s)
print('save json (raw vid info), please wait 1 min~')
json.dump(vid, open('vid.json', 'w'), indent=4, sort_keys=True)
print('done!')

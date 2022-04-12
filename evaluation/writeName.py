import os

jpgs_dir = r"F:\program\PTB-TIR_Evaluation_toolkit-master\PTB-TIR_Evaluation_toolkit-master\perfMat\Overall_all"
# jpgs_dirs = r'F:\program\tool\toolkit-python\vot\sequences'
# videos = ['birds','car','crossing',
# 'crouching',
# 'crowd','depthwise_crossing'
# 'garden',
# 'hiding'
# horse'
# jacket
# mixed_distractors
# quadrocopter
# quadrocopter2
# rhino_behind_tree
# running_rhino
# saturated
# selmaSimaGAT_TIR+GOT_0.5
# soccer
# street
# trees]
for jpg_name in os.listdir(jpgs_dir):
    #matlab
    portion = os.path.splitext(jpg_name)
    if portion[1] == ".txt":
        new_name = portion[0] + "_SiamGAT19_ssm_gray.mat"
        jpg_name = os.path.join(jpgs_dir, jpg_name)  # os.rename的参数需要的是路径和文件名，所以这里要加上路径，要不然脚本执行失败。
        new_name = os.path.join(jpgs_dir, new_name)
        print(jpg_name)
        print(new_name)
        os.rename(jpg_name, new_name)
    # new_name = jpg_name+ '3'
    # jpg_name = os.path.join(jpgs_dir,jpg_name)
    # new_name = os.path.join(jpgs_dir,new_name)
    # print((jpg_name))
    # print(new_name)
    # os.rename(jpg_name, new_name)

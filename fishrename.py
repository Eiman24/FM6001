# 对cocos捕鱼资源文件进行重命名

import os, sys


def main():
    pass
    # list_foldernames = ['dragon', 'quanpingzhadan', 'shayu', 'haitun', 'chuitousha', 'bianfuyu', 'hetun', 'jianzuiyu', 'shiziyu', 'dianman', 'xiaowugui', 'denglongyu', 'hudieyu', 'xiaochouyu']
    # for foldername in list_foldernames:
    #     name_changer(foldername + os.sep + foldername + '_move', foldername + '_move_')
    #     name_changer(foldername + os.sep + foldername + '_capture', foldername + '_capture_')



def name_changer(fish_folder, ren_str):

    # 定义文件路径
    # first_folder = 'fish_png_cocos'
    # second_folder = fish_folder
    filedir = fish_folder

    # 提取、排序
    list_rawname = []
    for filename in os.listdir(filedir):
        list_rawname.append(filename)
    list_rawname.sort()
    if '.DS_Store' in list_rawname:
        list_rawname.remove('.DS_Store')
    # 核对未更改前的文件名
    print(list_rawname)

    # 筛选
    name_dic = dict()
    for rawname in list_rawname:
        suffix = os.path.splitext(rawname)[-1]
        if suffix in name_dic.keys():
            name_dic[suffix] += 1
        else:
            name_dic[suffix] = 1
    print(name_dic)

    my_suffix = max(name_dic, key=name_dic.get)
    spam = []
    for rawname in list_rawname:
        print(rawname)
        suffix = os.path.splitext(rawname)[-1]
        if suffix != my_suffix:
            spam.append(rawname)
    for spamname in spam:
        list_rawname.remove(spamname)
    print(spam)

    # 修改
    rename_string = ren_str
    i = 0
    for rawname in list_rawname:
        src = filedir + os.sep + rawname

        # 提取文件后缀名
        suffix = os.path.splitext(rawname)[-1]

        zero_count = len(str(len(list_rawname)))
        #print(zero_count)

        dst = filedir + os.sep + ren_str + '0'*(zero_count - len(str(i))) + str(i) + suffix
        os.rename(src, dst)
        i += 1

    # notice
    print('重命名成功')


if __name__ == '__main__':
    main()

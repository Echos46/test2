import os
path = 'runs/detect/exp8/labels'
save = 'runs/detect/exp8/label'
os.makedirs(save, exist_ok=True)
for item in os.listdir(path):
    path_item = os.path.join(path, item)
    path_item2 = os.path.join(save, item)
    a = []
    with open(path_item, 'r') as f1, open(path_item2, "a") as f2:
        for line in f1:
            a.append(line)
        for i in a:
            b = str(i)
            m = list(b)
            if m[0] == '0':
                m[0] = 'Table'
            if m[0] == '1':
                m[0] = 'Figure'
            if m[0] == '2':
                m[0] = 'Text'
            if m[0] == '3':
                m[0] = 'Equation'
            b = ''.join(m)
            print(b)
            f2.write("%s" % (b))


txtfilepath = 'runs/detect/exp8/label'
total_txt = os.listdir(txtfilepath)
# print(total_txt)
num = len(total_txt)
list = range(num)
# print(list)
datatxt = open('runs/detect/exp8/datatxt.txt', 'w')
for i in list:
    txt_file = open(os.path.join(txtfilepath, total_txt[i]), 'r')
    txt_list = txt_file.read().splitlines()
    name = total_txt[i][:-4] + '.jpg'+' '
    listlen=len(txt_list)
    for j in range(listlen):
        datatxt.write(name)
        datatxt.write(str(txt_list[j])+ '\n')
    txt_file.close()
datatxt.close()

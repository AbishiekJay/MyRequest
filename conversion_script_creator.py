import os
import datetime
import re

urls_total=[]
urls_list=[]
today_date = datetime.datetime.now()
combined_date = today_date.strftime("%Y-%m-%d")
url_list = open("urlList.csv",'r')
urls_total.append(url_list.read())
print(urls_total)
for values in urls_total:
    urls_list = values.split('\n')
print(urls_list)
for urls in urls_list:
    service = re.search(r'service=(\w+)', urls)
    path_value = re.split(',',urls)
    print(path_value[1])
    folder_path = combined_date+'_'+service.group(1)
    print(folder_path)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        file = open(os.path.join(folder_path,'cjk.txt'),'w')
        file.write(path_value[1])
        file.close
    else:
        new_folder_path = folder_path+'_'+str(path_value[0])
        os.mkdir(new_folder_path)
        file = open(os.path.join(new_folder_path,'cjk.txt'),'w')
        file.write(path_value[1])
        file.close
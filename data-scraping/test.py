from bs4 import BeautifulSoup
import urllib.request
import csv

tien=[]
url = ['https://www.phuclong.com.vn/category/thuc-uong',\
       'https://vnexpress.net/','https://www.phuclong.com.vn/category/thuc-uong']
keywords = ['img','a','button']
get = ['alt','title','data-price']
outkey  = ['dathongbao','delivery']
dk=0
for i in range(len(url)):
    with urllib.request.urlopen(url[i]) as response:
        soup = BeautifulSoup(response,'html.parser')
        read_file = open('data'+str(i+1)+'.txt','a+')
        read_file.close()
        read_file1 = open('data'+str(i+1)+'.txt','r+')
        a = read_file1.readline().split()
        read_file1.close()
        for anchor in soup.find_all(keywords[i]):
            get_ = anchor.get(get[i])
            if get_ in a:
                dk = 1
                
            if dk == 0:
                if get_ == None or ( get_ in outkey):
                        pass
                else:
                    read_file2 = open('data'+str(i+1)+'.txt','a+')
                    read_file2.write(str(get_)+'\n')
                    read_file2.close()
        if dk == 0:
            print ("ok")
            with open('data'+str(i+1)+'.csv', 'w+',encoding='utf-8') as csv_file :
                    
                    for anchor in soup.find_all(keywords[i]):
                        get_ = anchor.get(get[i])
                        
                        if get_ == None or ( get_ in outkey):
                            pass
                        else:
                            if i ==2 :
                                tien.append(get_)
                                writer = csv.writer(csv_file)
                                writer.writerow(['content','min','max'])
                                writer.writerow([get_,min(tien),max(tien)])
                            else:
                                writer = csv.writer(csv_file)
                                writer.writerow(['content','result'])
                                writer.writerow([get_,get_])
        else:
            print("ko")
            continue
                    


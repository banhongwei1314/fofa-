import base64
import requests
from lxml import etree
import time
import xlsxwriter as xw


api_key = ""
headers = {
    'cookie':''
}

def yufa(yeshu,fileName):
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['序号', '网址','名称']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    y2 = 1
    if yeshu >=1 & yeshu <= ip_data3:  #对赋值的值进行判断，不能小于1并大于得到的页数
        for x in range(1,int(yeshu+1)):  #继续循环，限制范围在输入的yeshu（页数），页数加一是结果只是到输入的数小一
            url='https://fofa.so/result?page='+str(x) + "&page_size=10" + '&qbase64=' +search_data  #获得完整的页面
            print('==============================++++分割线++++==================================================')
            print(url)
            try:  #设置异常处理，防止代码运行不下去
                print('正在提取第' + str(x) + '页')
                result=requests.get(url,headers=headers).text  #访问网站，并将headers中的cookie进行使用，因为该网站游客只允许访问一页
                result1=result.encode('utf-8').decode('utf-8')
                soup=etree.HTML(result1) #获取result的数据进行截取信息
                ip_data=soup.xpath('//span[@class="aSpan"]/a[@target="_blank"]/@href')   #截取查询页面中的url
                ip_data1 = soup.xpath('//div[@class="contentLeft"]/p/text()')
                ipdata2 = '\n'.join(ip_data1).replace(' ','')
                ipdata3=str(ipdata2).split()
                # print(ipdata2)
                #     ip_data=soup.xpath('//div[@class="re-domain"]/a[@target="_blank"]/@href')
                # print(ip_data)
                # ipdata='\n'.join(ip_data)  #将’/n‘加入到ip_data里面，实现换行。
                # print(ipdata)

                zzdate =len(ip_data) #得到ip_data数组的长度（数字）
                zzdate1=[]  #形成一个空数组
                for y in range(int(zzdate)):
                    mydict = {}  #形成一个空字典，进行添加数据
                    mydict["id"] = str(y2)   #字典的第一个
                    mydict["url"] = ip_data[y]   #字典的第二个
                    mydict["name"] = ipdata3[y]
                    zzdate1.append(mydict)    #添加数据到字典中
                    y2 +=1   #序号加一
                # print(zzdate1)
                for j in range(len(zzdate1)):
                    insertData = [zzdate1[j]["id"],zzdate1[j]["url"], zzdate1[j]["name"]]  #将字典中的数据赋值给excl文件对应的表头
                    row = 'A' + str(i)
                    worksheet1.write_row(row, insertData)
                    i += 1
                    time.sleep(0.5)
            except Exception as e:
                print(e)
                # print(ipdata)
    workbook.close()  # 关闭表
    print('任务已完成')

if __name__ == '__main__':
    search_data = input("请输入搜索语法：") #给参数赋值
    # search_data ='body="admin123"'
    filename=input("请输入文件名称：")
    fileName=filename +".xlsx"
    search_data = str(base64.b64encode(search_data.encode('utf-8')), 'utf-8')  #将值进行base64加密
    url1 = 'https://fofa.so/result?qbase64=' + search_data  # 将base64假面的值传过来获得fofa页面正常页面
    result1 = requests.get(url1).text  # 访问页面获取页面信息
    soup1 = etree.HTML(result1)  # 获取截图页面信息
    ip_data1 = soup1.xpath('//p[@class="nav-font-size"]/span/text()')  # 对选定的信息进行截取，截取的数据是页面搜索结果的总数
    ip_data2 = ip_data1[0].replace(',', '')  # 因为数字中间存在逗号，使用replace对逗号进行替换
    ip_data3 = round(int(ip_data2) / 10)  # 因展示的页面，一页为十个结果，除以十获得页数。使用round是因为四舍五入
    print('搜索出共' + ip_data2 + '个结果' + '-----------共' + str(ip_data3) + '页')
    yeshu = int(input('请输入下载页数：'))
    yufa(yeshu,fileName) #将值进行传递


























import io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
from bs4 import BeautifulSoup
import re
'''
with open('d:/selenium_test.txt','r+') as f:
    html=f.read()
'''
def resolve(html):
    soup=BeautifulSoup(html,features='html.parser')
    res_list=soup.find_all('span',{'class':'showchild'})
    result_list=[]
    for res in res_list:
        title=res.find_previous_siblings()[0] #兄弟元素中最近的标签.
        category=res.find_parents()[5].find_previous_siblings()[1].find('span',{'id':re.compile('.*CategoryName')})['title']
        title_content=re.sub('[^\u4e00-\u9fa5]','',str(title.contents))
        src=title['href']
        num=res.get_text()
        '''
        print(num)#转载数量
        print(category)#分类
        print(src)#网址
        print(title_content)#标题内容
        '''
        list=[category,src,title_content,num]
        result_list.append(list)
    return result_list



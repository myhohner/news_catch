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
    title_content_list=set()
    for res in res_list:
        title=res.find_previous_siblings()[0] #兄弟元素中最近的标签.
        category=res.find_parents()[5].find_previous_siblings()[1].find('span',{'id':re.compile('.*CategoryName')})['title']
        title_content=re.sub('[^\u4e00-\u9fa5]','',str(title.contents))
        src=title['href']
        num=int(re.sub('[（）]','',res.get_text())) #将()去除
        '''
        print(num)#转载数量
        print(category)#分类
        print(src)#网址
        print(title_content)#标题内容
        '''
        list=[category,src,title_content,num]
        if title_content not in title_content_list:
            result_list.append(list)
            title_content_list.add(title_content)
    return result_list



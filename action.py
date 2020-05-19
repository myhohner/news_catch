import tkinter as tk
from selenium_test import Campaign
from tkinter import ttk
import time
import excel,resolve,os,threading,datetime
import re
window = tk.Tk()
window.title('my window')
window.geometry('400x300')

def thread_it(func):
    # 创建线程
    t = threading.Thread(target=func)
    # 守护线程
    t.setDaemon(True)
    # 启动
    t.start()

var = tk.StringVar()    # 这时文字变量储存器
entry_var=tk.StringVar(value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
def hit_me():
    pb.start()
    var.set('请稍等...')
    
    
    startTime = e.get()
    a=Campaign()
    a.setUp()
    a.select_all(startTime)
    a.select_title()
    html1=a.crawl()
    result_list1=resolve.resolve(html1)
    title_one='single'
    excel.insert(result_list1,title_one)
    time.sleep(3)
    
    a.select_all(startTime)
    html2=a.crawl()
    result_list2=resolve.resolve(html2)

    bowl=[]
    x=''.join('%s'%a[2] for a in result_list1)
    for b in result_list2:
        if re.search(b[2][:10],x):
            bowl.append(b)
    
    for i in bowl:
        result_list2.remove(i)

    title_two='all'
    excel.insert(result_list2,title_two)
    
    a.tearDown()
    var.set('')
    var.set('Finish')
    pb.stop()

l = tk.Label(window, 
    text=r'无烟草',    # 标签的文字
    bg='green',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
l.pack()    # 固定窗口位置


l = tk.Label(window, 
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2,fg='blue')
l.pack() 

#创建输入框entry，用户输入任何内容都显示为*
e = tk.Entry(window,textvariable=entry_var)
e.pack()

b = tk.Button(window, 
    text=r'开始调研',      # 显示在按钮上的文字
    width=15, height=2, 
    command=lambda:thread_it(hit_me))     # 点击按钮式执行的命令
b.pack()    # 按钮位置

pb = ttk.Progressbar(window, length = 400, value = 0, mode = "indeterminate")
pb.pack(pady = 10)



# 这里是窗口的内容
on_hit = False  # 默认初始状态为 False


window.mainloop()
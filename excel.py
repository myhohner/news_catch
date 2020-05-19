import openpyxl,sys,os

def app_path():
    if hasattr(sys,'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)

def insert(result_list,title):
    wb=openpyxl.Workbook()
    ws=wb.active

    ws['A1']='分类'
    ws['B1']='地址'
    ws['C1']='标题'
    ws['D1']='数量'
    for result in result_list:
        ws.append(result)
    path=app_path()+'\\'+title+'.xlsx'
    wb.save(path)

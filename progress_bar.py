import  time  
from progressbar import *  
  
total = 100  
  
def dosomework():  
    time.sleep(0.01)  
  
widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),  
           ' ', ETA(), ' ', FileTransferSpeed()]  
pbar = ProgressBar(widgets=widgets, maxval=10*total).start()  
for i in range(total):  
    # do something  
    pbar.update(10 * i + 1)  
    dosomework()  
pbar.finish()  
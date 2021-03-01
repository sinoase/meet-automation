import time
import subprocess
import webbrowser
from win10toast import ToastNotifier #install dependence: pip install win10toast


hora=time.strftime("%H")
opened =[False,False,False,False,False,False]
classname=""
while int(hora)<14 and int(hora)>0:
	hora=time.strftime("%H")
	urls=""
	if (hora =="08")and(opened[0]==False):
		urls=["Link 1"]#Replace with your meet link
		opened[0] = True
		classname="Class 1"#name of your class
	elif (hora=="09")and(opened[1]==False):
		urls=["Link 2"]
		opened[1]= True
		classname="Class 2"
	elif (hora =="10")and(opened[2]==False):
		urls=["Link 3"]
		opened[2]= True
		classname="Class 3"
	elif hora =="11"and(opened[3]==False):
		urls=["Link 4"]
		opened[3]= True
		classname="Class 4"
	elif hora=="12"and(opened[4]==False):
		urls = ["Link 5"]
		opened[4]= True
		classname="Class 5"
	elif hora=="13"and(opened[5]==False):
		urls = ["Link 6"]
		opened[5]= True
		classname="Class 6"
	if(urls!=""):
		edge_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' #replace with your browser path
		def processExists(processname):
			prog=[line.split() for line in subprocess.check_output("tasklist").splitlines()]
			return any([task[0] == bytes(processname, 'utf8') for task in prog[3:]])
		if processExists('edge.exe'):#Replace 
			for url in urls:
				webbrowser.open_new_tab(url)
		else:
			subprocess.run([edge_path]+urls)
			toaster = ToastNotifier()
			toaster.show_toast(
				"Es hora de entrar a meet ;v",
				"Abriendo la clase "+ classname,
				duration=10
			)
				
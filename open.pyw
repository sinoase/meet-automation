
import time
import subprocess
import webbrowser
import data 
from win10toast import ToastNotifier #install dependence: pip install win10toast
from datetime import date
import calendar

def today_meets(today):
	if today=="Monday":
			todayMeets=data.monday
	if today=="Tuesday":
			todayMeets=data.tuesday
	if today=="Wednesday":
			todayMeets=data.wednesday
	if today=="Thursday":
			todayMeets=data.thursday
	if today=="Friday":
			todayMeets=data.friday
	if today=="Saturday":
			todayMeets=data.saturday
	if today=="Sunday":
			todayMeets=data.sunday
	return todayMeets
		

def send_toast(title,message):
	toaster = ToastNotifier()
	toaster.show_toast(title,message,duration=10)

def processExists(processname):
	prog=[line.split() for line in subprocess.check_output("tasklist").splitlines()]
	return any([task[0] == bytes(processname, 'utf8') for task in prog[3:]])

def open_meet(urls,names):
	if processExists(data.exe_name):
		for url in urls:
			webbrowser.open_new(url)
		send_toast("Meet Time!","Openning Google Meet class: "+names[0])#Set the message!(;
	else:
		subprocess.run([data.browser_path]+urls)
		send_toast("Meet Time!","Openning Google Meet class: "+ names[0])#Set the message!
def run(todayMeets,opened):	
	while True:
		hour=time.strftime("%H")c#
		if(todayMeets.get('hours').__contains__(hour)):
			meets_list=[]
			names=[]
			for meet in todayMeets.get('meets'):
				if meet.get('hour')==hour and not opened[meet.get('id')]:
					meets_list.append(meet.get('link'))
					names.append(meet.get('name'))
					opened[meet.get('id')]=True		
			if meets_list!=[]:
				open_meet(meets_list,names)
		if not opened.__contains__(False):
			break


if __name__ == "__main__":
	curr_date = date.today()
	today=calendar.day_name[curr_date.weekday()]
	todayMeets=today_meets(today)
	count=len(todayMeets.get('hours'))

	opened =[]		
	for i in range(0,count+1):
		opened.append(False)
	run(todayMeets,opened)




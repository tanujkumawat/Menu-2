import os
import getpass
import subprocess

apassword = "wish"
#print("Enter your password = ", end='')
password = getpass.getpass("Enter your passwors :")
if apassword != password:
	print("you are not auth")
	exit()
else:
	os.system("tput setaf 1")            #change the colour of font
	print("\t\twelcome to my menu")
	print("\t\t------------------")
	print("""
	press 1: Check date 
	press 2: Check cal
	press 3: Create user 
	press 4: Create file 
	press 5: To install jdk
	press 6: To install hadoop 
	press 7: install docker
	""")

	print("\n Enter your choice : ", end=' ')
	ch = input()
	if int(ch)==1:
		date_op = subprocess.getstatusoutput("date")
		date_exitcode = date_op[0]		
		date_output = date_op[1]
		if date_exitcode == 0:
			print(date_output) 
	elif int(ch)==2:
		cal_op = subprocess.getstatusoutput("cal")
		cal_exitcode = cal_op[0]
		cal_output = cal_op[1]
		if cal_exitcode == 0:
			print(cal_output)
	elif int(ch)==3:
		print("enter user name : ",end = '')
		user_name_creation = input()
		useradd_op = subprocess.getstatusoutput("useradd {}".format(user_name_creation))
		user_exitcode = useradd_op[0]
		user_output = useradd_op[1]
		if user_exitcode == 0:
			print("{} user has created".format(user_name_creation))
		else:
			print("user exist try another") 
	elif int(ch)==5:
		jdk_op = subprocess.getstatusoutput("rpm -ivh /root/Desktop/jdk-8u171-linux-x64.rpm")
		jdk_exitcode = jdk_op[0]
		jdk_output = jdk_op[1]
		if jdk_exitcode == 0:
			print("installed")
		else:
			print("Already installed")
		os.system("java -version") 
		#os.system("echo # .bashrc\n# User specific aliases and functions\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n. /etc/bashrc\nfi\nexport JAVA_HOME=/usr/java/jdk1.8.0_171-amd64\nexport PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH | cat > /root/.bashrc")
		print("jdk is ready to use")
		os.system("java -version")
	elif int(ch)==6:
		hadoop_op = subprocess.getstatusoutput("rpm -ivh /root/Desktop/hadoop-1.2.1-1.x86_64.rpm")
		hadoop_exitcode = hadoop_op[0]
		hadoop_output = hadoop_op[1]
		if hadoop_exitcode == 0:
			print("installing")
			print(hadoop_output)
		else:
			print("Already installed")
	elif int(ch) == 7:
		docker_op = subprocess.getstatusoutput("yum install docker-ce")
		docker_exitcode = docker_op[0]
		docker_output = docker_op[1]
		if docker_exitcode == 0:
			print("installing")
			print(docker_output)
		else:
			print("Already installed")
			os.system("rpm -q docker-ce")

	else:
		print("do not support")

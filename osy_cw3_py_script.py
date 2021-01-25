import paramiko
import getpass
from time import perf_counter

#parameters for connection to be input by the user
host = input("Enter host IP: ")
port = 22
username = input("Enter your remote account: ")
password = getpass.getpass()

#Initialize SSH client
client = paramiko.SSHClient()
#Add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#tries to connect to the host with the parameters given by the user
#if the parameters are not correct, an exception will be handled
try:
	client.connect(host, port, username, password)
except paramiko.AuthenticationException as error:
	print("Parameters incorrect!")
else:
	#counter stars
	t1_start = perf_counter()
	#the user can input the name of the shell script that will execute on the host VM
	bash_script = open(input("Enter file name: ")).read()
	#execution of the shell script starts
	stdin, stdout, stderr = client.exec_command(bash_script)
	print(stdout.read().decode())

	#counter stops
	t2_stop = perf_counter()

	#counter shown
	print(f"Elapsed time from script execution: {t2_stop - t1_start:0.4f} seconds")

	stdin.close()
finally:
	client.close()
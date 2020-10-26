import subprocess, os, time, sys, shutil

#os.chdir("/home/gabriel/Desktop/repository/proj")
buildNr = 0

while(True):
	os.chdir("/home/gabriel/Desktop/repository/proj")
	print("Start Script")
	print("--------------------")	
	try:
		gitCommit = subprocess.check_output(["git","pull","origin","master"])
		#gitAdd = subprocess.check_output(["git","add","."])
		#gitCommit = subprocess.check_output(["git","commit","-m","mm"])
	except subprocess.CalledProcessError as e:
		gitCommit = e.output.decode()
	commitMessage = gitCommit.decode(sys.stdout.encoding)
	print(commitMessage)
	
	if("Already up to date" in commitMessage):
		print("Commits not detected")
		print("--------------------")
	else:	
		print("Commits detected")
		print("Start Build")
		print("--------------------")
		os.chdir("/home/gabriel/Desktop/proj/proj")
		makeCall = subprocess.call(["make","-f","/home/gabriel/Desktop/proj/script/MakeFile"])
		if(makeCall == 0):
			os.chdir("/home/gabriel/Desktop/repository/builds")
			buildNr += 1
			mkdirCall = subprocess.call(["mkdir","build_" + str(buildNr)])
			mvCall = subprocess.call(["mv","/home/gabriel/Desktop/proj/proj/a.out","/home/gabriel/Desktop/repository/builds/build_" + str(buildNr)])
		else:
			print("Build Failed")

		#print("Push Commits")
		#print("--------------------")
		#os.chdir("/home/gabriel/Desktop/repository/proj")
		#gitpush = subprocess.check_output(["git","push","-u","origin","master"])
		#g = gitpush.decode(sys.stdout.encoding)
		#print(g)
		
	time.sleep(30)

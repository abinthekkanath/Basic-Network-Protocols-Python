from  ftplib import FTP
ftp=FTP('192.168.3.78')
ftp.login(user='anlab008',passwd='Anlab@123')
ftp.cwd('/home/anlab008/')
contents=[]
ftp.dir(contents.append)

ftp.quit()
for item in contents:
	print item

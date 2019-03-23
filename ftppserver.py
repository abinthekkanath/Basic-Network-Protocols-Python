from  ftplib import FTP
ftp=FTP('192.168.3.78')
ftp.login(user='anlab008',passwd='Anlab@123')
ftp.cwd('/home/anlab008/')
remotefilename='publicchat.py'
localfile=open(remotefilename,'wb')
ftp.retrbinary('RETR '+remotefilename,localfile.write,1024)
localfile.close()
ftp.quit()


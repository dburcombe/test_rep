import MySQLdb
import xlsxwriter
import time
#import smtplib
import paramiko
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText

db = MySQLdb.connect(host="localhost",      
                     user="root",           
                     passwd="Waterloo101",  
                     db="testdb")

#datetimesecs = f"{datetime.datetime.now():%Y-%m-%d-%H-%S}"
datetimesecs = time.strftime("%Y-%m-%d-%H-%M")
new_filename = "access" + datetimesecs + ".xlsx"

cursor = db.cursor()
cursor.execute("SELECT * FROM access_details")
table_data = cursor.fetchall()
access_data = [list(ele) for ele in table_data]

wb = xlsxwriter.Workbook(new_filename)
ws = wb.add_worksheet()
i = len(access_data) + 1
ws.add_table("A1:E" + str(i),
{'data':access_data,
   'columns': [
   {'header': 'serial_number'},
   {'header': 'ip_address'},
   {'header': 'timestamp'},
   {'header': 'http_method'},
   {'header': 'browser'}]
   })

wb.close()

#Email

#test_email = 'danielburcombe21@gmail.com'
#message = 'Here is the new access data'

#msg = MIMEMultipart()
#msg['Subject'] = 'access data'
#msg['From'] = test_email
#msg['To'] = test_email

#coud do: msgText = MIMEText(content, 'plain') 
#msgText = MIMEText('<body>{}</body>'.format(message, 'html')
#msg.attach(msgText)

#msg.attach(MIMEText(open(new_filename).read()))

#server = smtplib.SMTP ('smtp.gmail.com', 535)
#server.starttls()
#server.login(test_email, '@Leicester5')
#server.sendmail(test_email, test_email, message)
#server.quit()
#server = smtplib.SMTP ('smtp.gmail.com', 587)
#server.echlo()
#server.starttls()
#server.login(test_email, '@Leicester5')
#server.sendmail(test_email, test_email, msg.as_string())

#connect to new server

hostname = "20.87.214.18"
username = "dburc"
password = "Waterloo1234"

#dirname = "/tmp/"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("df")
print(_stdout.read().decode())
sftp = client.open_sftp()

local_file_path =  new_filename
remote_file_path = "/home/dburc/" + new_filename
sftp.put(local_file_path, remote_file_path)
sftp.close()
#f = sftp.open(dirname + '/' + filename, 'w')
#f.write()
#f.write('testing html')
#f.close()
client.close()


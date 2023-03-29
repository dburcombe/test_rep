import MySQLdb
from tabulate import tabulate
import paramiko
import getpass

db = MySQLdb.connect(host="localhost",      
                     user="root",           
                     passwd="Waterloo101",  
                     db="testdb")

cursor = db.cursor()
cursor.execute("SELECT * FROM bbc_headlines")
table_data = cursor.fetchall()

html_data = []
for ele in table_data:
    html_data.append([repr(string).encode() for string in ele])

table_list = [list(ele) for ele in table_data]
#print(table_data)
#print(html_data)
#print("End of HTML DATA ##############################################")
print(tabulate(html_data, tablefmt='html'))
htmlformat = tabulate(html_data, tablefmt='html')

hostname = "20.87.214.18"
username = "dburc"
#password = "Waterloo1234"
password = getpass.getpass('Password:')
filename = "BBC_Headlines.html"
#filename = "access.html"
dirname = "/var/www/html/"
#dirname = "/tmp/"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("df")
print(_stdout.read().decode())
sftp = client.open_sftp()
f = sftp.open(dirname + '/' + filename, 'w')
f.write(htmlformat)
#f.write("<Table></Table>")
#f.write('testing html')
f.close()
client.close()

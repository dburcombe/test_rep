import paramiko
import MySQLdb

db = MySQLdb.connect(host="localhost",      
                     user="root",           
                     passwd="Waterloo101",  
                     db="testdb")

cursor = db.cursor()
cursor.execute("SELECT * FROM access_details")
table_data = cursor.fetchall()
print(table_data)

html = "<html>\n"
html += "<body>\n"
html += "<h2>Access Table</h2>\n"
html += "<table>\n" 
html += "<tr>\n" 
html += "<th>ip_address</th>\n" 
html += "<th>timestamp</th>\n" 
html += "<th>http_method</th>\n"
html += "<th>browser</th>\n"
html += "</tr>\n" 
for row in table_data: 
    html += "<tr>\n" 
    html += "<td>{}</td>\n".format(row[1]) 
    html += "<td>{}</td>\n".format(row[2]) 
    html += "<td>{}</td>\n".format(row[3])
    html += "<td>{}</td>\n".format(row[4]) 
    html += "</tr>\n" 
html += "</table>\n"  
html += "</body>\n"
html += "</html>"

print(html)

# Update the next three lines with your
# server's information

hostname = "20.87.214.18"
username = "dburc"
password = "Waterloo1234"

filename = "access.html"
dirname = "/var/www/html/"
#dirname = "/tmp/"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("df")
print(_stdout.read().decode())
sftp = client.open_sftp()
f = sftp.open(dirname + '/' + filename, 'w')
f.write(html)
#print(f.read())
#f.write('testing html')
f.close()
client.close()

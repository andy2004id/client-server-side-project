import smtplib
import sqlite3 as db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("andy555id@gmail.com", "Digimon1")
sender="andy555id@gmail.com"

conn=db.connect('email.db')

c1 = conn.cursor()
c2 = conn.cursor()
# Create table
#c.execute('''CREATE TABLE email
#             (addr text, weekday text)''')
#             
#c.execute('''CREATE TABLE sport
#             (others text, weekday text)''')
#
## Insert a row of data
#c.execute("INSERT INTO email VALUES ('testing@gmail.com','tuesday')")
#c.execute("INSERT INTO sport VALUES ('hello world','monday')")
## Save (commit) the changes
#conn.commit()
#conn.close()


def sendMail():

    global sender,c1,c2
    
    
    
    for client in c1.execute('SELECT addr FROM email'):
        msg=''
        msg = MIMEMultipart()
        msg['Subject'] = 'Test Subject no.1'
        msg['From'] ="WHo cares"
        print client[0]+" send"

        for data in c2.execute("SELECT sport.others FROM (email INNER JOIN sport ON email.weekday=sport.weekday) WHERE email.addr='%s'"% client[0]):
            msg.attach( MIMEText(data[0]) )
            
        server.sendmail(sender, client, msg.as_string())
       

def main():
    while(1):
        sendMail()
        # 86400 = 3600*24 = 24hr schduled work
        time.sleep(86400)
    
    
    
    
main()
server.quit()
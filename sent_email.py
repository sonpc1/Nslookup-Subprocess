import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Network.fileDT import DT_trigger

DT_trigger()
fromaddr = "sonpc1@viettel.com.vn"
toaddr = "sonpc1@viettel.com.vn"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Nslookup by subprocess"
body = """
.......................................
"""
try:
    msg.attach(MIMEText(body, 'plain'))
    filename = "kq.csv"
    filename1 = "DOMAIN.csv"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    #encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s %s" % (filename, filename1))
    msg.attach(part)
    server = smtplib.SMTP_SSL('smtp.viettel.com.vn')
    #server.starttls()
    server.login(fromaddr, "Friday@417")
    text = msg.as_string()
    server.sendmail(fromaddr, (toaddr, 'congson20395@gmail.com'), text)
    server.quit()
except Exception as e:
    print(str(e))
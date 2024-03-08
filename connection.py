import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from netmiko import ConnectHandler

useremail = '1358198228@163.com'
password = 'Cisco$2010'
alert_mail = '758965456@qq.com'
smtpserver = 'smtp.163.com'
smtpport = 25

class Net:
    def __init__(self, device_type, host, username, password):
        self.device_info = {
            'device_type': device_type,
            'ip': host,
            'port': 22,
            'username': username,
            'password': password
        }
        self.device = self.connect()
    
    def connect(self):
        return ConnectHandler(**self.device_info)
    
    def reconnect(self):
        self.device.disconnect()
        self.device =self.connect()

    def to_json(self, data_dict, file_path):
        with open(file_path, 'w') as f:
            json.dump(data_dict, fp=f, indent=4)

    def send_mail(self, subject, body):
        message = MIMEText(body, 'html', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = useremail
        message['To'] = alert_mail
        sender = smtplib.SMTP(smtpserver, smtpport)
        sender.login(useremail, password)
        sender.sendmail(useremail, alert_mail, message)
        sender.quit()


    
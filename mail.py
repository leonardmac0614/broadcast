# coding=utf-8
import os
import smtplib
from email.mime.text import MIMEText
from manage import Broadcast
from email.mime.multipart import MIMEMultipart

_user = "147640157@student.usst.edu.cn"
_pwd  = "q2520457"
_to   = "405666135@qq.com"

cityid = "CN101200101"
content = Broadcast().convert_content_for_html(cityid)

fname = os.path.join("email_template.tpl")
with open(fname, "r") as tmpl:
    tst = tmpl.read()
tst = tst.replace("<content>",content)

msg = MIMEMultipart()
msg = MIMEMultipart('alternative')
msg.attach(MIMEText(tst, 'html', 'utf-8'))


msg["Subject"] = "每日早操"
msg["From"]    = _user
msg["To"]      = _to


try:
    s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e
# what

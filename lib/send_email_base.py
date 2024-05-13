#用于建立smtp连接
import smtplib
# 邮件需要专门的MIME格式
from email.mime.text import MIMEText
# plain指普通文本格式邮件内容
msg = MIMEText('今天是个好天气','plain',"utf-8")
# 发件人
msg['From']='157636619@qq.com'
# 收件人
msg['To']='157636619@qq.com'
# 邮件的标题
msg['Subject']='邮件标题-晴天'

smtp =smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('157636619@qq.com','abxamhvliypmbhgd')
smtp.sendmail("157636619@qq.com","157636619@qq.com",msg.as_string())
smtp.quit()

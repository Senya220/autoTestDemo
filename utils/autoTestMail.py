import os
import smtplib
import yagmail
import zipfile
import datetime
import time
from excelHandle import handle_report_data

from email import encoders
from email.mime.image import MIMEImage  # 图片邮件对象
from email.mime.text import MIMEText  # 文本邮件对象
from email.mime.multipart import MIMEMultipart  # 表示整个邮件
from email.mime.base import MIMEBase
from email.header import Header


class mail:
    def __init__(self):
        self.host = 'smtp.163.com'
        self.sender = 'selina202212@163.com'
        self.passwd = 'WVOFIBCOBLYDMKLS'
        # self.receiver = '2042687241@qq.com'
        self.receiver = 'chunyan.guo@thundersoft.com'
        self.port = 25

    def send_mail(self, msg):
        smtp = smtplib.SMTP()
        # smtp.starttls()
        smtp.connect(self.host, self.port)
        smtp.login(self.sender, self.passwd)
        try:
            # encode 附件中有超链接 ascii编码错误
            smtp.sendmail(self.sender, self.receiver, msg.as_string().encode('ascii', errors='ignore'))
            print('send email success')
        except Exception as e:
            print('Error.sent email fail: {}'.format(e))
        smtp.quit()

    def mail_content(self, mail_type, content=None, attachments=None, msg=MIMEMultipart('mixed')):

        # 附件加上allure报告 但allure 单独的index.html打不开，需要想办法生成一个在线报告--服务器！！！

        """

        :param mail_type: text/html/attach/image
        :param attachments:
        :return:
        """
        # 构造邮件对象 （mixed支持附件，related支持内嵌(文本+图片)，alternative支持纯文本+超文本）

        msg['Subject'] = "test mail"
        msg['From'] = self.sender
        msg['To'] = self.receiver

        print('content:{}'.format(content))

        if mail_type == 'text':
            # msg = MIMEText()
            # text_info = 'hello text info'
            text_sub = MIMEText(content, 'plain', 'utf-8')
            msg.attach(text_sub)

        elif mail_type == 'html':
            # 文本消息+csdn.html附件
            html_sub = MIMEText(content, 'html', 'utf-8')
            # 如果不加下边这行代码的话，上边的文本是不会正常显示的，会把超文本的内容当做文本显示
            # 这个地方也可重命名image文件
            # html_sub["Content-Disposition"] = 'attachment; filename="csdn.html"'
            # 把构造的内容写到邮件体中
            msg.attach(html_sub)

        elif mail_type == 'att':
            # msg = MIMEMultipart()
            text_info = 'there hava a allure-result.txt'
            text_sub = MIMEText(text_info, 'plain', 'utf-8')

            att = MIMEBase('application', 'octet-stream')
            att.set_payload(open('report.txt', 'rb').read())
            att.add_header('Content-Disposition', 'attachment', filename=Header('allure-result.txt', 'gbk').encode())
            encoders.encode_base64(att)
            msg.attach(att)
            msg.attach(text_sub)

        elif mail_type == 'image':
            text_info = 'there hava a test.png'
            text_sub = MIMEText(text_info, 'plain', 'utf-8')

            # msg = MIMEMultipart('related')
            image_file = open(attachments, 'rb').read()
            image = MIMEImage(image_file)
            image.add_header('Content-ID', '<image1>')
            # 如果不加下边这行代码的话，会在收件方方面显示乱码的bin文件，下载之后也不能正常打开,这个地方也可以对文件重命名
            image["Content-Disposition"] = 'attachment; filename="red_people.png"'
            msg.attach(image)
            msg.attach(text_sub)

        print('msg:{}'.format(msg))

        return msg

    def ci_html_report(self, data):
        Date = datetime.date.today().isoformat()
        module_data = data['module_data']
        Version = "1.0.0"

        html = """
        <div id="container">
            <div id="content">
                <p>
                    <h1>CI Auto Test Report</h1>
                    <h3>Tester: """ + str(data['tester']) + """ <br>
                    <h3>Version: """ + Version + """ <br>
                    <h3>Start_Time: """ + str(data['start_time']) + """ <br>
                    <h3>End_Time: """ + str(data['end_time']) + """ <br>
                    <h3>Duration: """ + str(data['duration']) + """ <br>
                    <h3>total_cases: """ + str(data['total_cases']) + """ passed: """ + str(
            data['total_passed']) + """ failed: """ + str(data['total_failed']) + """ passed_rate: """ + str(
            data['passed_rate']) + """</p><br>
        <table width="400" border="2" bordercolor="black" cellspacing="2">
            <tr>
                <td ><strong>test_suite</strong></td>
                <td ><strong>total</strong></td>
                <td ><strong>passed</strong></td>
                <td ><strong>failed</strong></td>
                <td ><strong>errored</strong></td>
            </tr>"""
        for item in module_data:
            html += """<tr>
                <td >""" + str(item) + """</td>
                <td >""" + str(module_data[item]['total']) + """</td>
                <td >""" + str(module_data[item]['passed']) + """</td>
                <td >""" + str(module_data[item]['failed']) + """</td>
                <td >""" + str(module_data[item]['errored']) + """</td>
            </tr>"""
        html += """
        </table>
        <p>
            detail in enclose <a href="xxxxxx">
        </p>
        </div>
    </div>"""
        return html


# # 查找最新报告
# def new_report(self, report_path):
#     lists = os.listdir(report_path)  # 列出目录的下所有文件和文件夹保存到lists
#     lists.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn))  # 按时间排序
#     file_new = os.path.join(report_path, lists['-'])  # 获取最新的文件保存到file_new
#     print(file_new)
#     return file_new


# # 对比yamail和smtplib email，选择更好用的
# class yagmail:
#     def __init__(self):
#         self.host = 'smtp.163.com'
#         self.sender = 'selina202212@163.com'
#         self.passwd = 'WVOFIBCOBLYDMKLS'
#         self.receiver = '2042687241@qq.com'
#         self.port = 25


if __name__ == "__main__":
    test_mail = mail()
    # msg = test_mail.mail_content('image', 'test.png')

    data = handle_report_data()
    html = test_mail.ci_html_report(data)
    msg = test_mail.mail_content('html', content=html)
    test_mail.send_mail(msg)

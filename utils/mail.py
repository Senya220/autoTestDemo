import yagmail
import logging


class pmail:
    """
    selina202212@163.com
    Test@20220812
    AFAFYFLRPKDBCIQH
    """
    # def __int__(self):
    #     user = 'selina202212@163.com',
    #     password = 'Test@20220812',
    #     host = 'smtp.163.com',
    #     port = 465,
    #     smtp_starttls=None,
    #     smtp_ssl = True,
    #     smtp_set_debuglevel=0,
    #     smtp_skip_login=False,
    #     encodings='utf-8',
    #     oauth2_file=None,
    #     soft_email_validation=True,
    #     # **kwargsyagmail.SMTP

    def send(self, attachments=None):
        """
        cc: ['1111@qq.com']
        bcc: ['2222@qq.com']

        :param attachments: [r'c://text.txt']
        :return:
        """
        yag = yagmail.SMTP(user='selina202212@163.com', password='Test@20220812', host='smtp.163.com')
        try:
            yag.send(
                to=['2042687241@qq.com'],
                subject='CI自动化测试报告',
                contents='CI测试邮件',
                attachments=attachments,
                cc=None,
                bcc=None
            )
        except Exception as e:
            print('send eamil error:{}'.format(e))
        yag.close()

if __name__ == "__main__":
    pmail().send()
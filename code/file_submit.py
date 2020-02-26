import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl

#添付データ設定用の追加import
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os

#Gamillにログイン系
FROM_ADDRESS = 'zyohoukagaku.misaki@gmail.com' #送信元メールアドレスを指定
MY_PASSWORD = 'misaki0904' #送信元メールアカウントのパスワードを記入

#次のブロックは変更しない
def create_message_jpg(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    body = MIMEText(body)
    msg.attach(body)
    #name には添付ファイル名、path には添付ファイルの所在とファイル名を指定
    attach_file = {'name': 'sample.jpg', 'path': './sample.jpg'}
    #MIMEBase で添付ファイルの種類を指定 (これは JPEG 形式画像データ用の設定)
    attachment = MIMEBase('image', 'jpg')
    file = open(attach_file['path'], 'rb+')
    attachment.set_payload(file.read())
    file.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment",filename=attach_file['name'])
    msg.attach(attachment)
    return msg

def send(from_addr, to_addrs, msg):
    #次の行の引数で SMTP サーバと使用 Port を指定する
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()
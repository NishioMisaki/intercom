from head import *

input_pin = 17
flag = False

#送信先系の変数
TO_ADDRESS = '170440057@gmath.meijo-u.ac.jp' #送信先メールアドレスを指定
BCC = ''
SUBJECT ='報告メール' #送信するメールのタイトル
BODY ='留守中人が訪ねて来ました。' #送信するメールの本文

pi.wiringPiSetupGpio()
pi.pinMode(input_pin,pi.INPUT)

while True:
    if( pi.digitalRead(input_pin) == pi.LOW ):
        if( flag == False ):
            audio()
            flag = True
            cam() #画像撮影
            LED_put(h.shape1) #LEDを点灯
    
            if __name__ == '__main__': #import main.py した際実行されない : __name__ <- main
                                       #python main.py した際実行される : __name__ <- __main__
          
                #メール送信
                to_addr = TO_ADDRESS
                subject = SUBJECT
                body = BODY
                msg = create_message_jpg(fs.FROM_ADDRESS, to_addr, BCC, subject, body)
                LED_put(h.shape2)
                send(fs.FROM_ADDRESS, to_addr, msg)
                print("家主へメール送信完了！")
                LED_put(h.shape3)
    else:
        flag = False
        time.sleep(1)
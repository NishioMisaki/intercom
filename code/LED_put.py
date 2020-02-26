import wiringpi as pi
import time 
def LED_put( shape_tmp ):
    i2c=pi.I2C() # I2Cの準備

    shape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #16bit
    ht16k33 = i2c.setup(0x70) #通信準備
    i2c.writeReg8(ht16k33,0x21,0x01) #ドライバー準備
    i2c.writeReg8(ht16k33,0x81,0x01) #出力準備
    
    for j in range(len(shape_tmp)-2*8 ):
        for i in range(8):
            z = j//8
            shape[i] = (shape_tmp[i+(z)*8]|(shape_tmp[i+(z+1)*8]<<8))<<8*z
            i2c.writeReg8(ht16k33,i*2,shape[i]>>j)
            shape[i] = (shape_tmp[i+(z+1)*8]|(shape_tmp[i+(z+2)*8]<<8))<<8*z
            i2c.writeReg8(ht16k33,i*2+1,shape[i]>>j)
        time.sleep(0.03)
    
    i2c.writeReg8(ht16k33,0x80,0x01) #出力停止
    i2c.writeReg8(ht16k33,0x20,0x01) #ドライバー停止

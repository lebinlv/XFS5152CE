#coding:utf-8
import serial
import binascii
import sys

class xf_speech(object):

    def __init__(self, port, bps=9600, byte_size=8, parity='N', stop_bit=1, time_out=3):

        #打开端口
        self.ser = serial.Serial(port, bps, byte_size, parity, stop_bit, time_out)
        #self.ser.open()

    #语音合成函数
    def speech_sy(self, data='欢迎使用', code_way='gb2312'):

        data_str = str(binascii.b2a_hex(data.encode(code_way)))[2:-1]

        length_str = hex(int(len(data_str)/2)+2)
        if len(length_str)==3:
            n_str = '000'+length_str[2:]
        elif len(length_str)==4:
            n_str = '00'+length_str[2:]
        elif len(length_str)==5:
            n_str = '0'+length_str[2:]
        else:
            n_str = '0000'

        frame_str = 'fd'+n_str+'01'+'00'+data_str
        #print(data_str)
        self.ser.write(binascii.a2b_hex(frame_str))

    #停止语音合成
    def speech_stop(self):
        frame_str = 'fd000102'
        self.ser.write(binascii.a2b_hex(frame_str))

    #暂停语音合成
    def speech_pause(self):
        frame_str = 'fd000103'
        self.ser.write(binascii.a2b_hex(frame_str))

    #恢复语音合成
    def speech_con(self):
        frame_str = 'fd000104'
        self.ser.write(binascii.a2b_hex(frame_str))

    #获取当前状态
    def get_state(self):
        frame_str = 'fd000121'
        self.ser.write(binascii.a2b_hex(frame_str))
        info = self.ser.read(2)
        print (info)

    #进入省电模式
    def power_save(self):
        frame_str = 'fd000188'
        self.ser.write(binascii.a2b_hex(frame_str))

    #唤醒
    def wake_up(self):
        frame_str = 'fd0001ff'
        self.ser.write(binascii.a2b_hex(frame_str))

def speech_test():
    args = sys.argv
    if len(args)==1:
        print('No port provided!')
    elif len(args)==2:
        print('Use default bps: 9600.')
        s=xf_speech(args[1])
    elif len(args)==3:
        s=xf_speech(args[1],args[2])
    else:
        print('Too many arguments')
    s.speech_sy()
    #s.ser.close()

if __name__=='__main__':
    speech_test()

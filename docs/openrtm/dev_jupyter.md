# OpenRTMをJupyerから操作する

## RaspberryPI向け調整

改行コードは、¥r¥nになっているので、¥nに修正。

## Jupyterとの調整

configファイル(rtc.conf)の参照先が、jupyterによる上書きされるので、defaultのconfigファイルの参照先でconfigを呼び出すように修正。

## Jupyterからの起動

一般的なPythonプログラムでJupyterからRTCの開発が可能になる。

問題点としては、RTCを終了した際に、KernelがShutdownする。

## Sample Code

FloatSeqをから、コントロール座標を読み取るサンプル

RTC, OpenRTM_aist, robotcarをimportする。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import sys
import time

import RTC
import OpenRTM_aist

import robotcar
```

RTCの属性情報

```python
seqin_spec = ["implementation_id", "SeqIn",
              "type_name",         "RobotCarComponent",
              "description",       "RobotCar InPort component",
              "version",           "1.0",
              "vendor",            "GClue, Inc.",
              "category",          "robot",
              "activity_type",     "DataFlowComponent",
              "max_instance",      "10",
              "language",          "Python",
              "lang_type",         "script",
              ""]
```

map関数を自作する

```python
def valueMap(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
```

Robotcar制御のサンプル

```python
class SeqIn(OpenRTM_aist.DataFlowComponentBase):
    
    def __init__(self, manager):
        print "__init__"
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
        
        return

    def onInitialize(self):
        print "onInitialize"
        self._r = robotcar.Robot()
        self._r.handle_init()
        self._floatSeq  = RTC.TimedFloatSeq(RTC.Time(0,0),[])        
        self._floatSeqIn  = OpenRTM_aist.InPort("FloatSeq", self._floatSeq)

        # Set InPort buffer
        self.addInPort("FloatSeq", self._floatSeqIn)
        return RTC.RTC_OK
    
    def onExecute(self, ec_id):
        
        floatSeq_  = self._floatSeqIn.read()        
        floatSize_  = len(floatSeq_.data)
        
        if floatSize_ > 0:
            power = int(floatSeq_.data[1])
            handle = int(floatSeq_.data[0])
            sys.stdout.write("\r%d  %d   " % (power, handle))
            sys.stdout.flush()
        
            if power < -10:
                power = valueMap(-power, 0, 150, 0, 100)
                self._r.car_back(power)
            elif power > 10:
                power = valueMap(power, 0, 150, 0, 100)
                self._r.car_forward(power)
            else:
                self._r.car_stop()
                
            handle = valueMap(handle, -150, 150, 7.5, 10.5)
            if handle < 8.9 or handle > 9.1:
                self._r.handle_move(handle)
            else:
                self._r.handle_move(9)
            
        time.sleep(0.5)
        return RTC.RTC_OK
```

Mainの呼び出し

```python
def SeqInInit(manager):
    print "SeqInInit"
    profile = OpenRTM_aist.Properties(defaults_str=seqin_spec)
    manager.registerFactory(profile,
                          SeqIn,
                          OpenRTM_aist.Delete)

def MyModuleInit(manager):
    print "MyModuleInit"
    SeqInInit(manager)

    # Create a component
    comp = manager.createComponent("SeqIn")

def main():
    print "run"
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()
    
if __name__ == "__main__":
    main()
```

## rtc.confを用意する

rtc.conf
```
corba.nameservers: localhost
naming.formats: %n.rtc
logger.enable: NO
```

## rtc.confの環境変数を設定

```shell
!export RTC_MANAGER_CONFIG="/home/pi/OpenRTM/SeqIO/rtc.conf"
```
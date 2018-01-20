# XFS5152C语音合成芯片上位机模块


## Requirements


* Python3.6 or newer 
* pyserial

## Introduction

Connect your chip with your device through serial, this module will help you to control your chip. This module support both and English.

## Start use


```python

from speech import xf_speech

s = xf_speech('COM9')         #default bps=9600

```

Start eith bps setted:

`s = xf_speech('COM9', 9600)    #set bps=9600`


## Api introduction

### Start speech synthesis


```python

s.speech_sy()    # It will speek "欢迎使用" 

s.speech_sy('再次尝试')      #Speek "再次尝试"

```

### Stop speech synthesis

` s.speech_stop()`

### Suspend speech synthesis

`s.speech_pause()`

### Continue speech synthesis

`s.speech_con()`

### Power save mode

`s.power_save()`

### Wake up form power save mode

`s.wake_up()`

## Test through console

> python3 .\speech.py COM9 9600   #"COM9" and "9600" should be setted according to actual condition

If your chip speaks "欢迎使用", It works!

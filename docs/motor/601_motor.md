# #601 Motor Shield for Arduino

[](../img/600_shield/product/600_motor_product.jpg)
<!--COLORME-->

## Overview
2個のDCモーターを制御することができるシールドです。

モーターを動かすには外部からの電源供給が必要になります。

## コネクタ

### DCモータ用コネクタ
- Moter1用コネクタ
 - D2 (信号1)
 - D4 (信号2)
- Moter2用コネクタ
 - D5 (信号1)
 - D7 (信号2)
- 外部電源(DCモータ用)

### アナログコネクタ
- A0
- A1

### デジタルコネクタ
- D12
- D13

### PWM/Servoコネクタ
- サーボモータ接続用コネクタ
 - PWMに対応するD9

### シリアルコネクタ
SoftwareSerialとして使用するため、RX,TXはそれぞれ、D12,D13になります

### I2Cコネクタ
Arduino MEGAではR3以降から対応になります。
Arduino UNO R3/R2では使用可能です。


## PIN配置について
モーターシールドのピンは以下のようになっています。

| Pin |モーターNo| 説明 |
| -- | -- | -- |
| D2 | 1 | 信号1 |
| D3 | 1 | 出力値設定 |
| D4 | 1 | 信号2 |

| Pin |モーターNo| 説明 |
| -- | -- | -- |
| D5 | 2 | 信号1 |
| D6 | 2 | 出力値設定 |
| D7 | 2 | 信号2 |


## 動作方法について
モーター（モータードライバ）に対して2つの信号を送り、その組み合わせによってモーターを制御することができます。

| 信号1 | 信号2 | 動作 |
| -- | -- | -- |
| <font color='#FF0000'>HIGH | <font color='#0000FF'>LOW | 前進 |
| <font color='#0000FF'>LOW | <font color='#FF0000'>HIGH | 後退 |
| <font color='#0000FF'>LOW | <font color='#0000FF'>LOW | 静止 |

<font color='#FF0000'> 信号1、信号2の両方をHIGHにすると、部品が壊れる可能性があるので設定しないようにして下さい。




### for Arduino

```c
void setup() 
{ 
  // DCモーター1
  pinMode(2, OUTPUT); // モーター1のピン1(前進用)
  pinMode(3, OUTPUT); // モーター1の出力設定用
  pinMode(4, OUTPUT); // モーター1のピン2(後退用)
  
  // DCモーター2
  pinMode(5, OUTPUT); // モーター2のピン1(前進用)
  pinMode(6, OUTPUT); // モーター2の出力設定用
  pinMode(7, OUTPUT); // モーター2のピン2(後退用)
  
} 

void loop()
{
  // モーター1の設定(HIGH/LOW:前進)
  digitalWrite(2, HIGH); 
  digitalWrite(4, LOW);   
  analogWrite(3, 255); // 0-255 強さ
  
  // モーター2の設定(LOW/HIGH:後退)
  digitalWrite(5, LOW); 
  digitalWrite(7, HIGH);   
  analogWrite(6, 255); // 0-255 強さ

  delay(10);
}

```

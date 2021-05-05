# What's this?
- ラズパイで色や水流を制御するプログラム

# How to use?
- LED.py
  - クラス `LED` のコンストラクタにRed,Green,Blueそれぞれのピン番号を渡す
  - 呼び出しは()演算子、引数はRGBそれぞれを0〜255まで
    - ex) led(255, 0, 0)
    - 内部処理としては、これを100/255倍して整数にしている
- PUMP.py
  - クラス `PUMP` のコンストラクタにPUMPのピン番号を渡す
  - 呼び出しは()演算子、引数はポンプのオン/オフ
    - ex) pump(True)
    - 内部処理としては、これをboolで評価してTrueのときにHIGHの信号を出力している

# Test
- lchika.py
  - lチカする
- pwm.py
  - pwmを用いて色を連続的に変化させる
- dynamic_control.py
  - ダイナミック制御を用いた制御の例
  - testにあるプログラムは失敗する


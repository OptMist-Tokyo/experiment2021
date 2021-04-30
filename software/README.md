# What's this?
- 音楽から色を指定してファームウェアに渡すプログラム

# How to use?
## install
- pyAudioAnalysis
  - `$ pip install numpy matplotlib scipy sklearn hmmlearn simplejson eyed3 pydub`

## firmware-intrerface
- firmwareを使う際は、プログラムの最初に次の行を追加
```
import sys
import pathlib
firmware_path = str(pathlib.Path('../firmware').resolve())
sys.path.append(firmware_path)
```
- firmwareのディレクトリにあるプログラムをimportできるようになる


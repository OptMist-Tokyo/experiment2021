echo "alias pip='pip3'" >> ${HOME}/.bashrc
echo "alias python='python3'" >> ${HOME}/.bashrc

git submodule update --init --recursive
pip3 install -r color_your_music_mood/requirements.txt
pip3 install opencv-python
pip3 install scipy
sudo apt install libatlas-base-dev
pip3 install pyAudioAnalysis
pip3 install matplotlib
pip3 install eyed3
pip3 install pydub
pip3 install tqdm
pip3 install sklearn
pip3 install plotly
pip3 install pyaudio
sudo apt-get install libportaudio2

sudo touch /etc/modprobe.d/alsa-base.conf
sudo vim /etc/modprobe.d/alsa-base.conf

options snd slots=snd_usb_audio,and_bcm2835
options snd_usb_audio index=0
options snd_bcm2835 index=1

sudo reboot

amixer -D hw:1 sset Mic 100%


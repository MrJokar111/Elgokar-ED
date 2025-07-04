اكتب الاوامر دي أمر أمر الافضل تنسخهم امر امر بدون اخطاء !



sudo apt update && sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget curl git openssl nodejs

cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
sudo tar xzf Python-2.7.18.tgz
cd Python-2.7.18
sudo ./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall


curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo /usr/local/bin/python2.7 get-pip.py

sudo ln -s /usr/local/bin/python2.7 /usr/bin/python2
sudo ln -s /usr/local/bin/pip2 /usr/bin/pip2

pip2 install requests mechanize bs4 uncompyle6

sudo npm install -g bash-obfuscate



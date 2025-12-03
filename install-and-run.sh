cd
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3 python3-pip python3-venv
python3 -m venv ~/venv
git config --global --add safe.directory /root/flutter/3.29.2
git clone https://github.com/nekstas/simple-game-lib.git app
cd app
git checkout snake
source ~/venv/bin/activate
python3 -m pip install flet[all]
cd src
flet publish <your-flet-app.py>
python -m http.server --directory dist

# api
sudo pip3 install virtualenv
python3 -m venv api/venv
source api/venv/bin/activate
pip3 install -r api/requirements.txt

# ui
npm install --prefix ui
npm run build --prefix ui


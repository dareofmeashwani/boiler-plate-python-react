export ENV=development
cd api
source venv/bin/activate
python3 -m debugpy --listen localhost:5678 --wait-for-client ./main.py
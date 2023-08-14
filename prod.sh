export ENV=production
source api/venv/bin/activate
npm run build --prefix ui
python3 api/main.py

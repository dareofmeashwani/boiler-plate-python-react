export ENV=development
source api/venv/bin/activate
./parallel.sh "npm run start --prefix ui" "python3 api/main.py"
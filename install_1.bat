python -m venv venv
CALL ".\venv\Scripts\activate.bat"
python -m pip install --upgrade pip
pip install -r requirements.txt
cd ./Gym-FightingICE
pip install -e .

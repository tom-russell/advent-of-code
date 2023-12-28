### Setting up the repo
Recommended to use a virtual environment. Create a new venv like so:
```
python -m venv .venv
```
Activate your venv and install requirements like so:
```
source .venv/bin/activate
pip install -r requirements.txt
```

### Adding a new day
Use the `new_day.py` file to generate a new day directory like so:
```
python new_day.py <year> <day_no> <day_name> 
```
example:
```
python new_day.py 2023 01 Trebuchet?!
```

To generate the ASCII Art:
http://patorjk.com/software/taag/#p=display&f=Big
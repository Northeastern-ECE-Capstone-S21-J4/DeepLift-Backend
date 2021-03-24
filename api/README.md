# DeepLift Backend API

## Install
You will need a functioning Python install and to be running in Unix/MacOS.
0. Clone this repo and change to the `api/` directory
```
git clone git@github.com:Northeastern-ECE-Capstone-S21-J4/DeepLift-Backend.git
cd DeepLift-Backend/api
```
1. Create a virtual env with Python and activate it
```
python3 -m venv backend
source backend/bin/activate
``` 
2. Install Python dependencies
```
pip install -r requirements.txt
```
3. Start FastAPI server
```
uvicorn main:app --reload
```
4. Test server by going to http://127.0.0.1:8000. You should see `{"Hello":"World"}` in your browser.

5. To see the API docs, go to http://127.0.0.1:8000/redoc.  
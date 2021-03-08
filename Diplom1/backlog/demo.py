from mygoogle import Create_Service

CLIENT_SECRET_FILE = 'client_secret_318809934297-tlr9ssl5mqeqd53ha07c8s29p1fn274c.apps.googleusercontent.com.json'
API_SERVICE_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

print(dir(service))
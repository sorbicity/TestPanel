import sys
path = '/home/sorbia/sorbia.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)

from api import app
application = app

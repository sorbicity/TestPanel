import sys
path = '/home/sorbia/mysite'
if path not in sys.path:
    sys.path.append(path)

from api import wsgi_app as application

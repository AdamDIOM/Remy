import sys
path = '/home/zxtheo/mysite'
if path not in sys.path:
   sys.path.insert(0, path)

import server as application
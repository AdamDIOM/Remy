import sys
path = '/home/yourusername/mysite/Remy'

if path not in sys.path:
   sys.path.insert(0, path)

import server as application
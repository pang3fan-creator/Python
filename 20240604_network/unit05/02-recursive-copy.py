
import os
import shutil
from time import  time

def copy_directory(src,dest):
    if not os.path.exists(src) or os.path.exists(dest):
        return False
    if not os.path.exists(dest):
        os.mkdir(dest)
    items = os.listdir(src)
    for item in items:
        if os.path.isfile(os.path.join(src,item)):
            shutil.copy(os.path.join(src,item),os.path.join(dest,item))
        if os.path.isdir(os.path.join(src,item)):
            copy_directory(os.path.join(src,item),os.path.join(dest,item))

src = 'images'
dest = 'abcdef'
start = time()
copy_directory(src,dest)
end = time()
print(end-start)
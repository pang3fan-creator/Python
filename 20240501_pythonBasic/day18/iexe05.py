from datetime import datetime
from pathlib import Path

for item in Path.cwd().parent.rglob('*.png'):
    print(item)
for item in Path.cwd().parent.rglob('*.txt'):
    print(datetime.fromtimestamp(item.stat().st_mtime)
          .strftime('%Y-%m-%d %H:%M:%S'))
for item in Path.cwd().parent.rglob('exercise*'):
    print(item)
print(list(map(lambda x: x.stat().st_size,
               Path.cwd().parent.rglob('exercise*'))))

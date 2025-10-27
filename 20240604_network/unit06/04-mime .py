import mimetypes

filepath_list = ['a/1.html', 'b/1.css', '1.js', '1.json', '1.jpg', '1.jpeg', '1.png', '1.gif']

for item in filepath_list:
    mime_type, _ = mimetypes.guess_type(item)
    print(f'文件{item},其MIME类型为:{mime_type}')
    print(_)

import uuid

filename = '123.txt.png.css.html.Jpg'

extension = filename[filename.rfind('.')+1:].lower()

mainame = str(uuid.uuid1())

new_filename = mainame + '.' + extension

print(new_filename)


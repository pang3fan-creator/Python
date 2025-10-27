import os.path
import time


def copy_directory(src, dest):
    if (not os.path.exists(src)) or os.path.exists(dest):
        print('出错了')
        raise Exception('src or dest is not exist')
    if not os.path.exists(dest):
        os.mkdir(dest)
    for item in os.listdir(src):
        if os.path.isdir(os.path.join(src, item)):
            copy_directory(os.path.join(src, item), os.path.join(dest, item))
        else:
            with open(os.path.join(src, item), 'rb') as f:
                with open(os.path.join(dest, item), 'wb') as f1:
                    f1.write(f.read())


if __name__ == '__main__':
    src = 'images'
    dest = 'images_copy'
    start = time.time()
    copy_directory(src, dest)
    end = time.time()
    print(end - start)

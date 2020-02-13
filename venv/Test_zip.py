import zipfile
import os
import time

source = "C:\\1"
backup = "D:\\"


def backupZip(s, b):
    if not (os.path.isabs(s) and os.path.isdir(s)):
        print("Директория {} не существует".format(s))
        return
    if not (os.path.isabs(b) and os.path.isdir(b)):
        print("Директория {} не существует".format(b))
        return

    comment = input("введите комментарий ")
    if comment == '':
        pass
    else:
        comment = '_' + comment.replace(' ', '_')

    name = time.strftime('%Y%m%d%H%M%S') + comment + '.zip'
    backupFile = os.path.join(backup, name)

    zipFile = zipfile.ZipFile(backupFile, 'w')

    dirName = ''
    for root, dir_, files in os.walk(source):
        print('добавление файлов из директории {}'.format(root))
        dirName = '/'.join(([dirName, os.path.basename(root)]))
        # print(dirName)
        zipFile.write(root, dirName)
        for file in files:
            fileName = dirName + '/' + file
            zipFile.write(os.path.join(root, file), fileName)
    # zipFile.write('Hello.txt')

    zipFile.close()


backupZip(source, backup)

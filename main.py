import zipfile
import os
# import socket
# import pathlib

file = 'C:\\Users\\Admin\\PycharmProjects\\DZ_1\\files.zip'

with zipfile.ZipFile(file, 'r') as myzip:
    while True:
        infoStr = f'localhost:$ '
        command = input(infoStr)
        if command == 'ls':
            for i in myzip.namelist():
                print(i, end='   ')
            print()

        elif command == 'ls -l':
            for file_info in myzip.infolist():
                print(file_info.filename, file_info.date_time, file_info.file_size)

        elif command[0:2] == 'cd':
            # os.chdir(command[3:])

            current_dir = os.getcwd()
            new_dir = os.path.join(current_dir, command[3:])

        elif command[0:3] == 'rev':
            list = []
            with myzip.open(f'{command[4:]}', 'r') as zipfile:
                for i in zipfile.readlines():
                    list.append(i.decode('utf8').split('\r\n')[0])
                for line in list:
                    print(line[::-1])
                zipfile.close()

        elif command[0:4] == 'tail':
            list = []
            with myzip.open(f'{command[5:]}', 'r') as zipfile:
                for i in zipfile.readlines():
                    list.append(i.decode('utf8').split('\r\n')[0])
                for line in range(-10, 0):
                    print(list[line])
                zipfile.close()

        elif command[0:5] == 'rmdir':
            directory = command[6:]
            os.rmdir(directory)

        elif command == "exit":
            myzip.close()
            break

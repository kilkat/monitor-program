import os
import hashlib

def get_file_hash(file_path):
    hasher = hashlib.sha256()

    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(4096), b''):
            hasher.update(block)

    return hasher.hexdigest()

def get_directory_hash(directory_path):
    directory_hasher = hashlib.sha256()

    for root, dirs, files in os.walk(directory_path):
        dirs.sort()
        files.sort()

        directory_hasher.update(root.encode())

        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f'{file_path}: {get_file_hash(file_path)}')

    return directory_hasher.hexdigest()

path = 'C:\\Users\\rhkdd\\Desktop\\game'

print(f'Directory Hash: {get_directory_hash(path)}')

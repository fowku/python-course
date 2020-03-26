import os


def show_files():
    dir = input('Enter directory')
    files = []

    directory = os.listdir(dir)

    for file in directory:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            files.append({'name': file, 'size': os.stat(path).st_size})

    files.sort(key=lambda x: (-x['size'], x['name']))

    print(files)

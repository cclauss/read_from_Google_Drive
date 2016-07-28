#!/usr/bin/env python3
# coding: utf-8

# Appex script to copy a file or folder from the Google Drive app

import appex, os, shutil

from_gd = os.path.abspath(os.path.expanduser('from Google Drive'))


def move_files(file_paths):
    for file_path in file_paths:
        local_path = file_path[0].split('/GDKGenoaContentProvider/')[-1]
        local_path, file_name = os.path.split(local_path)
        if local_path == '/':
            local_path = ''
        local_path = os.path.join(from_gd.strip(), local_path.strip())
        # print(from_gd, local_path)
        os.makedirs(local_path, exist_ok=True)
        # print(local_path)
        shutil.copy2(file_paths[0], local_path)
        print('{} was copied to {}'.format(file_name, local_path))


def main():
    if appex.is_running_extension():
        file_paths = appex.get_file_paths()
        assert file_paths, 'No file paths found!'
        print(len(file_paths), file_paths)
        move_files(file_paths)
    else:
        print('''In Google Drive app select a file, to be copied into
Pythonista.  Click the "Send a copy".  Click "Run Pythonista Script".  Pick
this script and click the run button.  When you return to Pythonista the
files should be in the 'from Google Drive' directory.'''.replace('\n', ' '))

if __name__ == '__main__':
    main()

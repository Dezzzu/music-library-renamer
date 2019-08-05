import argparse
import os
import shutil
import pathlib

about = {
    'name': 'Music Library Renamer',
    'version': '1.1',
    'author': 'Daniil Naumov (Dezzzu)',
    'desc': 'Renames all files in given directory and its sub-directories and changes directory structure. Output'
            'format: folders are named CD01, CD02, ...; files are named 001, 002, ... + old name.',
    'url': 'https://github.com/Dezzzu/music-library-renamer'
}

default_directory = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument('--about',
                    action='store_true',
                    default=False,
                    help='Prints info about this script')
parser.add_argument('--copy',
                    action='store_true',
                    default=False,
                    help='Copies files instead of renaming them if present')
parser.add_argument('--noclear',
                    action='store_true',
                    default=False,
                    help='Prevents removing input directory tree')
parser.add_argument('--input',
                    action='store',
                    default=default_directory,
                    dest='input_directory',
                    help='Input directory in OS-specific format')
parser.add_argument('--output',
                    action='store',
                    default=default_directory,
                    dest='output_directory',
                    help='Output directory in OS-specific format')
args = parser.parse_args()


def is_empty(directory_path):
    for _, _, no_filenames in os.walk(directory_path):
        if len(no_filenames) > 0:
            return False
    return True


if __name__ == '__main__':
    if args.about:
        print('\nName: ' + about['name'])
        print('Version: ' + about['version'])
        print('Author: ' + about['author'])
        print('Description: ' + about['desc'])
        print('GitHub: ' + about['url'])
    else:
        print('Please don\'t close console window while script works, it will state it has ended its work.')

        current_cd = 1
        current_track = 1

        action = shutil.copy2 if args.copy else shutil.move
        action_name = 'Copying' if args.copy else 'Renaming'

        for directory, _, filenames in os.walk(args.input_directory):
            for filename in filenames:
                if filename.endswith('.mp3'):
                    source_file = os.path.join(directory, filename)
                    destination_directory = os.path.join(args.output_directory,
                                                         'CD' + ('0' if current_cd < 10 else '') + str(current_cd))
                    pathlib.Path(destination_directory).mkdir(parents=True, exist_ok=True)
                    destination_file = os.path.join(destination_directory,
                                                    ('00' if current_track < 10 else '0') +
                                                    str(current_track) + ' ' + filename)
                    print(action_name + ' ' + source_file + ' to ' + destination_file)
                    action(source_file, destination_file)
                    current_track += 1
                    if current_track > 99:
                        current_track = 1
                        current_cd += 1

        if not args.copy and not args.noclear:
            for directory, _, _ in os.walk(args.input_directory):
                if is_empty(directory):
                    print('Removing ' + directory)
                    shutil.rmtree(directory)

        print('All done!')

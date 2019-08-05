# Music Library Renamer  

I got myself a Yatour YT-M06 digital CD changer which can only read files from USB stick if they are separated into several "CDXX" folders and have names "0XX filename.mp3".  
My music library is large so renaming files manually wasn't an option - which is why I decided to write a simple Python script that is doing this routine work for me.

## Usage
python main.py [-h] [--about] [--copy] [--noclear] [--input INPUT_DIRECTORY]
               [--output OUTPUT_DIRECTORY]

## Arguments
| Argument                  | Description                                                                    |
| ------------------------- | ------------------------------------------------------------------------------ |
| -h, --help                | Shows this help message and exit                                               |  
| --about                   | Prints info about this script                                                  |
| --copy                    | Copies files instead of renaming them if present                               |
| --noclear                 | Prevents removing input directory tree                                         |
| --input INPUT_DIRECTORY   | Input directory in OS-specific format (defaults to current working directory)  |
| --output OUTPUT_DIRECTORY | Output directory in OS-specific format (defaults to current working directory) |

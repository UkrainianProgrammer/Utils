# Util to remove duplicated images across subdirectories
import hashlib
import os

def pathInput() -> str:
    directory = input("Please provide full path to the directory: ")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"No such directory named {directory} exists")
    else:
        return directory

def main():
    directory = pathInput()
    hashset=set()

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            digest = hashlib.sha1(open(path, 'rb').read()).digest()
            if digest not in hashset:
                hashset.add(digest)
            else:
                print(f"Removing {path}...")
                os.remove(path)

# prompt the user for the path
if __name__ == '__main__':
    main()
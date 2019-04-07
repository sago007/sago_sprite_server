import pathlib
import json
from typing import Dict,Any

def getTextures():
    arr = []
    for p in pathlib.Path('data/textures').iterdir():
        arr.append(p)
    return arr


def getSprites():
    arr = []
    for p in pathlib.Path('data/sprites').iterdir():
        arr.append(p)
    return arr


def loadSpriteFile(filename):
    arr = []
    with open(filename) as json_file:
        data = json.load(json_file)
        arr.append(data)
    return arr


def loadJsonDict(filenames) -> Dict[str, Any]:
    myDict = {}
    for filename in filenames:
        with open(filename) as json_file:
            data = json.load(json_file)
            myDict[filename] = data
    return myDict


def main():
    print("Starting")
    textures = getTextures()
    sprite_files = getSprites()
    json_data_dict = loadJsonDict(sprite_files)
    for sprite_file in sprite_files:
        json_data = json_data_dict.get(sprite_file)
        for (k, v) in json_data.items():
            if k.startswith("_"):
                #keys starting with "_" is comments, skip them
                continue
            print(k, v)


main()
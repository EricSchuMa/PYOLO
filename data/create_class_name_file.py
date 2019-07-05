import json
from bdd100k.labels.parse_labels import load_json_file, PATH_CATEGORY_DICT


PATH = "bdd100k/labels/" + PATH_CATEGORY_DICT


def main():
    loaded = load_json_file(PATH)
    with open("classes.names", "w+") as f:
        for category in sorted(loaded.items(), key=lambda x: x[1]):
            f.write(category[0] + "\n")

    

if __name__ == "__main__":
    main()

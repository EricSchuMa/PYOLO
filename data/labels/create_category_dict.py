import json
from parse_labels import load_json_file, PATH_MINI, PATH_TRAIN, PATH_VAL, PATH_CATEGORY_DICT


def main():
    # Load the label file
    loaded = load_json_file(PATH_VAL)

    category_dict = {}
    i = 0
    for image in loaded:
        labels = image["labels"]
        for label in labels:
            category = label["category"]
            # Ignore labels without a bounding box and add key only once
            if "box2d" in label.keys() and category not in category_dict.keys():
                category_dict[category] = i
                i += 1
    
    with open(PATH_CATEGORY_DICT, "w+") as f:
        json.dump(category_dict, f, indent=4)


if __name__ == "__main__":
    main()

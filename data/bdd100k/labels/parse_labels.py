import json


PATH_MINI = "first_two.json"

PATH_TRAIN = "bdd100k_labels_images_train.json"
PATH_VAL = "bdd100k_labels_images_val.json"

PATH_OUTPUT = "parsed/"

PATH_CATEGORY_DICT = "category_dict.json"

IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720


def write_first_two_objects(loaded):
    first_two = loaded[:2]
    with open(PATH_MINI, 'w+') as f:
        json.dump(first_two, f, indent=4)

def load_json_file(path):
    try:
        f = open(path)
    except FileNotFoundError as fne:
        print(fne)
        exit(1)
    
    try:
        loaded = json.load(f)
    except json.JSONDecodeError as jde:
        print('"%s" is not a valid json file' % path)
        print(jde)
        exit(1)
    finally:
        f.close()

    return loaded

def parse_label_file(path: str) -> None:
    print('Parsing file "%s"' % path)

    loaded = load_json_file(path)

    category_dict = load_json_file(PATH_CATEGORY_DICT)

    path_stripped = path[:path.rfind(".json")] if ".json" in path else path
    path_output = PATH_OUTPUT + path_stripped
    for image in loaded:
        name = image["name"]
        name_stripped = name[:name.rfind(".jpg")] + ".txt"
        labels = image["labels"]

        # open file to write 
        path_new = path_output + "/" + name_stripped
        try:
            f = open(path_new, "w+")
        except Exception as e:
            print('Could not open "%s"' % (path_new))
            print("Does the containing folder exist?")
            print(e)
            exit(1)
        
        for label in labels:
            if "box2d" not in label.keys():
                continue

            category = label["category"]
            index = category_dict[category]

            box = label["box2d"]
            top_left_x = box["x1"]
            top_left_y = box["y1"]
            bottom_right_x = box["x2"]
            bottom_right_y = box["y2"]

            width = bottom_right_x - top_left_x
            height = bottom_right_y - top_left_y
            center_x = (top_left_x + width / 2) / IMAGE_WIDTH
            center_y = (top_left_y + height / 2) / IMAGE_HEIGHT

            width /= IMAGE_WIDTH
            height /= IMAGE_HEIGHT

            index = str(index)
            center_x = str(center_x)
            center_y = str(center_y)
            width = str(width)
            height = str(height)
            f.write(" ".join([index, center_x, center_y, width, height]) + "\n")
        
        f.close()

    
if __name__ == "__main__":
    # parse_label_file(PATH_MINI)
    parse_label_file(PATH_VAL)
    parse_label_file(PATH_TRAIN)

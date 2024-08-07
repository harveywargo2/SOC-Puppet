import os
import yaml
from socpuppet.detectpy import detectpy_path


def yaml_file_list():
    yaml_df = []
    for root, path, files in os.walk(detectpy_path()):
        for file in files:
            if file.endswith('.yaml'):
                yaml_df.append(os.path.join(root, file))

    return yaml_df

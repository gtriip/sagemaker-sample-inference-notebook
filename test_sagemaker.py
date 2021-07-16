import json
import os
import base64

image_directory = '/Users/frostjack/Data/sagemaker_validation/validation_input/'
image_file_list = os.listdir(image_directory)

for image_file in image_file_list:
    with open(f'{image_directory}{image_file}', 'rb') as image_file_bytes:
        b64_encoded_image = base64.b64encode(image_file_bytes.read())
        json_file_dict = {'image': b64_encoded_image.decode('ascii')}
        with open(f'/Users/frostjack/Data/sagemaker_validation/validation_input_json/{image_file[:-4]}.json', 'w+', encoding='utf-8') as json_file:
            json.dump(json_file_dict, json_file, indent=4)

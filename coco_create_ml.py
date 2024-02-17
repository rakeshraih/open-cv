import json

input_annotations = json.load(open('./label-studio/annotations/result.json'))
output_annotations = []

images = input_annotations['images']
image_dict = {}
for image in images:
  image_dict[image['id']] = image['file_name']

for annotation in input_annotations['annotations']:
  coords_dict = {}
  coords_dict['x'] = annotation['bbox'][0] + annotation['bbox'][2]/2
  coords_dict['y'] = annotation['bbox'][1] + annotation['bbox'][3]/2
  coords_dict['width'] = annotation['bbox'][2]
  coords_dict['height'] = annotation['bbox'][3]
  cur_dict = {}
  cur_dict['annotation'] = [{'coordinates': coords_dict, 'label': annotation['category_id']}]
  cur_dict['imagefilename'] = image_dict[annotation['image_id']]
  output_annotations.append(cur_dict)

with open('annotations.createml.json', 'w') as f:
  json.dump(output_annotations, f)
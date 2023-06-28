from collections import namedtuple


IngredientsPickerConfig=namedtuple("IngredientsPickerConfig", [
    "root_dir",
    "no_of_classes",
    "trained_model_path",
    "save_image_dir_name",
    "save_image_file_name",
    "yolo_model_name"
])

UpsamplingConfig=namedtuple("UpsamplingConnfig",
[
    "root_dir",
    "model_path",
    "upsample_image_dir_name",
    "upsample_image_file_name",
    "test_image_dir_path"
]
)
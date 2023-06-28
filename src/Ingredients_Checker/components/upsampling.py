import os.path as osp
from pathlib import Path
import cv2
import os
import numpy as np
import torch
import RRDBNet_arch as arch
from Ingredients_Checker.config import Configuration


def upsample_image(model_path:Path,upsample_image_list:list[Path],save_image_path_list:list[Path]):
    model_path = model_path  # models/RRDB_ESRGAN_x4.pth OR models/RRDB_PSNR_x4.pth
    # device = torch.device('cuda')  # if you want to run on CPU, change 'cuda' -> cpu
    device = torch.device('cpu')


    model = arch.RRDBNet(3, 3, 64, 23, gc=32)
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    model = model.to(device)


    idx = 0
    for path,save_path in zip(upsample_image_list,save_image_path_list):
        idx += 1
        base = osp.splitext(osp.basename(path))[0]
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = img * 1.0 / 255
        img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
        img_LR = img.unsqueeze(0)
        img_LR = img_LR.to(device)

        with torch.no_grad():
            output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
        output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
        output = (output * 255.0).round()
        cv2.imwrite(save_path, output)
        print(f'file writed done {save_path}')

if __name__=="__main__":
    upsampling_config=Configuration().get_upsampling_config()
    upsample_image_file_name=[Path(upsampling_config.upsample_image_file_name)]
    test_image_dir_path=upsampling_config.test_image_dir_path
    test_images_path=[os.path.join(test_image_dir_path,img_name) for img_name in os.listdir(test_image_dir_path)]
    model_path=upsampling_config.model_path
    if len(upsample_image_file_name) != len(test_images_path):
        raise Exception(f"upsample image name list {len(upsample_image_file_name)} and test image list {len(test_images_path)} must be same")

    upsample_image(model_path=Path(model_path),upsample_image_list=test_images_path,save_image_path_list=upsample_image_file_name)
    
from super_gradients.training import models

if __name__=="__main__":
    # get_bounding_box("/config/workspace/src/1f783016-fc7c-11ed-b2b0-0242ac1c000c.jpg")
    best_model = models.get("yolo_nas_m",
                        num_classes=1,
                        checkpoint_path="/config/workspace/ckpt_best.pth")
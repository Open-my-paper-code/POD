import os
import os.path as osp
import sys
sys.path.insert(0, osp.join(osp.dirname(osp.abspath(__file__)), '../'))
from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='D2Det inference demo')
    parser.add_argument('config', help='test config file path')
    parser.add_argument('checkpoint', help='checkpoint file')
    parser.add_argument('img_file', help='img path')
    parser.add_argument('--out', help='output result path')
    args = parser.parse_args()
    return args
# ../configs/D2Det/D2Det_instance_r101_fpn_2x.py ./D2Det-instance-res101.pth ../demo/demo.jpg --out ../demo/bb.jpg

def main():
    args = parse_args()
    # build the model from a config file and a checkpoint file
    args.checkpoint = "/home/ubuntu/bigdisk/part1/D2Det/checkpoints/D2Det_detection_r50_fpn_2x_OPIXray/epoch_24.pth"
    args.config = "/home/ubuntu/bigdisk/part1/D2Det/configs/D2Det/D2Det_detection_r50_fpn_2x.py"
    args.img_file = "025857.jpg"

    model = init_detector(args.config, args.checkpoint, device='cuda:0')
    # test a single image
    result = inference_detector(model, args.img_file)
    # show the results
    show_result_pyplot(args.img_file, result, model.CLASSES, out_file=args.out)


if __name__ == '__main__':
    main()

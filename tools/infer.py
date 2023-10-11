# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser

from mmocr.apis.inferencers import MMOCRInferencer


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--inputs',default='/home/rujan/Documents/sangam/mmocr/MicrosoftTeams-image.png', type=str, help='Input image file or folder path.')
    parser.add_argument(
        '--out-dir',
        type=str,
        default='results/',
        help='Output directory of results.')
    parser.add_argument(
        '--det',
        type=str,
        default='/home/rujan/Documents/sangam/mmocr/configs/textdet/dbnetpp/dbnetpp_resnet50-oclip_fpnc_1200e_icdar2015.py',
        help='Pretrained text detection algorithm. It\'s the path to the '
        'config file or the model name defined in metafile.')
    parser.add_argument(
        '--det-weights',
        type=str,
        default='/home/rujan/Documents/sangam/mmocr/weights/DBNet/dbnetpp_resnet50-oclip_fpnc_1200e_icdar2015_20221101_124139-4ecb39ac.pth',
        help='Path to the custom checkpoint file of the selected det model. '
        'If it is not specified and "det" is a model name of metafile, the '
        'weights will be loaded from metafile.')
    parser.add_argument(
        '--rec',
        type=str,
        default='/home/rujan/Documents/sangam/mmocr/configs/textrecog/abinet/abinet_20e_st-an_mj.py',
        #default=None,
        help='Pretrained text recognition algorithm. It\'s the path to the '
        'config file or the model name defined in metafile.')
    parser.add_argument(
        '--rec-weights',
        type=str,
        default='/home/rujan/Documents/sangam/mmocr/weights/ABINet/abinet_20e_st-an_mj_20221005_012617-ead8c139.pth',
        # default=None,
        help='Path to the custom checkpoint file of the selected recog model. '
        'If it is not specified and "rec" is a model name of metafile, the '
        'weights will be loaded from metafile.')
    parser.add_argument(
        '--kie',
        type=str,
        # default='/home/rujan/Documents/sangam/mmocr/configs/kie/sdmgr/sdmgr_unet16_60e_wildreceipt.py',
        default=None,
        help='Pretrained key information extraction algorithm. It\'s the path'
        'to the config file or the model name defined in metafile.')
    parser.add_argument(
        '--kie-weights',
        type=str,
        # default='/home/rujan/Documents/sangam/mmocr/configs/kie/sdmgr/sdmgr_unet16_60e_wildreceipt.py',
        default=None,
        help='Path to the custom checkpoint file of the selected kie model. '
        'If it is not specified and "kie" is a model name of metafile, the '
        'weights will be loaded from metafile.')




    parser.add_argument(
        '--device',
        type=str,
        default=None,
        help='Device used for inference. '
        'If not specified, the available device will be automatically used.')
    parser.add_argument(
        '--batch-size', type=int, default=1, help='Inference batch size.')
    parser.add_argument(
        '--show',
        default=True,
        action='store_true',
        help='Display the image in a popup window.')
    parser.add_argument(
        '--print-result',
        default=True,
        action='store_true',
        help='Whether to print the results.')
    parser.add_argument(
        '--save_pred',
        default=True,
        action='store_true',
        help='Save the inference results to out_dir.')
    parser.add_argument(
        '--save_vis',
        default=True,
        action='store_true',
        help='Save the visualization results to out_dir.')

    call_args = vars(parser.parse_args())

    init_kws = [
        'det', 'det_weights', 'rec', 'rec_weights', 'kie', 'kie_weights',
        'device'
    ]
    init_args = {}
    for init_kw in init_kws:
        init_args[init_kw] = call_args.pop(init_kw)

    return init_args, call_args


def main():
    init_args, call_args = parse_args()
    ocr = MMOCRInferencer(**init_args)
    ocr(**call_args)


if __name__ == '__main__':
    main()
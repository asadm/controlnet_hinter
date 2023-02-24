import pytest
from diffusers.utils import load_image
from PIL import Image
from controlnet_hinter import *
import os


def test_functions_without_exception():
    result_folder = 'result/'
    os.makedirs(result_folder, exist_ok=True)

    original_image = load_image(
        "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png")

    hint_canny(original_image).save(result_folder + 'canny.png')
    hint_depth(original_image).save(result_folder + 'depth.png')
    hint_fake_scribble(original_image).save(
        result_folder + 'fake_scribble.png')
    hint_hed(original_image).save(result_folder + 'hed.png')
    hint_hough(original_image).save(result_folder + 'hough.png')
    hint_normal(original_image).save(result_folder + 'normal.png')
    hint_openpose(original_image).save(result_folder + 'openpose.png')
    hint_scribble(original_image).save(result_folder + 'scribble.png')
    hint_segmentation(original_image).save(result_folder + 'segmentation.png')

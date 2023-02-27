# controlnet_hinter: ControlNet control image preprocess library


## What is this?

[ControlNet](https://github.com/lllyasviel/ControlNet) by [@lllyasviel](https://huggingface.co/lllyasviel) is a neural network structure to control diffusion models by adding extra conditions. This library was created to assist [🤗Diffusers](https://github.com/huggingface/diffusers) when building ControlNet models with Diffusers. It is intended to be easy to use with  Diffusers’ `StableDiffusionControlNetPipeline` (under development). 

<img width="512" src="https://github.com/takuma104/controlnet_hinter/raw/main/docs/images/controlnet_hinter.png"/>

## To install

### Relatively stable version:
```sh
pip install controlnet_hinter
```

### Bleeding-edge version:
```
pip install git+https://github.com/takuma104/controlnet_hinter
```

## Usage Example

Canny Edge Detection
```py
import controlnet_hinter
from diffusers import StableDiffusionControlNetPipeline
from diffusers.utils import load_image

original_image = load_image("https://huggingface.co/datasets/diffusers/test-arrays/resolve/main/stable_diffusion_imgvar/input_image_vermeer.png")
control_image = controlnet_hinter.hint_canny(original_image) # this one line to add
image = pipe_canny(prompt="best quality, extremely detailed", 
                   negative_prompt="lowres, bad anatomy, worst quality, low quality",
                   image=control_image).images[0]
image.save('generated.png')
```



## API

Currently, supports the following:

|API|Description|Model(Checkpoint) to be applied|
|---|---|---|
|hint_canny()|canny edge detection|[takuma104/control_sd15_canny](https://huggingface.co/takuma104/control_sd15_canny)|
|hint_depth()|Midas depth estimation|[takuma104/control_sd15_depth](https://huggingface.co/takuma104/control_sd15_depth)|
|hint_hed()|HED edge detection (soft edge)|[takuma104/control_sd15_hed](https://huggingface.co/takuma104/control_sd15_hed)|
|hint_hough()|M-LSD straight line detection|[takuma104/control_sd15_mlsd](https://huggingface.co/takuma104/control_sd15_mlsd)|
|hint_normal()|Normal map estimation|[takuma104/control_sd15_normal](https://huggingface.co/takuma104/control_sd15_normal)|
|hint_openpose()|Human pose estimation using OpenPose|[takuma104/control_sd15_openpose](https://huggingface.co/takuma104/control_sd15_openpose)|
|hint_scribble()|Conversion from user scribble. White backgorund|[takuma104/control_sd15_scribble](https://huggingface.co/takuma104/control_sd15_scribble)|
|hint_fake_scribble()|Synthesize scribbles from input images|[takuma104/control_sd15_scribble](https://huggingface.co/takuma104/control_sd15_scribble)|
|hint_segmentation()|Semantic segmentation estimation|[takuma104/control_sd15_seg](https://huggingface.co/takuma104/control_sd15_seg)|





# 



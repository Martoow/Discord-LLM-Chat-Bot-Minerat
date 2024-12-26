import torch
from diffusers import FluxPipeline
import random
import string


def initiateImageGen():
    llmObj = fetchLLMConfig()
    model="black-forest-labs/FLUX.1-schnell"
    pipeline = FluxPipeline.from_pretrained(model, torch_dtype=torch.bfloat16)
    pipeline.to("cuda")
    return pipeline


def generateString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


def generateImage(prompt):
    ckpt_id = "black-forest-labs/FLUX.1-schnell"
    # prompt = []
    height, width = 1024, 1024

    # denoising
    pipe = FluxPipeline.from_pretrained(
        ckpt_id,
        torch_dtype=torch.bfloat16,
    )
    pipe.vae.enable_tiling()
    pipe.vae.enable_slicing()
    pipe.enable_sequential_cpu_offload() # offloads modules to CPU on a submodule level (rather than model level)

    image = pipe(
        prompt,
        num_inference_steps=5,
        guidance_scale=0.0,
        height=height,
        width=width,
    ).images[0]
    print('Max mem allocated (GB) while denoising:', torch.cuda.max_memory_allocated() / (1024 ** 3))
    imageName = generateString()
    imageName = "./images/" + imageName + ".png"
    image.save(imageName)
    return imageName

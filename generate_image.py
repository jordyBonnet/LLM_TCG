
import torch
from diffusers import FluxPipeline
from huggingface_hub import login

class ImageGenerator:
    def __init__(self):
        # self.token = ""
        self.model_name = "black-forest-labs/FLUX.1-dev"
        # self.model_name = "black-forest-labs/FLUX.1-schnell"
        self.torch_dtype = torch.bfloat16
        self.pipe = None
        self.login()
        self.load_model()

    def login(self):
        login(token=self.token)

    def load_model(self):
        self.pipe = FluxPipeline.from_pretrained(self.model_name, torch_dtype=self.torch_dtype)
        self.pipe.enable_model_cpu_offload()

    # 816 x 1110 pixels is what your source images should be when printing 63x88mm cards.
    def generate_image(self, prompt, height=352, width=256, guidance_scale=2.5, num_inference_steps=25, max_sequence_length=512):
        generator = torch.Generator("cpu").manual_seed(0)
        image = self.pipe(
            prompt,
            height=height,
            width=width,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            max_sequence_length=max_sequence_length,
            generator=generator
        ).images[0]
        return image

    def save_image(self, image, filename):
        image.save(filename)
"""
# Usage
prompt = "A half-elf warrior with green skin, dressed in a leafy cloak and holding a staff made from twisted vines. The background should feature a serene forest with towering trees, sunlight filtering through the leaves. The Guardian's eyes should glow softly like embers. Art fantastic"

generator = ImageGenerator()
image = generator.generate_image(prompt)
generator.save_image(image, "out_images/02.png")
"""
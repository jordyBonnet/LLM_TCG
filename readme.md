# LLM_TCG
Trading Card Game (TCG) entirely built with local generative AI using<br>
Large Langage Model (LLM) + AI image generation tool

see the results on this reddit post:
https://www.reddit.com/r/TCG/comments/1f960wt/how_to_create_a_fully_ai_generated_tcg/

## ollama / mixtral - Local LLM
- Install [ollama](https://ollama.com/)
- run ```ollama run mixtral``` in command to automatically download it

## FLUX.1 [dev] - Local Image Generator
- [quick video](https://www.youtube.com/watch?v=QYVucud3ptc&list=PLR39E8JPWRwIQWpkd52W0kuI9gs6QeTUf&index=8) from Fireship youtube channel<br>
- [Hugging face link](https://huggingface.co/black-forest-labs/FLUX.1-dev)

## file / folders
- LLM_TCG.ipynb - is the main file and contains the different steps to create the TCG
- out_images folder - contains all images
- generate_image.py - Flux.1 [dev] piece of code to generate images with some prompt
- card_layers.py - add simple layered informations (HP, mana...) to a raw card
- generate_image_quick.py - test on a quicker version of generate_image.py (NOT WORKING) 

## Pip installs
- ```pip install -U diffusers```<br>
- ```pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu124``` see [pytorch Start Locally](https://pytorch.org/get-started/locally/)
- ```pip install transformers```
- ```pip install sentencepiece```
- ```pip install protobuf```
- ```pip install accelerate```


<div align="center">

# A Gradient Guidance Perspective on Stepwise Preference Optimization for Diffusion Models

<a href="https://openreview.net/forum?id=d6lIOnvOX2">
  <img src="https://img.shields.io/badge/Paper-OpenReview-green?style=for-the-badge" height="22.5">
</a>

</div>


This repository contains the official implementation of **GradSPO**, an enhanced aesthetic post-training framework for diffusion models. Built upon the [SPO framework](https://github.com/RockeyCoss/spo), GradSPO utilizes noise reduction techniques to amplify reward signals, facilitating superior preference alignment and more robust aesthetic refinement.

## Environment Setup

To set up the environment, we recommend using Conda.

1. **Create and activate a new environment:**
   ```bash
   conda env create -f environment.yaml --name gradspo
   conda activate gradspo
    ```


## Usage

GradSPO introduces several hyperparameters to control the optimization dynamics during training.

### Key Hyperparameters
- **`config.train.ema_decay`** (default: `0.9`)  
  Controls the Exponential Moving Average (EMA) decay for the sampling model.
- **`config.train.grad_scale`** (default: `0.5`)  
  Scales gradients of the reward signals.


## Training

### Stable Diffusion v1.5
To fine-tune **Stable Diffusion v1.5** with the default GradSPO parameters, run:
```bash
bash launch_sd15.sh
```

### SDXL

To fine-tune **SDXL** with the default GradSPO parameters, run:

```bash
bash launch_sdxl.sh
```


## Available Checkpoints
---

We provide pretrained **LoRA checkpoints** for both **Stable Diffusion v1.5** and **SDXL**, trained with **GradSPO**.

| Model | Base Model | HuggingFace Repository | Description |
|------|-----------|------------------------|-------------|
| SD v1.5 | Stable Diffusion v1.5 | [`JTTJ/GradSPO`](https://huggingface.co/JTTJ/GradSPO) | LoRA trained with `grad_scale=0.5`, `ema_decay=0.9` |
| SDXL | SDXL | [`JTTJ/GradSPO`](https://huggingface.co/JTTJ/GradSPO) | LoRA trained with `grad_scale=0.5`, `ema_decay=0.9` |


## Acknowledgements

Our codebase builds upon and references implementations from [Diffusers](https://github.com/huggingface/diffusers), [D3PO](https://github.com/yk7333/d3po), and [PickScore](https://github.com/yuvalkirstain/PickScore). We sincerely thank the authors for open-sourcing their work.

This project is heavily based on the [SPO framework](https://github.com/RockeyCoss/SPO/tree/main). If you find this code or our gradient guidance perspective useful in your research, please consider citing our work:


## Citation

```bibtex
@inproceedings{
tee2025a,
title={A Gradient Guidance Perspective on Stepwise Preference Optimization for Diffusion Models},
author={Joshua Tian Jin Tee and Hee Suk Yoon and Abu Hanif Muhammad Syarubany and Eunseop Yoon and Chang D. Yoo},
booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems},
year={2025},
url={https://openreview.net/forum?id=d6lIOnvOX2}
}
from typing import Optional, Tuple, Union

import math
import torch

from diffusers.utils.torch_utils import randn_tensor
from diffusers.schedulers.scheduling_ddim import DDIMSchedulerOutput, DDIMScheduler
import copy

def score_matching_loss(
    self: DDIMScheduler,
    model_output: torch.FloatTensor,
    timestep: int,
    generator=None,
    noise_added=None,
    ema_noise=None,
    grad_scale=1.0,
):
    assert isinstance(self, DDIMScheduler)
    if self.num_inference_steps is None:
        raise ValueError(
            "Number of inference steps is 'None', you need to run 'set_timesteps' after creating the scheduler"
        )

    alpha_prod_t = self.alphas_cumprod.gather(0, timestep).view(-1,1,1,1)
    grad = noise_added
    eps_target = ema_noise - grad_scale*(1-alpha_prod_t)**0.5*grad
    loss = -((model_output-eps_target.detach())**2).mean(dim=(1,2,3))
    return loss
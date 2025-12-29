accelerate launch --main_process_port 22343 \
  --config_file accelerate_cfg/config.yaml train_scripts/train_gradspo_sdxl.py \
  --config configs/gradspo_sdxl.py

# python train_scripts/train_gradspo_sdxl.py \
#   --config configs/gradspo_sdxl.py
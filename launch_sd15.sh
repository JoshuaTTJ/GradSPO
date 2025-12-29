accelerate launch --main_process_port 34325 \
  --config_file accelerate_cfg/config.yaml \
  train_scripts/train_gradspo.py \
  --config configs/gradspo_sd1_5.py

# python train_scripts/train_gradspo.py \
#     --config configs/gradspo_sd1_5.py
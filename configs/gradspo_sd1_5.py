from configs.basic_config import basic_config

def get_config():
    return exp_config()

def exp_config():
    config = basic_config()
    
    ###### Training ######
    config.sample.num_sample_each_step = 4
    
    #### logging ####
    config.run_name = "gradspo_sd1_5"
    # config.run_name = "debug"
    
    return config

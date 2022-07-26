from environs import Env

env = Env()
env.read_env()

SEC_KEY = env.str("SECRET_KEY")
import os
from dotenv import load_dotenv


def load_dot_env():
    """ Init .env file"""
    project_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
    env_file = os.path.join(project_folder, '.env')
    if not os.path.isfile(env_file):
        raise FileNotFoundError('Environment configuration file (.env) not found. Please create one and rerun the app')
    load_dotenv(env_file)

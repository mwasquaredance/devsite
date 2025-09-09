# main.py
import yaml, pathlib

def define_env(env):
    data_path = pathlib.Path(env.project_dir) / 'docs' / 'data' / 'directory.yml'
    with open(data_path, 'r', encoding='utf-8') as f:
        env.variables['clubs'] = yaml.safe_load(f) or []

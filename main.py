# main.py
import yaml, pathlib

def define_env(env):
    data_path = pathlib.Path(env.project_dir) / "docs" / "data" / "directory.yml"
    with open(data_path, "r", encoding="utf-8") as f:
        entries = yaml.safe_load(f) or []

    # isolate council and clubs
    council = next((e for e in entries if e.get("id") == "council"), {})
    clubs = sorted(
        (e for e in entries if e.get("id") != "council"),
        key=lambda e: e.get("name", "").lower(),
    )

    # expose in macro environment
    env.variables["council"] = council
    env.variables["clubs"] = clubs
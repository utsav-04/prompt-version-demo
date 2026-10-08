import yaml
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def load_config():
    config_path = BASE_DIR / "config" / "prompt-config.yaml"

    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def load_prompt(prompt_name, version):
    prompt_path = (
        BASE_DIR
        / "prompts"
        / prompt_name
        / f"v{version}.yaml"
    )

    with open(prompt_path, "r") as file:
        return yaml.safe_load(file)


def get_active_prompt():
    config = load_config()

    version = config["customer_support"]["active_version"]

    prompt = load_prompt(
        "customer_support",
        version
    )

    return prompt


if __name__ == "__main__":

    prompt = get_active_prompt()

    print("================================")
    print("Customer Support Prompt")
    print("================================")
    print(f"Active Version: {prompt['version']}")
    print()
    print("Prompt:")
    print(prompt["prompt"])
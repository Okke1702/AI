import json
import os


MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "memory.json"
)


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception:
        return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            memory,
            file,
            ensure_ascii=False,
            indent=4
        )


def remember(key, value):
    memory = load_memory()

    memory[key] = value

    save_memory(memory)

    return f"Đã ghi nhớ: {key} = {value}"


def forget(key):
    memory = load_memory()

    if key not in memory:
        return f"Không tìm thấy thông tin: {key}"

    del memory[key]

    save_memory(memory)

    return f"Đã quên: {key}"


def get_memory():
    return load_memory()
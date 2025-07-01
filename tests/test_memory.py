# from local kv store (not redis)

from tools.memory.memory_tool import save_memory, load_memory

def test_memory_save_and_load():
    save_memory("test_key", "test_value")
    memory = load_memory()
    assert memory.get("test_key") == "test_value"
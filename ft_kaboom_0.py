from alchemy import grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result = grimoire.light_spell_record("Lumos", "FIRE")
    print("Testing record light spell:", result)

import random, json

file_name = "npc_data.json"
def load_data():
    with open(file_name, encoding="utf-8") as f:
        return json.load(f)
def generate_npc(data):
    name_dict = random.choice(data["names"])
    return {
    "name": name_dict["name"],
    "meaning": name_dict["meaning"],
    "trait": random.choice(data["physical_traits"]),
    "role": random.choice(data["roles"]),
    "personality": random.choice(data["personality_traits"]),
    "motivation": random.choice(data["motivations"]),
    "secret": random.choice(data["secrets"])
    }
def show_npc(data):
    for i in range(1, 4):
        npc = generate_npc(data)
        print(f"НПС {i}:")
        print(f"🪪      {npc["name"]}, что значит '{npc["meaning"]}'")
        print(f"👁️      Физическая черта - {npc['trait']}.")
        print(f"🎭     Роль - {npc['role']}")
        print(f"😊     Характер - {npc['personality']}")
        print(f"🎯     Мотивация - {npc['motivation']}")
        print(f"🗝️      Тайна - {npc['secret']}\n")


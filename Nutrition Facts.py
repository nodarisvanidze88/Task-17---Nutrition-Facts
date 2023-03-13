items = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "lemon": 15
}

def main():
    item = input("Item: ").lower().strip()
    print("Calories:",items[item])
main()

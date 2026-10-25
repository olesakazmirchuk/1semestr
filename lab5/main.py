
from config import MAX_DAYS, RECEPI, WIN_ZOLOTO
from game_logic import AlchemyGame


def show_inventory(game):
    print(f"\nIngredients ({game.inv_ing.get_info()} slots):")

    if game.inv_ing.slots:
        for name, quantity in game.inv_ing.slots.items():
            print(f"{name}: {quantity}")
    else:
        print("No ingredients.")

    print(f"\nPotions ({game.inv_pot.get_info()} slots):")

    if game.inv_pot.slots:
        for name, quantity in game.inv_pot.slots.items():
            print(f"{name}: {quantity}")
    else:
        print("No potions.")


def show_recipes():
    print("\n--- Potion recipes ---")

    for potion_name, ingredients in RECEPI.items():
        print(
            f"{potion_name}: "
            f"{ingredients[0]} + {ingredients[1]}"
        )


def craft_potion(game):
    try:
        number = input("Enter potion number (1-50): ").strip()

        if not number.isdigit():
            raise ValueError("Enter a number.")

        number = int(number)

        if number < 1 or number > 50:
            raise ValueError("Number must be from 1 to 50.")

        game.craft(f"Potion_{number}")

    except ValueError as error:
        print(f"Input error: {error}")

    else:
        print("Command processed.")

    finally:
        print("---")


def main():
    print("=== RPG ALCHEMIST ===")
    print(f"Goal: earn {WIN_ZOLOTO} gold in {MAX_DAYS} days.")

    try:
        game = AlchemyGame()

        while True:
            status = game.check_status()

            if status == "WIN":
                print("\nVICTORY! You saved your laboratory!")
                print(f"Your gold: {game.zoloto}")
                break

            if status == "LOSE":
                print("\nDEFEAT! You lost your laboratory.")
                print(f"Your gold: {game.zoloto}/{WIN_ZOLOTO}")
                break

            print(f"\nDay: {game.den}/{MAX_DAYS}")
            print(f"Gold: {game.zoloto}/{WIN_ZOLOTO}")
            print("\n1. Inventory")
            print("2. Recipes")
            print("3. Craft potion")
            print("4. Sell potions and end day")
            print("5. Exit")

            choice = input("Choose action: ").strip()

            try:
                if choice == "1":
                    show_inventory(game)

                elif choice == "2":
                    show_recipes()

                elif choice == "3":
                    craft_potion(game)

                elif choice == "4":
                    game.sell_potions()

                elif choice == "5":
                    print("You left the game.")
                    break

                else:
                    print("Invalid command.")

            except (ValueError, KeyError, IndexError) as error:
                print(f"Action error: {error}")

            else:
                print("Action completed.")

            finally:
                print("---")

    except (ValueError, KeyError, IndexError) as error:
        print(f"Game error: {error}")

    finally:
        print("Game finished.")


if __name__ == "__main__":
    main()

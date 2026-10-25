
import random

from config import (
    INGREDIENTS_POOL,
    POTIONS_POOL,
    RECEPI,
    WIN_ZOLOTO,
    MAX_DAYS,
    DAILY_ING,
)
from inventory import LimitedInventory


class AlchemyGame:
    def __init__(self):
        self.den = 1
        self.zoloto = 0
        self.inv_ing = LimitedInventory(25, 25)
        self.inv_pot = LimitedInventory(10, 10)
        self.start_day()

    def start_day(self):
        try:
            print(f"\n--- Day {self.den} ---")

            ingredients_list = list(INGREDIENTS_POOL.keys())

            for _ in range(DAILY_ING):
                ingredient = random.choice(ingredients_list)

                try:
                    self.inv_ing.add_item(ingredient)
                except IndexError:
                    print(f"Inventory full! Lost: {ingredient}")
                else:
                    print(f"Received: {ingredient}")

        except (ValueError, IndexError) as error:
            print(f"Day error: {error}")

        finally:
            print("Day preparation finished.")

    def craft(self, potion_name):
        try:
            if potion_name not in RECEPI:
                raise ValueError("Potion not found.")

            ingredients = RECEPI[potion_name]

            for ingredient in ingredients:
                if self.inv_ing.slots.get(ingredient, 0) < 1:
                    raise ValueError("Not enough ingredients.")

            self.inv_pot.add_item(potion_name)

            for ingredient in ingredients:
                self.inv_ing.remove_item(ingredient)

        except ValueError as error:
            print(f"Crafting error: {error}")

        except IndexError:
            print("Potion inventory is full!")

        except KeyError as error:
            print(f"Ingredient error: {error}")

        else:
            print(f"Potion crafted: {potion_name}")

        finally:
            print("Crafting attempt finished.")

    def sell_potions(self):
        try:
            print("\n--- Evening sale ---")

            if not self.inv_pot.slots:
                print("No potions to sell.")
            else:
                total_earned = 0

                for potion_name in list(self.inv_pot.slots.keys()):
                    quantity = self.inv_pot.slots[potion_name]
                    price = POTIONS_POOL[potion_name]
                    total_price = quantity * price

                    total_earned += total_price

                    self.inv_pot.remove_item(potion_name, quantity)

                    print(
                        f"Sold {potion_name} x{quantity} "
                        f"for {total_price} gold."
                    )

                self.zoloto += total_earned

                print(f"Earned today: {total_earned} gold.")
                print(f"Total gold: {self.zoloto}.")

        except (KeyError, ValueError) as error:
            print(f"Sale error: {error}")

        else:
            print("Sale completed.")

        finally:
            print("Evening sale finished.")

        if self.zoloto < WIN_ZOLOTO:
            if self.den >= MAX_DAYS:
                self.den = MAX_DAYS + 1
            else:
                self.den += 1
                self.start_day()

    def check_status(self):
        if self.zoloto >= WIN_ZOLOTO:
            return "WIN"

        if self.den > MAX_DAYS:
            return "LOSE"

        return "PLAY"


class LimitedInventory:
    def __init__(self, max_slots, max_stack):
        self.max_slots = max_slots
        self.max_stack = max_stack
        self.slots = {}

    def add_item(self, name, count=1):
        try:
            if count <= 0:
                raise ValueError("Count must be positive.")

            current = self.slots.get(name, 0)

            used_slots = sum(
                (quantity + self.max_stack - 1) // self.max_stack
                for quantity in self.slots.values()
            )

            free_slots = self.max_slots - used_slots
            free_in_existing_stack = 0

            if current > 0:
                free_in_existing_stack = (
                    self.max_stack - current % self.max_stack
                ) % self.max_stack

            available = (
                free_in_existing_stack + free_slots * self.max_stack
            )

            if count > available:
                raise IndexError("Inventory is full!")

            self.slots[name] = current + count

        except (ValueError, IndexError):
            raise

        else:
            return True

    def remove_item(self, name, count=1):
        try:
            if count <= 0:
                raise ValueError("Count must be positive.")

            if name not in self.slots:
                raise KeyError("Item not found.")

            if self.slots[name] < count:
                raise KeyError("Not enough items.")

            self.slots[name] -= count

            if self.slots[name] == 0:
                del self.slots[name]

        except (ValueError, KeyError):
            raise

        else:
            return True

    def get_info(self):
        used_slots = sum(
            (quantity + self.max_stack - 1) // self.max_stack
            for quantity in self.slots.values()
        )

        return f"{used_slots}/{self.max_slots}"

"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    items_set = set(items)
    for item in items_set:
        return {item: items.count(item) for item in items}


def desmembrar_inventorio(inventory):
    '''Turns an inventory dict into a list
    '''
    til = list(inventory.items())  # til = total inventory list

    final_inventory_list = []

    for pair in til:
        num_of_items_zeroplus = 0
        while (pair[1]) > num_of_items_zeroplus:
            final_inventory_list.append(pair[0])
            num_of_items_zeroplus += 1
    return final_inventory_list


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    # turning inventory dict into a list:

    dict_into_list = desmembrar_inventorio(inventory)

    # adding the correct list to items list:

    final_list = dict_into_list + items

    # the result is:

    return create_inventory(final_list)


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    # items_to_dict = create_inventory(items)

    for main_metal in inventory:
        for remove_metal in items:
            if remove_metal == main_metal:
                inventory[main_metal] -= 1
                if inventory[main_metal] < 0:
                    inventory[main_metal] = 0
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    final_dict = {metal: quant for metal,
                  quant in inventory.items() if metal != item}
    return final_dict


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    lets_try = [(pair, inventory[pair])
                for pair in inventory if inventory[pair] > 0]

    return lets_try

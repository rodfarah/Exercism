"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    # My solution:
    # for item in items_to_add:
    #     if item not in current_cart.keys():
    #         current_cart.update([(item, 1)])
    #     else:
    #         for product in current_cart.keys():
    #             if product == item:
    #                 current_cart[product] += 1
    # return current_cart
    
    # Better solution:
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0)+1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    # My first solution:
    # order_dict = {}
    # only_one = set(notes)
    # for item in only_one:
    #     order_dict[item] = 0
    # for product in notes:
    #     order_dict[product] += 1
    # return order_dict

    # Better solution:
    # shopping_cart = {}
    # for item in notes:
    #     shopping_cart[item] = shopping_cart.setdefault(item, 0)+1
    # return shopping_cart


    # Even better solution (Each item should be added with a quantity of 1.):
    cart=dict.fromkeys(notes, 1)
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas
    section.
    :return: dict - updated "recipe ideas" dict.
    """

    # My first solution:
    # for item in recipe_updates:
    #     if item[0] in ideas.keys():
    #         ideas[item[0]] = item[1]
    #     else:
    #         ideas.update([(item[0], item[1])])
    # return ideas

    # Better Solution:
    ideas |= recipe_updates
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    # My first solution:
    # sorted_cart = {}
    # for item in sorted(cart.keys()):
    #     sorted_cart.update([(item, cart[item])])

    # return sorted_cart

    # Better solution:
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    bought_items = sorted(cart.keys(), reverse=True)
    fulfillment_dictionary = {}
    for item in bought_items:
        fulfillment_dictionary.update(
            [(item, [cart[item], aisle_mapping[item][0], aisle_mapping[item][1]])])

    return fulfillment_dictionary


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for product, info in fulfillment_cart.items():
        for item, details in store_inventory.items():
            if item == product:
                details[0] -= info[0]
                if details[0] <= 0:
                    details[0] = "Out of Stock"
    return store_inventory

# Inventory allocator function:
#   INPUTS: order - a map of items being ordered and their quantities
#           warehouses - a list of objects with warehouse name and
#                          inventory distributions
#
#   OUTPUT: a list of objects with warehouse name and inventory
#           distributions where the list constitutes the cheapest shipment
#
#   ASSUMPTIONS:

def inventoryAllocator(order, warehouses):
    # Initializing the result (cheapest shipment)
    result = []

    # Iterate through each warehouse
    for warehouse in warehouses:

        # If the order is empty, we return the result (order could be empty
        # to begin with, or it could be filled and we don't want to continue)
        if not order:
            return result

        # Temporary storage to contain all the items from one warehouse
        # that will supply an order
        supply = {}

        # Iterate through each item in the order
        for item, orderAmt in order.items():

            # If the item is in the warehouse, we want to fill as much of the
            # order as possible (since the first warehouses are cheaper)
            if orderAmt > 0 and item in warehouse['inventory']:

                # Filling the order (assuming warehouse inventory > 0)
                itemSupply = min(order[item], warehouse['inventory'][item])
                if (itemSupply):
                    supply[item] = itemSupply

                # Adjusting quantities as necessary
                warehouse['inventory'][item] -= itemSupply
                order[item] -= itemSupply

        # We pop item if order is filled (that way we don't need to constantly
        # check in future warehouse iterations). 
        tempOrder = {}
        for item, orderAmt in order.items():
            if orderAmt:
                tempOrder[item] = orderAmt
        order = tempOrder

        # NOTE: This improves the efficiency when orders are fulfilled very 
        #       early on (i.e for cheaper shipments) but negatively affects 
        #       the efficiency when orders aren't fulfilled immediately.
            

        # Adding the supply to our result, assuming it's not empty
        if len(supply) > 0:
            result.append({warehouse['name']: supply})

    # Return result or empty if order isn't completely filled
    return [] if order else result
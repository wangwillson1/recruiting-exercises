import unittest
from inventoryAllocator import inventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
    # Provided tests
    def test_provided_one_warehouse(self):
        order = { 'apple': 1 }
        warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
        expected = [{ 'owd': { 'apple': 1 } }]
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

        # We can also test to make sure the remaining inventory in
        # the warehouses is correct, but since this is not required,
        # we will skip these tests (a sample is below)
        expected_remaining = [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
        self.assertEqual(warehouses, expected_remaining)

    def test_provided_multiple_warehouses(self):
        order = { 'apple': 10 }
        warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        expected = [{ 'owd': { 'apple': 5 } }, { 'dm': { 'apple': 5 }}]
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    def test_provided_not_enough_inv(self):
        order = { 'apple': 1 }
        warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
        expected = []
        self.assertEqual(expected, inventoryAllocator(order, warehouses))


    # Everything empty
    def test_everything_empty(self):
        order = {}
        warehouses = []
        expected = []
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Empty order
    def test_empty_order(self):
        order = {}
        warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
        expected = []
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Empty warehouses
    def test_empty_warehouses(self):
        order = { 'apple': 1, 'banana': 3 }
        warehouses = []
        expected = []
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Order with 0 of everything
    def test_order_nothing(self):
        order = { 'apple': 0, 'banana': 0, 'cherries': 0 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'apple': 1, 'banana': 2, 'lemon': 1 }},
                        { 'name': 'wh2', 
                        'inventory': { 'apple': 2, 'cherries': 5, 'lemon': 1 }}]
        expected = []
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Warehouses with no inventory
    def test_no_inventory(self):
        order = { 'apple': 1, 'banana': 12, 'cherries': 42 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'apple': 0, 'banana': 0, 'lemon': 0 }},
                        { 'name': 'wh2', 
                        'inventory': { 'apple': 0, 'cherries': 0, 'lemon': 0 }}]
        expected = []
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Order with 0 of everything and empty warehouses
    def test_order_nothing_no_inv(self):
        order = { 'apple': 0, 'banana': 0, 'cherries': 0 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'apple': 0, 'banana': 0, 'lemon': 0 }},
                        { 'name': 'wh2', 
                        'inventory': { 'apple': 0, 'cherries': 0, 'lemon': 0 }}]
        expected = []
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Exact match from single warehouse
    def test_exact_match_single(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': {'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1}}]
        expected = [{ 'wh1': {'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1}}]
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Exact match from multiple warehouses
    def test_exact_match_multiple(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'item2': 2 }},
                        { 'name': 'wh2', 
                        'inventory': { 'item1': 1, 'item4': 3, 'item5': 1 }},
                        { 'name': 'wh3', 
                        'inventory': { 'item1': 1, 'item3': 6 }},
                        { 'name': 'wh4', 
                        'inventory': { 'item2': 5, 'item3': 3}},
                        { 'name': 'wh5', 
                        'inventory': { 'item2': 3, 'item3': 3, 'item4': 1 }}]
        expected = [{'wh1': {'item2': 2 }},
                    {'wh2': {'item1': 1, 'item4': 3, 'item5': 1}},
                    {'wh3': {'item1': 1, 'item3': 6}},
                    {'wh4': {'item2': 5, 'item3': 3}},
                    {'wh5': {'item2': 3, 'item3': 3, 'item4': 1}}]

        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Fill from multiple warehouses
    def test_fill_multiple(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'item2': 2, 'item6': 10 }},
                        { 'name': 'wh2', 
                        'inventory': { 'item1': 1, 'item4': 3, 'item5': 1 }},
                        { 'name': 'wh3', 
                        'inventory': { 'item1': 1, 'item3': 6, 'item8': 6 }},
                        { 'name': 'wh4', 
                        'inventory': { 'item2': 5, 'item3': 3}},
                        { 'name': 'wh5', 
                        'inventory': { 'item2': 3, 'item3': 3, 'item4': 1 }},
                        { 'name': 'wh6', 
                        'inventory': { 'item1': 2, 'item2': 10, 'item3': 5 }}]
        expected = [{'wh1': {'item2': 2 }},
                    {'wh2': {'item1': 1, 'item4': 3, 'item5': 1}},
                    {'wh3': {'item1': 1, 'item3': 6}},
                    {'wh4': {'item2': 5, 'item3': 3}},
                    {'wh5': {'item2': 3, 'item3': 3, 'item4': 1}}]

        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Extra warehouses (order fulfilled earlier)
    def test_extra_warehouses(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'item2': 10, 'item3': 10 }},
                        { 'name': 'wh2', 
                        'inventory': { 'item1': 2, 'item4': 4, 'item5': 1 }},
                        { 'name': 'wh3', 
                        'inventory': { 'item1': 1, 'item3': 2, 'item8': 6 }},
                        { 'name': 'wh4', 
                        'inventory': { 'item2': 5, 'item3': 3}},
                        { 'name': 'wh5', 
                        'inventory': { 'item2': 3, 'item3': 3, 'item4': 1 }},
                        { 'name': 'wh6', 
                        'inventory': { 'item1': 2, 'item2': 10, 'item3': 5 }}]
        expected = [{'wh1': {'item2': 10, 'item3': 10 }},
                    {'wh2': {'item1': 2, 'item4': 4, 'item5': 1}},
                    {'wh3': {'item3': 2}}]

    # Two warehouses with the exact same inventory
    def test_same_inventory(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12}
        warehouses = [{ 'name': 'wh1', 'inventory': {'item1': 2, 'item2': 10, 'item3': 12}},
                      { 'name': 'wh2', 'inventory': {'item1': 2, 'item2': 10, 'item3': 12}}]
        expected = [{ 'wh1': {'item1': 2, 'item2': 10, 'item3': 12}}]
        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Order unfulfilled (inventory quantity off by 1)
    def test_unfulfilled_off_by_one(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'item2': 2, 'item6': 10 }},
                        { 'name': 'wh2', 
                        'inventory': { 'item1': 1, 'item4': 3, 'item5': 1 }},
                        { 'name': 'wh3', 
                        'inventory': { 'item1': 1, 'item3': 6, 'item8': 6 }},
                        { 'name': 'wh4', 
                        'inventory': { 'item2': 5, 'item3': 3 }},
                        { 'name': 'wh5', 
                        'inventory': { 'item2': 3, 'item3': 3 }},
                        { 'name': 'wh6', 
                        'inventory': { 'item10': 2, 'item12': 10, 'item7': 5 }}]
        expected = []

        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Order unfulfilled (warehouse missing 1 item)
    def test_unfulfilled_missing_item(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'item2': 2, 'item6': 10 }},
                        { 'name': 'wh2', 
                        'inventory': { 'item1': 1, 'item4': 3, 'item6': 1 }},
                        { 'name': 'wh3', 
                        'inventory': { 'item1': 1, 'item3': 6, 'item8': 6 }},
                        { 'name': 'wh4', 
                        'inventory': { 'item2': 5, 'item3': 3 }},
                        { 'name': 'wh5', 
                        'inventory': { 'item2': 3, 'item3': 3 }},
                        { 'name': 'wh6', 
                        'inventory': { 'item10': 2, 'item12': 10, 'item7': 5 }}]
        expected = []

        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Order unfulfilled (none of the warehouses have the items)
    def test_unfulfilled_missing_all(self):
        order = { 'item50': 2, 'item51': 10, 'item52': 12, 'item53': 4, 'item54': 1 }
        warehouses = [{ 'name': 'wh1', 
                        'inventory': { 'item2': 2, 'item6': 10 }},
                        { 'name': 'wh2', 
                        'inventory': { 'item1': 1, 'item4': 3, 'item5': 1 }},
                        { 'name': 'wh3', 
                        'inventory': { 'item1': 1, 'item3': 6, 'item8': 6 }},
                        { 'name': 'wh4', 
                        'inventory': { 'item2': 5, 'item3': 3 }},
                        { 'name': 'wh5', 
                        'inventory': { 'item2': 3, 'item3': 3 }},
                        { 'name': 'wh6', 
                        'inventory': { 'item10': 2, 'item12': 10, 'item7': 5 }}]
        expected = []

        self.assertEqual(expected, inventoryAllocator(order, warehouses))

    # Big test
    def test_big(self):
        order = { 'item1': 2, 'item2': 10, 'item3': 12, 'item4': 4, 'item5': 1,
                  'item6': 4, 'item7': 6, 'item8': 17, 'item9': 24, 'item10': 5 }

        warehouses = [  { 'name': 'wh1', 
                        'inventory': { 'item1': 2, 'item2': 5, 'item10': 4, 'item12': 20}},
                        { 'name': 'wh2', 
                        'inventory': { 'item1': 1, 'item4': 3, 'item5': 1 }},
                        { 'name': 'wh3', 
                        'inventory': { 'item1': 1, 'item5': 6}},
                        { 'name': 'wh4', 
                        'inventory': { 'item2': 8, 'item3': 18}},
                        { 'name': 'wh5', 
                        'inventory': { 'item2': 3, 'item3': 3, 'item4': 1 }},
                        { 'name': 'wh6', 
                        'inventory': { 'item8': 2, 'item9': 10, 'item10': 1 }},
                        { 'name': 'wh7', 
                        'inventory': { 'item6': 3, 'item8': 5, 'item9': 7 }},
                        { 'name': 'wh8', 
                        'inventory': { 'item5': 3, 'item7': 3, 'item10': 1 }},
                        { 'name': 'wh9', 
                        'inventory': { 'item25': 3, 'item3': 3, 'item4': 1 }},
                        { 'name': 'wh10', 
                        'inventory': { 'item6': 1, 'item7': 3, 'item8': 15, 'item9': 42 }},
                        { 'name': 'wh10', 
                        'inventory': { 'item22': 1, 'item46': 3, 'item10': 3}}]

        expected = [{'wh1': {'item1': 2, 'item2': 5, 'item10': 4}},
                    {'wh2': {'item4': 3, 'item5': 1}},
                    {'wh4': {'item2': 5, 'item3': 12}},
                    {'wh5': {'item4': 1}},
                    {'wh6': {'item8': 2, 'item9': 10, 'item10': 1}},
                    {'wh7': {'item6': 3, 'item8': 5, 'item9': 7}},
                    {'wh8': {'item7': 3}},
                    {'wh10': {'item6': 1, 'item7': 3, 'item8': 10, 'item9': 7}}]

        self.assertEqual(expected, inventoryAllocator(order, warehouses))

if __name__ == '__main__':
    unittest.main()
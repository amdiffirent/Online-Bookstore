import unittest
#from creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory

from Assignment_10.creational_patterns.builder import OrderBuilder, Order
from Assignment_10.creational_patterns.abstract_factory import BookstoreFactory, BookFactory, AuthorFactory

class TestBuilderPattern(unittest.TestCase):

    def test_basic_order(self):
        builder = OrderBuilder("001", "Alice")
        order = builder.build()
        self.assertEqual(order.order_id, "001")
        self.assertEqual(order.customer_name, "Alice")
        self.assertEqual(order.items, [])
        self.assertIsNone(order.discount)
        self.assertEqual(str(order), "Order[ID=001, Customer=Alice, Items=[], Discount=None, Delivery=None]")

    def test_full_order(self):
        builder = OrderBuilder("002", "Bob")
        order = (
            builder
            .add_item("Book", 2)
            .add_item("Pen", 5)
            .set_discount("10%")
            .set_delivery("Express")
            .build()
        )
        self.assertEqual(order.items, [("Book", 2), ("Pen", 5)])
        self.assertEqual(order.discount, "10%")
        self.assertEqual(order.delivery, "Express")
        self.assertEqual(
            str(order),
            "Order[ID=002, Customer=Bob, Items=[('Book', 2), ('Pen', 5)], Discount=10%, Delivery=Express]"
        )

    def test_invalid_item_quantity(self):
        builder = OrderBuilder("003", "Charlie")
        with self.assertRaises(ValueError):
            builder.add_item("Notebook", 0)

if __name__ == '__main__':
    unittest.main()

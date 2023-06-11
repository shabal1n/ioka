import unittest
import ioka
from dotenv import load_dotenv
import os


class IokaTests(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        ioka.api_key = os.getenv("API_KEY")
        self.test_orders = ioka.Order.get_orders()
        self.customers = ioka.Customer.get_customers()
        self.cards = ioka.Card.get_cards(self.customers[0].id)

    def test_get_orders(self):
        result = ioka.Order.get_orders()
        self.assertNotIn('code', result[0])

    def test_create_order(self):
        result = ioka.Order.create_order(amount=100)
        self.assertNotIn('code', result[0])

    def test_capture_order(self):
        result = ioka.Order.capture_order(order_id=self.test_orders[0].id, amount=100)
        self.assertIsNone(result.code)
    
    def test_cancel_order(self):
        result = ioka.Order.cancel_order(order_id=self.test_orders[0].id)
        self.assertIsNone(result.code)
    
    def test_refund_order(self):
        result = ioka.Order.refund_order(order_id=self.test_orders[0].id, amount=100)
        self.assertIsNone(result.code)
    
    def test_get_order_by_id(self):
        result = ioka.Order.get_order_by_id(order_id=self.test_orders[0].id)
        self.assertIsNotNone(result.id)
    
    def test_get_order_events(self):
        result = ioka.Order.get_order_events(order_id=self.test_orders[0].id)
        self.assertIsNotNone(result[0].id)
    
    def test_get_refunds_by_order_id(self):
        result = ioka.Order.get_refunds(order_id=self.test_orders[0].id)
        self.assertIsNotNone(result)

    def test_create_card_payment(self):
        result = ioka.Payment.create_card_payment(order_id=self.test_orders[0].id, pan="4111111111111111", exp='12/25', cvc="123")
        self.assertNotIn('code', result[0])

    def test_create_card_payment_by_card_id(self):
        self.assertNotEqual([], self.cards, "No cards found for customer")
        result = ioka.Payment.create_card_payment(order_id=self.test_orders[0].id, card_id=self.cards[0].id)
        self.assertNotIn('code', result)

if __name__ == "__main__":
    unittest.main()

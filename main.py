import ioka
from dotenv import load_dotenv
import os

load_dotenv()

ioka.api_key = os.getenv("API_KEY")

orders = ioka.Order.get_orders()

print(orders)
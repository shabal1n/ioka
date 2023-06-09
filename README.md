# ioka-lib
============================
### Introduction
This is a library for ioka API written on Python.
### Usage
    1. Import ioka module.
    2. Initialize ioka.api_key variable with your API key.
    3. Make a request to ioka API.
### Example
```python
import ioka
from dotenv import load_dotenv
import os

load_dotenv()

ioka.api_key = os.getenv("API_KEY")

orders = ioka.Order.get_orders()

print(orders)
```
# Documentation
* [Order class](#order-class)
    * [Create order](#create-order)
    * [Capture order](#capture-order)
    * [Cancel order](#cancel-order)
    * [Refund order](#refund-order)
    * [Get orders](#get-orders)
    * [Get order by ID](#get-order-by-id)
    * [Get order events](#get-order-events)
    * [Get refunds by order ID](#get-refunds-by-order-id)
    * [Get refund by order & refund ID](#get-refund-by-order--refund-id)
* [Payment class](#payment-class)
    * [Create card payment by PAN](#create-card-payment-by-pan)
    * [Create card payment by card ID](#create-card-payment-by-card-id)
    * [Get payment by ID](#get-payment-by-id)
* [Customers class](#customers-class)
    * [Create customer](#create-customer)
    * [Get customers](#get-customers)
    * [Get customer by ID](#get-customer-by-id)
    * [Get customer events](#get-customer-events)
    * [Delete customer by ID](#delete-customer-by-id)
* [Cards class](#cards-class)
    * [Create binding](#create-binding)
    * [Get cards by customer ID](#get-cards-by-customer-id)
    * [Get card by card ID](#get-card-by-card-id)
    * [Delete card by card ID](#delete-card-by-card-id)
* [Webhooks class](*webhooks-class)
    * [Create webhook](#create-webhook)
    * [Get webhooks](#get-webhooks)
    * [Get webhook by ID](#get-webhook-by-id)
    * [Delete webhook by ID](#delete-webhook-by-id)
* [Dashboard class](#dashboard-class)
    * [Search dashboard payments](#search-dashboard-payments)
    * [Export dashboard payments](#export-dashboard-payments)

============================
### Order class

#### Create order
```python
ioka.Order.create_order(amount, currency, capture_method, external_id, description, mcc, extra_info, attempts, due_date, customer_id, card_id, back_url, success_url, failure_url, template)
```
Required arguments: amount(int) >= 100

#### Capture order
```python
ioka.Order.capture_order(order_id, amount, reason)
```
Required arguments: amount(int) >= 100, order_id(str)

#### Cancel order
```python
ioka.Order.cancel_order(order_id, reason)
```
Required arguments: order_id(str)

#### Refund order
```python
ioka.Order.refund_order(order_id, reason)
```
Required arguments: order_id(str)

#### Get orders
```python
ioka.Order.get_orders(page, limit, to_dt, from_dt, date_category, order_id, external_id, order_status, amount_category, fixed_amount, min_amount, max_amount)
```
#### Get order by ID
```python
ioka.Order.get_order_by_id(order_id)
```
Required arguments: order_id(str)

#### Get order events
```python
ioka.Order.get_order_events(order_id)
```
Required arguments: order_id(str)

#### Get refunds by order ID
```python
ioka.Order.get_refunds(order_id)
```
Required arguments: order_id(str)

#### Get refund by order & refund ID
```python
ioka.Order.get_refund_by_id(order_id, refund_id)
```
Required arguments: order_id(str), refund_id(str)

### Payment class

#### Create card payment by PAN
```python
ioka.Payment.create_card_payment(order_id, pan, exp, cvc, holder, save, email, phone, fingerprint, phone_check_date, channel)
```
Required arguments: order_id(str), pan(str), exp(str), cvc(str), holder(str)

#### Create card payment by card ID
```python
ioka.Payment.create_card_payment_by_card_id(order_id, card_id, cvc, save, email, phone, fingerprint, phone_check_date, channel)
```
Required arguments: order_id(str), card_id(str)

#### Get payment by ID
```python
ioka.Payment.get_payment(order_id, payment_id)
```
Required arguments: order_id(str), payment_id(str)

### Customers class

#### Create customer
```python
ioka.Customer.create_customer(external_id, email, phone, fingerprint, phone_check_date, channel)
```

#### Get customers
```python
ioka.Customer.get_customers(page, limit, to_dt, from_dt, date_category, customer_id, external_id, status)
```

#### Get customer by ID
```python
ioka.Customer.get_customer_by_id(customer_id)
```
Required arguments: customer_id(str)

#### Get customer events
```python
ioka.Customer.get_customer_events(customer_id)
```
Required arguments: customer_id(str)

#### Delete customer by ID
```python
ioka.Customer.delete_customer_by_id(customer_id)
```
Required arguments: customer_id(str)

### Cards class

#### Create binding
```python
ioka.Card.create_binding(customer_id, pan, exp, cvc, holder)
```
Required arguments: customer_id(str), pan(str), exp(str), cvc(str)

#### Get cards by customer ID
```python
ioka.Card.get_cards(customer_id)
```
Required arguments: customer_id(str)

#### Get card by card ID
```python
ioka.Card.get_card_by_id(customer_id, card_id)
```
Required arguments: customer_id(str), card_id(str)

#### Delete card by card ID
```python
ioka.Card.delete_card_by_id(customer_id, card_id)
```
Required arguments: customer_id(str), card_id(str)

### Webhooks class

#### Create webhook
```python
ioka.Webhook.create_webhook(url, events)
```
Required arguments: url(str), events(list)

#### Get webhooks
```python
ioka.Webhook.get_webhooks()
```

#### Get webhook by ID
```python
ioka.Webhook.get_webhook_by_id(webhook_id)
```
Required arguments: webhook_id(str)

#### Update webhook by ID
```python
ioka.Webhook.update_webhook_by_id(webhook_id, url, events)
```
Required arguments: webhook_id(str)

#### Delete webhook by ID
```python
ioka.Webhook.delete_webhook_by_id(webhook_id)
```
Required arguments: webhook_id(str)

### Dashboard class

#### Search dashboard payments
```python
ioka.Dashboard.search_dashboard_payments(page, limit, to_dt, from_dt, id, external_id, extra_info, payment_id, reference, pan_first6, pan_last4, payer_email, payer_phone, customer_id, card_id)
```

#### Export dashboard payments
```python
ioka.Dashboard.export_dashboard_payments(to_dt, from_dt, id, external_id, extra_info, payment_id, reference, pan_first6, pan_last4, payer_email, payer_phone, customer_id, card_id)
```
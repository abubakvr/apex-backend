# P2P Trading API Service

A FastAPI-based service for managing peer-to-peer (P2P) cryptocurrency trading operations, integrating with the Bybit P2P API.

## Features

- 🔄 P2P Advertisement Management
  - Create and manage buy/sell advertisements
  - View online advertisements
  - Cancel/offline existing advertisements
- 💰 Order Operations
  - View pending and historical orders
  - Mark orders as paid
  - Release digital assets
  - Get detailed order information
- 👤 User Management
  - Fetch account information
  - Get current balance
  - Manage payment methods

## Prerequisites

- Python 3.8+
- MongoDB
- FastAPI
- Motor (async MongoDB driver)

## API Endpoints

### Advertisements

- `POST /api/ads/create` - Create a new api advertisement
- `GET /api/ads/list` - Get personal advertisement list
- `GET /api/ads/online` - Get online advertisements
- `POST /api/ads/offline` - Take an advertisement offline
- `GET /api/ads/{ad_id}` - Get advertisement details

### Orders

- `GET /api/orders` - Get api orders with filters
- `GET /api/orders/pending` - Get pending orders
- `GET /api/orders/{order_id}` - Get order details
- `POST /api/orders/{order_id}/pay` - Mark order as paid
- `POST /api/orders/{order_id}/release` - Release digital assets

### User

- `GET /api/user/balance` - Get current balance
- `GET /api/user/info` - Get account information
- `GET /api/user/payments` - Get user payment methods

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

- `POST /p2p/ads/create` - Create a new P2P advertisement
- `GET /p2p/ads/list` - Get personal advertisement list
- `GET /p2p/ads/online` - Get online advertisements
- `POST /p2p/ads/offline` - Take an advertisement offline
- `GET /p2p/ads/{ad_id}` - Get advertisement details

### Orders

- `GET /p2p/orders` - Get P2P orders with filters
- `GET /p2p/orders/pending` - Get pending orders
- `GET /p2p/orders/{order_id}` - Get order details
- `POST /p2p/orders/{order_id}/pay` - Mark order as paid
- `POST /p2p/orders/{order_id}/release` - Release digital assets

### User

- `GET /p2p/user/balance` - Get current balance
- `GET /p2p/user/info` - Get account information
- `GET /p2p/user/payments` - Get user payment methods

## Usage Examples

### Creating a P2P Advertisement

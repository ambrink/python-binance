from binance.client import Client

user = Client('4bEU9tanngkNFNMfRXLen5qM7cAwLpNQa2wU5txEfJrzfNj9ib5Iby1mKXhkO64J', 'IvyZL1RvpCVqLlzO0bcwqXQviRPkjWprQxTtWDAVU0Acyp5JDS0ZLhFavQsKygwl')
info = user.get_exchange_info()
print(info)
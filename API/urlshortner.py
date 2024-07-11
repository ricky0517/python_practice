# eNjhzGJ1K1233MJu0IqVVvKhPuXrvMgrX5TXh3UPgB7AfRYZPQF2afQogP6w

from pyshorteners import Shortener

ACCESS_TOKEN = "eNjhzGJ1K1233MJu0IqVVvKhPuXrvMgrX5TXh3UPgB7AfRYZPQF2afQogP6w"

long_url = input()
url_shortener = Shortener(domain="tinyurl.com", api_key=ACCESS_TOKEN)
print("Short URL is: ",format(url_shortener.tinyurl.short(long_url)))
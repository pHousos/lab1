import requests
from datetime import datetime

url = input("Enter the URL: ")

try:
    with requests.get(url) as response:
        response.raise_for_status()
        
        server_software = response.headers.get('Server')
        if server_software:
            print(f"The server is powered by: {server_software}")
        else:
            print("Server software information not available.")
        
        if 'Set-Cookie' in response.headers:
            print("The page uses cookies.")
            
            print("\nCookies:")
            for cookie in response.cookies:
                print(f"Name: {cookie.name}, Value: {cookie.value}")
                expiration_date = datetime.fromtimestamp(cookie.expires)
                formatted_date = expiration_date.strftime("%d/%m/%Y %H:%M:%S")
                print(f"Expires: {formatted_date}")
        else:
            print("The page does not use cookies.")
except requests.RequestException as e:
    print("Error fetching URL:", e)

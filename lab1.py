import requests

url = input("Enter the URL: ")  # ζήτησε από τον χρήστη να εισάγει το URL

try:
    with requests.get(url) as response:
        response.raise_for_status()  # Ελέγχει αν υπάρχει σφάλμα κατά την αίτηση
        print("\nResponse Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
except requests.RequestException as e:
    print("Error fetching URL:", e)

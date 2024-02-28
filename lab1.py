import requests

url = input("Enter the URL: ")  # ζήτησε από τον χρήστη να εισάγει το URL

try:
    with requests.get(url) as response:
        response.raise_for_status()  # Ελέγχει αν υπάρχει σφάλμα κατά την αίτηση
        
        # Εκτύπωση του λογισμικού του εξυπηρετητή
        server_software = response.headers.get('Server')
        if server_software:
            print(f"The server is powered by: {server_software}")
        else:
            print("Server software information not available.")
        
        # Έλεγχος για τη χρήση cookies
        if 'Set-Cookie' in response.headers:
            print("The page uses cookies.")
        else:
            print("The page does not use cookies.")
except requests.RequestException as e:
    print("Error fetching URL:", e)

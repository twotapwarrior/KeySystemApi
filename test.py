import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_encrypt_route():
    data = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland"
    }
    response = requests.post(f"{BASE_URL}/encrypt", json=data)
    print("Status Code:", response.status_code)
    if response.headers.get('Content-Type') == 'application/json':
        response_json = response.json()
        print("Response JSON:", response_json)
        
        encrypted_data = response_json.get("encrypted_data")
        return encrypted_data
    else:
        print("Response content is not in JSON format or is empty.")
        print("Response Text:", response.text)
        return None

def test_decrypt_route(encrypted_data):
    if not encrypted_data:
        print("No encrypted data to decrypt.")
        return
    response = requests.post(f"{BASE_URL}/decrypt", data=encrypted_data)
    print("Status Code:", response.status_code)

    if response.headers.get('Content-Type') == 'application/json':
        print("Response JSON:", response.json())
    else:
        print("Response content is not in JSON format or is empty.")
        print("Response Text:", response.text)

def main():
    encrypted_data = test_encrypt_route()
    test_decrypt_route(encrypted_data)

if __name__ == "__main__":
    main()
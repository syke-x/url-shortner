import requests

BASE_URL = "http://127.0.0.1:5000"


def test_get_users_rate_limit(token):
    url = f"{BASE_URL}/api/users"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    for i in range(10):
        response = requests.get(url, headers=headers)

        print(f"Request {i+1} -> Status: {response.status_code}")

        try:
            print(response.json())
        except:
            print(response.text)

        print("-" * 40)


if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MzE0MDE3NCwianRpIjoiMTZiNWIzYjYtNGEwNy00YmE0LWI5OTUtNDQ0ZTllZmI1Y2IxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjQiLCJuYmYiOjE3NzMxNDAxNzQsImNzcmYiOiI1MzFlZWI1NS0wMGE5LTQwZjgtOThlZS03NjcwNDYxYjIyNmIiLCJleHAiOjE3NzMxNDE5NzQsInJvbGUiOiJ1c2VyIn0.LZbekw9vM0qxXB2fRmdDna_YZGv6TW6oSNH9QM1HN-0"
    test_get_users_rate_limit(token)
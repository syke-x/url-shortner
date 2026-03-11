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
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MzE2ODAwMiwianRpIjoiZDJhNTkzZDctNmNmMi00OTQ5LTg4ZjAtYTA2YWZmMmExMmNkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzMxNjgwMDIsImNzcmYiOiJlMzljYTdkMC0wNWQ2LTRlNDctYjc1OS03YjYxOWI0Y2U0NDgiLCJleHAiOjE3NzMxNjk4MDIsInJvbGUiOiJ1c2VyIn0.qwBNLUN7SFdco-kWVHfZyFERjXZUsP24KzMeqaMjYaY"
    test_get_users_rate_limit(token)
import requests
import concurrent.futures
import time
from collections import Counter

URL = "http://127.0.0.1:5000/api/shorten"

payload = {
    "long_url": "https://example.com"
}

headers = {
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MjQ0NjQ2NCwianRpIjoiYTU1MTVkNDItYTgzYi00NjAzLWE2MmItZGVjOWY3ZDgxZDZhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3NzI0NDY0NjQsImNzcmYiOiI5ZjIyYTE0ZS1jYjMxLTQ5MmQtODAxNC1mYzljMzM1ZjYwZmEiLCJleHAiOjE3NzI0NDgyNjQsInJvbGUiOiJ1c2VyIn0.d6cuIhdaQNer5Oxhk_ISDWlFtSFEWDxGRKklIybqyHk",
    "Content-Type": "application/json"
}

TOTAL_REQUESTS = 2000
CONCURRENT_WORKERS = 50


def send_request():
    start = time.time()
    response = requests.post(URL, json=payload , headers=headers)
    end = time.time()

    print(response.text)

    return {
        "status": response.status_code,
        "response_time": end - start
    }


def main():
    start_test = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENT_WORKERS) as executor:
        futures = [executor.submit(send_request) for _ in range(TOTAL_REQUESTS)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]

    end_test = time.time()

    total_time = end_test - start_test

    # Count status codes
    status_counts = Counter(r["status"] for r in results)

    # Response time stats
    response_times = [r["response_time"] for r in results]
    avg_response_time = sum(response_times) / len(response_times)
    max_response_time = max(response_times)
    min_response_time = min(response_times)

    # Throughput
    throughput = TOTAL_REQUESTS / total_time

    print("\n===== TEST RESULTS =====")
    print(f"Total Requests: {TOTAL_REQUESTS}")
    print(f"Concurrent Workers: {CONCURRENT_WORKERS}")
    print(f"Total Time: {total_time:.2f} sec")
    print(f"Throughput: {throughput:.2f} req/sec")
    print("\nStatus Code Counts:")
    print(status_counts)
    print("\nResponse Time Stats:")
    print(f"Average: {avg_response_time:.4f} sec")
    print(f"Max: {max_response_time:.4f} sec")
    print(f"Min: {min_response_time:.4f} sec")


if __name__ == "__main__":
    main()
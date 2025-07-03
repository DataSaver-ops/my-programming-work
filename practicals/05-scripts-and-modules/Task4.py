import sys
import http.client
from urllib.parse import urlparse

def check_url():
    if len(sys.argv) > 1:
        url = sys.argv[1]
        parsed_url = urlparse(url)
        conn = http.client.HTTPConnection(parsed_url.netloc)
        try:
            conn.request("HEAD", parsed_url.path)
            response = conn.getresponse()
            if response.status == 200:
                print(f"Website at {url} is working.")
            else:
                print(f"Website at {url} returned status code {response.status}.")
        except Exception as e:
            print(f"Error accessing {url}: {e}")
        finally:
            conn.close()
    else:
        print("No URL provided.")

check_url()



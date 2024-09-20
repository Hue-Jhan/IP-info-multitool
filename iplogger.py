import logging
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
from pyngrok import ngrok
import threading

# REMEMBER TO INSERT YOUR NGROK TOKEN IN THE YML FILE!!!


class HelloHandler(BaseHTTPRequestHandler):
    last_ip_time = 0
    delay_seconds = 1

    def do_GET(self):
        current_time = time.time()
        if current_time - HelloHandler.last_ip_time < HelloHandler.delay_seconds:
            self.send_response(429)
            self.end_headers()
            return

        forwarded_for = self.headers.get('X-Forwarded-For')
        visitor_ip = forwarded_for.split(',')[0].strip() if forwarded_for else self.client_address[0]

        print()
        print(f"\033[38;2;0;255;0m          New IP found: \033[38;2;0;150;215m{visitor_ip} \033[0m")
        HelloHandler.last_ip_time = current_time
        ip_info = self.get_ip_info(visitor_ip)

        body = bytes("Hello, nice IP", "utf-8")
        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def get_ip_info(self, ip):
        url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            for key, value in {
                "Hostname": data.get("hostname", "N/A"),
                "City": data.get("city", "N/A"),
                "Region": data.get("region", "N/A"),
                "Country": data.get("country", "N/A"),
                "Location": data.get("loc", "N/A"),
                "Organization": data.get("org", "N/A")
            }.items():
                print(f"    \033[38;2;0;230;128m           {key}:\033[38;2;0;150;215m{value}\033[0m")
        except requests.RequestException:
            print("Error retrieving IP info")

    def log_message(self, format, *args):
        return


def run_ip_logger():
    logging.getLogger().setLevel(logging.CRITICAL)
    server = HTTPServer(("localhost", 0), HelloHandler)
    port = server.server_address[1]
    public_url = ngrok.connect(port)
    print(f"\033[38;2;0;255;0m          {public_url} \033[0m")

    def serve():
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

    server_thread = threading.Thread(target=serve)
    server_thread.daemon = True  # So it will stop when the main thread stops
    server_thread.start()

    try:
        print("          Press Enter to stop the server...")
        input()
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        ngrok.disconnect(public_url)
        server.shutdown()
        server_thread.join()


if __name__ == "__main__":
    run_ip_logger()

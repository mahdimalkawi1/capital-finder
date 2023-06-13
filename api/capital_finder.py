from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_dict = dict(parse.parse_qsl(url_components.query))

        messages = []
        if 'country' in query_dict:
            country = query_dict.get('country')
            url = f"https://restcountries.com/v3.1/name/{country}"
            response = requests.get(url)
            data = response.json()
            for country_data in data:
                capital = country_data['capital'][0]
                message = f"The capital of {country} is {capital}"
                messages.append(message)

        elif 'capital' in query_dict:
            capital = query_dict.get('capital')
            url = f"https://restcountries.com/v3.1/capital/{capital}"
            response = requests.get(url)
            data = response.json()
            for country_data in data:
                name = country_data['name']['common']
                message = f"{capital} is the capital of {name}"
                messages.append(message)

        complete_message = '\n'.join(messages)
        self.wfile.write(complete_message.encode())
        return

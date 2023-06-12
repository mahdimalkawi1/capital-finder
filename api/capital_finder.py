from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    list_of_dif=[]
    message="testing"
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)

    # print(111,my_dict)
    if 'word' in my_dict:
      word = my_dict.get('word')
      url= 'https://api.dictionaryapi.dev/api/v2/entries/en/'
      res = requests.get(url+word)
      data = res.json()
    #   print(222,data)
    for word_data in data :
      definition = word_data['meanings'][0]['definitions'][0]['definition']
      message = str(definition)
      list_of_dif.append(message)
    print(2222,list_of_dif)




    self.wfile.write(message.encode())
    return
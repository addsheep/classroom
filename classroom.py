import logging
import os
import jinja2
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def write_response(response, response_type, target_page, params):
  if response_type == 'json':
    content = json.dumps(params)
  else:
    template = jinja_environment.get_template(target_page)
    content = template.render(params)
  response.out.write(content)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_environment.get_template('index.html')
        params = {
          'test': 'hahaha'
        }
        content = template.render(params)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

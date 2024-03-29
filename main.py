#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
form = """ <form method="post" action="/testform">
<input name = "q">
<input type = "submit">
</form>"""

rot13Form = """
<form method="post" action="/rot13">
<textarea name="text"></textarea>
<input type = "submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain' 
        self.response.out.write(form)
		
class TestHandler(webapp2.RequestHandler):
    def post(self):
	    #q = self.request.get("q")
		#self.response.out.write(q)
		
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request)

class Rot13(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(rot13Form)
	
	def post(self):
		self.response.out.write(rot13Form)


app = webapp2.WSGIApplication([
   ('/', MainPage), ('/testform', TestHandler), ('/rot13', Rot13)	
], debug=True)

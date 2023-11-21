from api import api

@api.route('/')
@api.route('/index')
def index():
    user = {'username': 'LEO'}
    return '''
<html>
    <head>
        <title>Home Page - GEPMS</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
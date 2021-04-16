import app

url = f'http://www.qszy9.com/index-{1}.html'

html = app.get_data(url)
print(html)
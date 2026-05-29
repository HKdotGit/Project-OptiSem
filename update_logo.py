import base64
import re

with open('C:/Users/hp/.gemini/antigravity/brain/026c335a-4295-40da-a708-4976d0410247/media__1779112073635.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

new_uri = 'data:image/png;base64,' + b64

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'const LOGO_SRC = "data:image/svg\+xml;base64,[A-Za-z0-9+/=]+";', f'const LOGO_SRC = "{new_uri}";', content)

if new_content == content:
    print('Failed to find and replace the logo src')
else:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully updated index.html with the user PNG base64.')

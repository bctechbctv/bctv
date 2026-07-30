import urllib.request
import xml.etree.ElementTree as ET

RSS_URL = 'https://rthk.hk/rthk/news/rss/c_expressnews_clocal.xml'

try:
    req = urllib.request.Request(
        RSS_URL, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req, timeout=10) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    titles = [item.text.strip() for item in root.findall('.//item/title') if item.text]

    if titles:
        with open('news.txt', 'w', encoding='utf-8') as f:
            f.write(" ✦ ".join(titles))
        print("Successfully updated news.txt")
except Exception as e:
    print(f"Error: {e}")
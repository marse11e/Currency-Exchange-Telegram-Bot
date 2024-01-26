import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, url) -> None:
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        }

    def html_method(self):
        response = requests.get(self.url, headers=self.headers)
        
        if response.status_code == 200:
            return response.text
        
        return False
    

    def proccessing_method(self):
        html = self.html_method()

        if html:
            soup = BeautifulSoup(html, "lxml").find("div", {"class": "blockquote-classic"}).text.split("\n")
            info = "Информация по курсам обновляется каждые 4 часа, курс обмена выбранной пары валют на сегодня: "
            return info + " ".join([i.strip() for i in soup if len(i) > 1 ])
        
        return False
    
    def proccessing_method_2(self):
        html = self.html_method()

        if html:
            soup = BeautifulSoup(html, "lxml").find("div", {"class": "col-text col-text-no-spaces-between-p col-text-sm-2 col-text-md-3 text-muted conversion-long-desc-text"}).get_text(strip=True)

            return " ".join([i.strip() for i in soup.split("\n") if len(i) > 1 ]).split(".")[3]
        
        return False
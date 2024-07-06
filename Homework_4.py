import requests
import re

def use_get():
    response = requests.get('https://www.lejobadequat.com/emplois')
    content = response.text
    job_list = re.findall(r'<div\s+class=["\']job_secteur_title["\'][^>]*>(.*?)<\/div>', content)
    clean_job_list = [re.sub(r'\<wbr\>', '', string) for string in job_list]

if __name__ == '__main__':
    use_get()


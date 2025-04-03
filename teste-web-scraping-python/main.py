
import requests
import os
from bs4 import BeautifulSoup
import zipfile

pageUrl = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
page = requests.get(pageUrl)


download_dir = "/mnt/d/pdfs" 
if not os.path.exists(download_dir):
    os.makedirs(download_dir)


soup = BeautifulSoup(
    page.content,
    'html.parser'
)

count = 0

for link in soup.find_all('a', class_='internal-link'):
     href = link.get('href')
     if '.pdf' in href: 
         count += 1
         if count > 2:
                break
         if not href.startswith("https"):
            href = pageUrl + href

         pdf_name = os.path.join(download_dir, href.split("/")[-1])
         try:
                        pdf_response = requests.get(href)
                        pdf_response.raise_for_status()  

                        with open(pdf_name, 'wb') as f:
                            f.write(pdf_response.content)

                        print(f"Arquivo salvo como {pdf_name}")
         except requests.exceptions.RequestException as e:
                        print(f"Erro ao baixar o arquivo {href}: {e}")

  
zip_filename = os.path.join(download_dir, "arquivos_pdfs.zip")       

with zipfile.ZipFile(zip_filename, "w") as zipf:
       for file in os.listdir(download_dir):
              pdf_path = os.path.join(download_dir, file)

              if file == "arquivos_pdfs.zip":
                     continue
              if file.endswith(".pdf"):       
                zipf.write(pdf_path, file)
                os.remove(pdf_path)

print(f"Arquivos compactados")                    

import requests
import pandas as pd
from bs4 import BeatifulSoup

th = "https://www.jobs.id/lowongan-kerja?kata-kunci=part time"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
print(hasil)

# Scraper web
# TIK
# X TKJ
# SMK RADEN PAKU

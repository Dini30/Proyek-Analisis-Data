# Proyek-Analisis-Data
Pada proyek analisis data ini saya menggunakan dataset E-Commerce Public Dataset (order_payments_dataset), dimana pertama saya melakukan proses analisis dibuat dalam notebook yang rapi.

Library yang saya gunakan disini :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Setelahnya saya import terlebih dahulu file csv yang saya gunakan, dengan kode:
from google.colab import files
uploaded = files.upload()

Untuk mencari Gathering Data
import pandas as pd
order_payments_dataset = pd.read_csv('order_payments_dataset.csv')
print(order_payments_dataset)

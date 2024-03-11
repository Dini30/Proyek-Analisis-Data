# Proyek Analisis Data

## Informasi Poyek
- Nama : Dini Ayuastina
- Email : diniayuastina02@gmail.com
- ID Dicoding : Dini Ayuastina

## Menentukan Pertanyaan Bisnis
1. Pertanyaan 1 : Bagaimana distribusi total pembayaran?
2. Pertanyaan 2 : Bagaimana tren penjualan peningkatan atau penurunan pembayaran dari waktu ke waktu?

## Library yang digunkana 
- pandas
- numpy
- matlotlib
- seaborn

## Langkah-langkah analisis data
1. Data Wrangling : Gatherin Data, Assesing Data, Cleaning Data
2. Exploratory Data Analysis (EDA): melakukan eksplorasi data untuk memahami karakteristik dan hubungan antar variabel.
3. Visualization & Explanatory Analysis : Melakukan visualisasi data unutk menjawab pertanyaan bisnis dan memberikan insight.

## Visualisasi dan Analisis
### Pertanyaan 1 : bagaimana distribusi total pembaryaran?
- menggunakan pie chart untuk memvisualisasikan distrbusi total pembayaran berdasarkan jenis pembayaran.
- - dari pie chart tersebut dapat dilihat persentase penggunaan tiap jenis pembayaran.
![image](https://github.com/Dini30/Proyek-Analisis-Data/assets/148301923/4d305097-a8cb-4a49-8d4d-0fc9c5a209c2)


### Pertanyaan 2 : baaimana tren penjualana peningkatan atau penururnan pembayaran dari waktu ke waktu
- melakukan analisis tren penjualan dan pembayaran dari waktu ke waktu menggunakan line plot
- dari line plot tersebut dapat dilihat tren penjualan dan pembayaran dari setiap pembayaran.
![image](https://github.com/Dini30/Proyek-Analisis-Data/assets/148301923/bd7b8820-d031-43ae-8d0e-5bfd58a73961)


## Kesimpulan 
- Berdasarkan hasil analisis, dapat disimpulkan bahwa penjualan dan pembayaran menunjukkan tren positif secara keseluruhan, dengan peningktana dari waktu ke waktu.

# Payment Data Visualizer 📊

Aplikasi ini memungkinkan untuk memvisualisasikan data pembayaran dengan mudah, kita dapat menggunakan dat yang ada atau memasukkan data kita sendiri untuk langsung membuat visualisasi yang menarik.

## Cara Menggunakan 
1. Pilih kolom : Pilih kolom yang ingin kita analisis dari menu dropdown yang tersedia.
2. Lihat Visualisasi : Aplikasi akan membuat Visualisasi berdasarkan kolom yang kita pilih. Kita dapat melihatanya di bawah data yang ditampilkan.

## Contoh Data
| payment_type  | payment_sequential | payment_value |
|---------------|--------------------|---------------|
| Credit_Card   | 1                  | 99.33         |
| Boleto        | 1                  | 51.95         |
| Voucher       | 1                  | 45.17         |
| Other         | 1                  | 227.12        |

## Requirements
Pastikan telah menginstal semua package yang dibutuhkan dengan menjalankan perintah berikut :
pip install -r requirements.txt

## Cara Menjalankan 
Kita dapat menjalankan aplikasi ini dengan menjalankan perintah berikut di terminal :
streamlit run distribusitotalpembayaran.py

## Library yang digunakan
- Stremlit : unutk membuat aplikasi web interaktif dengan Python.
- Pandas : untuk manipulasi dan analisis data.
- Plotly Express : untuk membuat visulalisasi data interaktif.

## Contoh Penggunaan
Berikut adalah contoh tampilan aplikasi saat digunakan :
![image](https://github.com/Dini30/Proyek-Analisis-Data/assets/148301923/25d70f32-233b-49e0-84ce-dd583f21c203)
![image](https://github.com/Dini30/Proyek-Analisis-Data/assets/148301923/179e3552-46bb-47d9-bcc6-8dc9fa42d2d4)

## Pengembang 
Dini Ayuastina - [diniayuastina02@gmail.com](email:diniayuastina02@gmail.com)


















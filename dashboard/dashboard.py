import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
order_delivery_satisfaction_df = pd.read_csv('https://raw.githubusercontent.com/hawadz/e-commerce--analysis/refs/heads/main/dashboard/order_delivery_satisfaction_df.csv')
avg_popularity_product_df = pd.read_csv('https://raw.githubusercontent.com/hawadz/e-commerce--analysis/refs/heads/main/data/avg_popularity_product.csv')

# Dashboard
st.title('E-commerce Analysis Dashboard')

# Analisis Pertanyaan 1
st.header('Analisis Pertanyaan 1: Korelasi antara waktu pengiriman pesanan dan tingkat kepuasan pelanggan')
st.write("Dari scatter plot tersebut, kita dapat melihat pola distribusi titik-titik data antara waktu pengiriman pesanan dan tingkat kepuasan pelanggan.")
st.write("Jika ada korelasi antara kedua variabel tersebut, kita dapat melihat pola linear atau non-linear yang menunjukkan hubungan antara waktu pengiriman dan tingkat kepuasan pelanggan.")
st.write("Namun, jika scatter plot menunjukkan pola yang acak dan tersebar secara merata, ini menunjukkan bahwa tidak ada hubungan yang jelas antara waktu pengiriman pesanan dan tingkat kepuasan pelanggan.")

fig = plt.figure(figsize=(8, 4))
plt.scatter(order_delivery_satisfaction_df['delivery_time'], order_delivery_satisfaction_df['review_score'], alpha=0.5)
plt.title('Korelasi antara Waktu Pengiriman Pesanan dan Tingkat Kepuasan Pelanggan')
plt.ylabel('Tingkat Kepuasan Pelanggan')
plt.xlabel('Waktu Pengiriman Pesanan (hari)')
plt.grid(True)
st.pyplot(fig)

# Analisis Pertanyaan 2
st.header('Analisis Pertanyaan 2: Rata-rata harga produk per kategori dan popularitas kategori')
st.write("Rata-rata harga per kategori menunjukkan variasi yang cukup besar, dengan beberapa kategori memiliki harga premium yang lebih tinggi dibandingkan lainnya.")
st.write("Terdapat beberapa kategori dengan harga rata-rata rendah yang memiliki penjualan tinggi, menunjukkan kemungkinan sensitivitas harga di pasar ini.")

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Subplot pertama: Bar plot untuk rata-rata harga produk per kategori
sns.barplot(data=avg_popularity_product_df.head(5), x='price', y='product_category_name_english', palette=colors, ax=ax1)
ax1.set_title('Rata-rata Harga Produk per Kategori')
ax1.set_xlabel('Kategori Produk')
ax1.set_ylabel('Harga Rata-rata Produk')

# Subplot kedua: Bar plot untuk popularitas kategori berdasarkan jumlah produk yang terjual
sns.barplot(data=avg_popularity_product_df.sort_values(by='product_id', ascending=False).head(5), x='product_id', y='product_category_name_english', palette=colors, ax=ax2)
ax2.set_title('Popularitas Kategori Berdasarkan Jumlah Produk yang Terjual')
ax2.set_xlabel('Jumlah Produk Terjual')
ax2.set_ylabel('Kategori Produk')

plt.tight_layout()
st.pyplot(fig)

st.write("- *Conclusion 1*: Mengurangi waktu pengiriman dapat secara signifikan meningkatkan kepuasan pelanggan. Mengoptimalkan logistik pengiriman harus menjadi prioritas untuk meningkatkan pengalaman pelanggan.")
st.write("- *Conclusion 2*: Barang-barang dengan harga tinggi di kategori populer seperti Elektronik dan Pakaian tidak sensitif terhadap harga, menunjukkan adanya peluang untuk promosi strategis dan penyesuaian harga di segmen ini.")
st.write("- *Future Work*: Analisis tambahan bisa mengeksplorasi faktor-faktor lain yang mempengaruhi kepuasan pelanggan, seperti kualitas produk, tingkat pengembalian, dan layanan pelanggan pasca pembelian.")

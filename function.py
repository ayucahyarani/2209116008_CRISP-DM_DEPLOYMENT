import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    URL = 'Mall_Customers.csv'
    cs = pd.read_csv(URL)
    return cs

def data_storytelling(cs):
    st.title("Mall Customer Segmentation")
    st.image("photo.jpg")
    st.markdown("""
                Di mal, pengunjung memiliki kebiasaan belanja yang berbeda-beda. Dengan data tentang usia, 
                jenis kelamin, dan pola belanja, kita bisa memahami preferensi mereka dan meningkatkan pelayanan. 
                Tujuan utama segmentasi pelanggan di mal adalah untuk lebih memahami pengunjung, meningkatkan 
                pengalaman belanja, dan tentu saja, keuntungan. Yuk, jelajahi aplikasi ini untuk menemukan wawasan 
                menarik tentang perilaku belanja di mal!""")
    
    st.header("Mall Customer Data")
    URL = 'Mall_Customers.csv'
    cs = pd.read_csv(URL)
    st.write(cs)

def data_distribution(cs) :
    st.header('Distribution')

    st.write("""
             Visualisasi ini menunjukkan bagaimana fitur yang dipilih tersebar. Histogram menunjukkan sebaran data secara horizontal, 
             sementara tingkat frekuensi munculnya nilai ditampilkan secara vertikal. Semakin tinggi puncak histogram, semakin sering 
             nilai itu muncul dalam data. Garis KDE membantu memperkirakan seberapa padat probabilitas data tersebut. Puncak KDE yang 
             tinggi atau curam menandakan tingkat kepadatan probabilitas yang lebih besar pada nilai-nilai tertentu.""")

    selected_feature_scatter = st.selectbox("Select features for Histogram:", ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'])

    if selected_feature_scatter == 'Age':
        plt.figure(figsize=(20, 5))
        plt.subplot(1, 3, 1)
        sns.histplot(cs['Age'], bins=10, kde=True, color='blue')
        plt.title('Histogram Age')
        plt.tight_layout()
        st.pyplot(plt)
        st.write("""
                 Distribusi usia berbentuk miring kanan dengan mayoritas orang berada di usia 20-an dan 30-an. Jumlah orang berkurang 
                 seiring dengan bertambahnya usia.""")

    elif selected_feature_scatter == 'Annual Income (k$)':
        plt.figure(figsize=(20, 5))
        plt.subplot(1, 3, 2)
        sns.histplot(cs['Annual Income (k$)'], bins=10, kde=True, color='green')
        plt.title('Histogram Annual Income')
        plt.tight_layout()
        st.pyplot(plt)
        st.write("""
                 Distribusi pendapatan tahunan rata-rata berbentuk miring kanan dengan mayoritas orang memiliki pendapatan di kisaran 
                 50.000 - 100.000 dolar per tahun. Ada beberapa orang dengan pendapatan yang sangat tinggi (di atas 140.000 dolar per 
                 tahun).""")

    elif selected_feature_scatter == 'Spending Score (1-100)':
        plt.figure(figsize=(20, 5))
        plt.subplot(1, 3, 3)
        sns.histplot(cs['Spending Score (1-100)'], bins=10, kde=True, color='red')
        plt.title('Histogram Spending Score')
        plt.tight_layout()
        st.pyplot(plt)
        st.write("""
                 Distribusi skor pengeluaran terdistribusi secara normal dengan mayoritas orang memiliki skor di kisaran 40-60.""")

def relationship(cs):
    st.header('Relationship')

    st.write("""
             Visualisasi di bawah adalah matriks korelasi yang menunjukkan hubungan linier antara fitur-fitur numerik dalam dataset. 
             dapat bernilai antara -1 hingga 1. Nilai 1 menandakan korelasi positif sempurna, -1 menandakan korelasi negatif sempurna, 
             dan 0 menunjukkan tidak adanya korelasi.""")

    fig, ax = plt.subplots()
    sns.heatmap(cs.corr(numeric_only=True), annot=True, fmt=".2f", cbar=True, cmap="Blues")
    plt.xlabel('Fitur')
    plt.ylabel('Fitur')
    plt.title('Matriks Korelasi Antar Fitur Numerik')
    plt.gcf().set_size_inches(15, 10)
    st.pyplot(fig)

    st.write("""
             Dari gambar tersebut, kita dapat melihat Heatmap yang memberikan informasi sebagai berikut:
             - CustomerID: Tidak memiliki korelasi yang kuat dengan variabel lain.
             - Age: Memiliki korelasi negatif lemah dengan Spending Score (1-100), yang berarti semakin tua seseorang, semakin sedikit kemungkinan mereka menghabiskan banyak uang.
             - Annual Income (k$): Memiliki korelasi positif kuat dengan Spending Score (1-100), yang berarti semakin tinggi pendapatan seseorang, semakin besar kemungkinan mereka menghabiskan banyak uang.""")

def comparison(cs):
    st.header('Comparison')

    st.write("""
             Visualisasi ini menunjukkan bagaimana fitur yang dipilih membandingkan data atau informasi antara dua atau lebih entitas. 
             Tujuannya adalah untuk memahami perbedaan, kesamaan, atau tren antara subjek yang dibandingkan.""")

    selected_feature_scatter = st.selectbox("Select features for the Scatter plot:", ['Age vs Spending Score', 'Age vs Annual Income'])

    if selected_feature_scatter == 'Age vs Spending Score':
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        sns.scatterplot(cs, x='Age', y='Spending Score (1-100)', hue='Gender', palette='Set1')
        plt.title('Age vs Spending Score')
        plt.tight_layout()
        st.pyplot(plt)
        st.write("""
                 Terdapat korelasi negatif yang lemah antara usia dan skor pengeluaran. Artinya, seiring bertambahnya usia, skor 
                 pengeluaran cenderung meningkat. Pola penyebaran data menunjukkan banyak variasi dalam skor pengeluaran untuk setiap kelompok usia.""")

    elif selected_feature_scatter == 'Age vs Annual Income':
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 2)
        sns.scatterplot(cs, x='Age', y='Annual Income (k$)', hue='Gender', palette='Set2')
        plt.title('Age vs Annual Income')
        plt.tight_layout()
        st.pyplot(plt)
        st.write("""
                 Terdapat korelasi positif yang kuat antara usia dan pendapatan tahunan rata-rata. Artinya, seiring bertambahnya 
                 usia, penghasilan tahunan cenderung meningkat secara signifikan. Pola penyebaran data menunjukkan variasi yang lebih 
                 kecil dalam penghasilan tahunan dibandingkan skor pengeluaran.""")

def composition(cs):
    st.header('Composition')

    st.write ("""
              Visualisasi ini menunjukkan bagaimana bagian-bagian dari suatu keseluruhan berkontribusi terhadap keseluruhan itu sendiri. Tujuannya adalah 
              untuk memperlihatkan proporsi, distribusi, atau kontribusi relatif dari setiap komponen dalam suatu sistem atau kumpulan data.""")

    gender_counts = cs['Gender'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#c7d1e0'])
    plt.title('Count of Gender', y=0.93)
    st.pyplot(plt)

    st.write ("""
              Berdasarkan gambar, terdapat Pie Chart yang menunjukkan jumlah pelanggan terbanyak berdasarkan gender adalah perempuan, yaitu sebanyak 56%.""")
    
def load_data2():
    URL1 = 'dataset.csv'
    cs2 = pd.read_csv(URL1)
    return cs2

def clustering():
    st.header("Clustering")

    st.write ("""
              Visualisasi ini menunjukkan bagaimana data dikelompokkan menjadi klaster berdasarkan kesamaan karakteristik atau atribut tertentu. Tujuannya 
              adalah untuk memahami pola alami atau struktur yang ada dalam data dan mengidentifikasi kelompok atau klaster yang berbeda.""")

    customer_data = load_data2()
    n_clusters = st.sidebar.slider("Select number of Clusters", 2, 10, 4)
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=42) 
    cluster_labels = kmeans_model.fit_predict(customer_data)

    customer_data['kmeans_cluster'] = cluster_labels

    st.subheader("Elbow Plot")

    st.write ("""
              Elbow Plot adalah metode visual yang digunakan dalam analisis klaster untuk membantu menentukan jumlah optimal dari klaster yang harus 
              digunakan untuk data yang diberikan. Tujuannya adalah untuk menemukan "siku" dalam grafik yang menunjukkan di mana penurunan jumlah variabilitas 
              dalam data berkurang secara signifikan, menunjukkan bahwa penambahan klaster setelah titik tersebut tidak memberikan peningkatan yang signifikan 
              dalam pemahaman atau interpretasi data.""")
    
    inertia_values = []

    k_range = range(2, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)  
        kmeans.fit(customer_data)
        inertia_values.append(kmeans.inertia_)
    
    plt.plot(k_range, inertia_values, marker='o')
    plt.xlabel('Number of clusters (K)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal K')
    plt.xticks(k_range)
    st.pyplot(plt)

    st.subheader("Data with Cluster Labels")

    st.write ("""
              Data dengan Label Klaster adalah data yang telah dikelompokkan atau diberi label berdasarkan hasil dari analisis klaster. Proses ini 
              melibatkan penggunaan algoritma klastering untuk mengelompokkan data menjadi kelompok-kelompok yang memiliki kesamaan karakteristik 
              atau atribut tertentu. Setelah data dikelompokkan, setiap titik data diberi label atau nomor klaster yang menunjukkan keanggotaannya 
              dalam klaster tertentu.""")

    st.write(customer_data)

    clusters(customer_data)

def clusters(customer_data):
    st.subheader("Clustered Data Visualization")

    st.write ("""
              Visualisasi ini menunjukkan data yang telah dikelompokkan (klaster) dalam bentuk diagram titik-titik yang tersebar di bidang dua dimensi. 
              Scatter plot memungkinkan kita untuk melihat pola, tren, dan hubungan antara klaster yang berbeda dalam data.""")

    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots()
        sns.scatterplot(data=customer_data, x='Annual Income (k$)', y='Age', hue='kmeans_cluster', palette='viridis', ax=ax)
        ax.set_title('Clustered Data (Annual Income vs Age)')
        ax.set_xlabel('Annual Income (k$)')
        ax.set_ylabel('Age')
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        sns.scatterplot(data=customer_data, x='Spending Score (1-100)', y='Age', hue='kmeans_cluster', palette='viridis', ax=ax)
        ax.set_title('Clustered Data (Spending Score vs Age)')
        ax.set_xlabel('Spending Score (1-100)')
        ax.set_ylabel('Age')
        st.pyplot(fig)
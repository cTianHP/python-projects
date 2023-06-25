import pandas as pd
import matplotlib.pyplot as plt

# Mendefinisikan path/file Excel yang ingin dibaca
file_path = 'DataNilai.xlsx'

# Membaca file Excel
data_frame = pd.read_excel(file_path)

# Mengklasifikasikan nilai siswa
def klasifikasi_nilai(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 70:
        return 'B'
    elif nilai >= 55:
        return 'C'
    elif nilai >= 40:
        return 'D'
    else:
        return 'E'

# Menambahkan kolom klasifikasi nilai ke dalam data frame
data_frame['Klasifikasi Nilai'] = data_frame['Nilai'].apply(klasifikasi_nilai)

# Menampilkan data frame
print(data_frame)

# Menyimpan DataFrame ke file Excel
output_file_path = 'outputDataNilai.xlsx'
data_frame.to_excel(output_file_path, index=False)

# Membuat plot grafik nilai siswa
nilai_kelas = data_frame['Klasifikasi Nilai'].value_counts().sort_index()
labels = nilai_kelas.index
jumlah_siswa = nilai_kelas.values

plt.bar(labels, jumlah_siswa)
plt.xlabel('Klasifikasi Nilai')
plt.ylabel('Jumlah Siswa')
plt.title('Histogram Nilai Siswa')
plt.show()

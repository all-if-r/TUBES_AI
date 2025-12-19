import json
import os

notebook_path = r'c:\Users\alifr\Documents\COOLYEAH TELKOM\SEMESTER 5\KECERDASAN ARTIFISIAL\TUBES AI\TUBES_AI\NYOBA\LogisticRegressionManual_Pima.ipynb'

# Baca notebook file
print(f"Membaca file: {notebook_path}")
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Temukan dan perbaiki cell dengan pd.read_csv('diabetes.xls')
found = False
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        source_text = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        if "pd.read_csv('diabetes.xls')" in source_text:
            found = True
            # Ganti dengan pd.read_excel
            new_source = """# Baca dataset dari file diabetes.xls menggunakan pd.read_excel()
# PENTING: Gunakan pd.read_excel() untuk file .xls/.xlsx, BUKAN pd.read_csv()
# pd.read_csv() untuk file .csv (text-based), sedangkan .xls adalah file binary

try:
    df = pd.read_excel('diabetes.xls')
except FileNotFoundError:
    print("File 'diabetes.xls' tidak ditemukan.")
    raise
except Exception as e:
    print(f"Error: {e}")
    raise

# Tampilkan informasi dasar
print("Shape dataset:", df.shape)
print("\\nKolom-kolom:")
print(list(df.columns))
print("\\nLima data pertama:")
print(df.head())
print("\\nInfo dataset:")
print(df.info())"""
            
            # Konversi source ke list of strings dengan newline
            cell['source'] = [line + '\n' for line in new_source.split('\n')[:-1]] + [new_source.split('\n')[-1]]
            print(f"✓ Cell #{i} diperbaiki: mengganti pd.read_csv dengan pd.read_excel")

if not found:
    print("⚠ Cell dengan pd.read_csv('diabetes.xls') tidak ditemukan")
else:
    # Simpan kembali
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    print(f"✓ File notebook berhasil disimpan")
    print(f"✓ Error UnicodeDecodeError sudah diperbaiki!")

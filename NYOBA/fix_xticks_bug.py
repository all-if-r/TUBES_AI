import json
import sys

notebook_path = r'c:\Users\alifr\Documents\COOLYEAH TELKOM\SEMESTER 5\KECERDASAN ARTIFISIAL\TUBES AI\TUBES_AI\NYOBA\LogisticRegressionManual_Pima.ipynb'

print(f"Membaca file: {notebook_path}")
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Cari cell dengan set_xticks(x_pos[0]) error
found = False
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        
        # Cari cell yang berisi error
        if 'ax.set_xticks(x_pos[0])' in source:
            print(f"✓ Menemukan cell #{i} dengan error")
            
            # Fix: ubah np.arange(2) -> np.array([0])
            new_source = source.replace(
                'x_pos = np.arange(2)',
                'x_pos = np.array([0])'
            )
            
            # Fix: ubah ax.set_xticks(x_pos[0]) -> ax.set_xticks(x_pos)
            new_source = new_source.replace(
                'ax.set_xticks(x_pos[0])',
                'ax.set_xticks(x_pos)'
            )
            
            cell['source'] = new_source.splitlines(keepends=True)
            print(f"✓ Cell #{i} berhasil diperbaiki")
            found = True

if found:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    print("✓ File notebook berhasil disimpan")
    print("✓ Error set_xticks sudah diperbaiki!")
else:
    print("✗ Tidak menemukan cell dengan error")
    sys.exit(1)

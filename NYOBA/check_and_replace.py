import json

# Read the file
with open('LogisticRegressionManual_Pima_FullTransparent.ipynb', 'r', encoding='utf-8') as f:
    content = f.read()

# Count occurrences before replacement
count1 = content.count('  Epochs: 100\\n')
count2 = content.count('       Epochs      100     1108\\n')
count3 = content.count('LR=0.01, Epochs=100, Threshold=0.5')

print(f'Before replacement:')
print(f'  "  Epochs: 100\\\\n" → {count1} occurrences')
print(f'  "       Epochs      100     1108\\\\n" → {count2} occurrences')
print(f'  "LR=0.01, Epochs=100, Threshold=0.5" → {count3} occurrences')

# Replace
content = content.replace('  Epochs: 100\\n', '  Epochs: 1000\\n')
content = content.replace('       Epochs      100     1108\\n', '       Epochs     1000     1108\\n')
content = content.replace('LR=0.01, Epochs=100, Threshold=0.5', 'LR=0.01, Epochs=1000, Threshold=0.5')

# Verify after replacement
count1_after = content.count('  Epochs: 100\\n')
count2_after = content.count('       Epochs      100     1108\\n')
count3_after = content.count('LR=0.01, Epochs=100, Threshold=0.5')

print(f'\nAfter replacement:')
print(f'  "  Epochs: 100\\n" → {count1_after} occurrences')
print(f'  "       Epochs      100     1108\\n" → {count2_after} occurrences')
print(f'  "LR=0.01, Epochs=100, Threshold=0.5" → {count3_after} occurrences')

# Write the file back
with open('LogisticRegressionManual_Pima_FullTransparent.ipynb', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n✓ File updated successfully!')
print(f'  - Replaced {count1} occurrences of "  Epochs: 100"')
print(f'  - Replaced {count2} occurrences of "       Epochs      100     1108"')
print(f'  - Replaced {count3} occurrences of "Epochs=100" in baseline context')

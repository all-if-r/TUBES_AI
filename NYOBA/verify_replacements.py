with open('LogisticRegressionManual_Pima_FullTransparent.ipynb', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for the replaced values
count1 = content.count('  Epochs: 1000\\n')
count2 = content.count('       Epochs     1000     1108\\n')
count3 = content.count('LR=0.01, Epochs=1000, Threshold=0.5')
count4 = content.count('baseline_epochs = 1000')

# Check that old values are gone
old1 = content.count('  Epochs: 100\\n')
old2 = content.count('       Epochs      100     1108\\n')
old3 = content.count('LR=0.01, Epochs=100, Threshold=0.5')

print('Verification of replacements:')
print(f'New values found:')
print(f'  "  Epochs: 1000" → {count1} occurrences')
print(f'  "       Epochs     1000     1108" → {count2} occurrences')
print(f'  "LR=0.01, Epochs=1000, Threshold=0.5" → {count3} occurrences')
print(f'  "baseline_epochs = 1000" → {count4} occurrences')
print()
print(f'Old values remaining:')
print(f'  "  Epochs: 100" → {old1} occurrences')
print(f'  "       Epochs      100     1108" → {old2} occurrences')
print(f'  "LR=0.01, Epochs=100, Threshold=0.5" → {old3} occurrences')
print()
if old1 == 0 and old2 == 0 and old3 == 0:
    print('✓ All replacements completed successfully!')
else:
    print('Warning: Some old values remain')

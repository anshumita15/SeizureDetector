import csv, sys
import numpy as np

filename = sys.argv[1]
mags = []
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        x, y, z = float(row[1]), float(row[2]), float(row[3])
        mags.append(np.sqrt(x**2 + y**2 + z**2))

mags = np.array(mags)
print(f"{filename}:")
print(f"  samples: {len(mags)}")
print(f"  mean: {mags.mean():.3f}")
print(f"  std:  {mags.std():.3f}")
print(f"  min:  {mags.min():.3f}  max: {mags.max():.3f}")
import pikepdf
import os

proj = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src = os.path.join(proj, 'cvv.pdf')
dst = os.path.join(proj, 'cvv_unlocked.pdf')

try:
    # try opening with owner password used earlier
    pdf = pikepdf.Pdf.open(src, password='ownerpass')
except Exception as e:
    # try opening without password
    pdf = pikepdf.Pdf.open(src)

# save without encryption (removes permission flags)
pdf.save(dst)
print('Saved unlocked PDF to', dst)

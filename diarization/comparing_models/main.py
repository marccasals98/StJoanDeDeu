import simpleder
from label_studio import label_studio_info
from pyannote_conversion import pyannote_info
from whisperX_conversion import whisperX_info

# maybe simpleder needs to be installed manually !

ref = label_studio_info()
hyp = pyannote_info()

error = simpleder.DER(ref, hyp)

print("DER={:.3f}".format(error))







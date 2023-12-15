import json
from pyannote.core import Annotation, Segment
from pyannote.metrics.diarization import DiarizationErrorRate
from config import PATHS
from label_studio import label_studio_info
from pyannote_conversion import pyannote_info
from whisperX_conversion import whisperX_info

# Create the references:
ref = Annotation()
hyp = Annotation()

# Import the references as list.
ref_list = label_studio_info()
hyp_list = pyannote_info()

for reference in ref_list:
    ref[Segment(reference[1], reference[2])] = reference[0]

for hyphotesis in hyp_list:
    hyp[Segment(hyphotesis[1], hyphotesis[2])] = hyphotesis[0]

"""
# This is the original Abir's version ---------------------------------------
with open(ref_path, 'r', encoding='utf-8') as file:
        ground_truth = json.load(file)
for item in ground_truth:
        ref[Segment(item['Start'], item['End'])] = item['Speaker']

with open(hyp_path, 'r', encoding='utf-8') as file:
        preds = json.load(file)
for item in preds:
        hyp[Segment(item['start'], item['end'])] = item['speaker']
# ---------------------------------------------------------------------------
"""

diarizationErrorRate = DiarizationErrorRate(skip_overlap=False, collar=0.25)
print("DER: ",diarizationErrorRate(ref, hyp, detailed=True))
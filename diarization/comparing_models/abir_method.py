import json
from pyannote.core import Annotation, Segment
from pyannote.metrics.diarization import DiarizationErrorRate
from config import PATHS

ref = Annotation()
hyp = Annotation()

ref_path = PATHS["ground_truth_simplified"]
hyp_path = PATHS["pyannote_simplified"]


with open(ref_path, 'r', encoding='utf-8') as file:
        ground_truth = json.load(file)
for item in ground_truth:
        ref[Segment(item['Start'], item['End'])] = item['Speaker']

with open(hyp_path, 'r', encoding='utf-8') as file:
        preds = json.load(file)
for item in preds:
        hyp[Segment(item['start'], item['end'])] = item['speaker']

diarizationErrorRate = DiarizationErrorRate(skip_overlap=True)
print("DER: ",diarizationErrorRate(ref, hyp, detailed=True))
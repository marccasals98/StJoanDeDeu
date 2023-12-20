import json
from pyannote.core import Annotation, Segment
from pyannote.metrics.diarization import DiarizationErrorRate
from label_studio import label_studio_info
from pyannote_conversion import pyannote_info
from whisperX_conversion import whisperX_info
from parlament_gt_conversion import parlament_conversion
from plot_diarization import diarization_plot

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

diarizationErrorRate = DiarizationErrorRate(skip_overlap=False, collar=0.0)

diarization_plot(ref=ref_list, hyp=hyp_list)

print("DER: ",diarizationErrorRate(ref, hyp, detailed=True))
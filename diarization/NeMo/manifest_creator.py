import json
"""
This file creates (or updates) the .json for not having to create it manually.
"""
meta = {
    'audio_filepath': "/home/usuaris/veu/marc.casals/943684.wav", 
    'offset': 0, 
    'duration':None, 
    'label': 'infer', 
    'text': '-', 
    'num_speakers': 2, 
    'rttm_filepath': None, 
    'uem_filepath' : None
}
with open('diarization/NeMo/data/input_manifest.json','w') as fp:
    json.dump(meta,fp)
    fp.write('\n')


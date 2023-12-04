from omegaconf import OmegaConf
from settings import PATHS
import os, wget


# CONFIGURATION THINGS (should be put in another file maybe)
ROOT = os.getcwd()
MODEL_CONFIG = os.path.join(PATHS['data_dir'],'diar_infer_telephonic.yaml')
pretrained_speaker_model = 'titanet_large'
pretrained_vad = 'vad_multilingual_marblenet'

if not os.path.exists(MODEL_CONFIG):
    config_url = "https://raw.githubusercontent.com/NVIDIA/NeMo/main/examples/speaker_tasks/diarization/conf/inference/diar_infer_telephonic.yaml"
    MODEL_CONFIG = wget.download(config_url,PATHS['data_dir'])

config = OmegaConf.load(MODEL_CONFIG)
print(OmegaConf.to_yaml(config))    


config.num_workers = 1 # Workaround for multiprocessing hanging with ipython issue 

output_dir = os.path.join(ROOT, 'outputs')
config.diarizer.manifest_filepath = 'diarization/NeMo/data/input_manifest.json'
config.diarizer.out_dir = output_dir #Directory to store intermediate files and prediction outputs

config.diarizer.speaker_embeddings.model_path = pretrained_speaker_model
config.diarizer.oracle_vad = False # compute VAD provided with model_path to vad config
config.diarizer.clustering.parameters.oracle_num_speakers=False

# Here, we use our in-house pretrained NeMo VAD model
config.diarizer.vad.model_path = pretrained_vad
config.diarizer.vad.parameters.onset = 0.8
config.diarizer.vad.parameters.offset = 0.6
config.diarizer.vad.parameters.pad_offset = -0.05


from nemo.collections.asr.models import ClusteringDiarizer
sd_model = ClusteringDiarizer(cfg=config)   
sd_model.diarize()



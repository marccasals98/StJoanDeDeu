from nemo.collections.asr.models import ClusteringDiarizer
from configuration import configure

def main():
    config = configure()
    sd_model = ClusteringDiarizer(cfg=config)   
    sd_model.diarize()


if __name__== "__main__":
    main()
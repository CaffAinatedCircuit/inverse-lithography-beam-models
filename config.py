# config.py
CONFIG = {
    "resolution": 256,
    "beam_counts": [4, 8, 16, 64],
    "epochs": 500,
    "learning_rate": 5e-3,
    "k0": 25.0,
    "device": "cuda"  #cpu if needed al
}
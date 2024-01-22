import torch.nn as nn


class datamodule(nn.Module):
  
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

        for key, value in kwargs.items():
            setattr(self, key, value)

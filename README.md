# Data Modules

Data modules for PyTorch.

```python
from datamodules import datamodule
import torch

class Autoencoder(datamodule):
    encoder: Encoder
    decoder: Decoder

    def forward(self, x: torch.Tensor) -> torch.Tensor

        x = self.encoder(x)
        x = self.decoder(x)

        return x
```

```
autoencoder = Autoencoder(
    encoder=Encoder(...),
    decoder=Decoder(...),
)
```

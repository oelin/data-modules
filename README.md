# datamodules

Data modules for PyTorch 🔥.


## Usage

Define a datamodule.

```python
from datamodules import datamodule

class Autoencoder(datamodule):
    encoder: Encoder
    decoder: Decoder

    def forward(self, x: torch.Tensor) -> torch.Tensor
        x = self.encoder(x)
        x = self.decoder(x)

        return x
```

Initialize it.

```python
autoencoder = Autoencoder(
    encoder=Encoder(...),
    decoder=Decoder(...),
)
```

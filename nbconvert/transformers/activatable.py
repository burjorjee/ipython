from .base import ConfigurableTransformer
from IPython.utils.traitlets import (Bool)

class ActivatableTransformer(ConfigurableTransformer):
    """A simple ConfigurableTransformers that have an enabled flag

    Inherit from that if you just want to have a transformer which is
    no-op by default but can be activated in profiles with

    c.YourTransformerName.enabled = True
    """

    enabled = Bool(True, config=True)

    def __call__(self, nb, other):
        if not self.enabled :
            return nb, other
        else :
            return super(ActivatableTransformer, self).__call__(nb, other)

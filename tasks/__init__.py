from invoke import Collection
from . import dev, test


namespace = Collection(
    dev,
    test,
)

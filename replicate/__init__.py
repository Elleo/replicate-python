from .client import Client

default_client = Client()
models = default_client.models
predictions = default_client.predictions

package_version = None
exec(open('replicate/package_version.py').read())
__version__ = package_version
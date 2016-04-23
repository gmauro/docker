#!/plone/instance/bin/python

import re
import os

class Environment(object):
    """ Configure container via environment variables
    """
    def __init__(self, env=os.environ,
                 zope_conf="/plone/instance/parts/instance/etc/zope.conf",
                 custom_conf="/plone/instance/custom.cfg"):
        self.env = env
        self.zope_conf = zope_conf
        self.custom_conf = custom_conf

    def zeoclient(self):
        """ ZEO Client
        """
        server = self.env.get("ZEO_ADDRESS", None)
        if not server:
            return

        config = ""
        with open(self.zope_conf, "r") as cfile:
            config = cfile.read()

        # Already initialized
        if "<blobstorage>" not in config:
            return

        read_only = self.env.get("ZEO_READ_ONLY", "false")
        zeo_ro_fallback = self.env.get("ZEO_CLIENT_READ_ONLY_FALLBACK", "false")
        shared_blob_dir=self.env.get("ZEO_SHARED_BLOB_DIR", "off")
        zeo_storage=self.env.get("ZEO_STORAGE", "1")
        zeo_client_cache_size=self.env.get("ZEO_CLIENT_CACHE_SIZE", "128MB")
        zeo_conf = ZEO_TEMPLATE.format(
            zeo_address=server,
            read_only=read_only,
            zeo_client_read_only_fallback=zeo_ro_fallback,
            shared_blob_dir=shared_blob_dir,
            zeo_storage=zeo_storage,
            zeo_client_cache_size=zeo_client_cache_size
        )

        pattern = re.compile(r"<blobstorage>.+</blobstorage>", re.DOTALL)
        config = re.sub(pattern, zeo_conf, config)

        with open(self.zope_conf, "w") as cfile:
            cfile.write(config)

    def buildout(self):
        """ Buildout from environment variables
        """
        # Already configured
        if os.path.exists(self.custom_conf):
            return

        eggs = self.env.get("BUILDOUT_EGGS", "").strip().split()
        zcml = self.env.get("BUILDOUT_ZCML", "").strip().split()
        develop = self.env.get("BUILDOUT_DEVELOP", "").strip().split()

        if not (eggs or zcml or develop):
            return

        buildout = BUILDOUT_TEMPLATE.format(
            eggs="\n\t".join(eggs),
            zcml="\n\t".join(zcml),
            develop="\n\t".join(develop)
        )

        with open(self.custom_conf, 'w') as cfile:
            cfile.write(buildout)

    def setup(self, **kwargs):
        self.buildout()
        self.zeoclient()

    __call__ = setup

ZEO_TEMPLATE = """
    <zeoclient>
      read-only {read_only}
      read-only-fallback {zeo_client_read_only_fallback}
      blob-dir /data/blobstorage
      shared-blob-dir {shared_blob_dir}
      server {zeo_address}
      storage {zeo_storage}
      name zeostorage
      var /plone/instance/parts/instance/var
      cache-size {zeo_client_cache_size}
    </zeoclient>
""".strip()

BUILDOUT_TEMPLATE = """
[buildout]
extends = develop.cfg
develop += {develop}
eggs += {eggs}
zcml += {zcml}
"""

def initialize():
    """ Configure Plone instance as ZEO Client
    """
    environment = Environment()
    environment.setup()

if __name__ == "__main__":
    initialize()

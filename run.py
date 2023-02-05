import logging
import subprocess
import os

from pynecone import pynecone

from pynecone.pynecone import pc


if __name__ == "__main__":
    pc.init()
    pc.run(pynecone.Env.PROD, port=os.environ["PORT"])

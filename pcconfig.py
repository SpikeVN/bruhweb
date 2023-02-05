import os

import pynecone as pc

config = pc.Config(
    api_url="0.0.0.0",
    app_name="pcweb",
    db_url="sqlite:///pynecone.db",
    frontend_packages=[
        "react-confetti",
        "react-colorful",
        "react-copy-to-clipboard",
    ]
)

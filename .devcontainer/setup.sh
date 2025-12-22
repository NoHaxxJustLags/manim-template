#!/bin/bashset -e

apt-get update
apt-get install -y --no-install-recommends curl ca-certificates

curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

uv sync

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'source .venv/bin/activate' >> ~/.bashrc
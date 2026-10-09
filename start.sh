set -e
cd "$(dirname "$0")"

echo "Starting Geospatial File Measurement API..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment"
    python3 -m venv .venv
fi

echo "Activating virtual environment"
source .venv/bin/activate

echo "Installing requirements"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Tables are created automatically on startup (see lifespan in app/main.py)
echo "Starting FastAPI server at http://127.0.0.1:8000 (docs at /docs)"
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

# pip freeze >> requirements.txt
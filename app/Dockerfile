# Layers will be ordered from least frequently changed to most frequently changed to re-use as much cached information as possible
# --------------------------------------------------------------------------------------------------------------------------------

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# 1st . is source (app/) 2nd . is destination (/app within the container)
COPY . .

# host 0.0.0.0 to listen all all interfaces, not only localhost
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
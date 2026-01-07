FROM python:3.11-slim

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Cloud Run provides $PORT
ENV PORT=8080

# Streamlit needs to listen on 0.0.0.0 and use the provided port
CMD ["bash", "-lc", "streamlit run streamlit_app.py --server.address=0.0.0.0 --server.port=$PORT --server.headless=true"]

# Use an appropriate base image for 32-bit systems
FROM i386/python:3.8

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Rust (required for compiling bcrypt)
# Note: The installation commands below are based on the standard rustup installation
# and might need adjustments for the specific architecture or OS version.
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Update pip and setuptools
RUN pip install --upgrade pip setuptools

# Rest of your Dockerfile
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV NAME World
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

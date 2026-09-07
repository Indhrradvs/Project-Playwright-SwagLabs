# Playwright's official image - already has Python + all 3 browsers pre-installed
FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

# Set the working folder inside the container
WORKDIR /app

# Copy just requirements.txt first (explained below, why separately)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install wget, unzip, and Java (Java required for Allure report generation)
RUN apt-get update && apt-get install -y wget unzip default-jre

# Install Allure CLI (same approach as CI workflow)
RUN ALLURE_VERSION=2.25.0 && \
    wget -qO /tmp/allure.zip "https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.zip" && \
    unzip -q /tmp/allure.zip -d /opt/ && \
    ln -sf "/opt/allure-${ALLURE_VERSION}/bin/allure" /usr/local/bin/allure && \
    chmod +x /usr/local/bin/allure

# Now copy the rest of the project code
COPY . .

# Default command - runs when the container starts
CMD ["pytest"]
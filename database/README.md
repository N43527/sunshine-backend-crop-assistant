# Database Connection Setup

## Prerequisites

To connect to Azure SQL Database using pyodbc, you need to install the Microsoft ODBC Driver for SQL Server on your system.

## Installation Steps

### 1. Install unixODBC

```bash
sudo apt-get update
sudo apt-get install unixodbc-dev
```

### 2. Add Microsoft Repository

Add the GPG key:
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
```

Add the repository (for Ubuntu 24.04):
```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/ubuntu/24.04/prod noble main" | sudo tee /etc/apt/sources.list.d/mssql-release.list
```

### 3. Install ODBC Driver 18 for SQL Server

```bash
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```

## Running the Connection Test

Make sure you're using the project's virtual environment:

```bash
pyenv activate .venv
python database/connect.py
```

If successful, you should see:
```
Connected!
```

## Troubleshooting

- **Error: `libodbc.so.2: cannot open shared object file`**
  - Solution: Install `unixodbc-dev` package

- **Error: `Can't open lib 'ODBC Driver 18 for SQL Server'`**
  - Solution: Install `msodbcsql18` package following the steps above

- **Error: `ModuleNotFoundError: No module named 'pyodbc'`**
  - Solution: Activate the virtual environment and ensure `pyodbc` is installed via `pip install -r requirements.txt`

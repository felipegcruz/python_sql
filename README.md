# Python and MySQL Integration

This repository provides an example of how to integrate Python with MySQL for database interactions. The example includes connecting to a MySQL database, querying data, and exporting data to a CSV file.

## Prerequisites

- Python 3.x installed on your machine
- MySQL server installed and running
- `mysql-connector-python` library installed (`pip install mysql-connector-python`)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python-mysql-integration.git
   cd python-mysql-integration
   ```

2. Install required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Update MySQL connection details:

   Open the script (`script.py`) and update the following variables with your MySQL server details:

   ```python
   host = "your_mysql_host"
   user = "your_mysql_username"
   password = "your_mysql_password"
   database = "your_database_name"
   ```

## Usage

Run the script to connect to MySQL, fetch data, and export it to a CSV file:

```bash
python script.py
```

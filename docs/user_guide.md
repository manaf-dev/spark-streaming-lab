# User Guide: Real-Time Data Pipeline

This guide provides step-by-step instructions to set up and run the real-time e-commerce data pipeline.

## Prerequisites

### Required Software
- **Docker**: Version 29.0 or higher
- **Git**: For cloning the repository

### System Requirements
- **RAM**: Minimum 8GB
- **CPU**: 4+ cores
- **Disk Space**: 50GB free space
- **OS**: Linux, macOS, or Windows with WSL2

### Verify Prerequisites

```bash
# Check Docker
docker --version

# Check Git
git --version

```


### 1. Initial Setup

#### Clone/Download Project
```bash
# If using git
git clone https://github.com/manaf-dev/spark-streaming-lab.git
cd spark-streaming-lab
```

#### Create an Environment Variable File
Open the project in your preferred text editor and create a `.env` file in the root directory.
Copy the details from `postgres_connection_details.txt` into the `.env` file.


### 2. Start Pipeline

#### Start All Services
```bash
docker compose up -d
```

#### Wait for Services to Initialize
PostgreSQL may take 30-60 seconds to fully initialize on first run.

```bash
# Confirm services are up
docker compose ps

# You should see the following services:
- db
- streaming_app
- events_app
```

#### View Service Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f spark_app
docker compose logs -f events_app
docker compose logs -f db
```

### 3. Access Service UIs

#### Spark Master UI
- View Spark Application UI: http://localhost:4040
- View the jobs completed under the Jobs tab.
- View the jobs' metrics

#### PostgreSQL (via CLI)
```bash
# Connect to PostgreSQL
docker compose exec db psql -U spark_user -d spark_db

# Connect to spark database
\c spark_db

# Query the database
SELECT * FROM user_events LIMIT 10;

SELECT COUNT(*) FROM user_events;

# Count events by type
SELECT event_type, COUNT(*) FROM user_events GROUP BY event_type;

# Query purchase analytics view
SELECT * FROM purchase_analytics LIMIT 5;

# User activity summary
SELECT * FROM user_activity_summary LIMIT 10;

# Exit
exit

```

### 4. Stop the Pipeline

#### Stop All Services
```bash
docker compose down -v
```


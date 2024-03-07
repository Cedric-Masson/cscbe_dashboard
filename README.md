<img src="https://i.ibb.co/X3hvFwF/CSCBE-2.png" alt="CSCBE Dashboard" height="120" />

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Overview

<img src="https://i.ibb.co/s97sYJN/image-psd.png" alt="Dashboard Overview" />



The **Cyber Security Challenge Belgium 2024 Dashboard** is a comprehensive tool designed to **visualize scores and metrics for participants** in the [Cyber Security Challenge Belgium](https://www.cybersecuritychallenge.be/). 

This project utilizes Docker to containerize and manage its multi-component setup, which includes:

- **[PostgreSQL](https://www.postgresql.org/)**: A robust and powerful database system used for storing challenge data.
- **[Python Scraper](https://www.python.org/)**: A custom Python application designed to scrape and process data related to the challenge, feeding it into the PostgreSQL database.
- **[Grafana](https://grafana.com/)**: An open-source platform for monitoring and observability, configured here to visualize the data stored in PostgreSQL through dashboards.



## Prerequisites

Before you begin, ensure you have Docker and Docker Compose installed on your machine. Instructions for installation can be found on the [official Docker documentation](https://docs.docker.com/get-docker/).

## Configuration

1. **Environment Variables**: Edit the `.env` file and fill in the values for the PostgreSQL and Grafana configurations.
    ```
    POSTGRES_USER=changeme
    POSTGRES_PASSWORD=changeme
    POSTGRES_DB=cscbe_db
   
    GRAFANA_USER=changeme
    GRAFANA_PASSWORD=changeme
    ```
    Modify the values accordingly to secure your setup.


2. **Volumes**: The Docker Compose configuration includes named volumes for PostgreSQL and Grafana to ensure data persistence. No additional setup is required for these.


3. **Customization**: You can customize the Grafana dashboards and data sources by modifying the files located in `./grafana/dashboards`, `./grafana/dashboard.yaml`, and `./grafana/datasources.yaml`.

## Running the Project

To start the project, navigate to the root directory of this repository in your terminal and run:

```bash
docker compose up -d
```

## Accessing Grafana

Once the containers are up and running, Grafana will be accessible at http://localhost:3000. Log in with the credentials you specified in your .env file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue or a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
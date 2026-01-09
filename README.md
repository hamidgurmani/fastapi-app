🚀 FastAPI Application with Docker, PostgreSQL & Nginx (HTTPS)

This project demonstrates a real-world containerized backend architecture using Docker and Docker Compose.

🔧 Tech Stack

FastAPI – Python web framework

PostgreSQL – Relational database

Nginx – Reverse proxy with HTTPS

Docker & Docker Compose – Container orchestration

Client (Browser)
      |
      | HTTPS (443)
      v
   Nginx (Reverse Proxy)
      |
      | Internal Docker Network
      v
 FastAPI Application (8000)
      |
      v
 PostgreSQL Database (5432)

✨ Key Features

Multi-container setup using Docker Compose

Nginx reverse proxy with TLS/HTTPS

Secure internal service-to-service communication

Health checks for application and database

Production-style container networking

Persistent database storage using Docker volumes

Access:

HTTPS App: https://<EC2_PUBLIC_IP>

Health Check: https://<EC2_PUBLIC_IP>/health

⚠️ Note: A self-signed SSL certificate is used. Browser warning is expected.

fastapi-app/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
├── nginx/
│   ├── nginx.conf
│   └── ssl/
│       ├── server.crt
│       └── server.key
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
└── README.md

🎯 What This Project Demonstrates

This setup reflects how backend services are deployed in real production environments, where:

Applications are not directly exposed

Traffic is routed via a secure reverse proxy

Containers communicate over isolated networks

Security and reliability are first-class concerns



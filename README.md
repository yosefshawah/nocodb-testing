# 🚀 NocoDB Testing Project

[![CI/CD Pipeline](https://github.com/yosefshawah/nocodb-testing/actions/workflows/deploy.yaml/badge.svg)](https://github.com/yosefshawah/nocodb-testing/actions/workflows/deploy.yaml)
[![UI Tests](https://github.com/yosefshawah/nocodb-testing/actions/workflows/ui-testing.yaml/badge.svg)](https://github.com/yosefshawah/nocodb-testing/actions/workflows/ui-testing.yaml)
[![API Tests](https://github.com/yosefshawah/nocodb-testing/actions/workflows/tests.yaml/badge.svg)](https://github.com/yosefshawah/nocodb-testing/actions/workflows/tests.yaml)

A comprehensive testing and deployment project for NocoDB, featuring automated CI/CD pipelines, API testing, and UI testing capabilities.

## 📋 What is NocoDB?

**NocoDB** is an open-source Airtable alternative that turns any MySQL, PostgreSQL, SQL Server, SQLite, or MariaDB into a smart spreadsheet and database. It provides:

- 🔧 **No-Code Database Builder**: Create databases without writing code
- 📊 **Smart Spreadsheet Interface**: Familiar spreadsheet-like interface for data management
- 🔗 **API Generation**: Automatically generates REST APIs for your data
- 👥 **Team Collaboration**: Real-time collaboration features
- 🔐 **Role-Based Access Control**: Secure access management
- 🌐 **Webhooks & Integrations**: Connect with external services

## 🏗️ Project Structure

```
nocodb-testing/
├── 📁 .github/workflows/          # GitHub Actions CI/CD pipelines
│   ├── deploy.yaml               # Automated deployment to EC2
│   ├── tests.yaml                # API testing workflow
│   └── ui-testing.yaml           # Selenium UI testing workflow
├── 📁 dummy-db/                  # Sample data for testing
│   ├── departments.csv           # Department data
│   └── employees.csv             # Employee data
├── 📁 tests/                     # Test files
│   └── test_api.py              # API endpoint tests
├── 📄 docker-compose.yml         # Docker configuration for NocoDB
├── 📄 requirements.txt           # Python dependencies
└── 📄 README.md                  # This file
```

## 🚀 Features

### 🔄 Automated Deployment

- **GitHub Actions Pipeline**: Automatic deployment to EC2 on push to main branch
- **Docker Integration**: Containerized NocoDB deployment
- **Zero-Downtime Updates**: Seamless deployment process

### 🧪 Testing Suite

- **API Testing**: Automated testing of NocoDB REST endpoints
- **UI Testing**: Selenium-based user interface testing
- **Health Checks**: Server availability and response validation

### 📊 Sample Data

- **Pre-loaded Datasets**: Departments and employees data for testing
- **CSV Import Ready**: Structured data for quick setup

## 🛠️ Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.11+
- Git

### Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yosefshawah/nocodb-testing.git
   cd nocodb-testing
   ```

2. **Start NocoDB with Docker**

   ```bash
   docker-compose up -d
   ```

3. **Access NocoDB**

   - Open your browser and go to `http://localhost:8080`
   - Default admin credentials:
     - Email: `admin@example.com`
     - Password: `12341234`

4. **Run API Tests**
   ```bash
   pip install -r requirements.txt
   pytest tests/ -v
   ```

## 🔧 Configuration

### Environment Variables

The project uses the following environment variables:

- `NC_ADMIN_EMAIL`: Admin email for NocoDB (default: admin@example.com)
- `NC_ADMIN_PASSWORD`: Admin password (default: 12341234)
- `OLLAMA_URL`: External service URL for testing

### Docker Configuration

The `docker-compose.yml` file configures:

- NocoDB service on port 8080
- Persistent data storage in `./nocodb/`
- Automatic restart policy

## 🧪 Testing

### API Tests

```bash
# Run all API tests
pytest tests/ -v

# Run specific test file
pytest tests/test_api.py -v
```

### UI Tests

UI tests are configured to run in GitHub Actions with:

- Headless Chrome browser
- Xvfb for display management
- Automated cleanup of browser processes

## 🚀 Deployment

### Automated Deployment

The project includes automated deployment to EC2 via GitHub Actions:

1. **Push to main branch** triggers deployment
2. **SSH connection** to EC2 instance
3. **Docker Compose** updates and restarts services
4. **Health checks** verify successful deployment

### Manual Deployment

```bash
# SSH to your EC2 instance
ssh ubuntu@your-ec2-ip

# Navigate to project directory
cd ~/nocodb-testing

# Pull latest changes
git pull

# Restart services
docker-compose down
docker-compose up -d
```

## 📊 Monitoring

### Health Checks

- **Server Status**: Automated health checks in CI/CD pipeline
- **Response Validation**: API endpoint response validation
- **Error Logging**: Comprehensive error tracking

### Performance

- **Docker Optimization**: Optimized container configuration
- **Resource Management**: Efficient memory and CPU usage
- **Scalability**: Ready for horizontal scaling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [NocoDB Documentation](https://docs.nocodb.com/)
- [NocoDB GitHub](https://github.com/nocodb/nocodb)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Made with ❤️ for efficient database management and testing**

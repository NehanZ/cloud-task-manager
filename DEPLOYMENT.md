## AWS Architecture Overview

This application is designed to run on AWS with the following architecture:

- **Frontend**: Next.js app served via CloudFront + S3
- **Backend**: FastAPI running on EC2
- **Database**: AWS RDS PostgreSQL
- **Container Registry**: AWS ECR (Public)

## Environment Configuration

### 1. Backend Production Environment

Update `backend/.env.production` with your actual AWS RDS credentials:

```bash
NODE_ENV=production
DATABASE_URL=postgresql://your-username:your-password@your-rds-endpoint.us-east-1.rds.amazonaws.com:5432/tasks
CORS_ORIGINS=https://your-cloudfront-domain.cloudfront.net
API_HOST=0.0.0.0
API_PORT=8000
```

### 2. Frontend Production Environment

Update `frontend/.env.production` with your actual EC2 backend URL:

```bash
NEXT_PUBLIC_API_URL=https://your-ec2-backend-domain.com
NEXT_PUBLIC_ENV=production
```
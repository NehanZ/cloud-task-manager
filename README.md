# 🧩 Cloud Task Manager

A full-stack **Task Management App** built with **FastAPI**, **Next.js**, and **PostgreSQL**, containerized using **Docker Compose** and ready for AWS deployment.

This project is designed as a **DevOps learning project** to practice:
- Containerization (Docker)
- CI/CD
- Cloud deployment (AWS EC2)
- Infrastructure as Code (optional with Terraform)
- Basic monitoring and logs

---

## 🚀 Tech Stack

| Layer | Technology | Description |
|-------|-------------|--------------|
| Frontend | **Next.js (React)** | Responsive UI for managing tasks |
| Backend | **FastAPI (Python)** | REST API for CRUD operations |
| Database | **PostgreSQL 14** | Persistent data storage |
| Containerization | **Docker & Docker Compose** | Multi-container orchestration |
| Deployment | **AWS EC2 / ECS (optional)** | Cloud deployment practice |

---

## 🧱 Project Architecture

```text
cloud-task-manager/
│
├── frontend/           # Next.js app
│   ├── app/            # App router
│   ├── package.json
│   ├── Dockerfile
│
├── backend/            # FastAPI app
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   └── models.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env
│
├── data/
│   └── db/             # Persistent Postgres volume (mounted)
│
├── docker-compose.yml  # Service orchestration
├── README.md
└── .gitignore
```

---

## ⚙️ Environment Variables

Create a `.env` file inside the `backend/` folder:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/tasks
```

---

## 🐳 Run Locally with Docker

1. **Start Docker Desktop**
2. **Run in project root:**

```bash
docker-compose up --build
```

3. **Access the services:**
   - Frontend: http://localhost:3000
   - Backend (FastAPI docs): http://localhost:8000/docs
   - PostgreSQL: port `5432`

4. **Stop services:**

```bash
docker-compose down
```

---

## 🧩 Development Commands (Optional Local Run)

If you want to run without Docker:

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📦 Docker Services

- **db**: PostgreSQL 14 database
- **backend**: FastAPI REST API (port 8000)
- **frontend**: Next.js app (port 3000)

---

## 🛠️ Future Enhancements

- [ ] Add CI/CD pipeline (GitHub Actions)
- [ ] Deploy to AWS EC2
- [ ] Implement Terraform for IaC
- [ ] Add monitoring (Prometheus/Grafana)
- [ ] Add authentication (JWT)

---
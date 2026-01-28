# Hackathon II Phase IV - Full-Stack Todo Web Application with AI Chatbot (Kubernetes Deployment)

A comprehensive full-stack todo application featuring Next.js frontend, FastAPI backend, and an intelligent AI chatbot for natural language task management. This application combines traditional task management with cutting-edge AI capabilities to provide an intuitive user experience. Deployed on Kubernetes using Minikube and Helm charts for container orchestration.

## 🌟 Key Features

### Core Functionality
- **Full-stack web application** with Next.js 16+ frontend and FastAPI backend
- **User authentication and authorization** with JWT tokens
- **CRUD operations** for todo tasks with comprehensive validation
- **User isolation** - users can only access their own tasks
- **Responsive UI** with Tailwind CSS styling and dark mode support

### AI-Powered Assistant
- **Natural Language Processing** with Google's Gemini AI model
- **Intelligent Task Management** - create, update, complete, and delete tasks using conversational commands
- **Context-Aware Interactions** with conversation history persistence
- **Smart Task Recognition** that understands various command formats

### Advanced Capabilities
- **MCP (Model Context Protocol) Integration** for standardized tool interactions
- **Real-time Task Syncing** across all application views
- **Cross-Platform Compatibility** with responsive design
- **Secure Authentication** with Better Auth integration

### Phase IV: Kubernetes Deployment
- **Container Orchestration** with Kubernetes on Minikube
- **Helm Chart Package Management** for easy deployment
- **Service Accounts Configuration** for secure pod communication
- **Load Balancing** with Kubernetes Services
- **Health Checks** with liveness and readiness probes
- **Scalability** with horizontal pod autoscaling

## 🏗️ Architecture

The application follows a modern microservices architecture deployed on Kubernetes:

- `frontend/`: Next.js 16+ frontend with App Router, Tailwind CSS, and Better Auth
- `backend/`: FastAPI backend with SQLModel ORM, JWT authentication, and AI integration
- `charts/`: Helm charts for Kubernetes deployment
- `specs/`: Specification files and project documentation
- `src/`: Source code for AI agents and core services
- `history/`: Historical records and project evolution

### Tech Stack
- **Frontend**: Next.js 16+, React, TypeScript, Tailwind CSS
- **Backend**: Python, FastAPI, SQLModel, Pydantic
- **Database**: PostgreSQL (with Neon compatibility)
- **Authentication**: Better Auth with JWT tokens
- **AI Services**: Google Gemini via OpenAI-compatible API
- **Containerization**: Docker for container packaging
- **Orchestration**: Kubernetes with Minikube for local deployment
- **Package Management**: Helm for Kubernetes manifests
- **State Management**: Client-side with React hooks
- **Styling**: Tailwind CSS with custom components

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- Docker Desktop
- Minikube
- Helm 3+
- PostgreSQL database (or Neon for cloud deployment)
- Google Gemini API key

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/nishanazar/Hackathon-II-Phase-III-Todo-Full-Stack-Web-Application_with_chat_bot.git
   cd Hackathon-II-Phase-III-Todo-Full-Stack-Web-Application_with_chat_bot
   ```

2. **Setup Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Setup Frontend**:
   ```bash
   cd ../frontend
   npm install
   ```

4. **Configure Environment Variables**:

   Backend (.env):
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   BETTER_AUTH_SECRET=your_secret_key
   DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
   ```

   Frontend (.env.local):
   ```env
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

5. **Terminal 1 - Start the backend**:
   ```bash
   cd ../backend
   uvicorn main:app --reload --port 8000
   ```

6. **Terminal 2 - Start the frontend**:
   ```bash
   cd ../frontend
   npm run dev
   ```

The frontend will be available at http://localhost:3000
The backend API will be available at http://localhost:8000

## 🚢 Kubernetes Deployment

### Prerequisites for Kubernetes Deployment
- Docker Desktop with Kubernetes disabled (we'll use Minikube)
- Minikube installed
- Helm 3+ installed
- kubectl installed

### Setting up Minikube

1. **Start Minikube**:
   ```bash
   minikube start
   ```

2. **Enable Docker environment for Minikube**:
   ```bash
   @FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env --shell cmd') DO @%i
   ```

### Building Docker Images

1. **Build the backend image**:
   ```bash
   docker build -t todo-backend:latest ./backend
   ```

2. **Build the frontend image**:
   ```bash
   docker build -t todo-frontend:latest ./frontend
   ```

### Deploying with Helm

1. **Install/Upgrade the Helm chart**:
   ```bash
   helm upgrade --install todo ./charts/todo-app --set frontend.image.pullPolicy=IfNotPresent --set backend.image.pullPolicy=IfNotPresent
   ```

2. **Create required service accounts** (if not defined in Helm chart):
   ```bash
   kubectl create serviceaccount todo-todo-app-backend
   kubectl create serviceaccount todo-todo-app-frontend
   ```

3. **Restart deployments to apply changes**:
   ```bash
   kubectl rollout restart deployment todo-todo-app-backend
   kubectl rollout restart deployment todo-todo-app-frontend
   ```

### Accessing the Application

#### Option 1: Port Forwarding (Recommended for local development)
1. **Forward frontend port**:
   ```bash
   kubectl port-forward service/todo-todo-app-frontend 3000:3000
   ```

2. **Forward backend port**:
   ```bash
   kubectl port-forward service/todo-todo-app-backend 8000:8000
   ```

3. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend health check: http://localhost:8000/health

#### Option 2: Using Minikube Service (Alternative)
1. **Open the frontend in browser**:
   ```bash
   minikube service todo-todo-app-frontend
   ```

### Verifying the Deployment

1. **Check all resources**:
   ```bash
   kubectl get all
   ```

2. **Check deployment status**:
   ```bash
   kubectl get deployments
   ```

3. **Check pods status**:
   ```bash
   kubectl get pods
   ```

4. **Check services**:
   ```bash
   kubectl get services
   ```

5. **Check logs of the pods**:
   ```bash
   kubectl logs -l app.kubernetes.io/component=frontend
   kubectl logs -l app.kubernetes.io/component=backend
   ```

### Troubleshooting Common Issues

1. **Pods not starting**:
   - Check if service accounts exist: `kubectl get serviceaccounts`
   - Verify image pull policy is set correctly
   - Check pod events: `kubectl describe pod <pod-name>`

2. **Application not accessible**:
   - Ensure port forwarding is active
   - Check firewall settings
   - Verify service configurations

3. **Environment variables not applied**:
   - Update deployment environment variables: `kubectl set env deployment/<deployment-name> KEY=VALUE`
   - Restart deployment: `kubectl rollout restart deployment/<deployment-name>`

## 🤖 AI Chatbot Capabilities

The integrated AI assistant supports natural language commands:

- **Task Creation**: "Add a task to buy groceries" or "Create a task to call mom"
- **Task Listing**: "Show my tasks" or "What do I have to do?"
- **Task Completion**: "Complete the grocery task" or "Mark 'buy groceries' as done"
- **Task Updates**: "Update 'grocery' to 'buy organic groceries'" or "Change description of task X"
- **Task Deletion**: "Delete the meeting task" or "Remove 'schedule meeting'"

The AI agent intelligently parses these commands and executes the appropriate backend operations.

## 🔐 Security Features

- JWT-based authentication with secure token handling
- User isolation with strict access controls
- Input validation and sanitization
- Secure API communication with HTTPS enforcement
- Role-based access control
- Kubernetes RBAC with service accounts

## 🧪 Testing

### Backend Testing
```bash
cd backend
pytest tests/ -v
```

### Frontend Testing
```bash
cd frontend
npm test
```

### Kubernetes Deployment Verification
```bash
# Run the verification script
bash verify_deployment.sh
```

## 📊 API Endpoints

### Task Management
- `GET /api/{user_id}/tasks` - List all tasks for the authenticated user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task completely
- `PATCH /api/{user_id}/tasks/{id}` - Partially update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task

### AI Chat Interface
- `POST /api/{user_id}/chat` - Natural language task management

### Health Check
- `GET /health` - Health check endpoint

## 🚢 Production Deployment

### Helm Chart Customization

The Helm chart in `charts/todo-app` can be customized with the following values:

```yaml
frontend:
  enabled: true
  image:
    repository: todo-frontend
    tag: "latest"
    pullPolicy: IfNotPresent
  service:
    type: ClusterIP
    port: 3000
  replicaCount: 1
  resources:
    requests:
      memory: "128Mi"
      cpu: "100m"
    limits:
      memory: "256Mi"
      cpu: "200m"

backend:
  enabled: true
  image:
    repository: todo-backend
    tag: "latest"
    pullPolicy: IfNotPresent
  service:
    type: ClusterIP
    port: 8000
  replicaCount: 1
  resources:
    requests:
      memory: "128Mi"
      cpu: "100m"
    limits:
      memory: "512Mi"
      cpu: "500m"
```

### Scaling the Application

To scale the application based on demand:

```bash
# Scale frontend replicas
kubectl scale deployment todo-todo-app-frontend --replicas=3

# Scale backend replicas
kubectl scale deployment todo-todo-app-backend --replicas=2
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Docker Containerization

This project includes Docker containerization for both frontend and backend applications.

### Prerequisites

- Docker Desktop installed
- Docker BuildKit enabled (recommended)

### Building the Images

To build the frontend and backend images separately:

```bash
# Build frontend image
cd frontend
docker build -t todo-frontend:latest .

# Build backend image
cd backend
docker build -t todo-backend:latest .
```

### Running with Docker Compose (Development)

For development purposes, use Docker Compose to run both services:

```bash
# Run in development mode (with live reload)
docker-compose up

# Run in detached mode
docker-compose up -d
```

### Running with Docker Compose (Production)

For production-like environment:

```bash
# Build and run production images
docker-compose -f docker-compose.prod.yml up --build

# Run in detached mode
docker-compose -f docker-compose.prod.yml up -d --build
```

### Running Individual Containers

After building the images, you can run them individually:

```bash
# Run frontend container
docker run -p 3000:3000 todo-frontend:latest

# Run backend container
docker run -p 8000:8000 todo-backend:latest
```

### Environment Variables

The containers support the following environment variables:

- `GEMINI_API_KEY`: API key for Gemini integration
- `DATABASE_URL`: Connection string for Neon PostgreSQL
- `BETTER_AUTH_SECRET`: Secret for JWT token signing

You can pass these when running the containers:

```bash
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your_key \
  -e DATABASE_URL=your_db_url \
  -e BETTER_AUTH_SECRET=your_secret \
  todo-backend:latest
```

## 🙏 Acknowledgments

- Built with Next.js and FastAPI for optimal developer experience
- Powered by Google's Gemini AI for intelligent task management
- Designed with accessibility and user experience in mind
- Developed using Spec-Driven Development methodology
- Kubernetes deployment with Helm for scalable infrastructure
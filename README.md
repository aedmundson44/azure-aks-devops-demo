# azure-aks-devops-demo

An end-to-end DevOps project: a containerized Python (FastAPI) API deployed to **Azure Kubernetes Service (AKS)**, with infrastructure defined in **Terraform** and build/deploy automated through a **CI/CD pipeline**.

Built as a hands-on learning project to practice the full path from code to a running, self-healing service in the cloud.

## Architecture (target)

```
Developer ──PR──> GitHub ──Actions──> Build & test ──> Azure Container Registry (ACR)
                                                              │
                                                              ▼
                                   Azure Kubernetes Service (AKS) ──> Service (LoadBalancer) ──> Users

Terraform ──> provisions ACR + AKS     (state stored remotely in Azure Storage)
```

## Tech stack

| Area | Tools |
|---|---|
| Application | Python 3.12, FastAPI, Uvicorn |
| Containers | Docker |
| Infrastructure as Code | Terraform (azurerm provider ~> 4.0), remote state in Azure Blob Storage |
| Cloud | Azure: Resource Groups, Storage, ACR, AKS |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |

## API endpoints

| Endpoint | Purpose |
|---|---|
| `GET /` | App name and version |
| `GET /health` | Health check used by Kubernetes liveness/readiness probes |
| `GET /info` | Hostname of the container serving the request (shows load balancing across pods) |

## Repository layout

```
app/
  main.py               FastAPI application
  requirements.txt      Python dependencies
Dockerfile              Container image definition
terraform/
  bootstrap/            Remote state backend (resource group, storage account, container)
```

## Run locally

With Docker:

```bash
docker build -t aks-demo .
docker run -p 8000:8000 aks-demo
```

Then open http://localhost:8000/info (interactive docs at http://localhost:8000/docs).

Without Docker:

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload
```

## Terraform remote state

`terraform/bootstrap` creates the backend that stores Terraform state for the rest of the project:

- Resource group: `rg-tfstate`
- Storage account: `asartfstate2026`
- Private blob container: `tfstate`

Keeping the state in Azure Storage, rather than on a laptop, makes it shareable and lockable. It's also safe to use from a CI/CD pipeline.

## Roadmap

- [x] FastAPI app with health and info endpoints
- [x] Dockerfile
- [x] Terraform remote state backend
- [ ] Unit tests and repo cleanup
- [ ] Terraform: Azure Container Registry + AKS cluster
- [ ] Kubernetes manifests (Deployment, Service, health probes)
- [ ] CI: tests, image build, and Terraform checks on every pull request
- [ ] CD: build, push to ACR, and deploy to AKS on merge to `main` using OIDC (no stored secrets)
- [ ] Monitoring and final write-up

## Cost note

AKS nodes bill hourly. Cluster infrastructure is destroyed between work sessions (`terraform destroy`); only the low-cost state storage is kept running.

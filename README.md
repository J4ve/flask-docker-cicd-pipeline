# flask-docker-cicd-pipeline

[![CI](https://github.com/J4ve/flask-docker-cicd-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/J4ve/flask-docker-cicd-pipeline/actions/workflows/ci.yml)

A small Flask web service used to build a CI/CD pipeline with GitHub Actions. Every push to `main` runs the tests, builds a Docker image, and deploys the app to a remote server over SSH. This repository was formerly named `se2-finalLT`.

The app has one route: `GET /` returns `Hello, World!`. The focus of the project is the pipeline around it.

## Methodology

The pipeline is defined in `.github/workflows/ci.yml`. It runs on every push and pull request to `main`, and can also be started by hand (`workflow_dispatch`). It has three jobs, and each one starts only if the one before it succeeded.

1. **build (tests).** Sets up Python 3.11, installs `requirements.txt` (`flask==3.0.0`, `pytest==8.0.0`) and runs `pytest -v`.
2. **docker.** Builds the image from the `Dockerfile` with Docker Buildx, tagged with the commit SHA (`se2-finallt:<sha>`).
3. **deploy.** Runs only on a push to `main`. It logs in to the server with `appleboy/ssh-action` using the `SSH_HOST`, `SSH_USER` and `SSH_PRIVATE_KEY` secrets, pulls the latest code, rebuilds the image and starts the container with `-p 80:5000 --restart unless-stopped`.

The `Dockerfile` starts from `python:3.11-slim`, installs the requirements before copying the source so that layer can be cached, exposes port 5000 and runs `python app.py`.

`test_app.py` uses Flask's test client. `test_hello` checks that `GET /` returns status 200 and the body `Hello, World!`. A commented-out `test_broken`, which expects `Goodbye, World!`, was used to show that a failing test stops the pipeline.

## Results

The full test, build and deploy chain passed on commit `7c97be1` (run 25171927720).

| Commit | Change | Run | Outcome |
|---|---|---|---|
| `7d5c338` | Added the app and tests, with `test_broken` active | [25170835060](https://github.com/J4ve/flask-docker-cicd-pipeline/actions/runs/25170835060) | build failed |
| `fd3b790` | Commented out `test_broken` | [25170942023](https://github.com/J4ve/flask-docker-cicd-pipeline/actions/runs/25170942023) | build passed |
| `2a80cf9` | Added the `Dockerfile` and the docker job | [25171104412](https://github.com/J4ve/flask-docker-cicd-pipeline/actions/runs/25171104412) | build and docker passed |
| `7c97be1` | Added the deploy job | [25171927720](https://github.com/J4ve/flask-docker-cicd-pipeline/actions/runs/25171927720) | build, docker and deploy passed |

- The test gate works. The failing `test_broken` made the build job fail, and commenting it out made it pass on the next commit.
- In run 25171927720 the deploy job failed on its first two attempts and passed on the third.
- The job logs for these runs have expired on GitHub, so only the job outcomes are listed.

## How to run

```bash
pip install -r requirements.txt
pytest -v
python app.py
```

Then open http://localhost:5000. To run it in Docker instead:

```bash
docker build -t se2-finallt .
docker run -d --name se2-finallt -p 5000:5000 se2-finallt
```

To deploy with the pipeline, add the `SSH_HOST`, `SSH_USER` and `SSH_PRIVATE_KEY` secrets for a server that has Git and Docker, then push to `main`.

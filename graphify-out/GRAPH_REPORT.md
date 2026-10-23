# Graph Report - flask-docker-cicd-pipeline  (2026-10-23)

## Corpus Check
- Large corpus: 500 files · ~680,437 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 12 nodes · 15 edges · 3 communities (2 shown, 1 thin omitted)
- Extraction: 73% EXTRACTED · 27% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- app.py
- build job (Python 3.11,
- requirements.txt (flask-docker-cicd-pipeline)

## God Nodes (most connected - your core abstractions)
1. `build job (Python 3.11, pip install -r requirements.txt, pytest -v)` - 4 edges
2. `ci.yml (Flask Docker CI/CD workflow)` - 3 edges
3. `requirements.txt (flask-docker-cicd-pipeline)` - 3 edges
4. `docker job (Buildx build se2-finallt:<sha>)` - 3 edges
5. `deploy job (SSH: git pull, docker build, docker run -p 80:5000)` - 3 edges
6. `hello()` - 2 edges
7. `flask==3.0.0` - 2 edges
8. `pytest==8.0.0` - 2 edges

## Surprising Connections (you probably didn't know these)
- `build job (Python 3.11, pip install -r requirements.txt, pytest -v)` --references--> `requirements.txt (flask-docker-cicd-pipeline)`  [EXTRACTED]
  .github/workflows/ci.yml → requirements.txt

## Import Cycles
- None detected.

## Communities (3 total, 1 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.50
Nodes (3): hello(), flask==3.0.0, route

### Community 1 - "build job (Python 3.11,"
Cohesion: 0.83
Nodes (4): ci.yml (Flask Docker CI/CD workflow), build job (Python 3.11, pip install -r requirements.txt, pytest -v), deploy job (SSH: git pull, docker build, docker run -p 80:5000), docker job (Buildx build se2-finallt:<sha>)

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build job (Python 3.11, pip install -r requirements.txt, pytest -v)` connect `build job (Python 3.11,` to `requirements.txt (flask-docker-cicd-pipeline)`?**
  _High betweenness centrality (0.345) - this node is a cross-community bridge._
- **Why does `requirements.txt (flask-docker-cicd-pipeline)` connect `requirements.txt (flask-docker-cicd-pipeline)` to `app.py`, `build job (Python 3.11,`?**
  _High betweenness centrality (0.256) - this node is a cross-community bridge._
- **Why does `deploy job (SSH: git pull, docker build, docker run -p 80:5000)` connect `build job (Python 3.11,` to `app.py`?**
  _High betweenness centrality (0.218) - this node is a cross-community bridge._
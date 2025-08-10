# Smart_home_vision

SHCSS prototype repository.

This first commit contains:
- Repository skeleton
- Flask-based mock detection endpoint
- Unit test
- GitHub Actions CI

Run locally:
```bash
pip install -r api_server/requirements/base.txt
pip install -r api_server/requirements/dev.txt
pytest
flask --app api_server.app.main run --port 8000


**`LICENSE`** — use MIT .

**`.gitignore`**
```gitignore
__pycache__/
*.py[cod]
.venv/
.env
*.egg-info
dist/
build/
.vscode/
.idea/
.DS_Store
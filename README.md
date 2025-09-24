# AI-SDLC-VISION · Humans as Gatekeepers, AI as Developers

[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-inactive.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A reference blueprint for an AI-accelerated SDLC where humans define intent & guardrails, and AI agents generate stories, code, and tests.

## Why
- **Governed speed**: AI scales delivery; humans approve merges.
- **Repeatability**: standardized story & test patterns.
- **Traceability**: every artifact is reviewable.

## Architecture (high-level)
```mermaid
flowchart LR
  BA[Business Analyst] -->|Requirement| JiraAgent[Jira AI Agent]
  JiraAgent --> Stories[Jira Story]
  Stories --> DevAgent[Developer Agent]
  DevAgent -->|Branch+Code| GitHub[GitHub Repo]
  DevAgent -->|Commit| UnitTestAgent[Unit Testing Agent]
  UnitTestAgent --> Tests[Automated Tests]
  Tests --> CICD[CI/CD Agent]
  GitHub --> CICD
  CICD --> Reports[Test & Coverage]
  CICD --> Gatekeepers[Human Review]
  Gatekeepers -->|Approve| Merge[Release]
```

## Quickstart (local demo)
```bash
uv venv && source .venv/bin/activate  # or python -m venv
pip install -r requirements.txt
pytest -q
```

## Roadmap
- [ ] Minimal Jira/GitHub integration behind feature flags
- [ ] LLM adapters (Bedrock, OpenAI) with offline fallback
- [ ] Golden path: story → branch → code → tests → PR → checks

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). Security policy in [SECURITY.md](SECURITY.md).

<div align="center">
  <img src="docs/assets/logo.svg" alt="CampaignForge" width="480">
  <p><strong>Multi-Agent Marketing Campaign Orchestration Platform</strong></p>
  <p>AI agents for content strategy · copywriting · SEO · social media · performance analysis</p>

  [![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://python.org)
  [![TypeScript](https://img.shields.io/badge/TypeScript-5.4%2B-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  [![CI](https://github.com/Crynge/CampaignForge/actions/workflows/ci.yml/badge.svg)](https://github.com/Crynge/CampaignForge/actions/workflows/ci.yml)
  [![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
  [![GitHub Stars](https://img.shields.io/github/stars/Crynge/CampaignForge?style=social)](https://github.com/Crynge/CampaignForge)

</div>

---

## Overview

CampaignForge orchestrates specialized AI agents to plan, create, optimize, and analyze marketing campaigns. Each agent brings domain expertise — content strategy, copywriting, SEO, social media, and performance analysis — and they collaborate through a central orchestrator.

## Key Features

- **Multi-agent orchestration** — Agents collaborate on campaign lifecycle
- **Content strategy engine** — Data-driven content planning and topic clustering
- **AI copywriting** — On-brand copy generation for all channels
- **SEO analysis** — Keyword research, gap analysis, and optimization
- **Social media management** — Cross-platform posting strategy and scheduling
- **Performance analytics** — Campaign ROI attribution and recommendations

## Architecture

```
User Input → CampaignOrchestrator → ContentStrategist → Copywriter
                                      → SEOAnalyst      → SocialManager
                                                        → PerformanceAnalyst
                                         → Unified Campaign Plan
```

## Quick Start

```bash
pip install -e .
python -m campaignforge plan --brief "Q4 product launch"
```

## Installation

```bash
git clone https://github.com/Crynge/CampaignForge.git
cd CampaignForge
pip install -e ".[dev]"
npm install
```

## Usage

```python
from campaignforge import CampaignOrchestrator

orchestrator = CampaignOrchestrator(
    brand_voice="professional",
    channels=["blog", "twitter", "linkedin", "email"],
    budget=50000
)

campaign = orchestrator.launch(
    name="Q4 Product Launch",
    target_audience="enterprise CTOs",
    key_message="10x productivity with AI",
    timeline="2026-10-01 to 2026-12-31"
)

print(campaign.summary())
```

## Agent Roles

| Agent | Role | Tools |
|-------|------|-------|
| ContentStrategist | Topic research, content calendar, gap analysis | Keyword planner, trend detection |
| Copywriter | Ad copy, email drafts, blog outlines, social posts | Tone analyzer, brand voice DB |
| SEOAnalyst | Keyword optimization, meta tags, internal linking | SERP scraper, rank tracker |
| SocialManager | Post scheduling, platform strategy, engagement plan | Platform APIs, calendar |
| PerformanceAnalyst | ROI tracking, attribution, A/B test recommendations | Analytics connector, reporting |

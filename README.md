[![CI](https://github.com/Crynge/CampaignForge/actions/workflows/ci.yml/badge.svg)](https://github.com/Crynge/CampaignForge/actions/workflows/ci.yml)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6)](https://typescriptlang.org)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB)](https://python.org)

# CampaignForge

**Marketing campaign orchestration dashboard.**

Plan, launch, and optimize multi-channel campaigns through a unified dashboard with AI-powered agents that automate workflows, analyze performance, and suggest optimizations.

---

## Campaign Board

```
┌─────────────────────────────────────────────────────────────────┐
│  CAMPAIGN PIPELINE                                      + New  │
├──────────┬──────────┬──────────┬──────────┬─────────────────────┤
│  DRAFT   │  ACTIVE  │  REVIEW  │ COMPLETE │                     │
├──────────┼──────────┼──────────┼──────────┤                     │
│  ☐ Q3    │  ▶ Summer│  🔍 Email│  ✓ Spring│                     │
│   Launch │   Sale   │   Series │   Launch │                     │
│   Due 8/1│   Live   │   Pending│   Done   │                     │
│          │   ROAS:  │   Rev:   │   ROAS:  │                     │
│          │   3.2x   │   $12.4K │   4.1x   │                     │
├──────────┼──────────┼──────────┼──────────┤                     │
│  ☐ Back  │  ▶ Retar-│          │          │                     │
│   to     │   get    │          │          │                     │
│   School │   Active │          │          │                     │
│   Due 9/1│   CTR:+5%│          │          │                     │
└──────────┴──────────┴──────────┴──────────┴─────────────────────┘
```

## Features

| Feature | Description |
|---|---|
| **Campaign Canvas** | Drag-and-drop campaign builder with timeline view |
| **AI Orchestrator** | Python agent that manages campaign workflows autonomously |
| **Multi-channel** | Email, social, display, search, and direct mail |
| **Budget Tracking** | Real-time spend vs. budget across all channels |
| **A/B Testing** | Built-in experiment designer with statistical analysis |
| **Automated Reports** | PDF and CSV exports with executive summaries |

## Quick Start

```bash
npm install @crynge/campaignforge

# Start the dashboard
npx campaignforge dashboard --port 3000

# Run the orchestrator
npx campaignforge orchestrate --config campaigns.yaml
```

```typescript
import { CampaignManager } from '@crynge/campaignforge/api/server';

const campaign = await CampaignManager.create({
  name: 'Q3 Product Launch',
  channels: ['email', 'linkedin', 'google'],
  budget: 75000,
  startDate: '2026-07-15',
  endDate: '2026-09-30',
  segments: ['enterprise', 'smb'],
});

await campaign.launch();
```

## Orchestrator

```python
from campaignforge.orchestrator import CampaignOrchestrator

orchestrator = CampaignOrchestrator(
    channels=["email", "social", "search"],
    budget=100000,
    objective="lead_generation",
)

workflow = orchestrator.plan()
for step in workflow:
    print(f"[{step.channel}] {step.action} — Due: {step.deadline}")
    step.execute()
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/api/campaigns` | List all campaigns |
| `POST` | `/api/campaigns` | Create campaign |
| `PUT` | `/api/campaigns/:id` | Update campaign |
| `POST` | `/api/campaigns/:id/launch` | Launch campaign |
| `GET` | `/api/campaigns/:id/metrics` | Get performance metrics |

## Modules

```
src/
├── api/
│   └── server.ts              # REST API
├── campaignforge/
│   └── orchestrator.py        # AI workflow orchestration
└── agents/
    └── agent.py               # Campaign monitoring agents
```

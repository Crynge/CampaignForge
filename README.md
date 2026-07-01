<div align="center">

# 🚀 CampaignForge

**Marketing campaign orchestration dashboard** — plan, launch, and optimize **multi-channel campaigns** with AI-powered agents that automate workflows, analyze performance, and suggest optimizations across email, social, search, and display.

[![CI](https://img.shields.io/github/actions/workflow/status/Crynge/CampaignForge/ci.yml?branch=main&label=CI&logo=github)](https://github.com/Crynge/CampaignForge/actions/workflows/ci.yml)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript)](https://typescriptlang.org)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://python.org)
[![License](https://img.shields.io/github/license/Crynge/CampaignForge?color=orange)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Crynge/CampaignForge?style=flat&logo=github)](https://github.com/Crynge/CampaignForge)
[![Last Commit](https://img.shields.io/github/last-commit/Crynge/CampaignForge?logo=git)](https://github.com/Crynge/CampaignForge/commits/main)

[Campaign Board](#-campaign-board) • [Quick Start](#quick-start) • [Architecture](#architecture) • [API](#api) • [Modules](#modules) • [Contributing](#contributing)

---

> **⭐ Orchestrating campaigns?** Star CampaignForge to support open-source marketing automation!

</div>

---

## 📋 Campaign Board

```
┌─────────────────────────────────────────────────────────────────────┐
│  CAMPAIGN PIPELINE                                        + New    │
├──────────┬──────────┬──────────┬──────────┬─────────────────────────┤
│  📝 DRAFT│  ▶ ACTIVE│  🔍 REVIEW│  ✓ DONE  │                         │
├──────────┼──────────┼──────────┼──────────┤                         │
│  Q4      │  Summer  │  Email   │  Spring  │                         │
│  Launch  │  Sale    │  Series  │  Launch  │                         │
│  Due 8/1 │  Live    │  Pending │  ROAS:   │                         │
│  Budget: │  ROAS:   │  Rev:    │  4.1x    │                         │
│  $50K    │  3.2x    │  $12.4K  │  ✅      │                         │
├──────────┼──────────┼──────────┼──────────┤                         │
│  Back to │  Retarget│  A/B     │          │                         │
│  School  │  Active  │  Test v2 │          │                         │
│  Due 9/1 │  CTR:+5% │  Draft   │          │                         │
│          │  🔥      │          │          │                         │
└──────────┴──────────┴──────────┴──────────┴─────────────────────────┘
```

## Features

| Feature | Description | Channels |
|---|---|---|
| **Campaign Canvas** | **Drag-and-drop** campaign builder with timeline view | All |
| **AI Orchestrator** | Python agent that manages **campaign workflows** autonomously | Email, Social, Search |
| **Multi-channel** | Email, social, display, search, and **direct mail** | 10+ channels |
| **Budget Tracking** | Real-time **spend vs. budget** across all channels | Per-channel + rollup |
| **A/B Testing** | Built-in experiment designer with **statistical analysis** | Subject, creative, audience |
| **Automated Reports** | PDF and CSV exports with **executive summaries** | Weekly / monthly |

---

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
  goals: {
    primary: 'revenue',
    target: 250000,
  },
});

await campaign.launch();
```

---

## Architecture

```mermaid
flowchart TB
    subgraph UI["Dashboard"]
        CB[Campaign Board] --> CF[Campaign Form]
        CB --> CM[Metrics View]
        CB --> CR[Reports]
    end

    subgraph API["API Layer"]
        CF --> REST[REST API]
        CM --> REST
        REST --> DB[(PostgreSQL)]
    end

    subgraph Orchestrator["AI Orchestrator (Python)"]
        DB --> ORCH[Orchestrator Engine]
        ORCH --> PL[Campaign Planner]
        ORCH --> EX[Channel Executor]
        ORCH --> MO[Monitor Agent]

        PL --> S1[Schedule Tasks]
        EX --> S2[Send via Channel API]
        MO --> S3[Track Metrics]
    end

    subgraph Channels["Channel Integrations"]
        S1 --> CH1[Email (SendGrid)]
        S1 --> CH2[Social (Meta/LinkedIn)]
        S1 --> CH3[Search (Google Ads)]
        S2 --> CH1
        S2 --> CH2
        S2 --> CH3
    end

    subgraph Intelligence["Intelligence Layer"]
        S3 --> AN[Performance Analyzer]
        AN --> REC[Recommendations]
        REC --> ALERT[Alerts]
        REC --> AUTO[Auto-Optimize]
    end
```

---

## API

```bash
# List campaigns
curl http://localhost:3000/api/campaigns

# Create campaign
curl -X POST http://localhost:3000/api/campaigns \
  -H "Content-Type: application/json" \
  -d '{"name": "Q3 Launch", "budget": 75000, "channels": ["email", "linkedin"]}'

# Launch campaign
curl -X POST http://localhost:3000/api/campaigns/1/launch

# Get metrics
curl http://localhost:3000/api/campaigns/1/metrics
```

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

---

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

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- [Open an issue](https://github.com/Crynge/CampaignForge/issues)

---

## License

[MIT](LICENSE)

---

## 🌐 Crynge Ecosystem

All repos are **free and open-source**. ⭐ Star what you use!

| Category | Repos |
|---|---|
| **LLM & AI** | [SpecInferKit](https://github.com/Crynge/SpecInferKit) · [AetherAgents](https://github.com/Crynge/AetherAgents) · [PromptShield](https://github.com/Crynge/PromptShield) |
| **Marketing** | [AdVerify](https://github.com/Crynge/AdVerify) · [Attributor](https://github.com/Crynge/Attributor) · [InfluencerHub](https://github.com/Crynge/InfluencerHub) · [EdgePersona](https://github.com/Crynge/EdgePersona) · [AdVantage](https://github.com/Crynge/AdVantage) · [BrandMuse](https://github.com/Crynge/BrandMuse) · [CampaignForge](https://github.com/Crynge/CampaignForge) |
| **Simulation** | [CivSim](https://github.com/Crynge/CivSim) · [EvalScope](https://github.com/Crynge/EvalScope) |
| **Operations** | [OpsFlow](https://github.com/Crynge/OpsFlow) |

<div align="center">
  <sub>Built by <a href="https://github.com/Crynge">Crynge</a> · ⭐ Star us on GitHub!</sub>
</div>

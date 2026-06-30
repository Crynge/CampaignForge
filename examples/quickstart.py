from campaignforge import CampaignOrchestrator

orchestrator = CampaignOrchestrator(
    brand_voice="professional",
    channels=["blog", "twitter", "linkedin"],
    budget=50000,
)

plan = orchestrator.launch(
    name="Q4 Product Launch",
    target_audience="enterprise CTOs",
    key_message="10x productivity with AI agents",
    timeline="2026-10-01 to 2026-12-31",
)

print(plan.summary())

from campaignforge import CampaignOrchestrator


class TestCampaignOrchestrator:
    def test_launch_returns_plan(self):
        orchestrator = CampaignOrchestrator()
        plan = orchestrator.launch(
            name="Test Campaign",
            target_audience="developers",
            key_message="Build faster with AI",
            timeline="2026-07-01 to 2026-09-30",
        )
        assert plan.name == "Test Campaign"
        assert "blog" in plan.channels
        assert plan.summary()

    def test_custom_config(self):
        orchestrator = CampaignOrchestrator(
            brand_voice="casual",
            channels=["tiktok"],
            budget=5000,
        )
        assert orchestrator.brand_voice == "casual"
        assert orchestrator.channels == ["tiktok"]

    def test_performance_targets(self):
        orchestrator = CampaignOrchestrator()
        plan = orchestrator.launch("X", "devs", "speed", "Q3")
        assert plan.performance_targets["target_roi"] == 3.0

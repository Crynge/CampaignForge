from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CampaignPlan:
    name: str
    target_audience: str
    key_message: str
    channels: list
    budget: float
    timeline: str
    content_strategy: dict = field(default_factory=dict)
    seo_plan: dict = field(default_factory=dict)
    social_plan: dict = field(default_factory=dict)
    performance_targets: dict = field(default_factory=dict)

    def summary(self) -> str:
        lines = [
            f"Campaign: {self.name}",
            f"Audience: {self.target_audience}",
            f"Channels: {', '.join(self.channels)}",
            f"Budget: ${self.budget:,.0f}",
            f"Timeline: {self.timeline}",
            f"Strategies drafted: {len(self.content_strategy)} topics, "
            f"{len(self.seo_plan)} keywords, {len(self.social_plan)} posts",
        ]
        return "\n".join(lines)


class CampaignOrchestrator:
    def __init__(
        self,
        brand_voice: str = "professional",
        channels: Optional[list] = None,
        budget: float = 10000,
    ):
        self.brand_voice = brand_voice
        self.channels = channels or ["blog", "social"]
        self.budget = budget

    def launch(
        self,
        name: str,
        target_audience: str,
        key_message: str,
        timeline: str,
    ) -> CampaignPlan:
        strategy = self._research_content(target_audience, key_message)
        seo = self._analyze_seo(key_message)
        social = self._plan_social(name, key_message, timeline)
        perf = self._set_targets()

        return CampaignPlan(
            name=name,
            target_audience=target_audience,
            key_message=key_message,
            channels=self.channels,
            budget=self.budget,
            timeline=timeline,
            content_strategy=strategy,
            seo_plan=seo,
            social_plan=social,
            performance_targets=perf,
        )

    def _research_content(self, audience: str, message: str) -> dict:
        return {
            "topics": [f"{message} overview", f"Benefits of {message.lower()}", f"{audience} guide"],
            "format": ["blog", "infographic", "video"],
            "content_calendar": ["Week 1: Announcement", "Week 2: Deep dive", "Week 3: Case study"],
        }

    def _analyze_seo(self, message: str) -> dict:
        return {
            "primary_keywords": [message.lower(), message.lower() + " benefits"],
            "secondary_keywords": ["guide", "best practices", "use cases"],
            "gap_opportunities": ["competitor comparison", "ROI analysis"],
        }

    def _plan_social(self, name: str, message: str, timeline: str) -> dict:
        return {
            "platforms": ["twitter", "linkedin", "email"],
            "post_mix": {"educational": 5, "promotional": 3, "engagement": 2},
            "frequency": "3 posts/week per platform",
        }

    def _set_targets(self) -> dict:
        return {
            "impressions": 500000,
            "click_through_rate": 0.035,
            "conversion_rate": 0.05,
            "target_roi": 3.0,
        }

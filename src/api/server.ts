import express from 'express';

const app = express();
app.use(express.json());

app.post('/api/v1/campaigns/plan', (req, res) => {
  const { name, targetAudience, keyMessage, budget } = req.body;
  res.json({
    campaign: {
      name,
      targetAudience,
      keyMessage,
      budget,
      channels: ['blog', 'twitter', 'linkedin', 'email'],
      timeline: `${new Date().toISOString().split('T')[0]} — 90 days`,
      contentStrategy: { topics: 3, formats: ['blog', 'infographic', 'video'] },
      seoPlan: { keywords: 5, opportunities: 2 },
      socialPlan: { posts: 30, platforms: 3 },
    },
  });
});

app.get('/api/v1/campaigns', (_req, res) => {
  res.json({ campaigns: [] });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`CampaignForge API on :${PORT}`));

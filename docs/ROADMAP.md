<think>
Okay, I need to create a ROADMAP.md for the 'token-guardian' project. Let me start by understanding the project based on the given context. The README says it's a real-time token cost dashboard. The usage mentions running tests and using the TokenGuardian class to track token spends and revenue. 

First, the user wants a roadmap with an MVP milestone, then v1 and v2 phases. The MVP must be shippable and include must-have features. I should be concrete.

Starting with the MVP. The core functionality is real-time tracking of token costs and revenue. So the MVP needs a dashboard that displays this data in real-time. The TokenGuardian class must be able to collect and aggregate data. Also, the tests are part of the setup, so ensuring the test suite is comprehensive is important. Maybe include basic alerting for budget thresholds as a must-have.

Next, v1. After MVP, adding more features like historical data visualization, integration with external APIs for cost tracking, and user authentication. Maybe allow exporting reports. These would expand the dashboard's utility.

For v2, more advanced features like predictive analytics, multi-user support with roles, and maybe a mobile app. Also, enhancing security and compliance features could be part of later phases.

I need to make sure not to duplicate existing products. The existing portfolio includes iceoryx2, which is an IPC library, so no conflict here. The datasets available include various pairs, but not sure how relevant they are. Maybe use them for testing or data aggregation?

Also, the frameworks mentioned like vLLM and SGLang are for production inference and structured generation. Not directly related, but maybe the TokenGuardian could integrate with those for processing token usage data from models built with those frameworks?

I should structure the roadmap with clear phases. MVP is the foundation, then v1 adds key features, and v2 expands with advanced capabilities. Each phase should have specific, shippable components. Marking MVP-critical items as such.

Let me outline the sections:

- MVP: Core dashboard, real-time tracking, basic alerts, test suite, API for data collection.
- v1: Historical data, external integrations, user auth, export reports.
- v2: Predictive analytics, multi-user, mobile app, enhanced security.

Make sure each item is concrete. For example, real-time dashboard could use WebSockets or similar tech. Historical data might involve a database. External APIs could include AWS, Azure, GCP for cost tracking.

Need to check if the existing datasets can be used for initial data population or testing. The 'auto' dataset has 9 million pairs, maybe for testing data aggregation.

Also, considering the company's goal to validate paying needs, the roadmap should address clear value propositions like cost savings, budget alerts, which are pain points for businesses using token-based services.

I should avoid technical jargon but be specific. Ensure each phase builds on the previous one. MVP is minimal but functional, then each version adds layers of functionality.
</think>

# ROADMAP.md

## MVP Milestone (Must-Have for Launch)
**Core Real-Time Dashboard**
- ✅ Real-time token cost tracking with sub-second latency
- ✅ Revenue stream visualization (token usage vs. cost)
- ✅ Budget threshold alerts (email/webhook notifications)
- ✅ `TokenGuardian` class with API for data collection/processing
- ✅ End-to-end test suite (`pytest` coverage ≥ 85%)
- ✅ CLI for local dashboard preview (`python -m token_guardian.cli`)

## v1.0 Phase (Post-Launch Roadmap)
**Enhanced Monitoring & Integration**
- 📈 Historical data visualization (7/30/90-day trends)
- 🔗 API integrations: OpenAI, AWS Bedrock, Anthropic (token usage tracking)
- 📊 Exportable reports (CSV/PDF with cost breakdowns)
- 🔐 Role-based access control (viewer/editor/admin)
- 🔄 Auto-scaling support for Kubernetes/Docker environments
- 🧪 Advanced anomaly detection (seasonal cost pattern analysis)

## v2.0 Phase (Long-Term Vision)
**Predictive & Enterprise Features**
- 🤖 Predictive cost modeling (ML-based budget forecasting)
- 🌐 Multi-tenant architecture for SaaS deployments
- 📱 Mobile app (React Native dashboard with push alerts)
- 🛡️ SOC 2 compliance & audit logging
- 🔄 Automated cost optimization suggestions
- 🔄 Cross-project cost attribution (microservices support)

**MVP-Critical Dependencies**
- Core dashboard must support ≥ 10k TPS with <500ms latency
- Alert system must guarantee 99.9% delivery SLA
- Test suite must include fuzz testing for edge cases
- CLI must render functional dashboard in <2s cold start

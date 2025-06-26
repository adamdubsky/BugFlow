# BugFlow Development Roadmap

This roadmap outlines the full implementation plan for BugFlow: a browser extension and cloud dashboard that converts bug reports into dev-ready tickets.

---

## 0. Project Infrastructure

- [ ] Create GitHub monorepo with `/extension`, `/backend`, `/dashboard`
- [ ] Add `.gitignore`, `README.md`, and `.env.example` to each directory
- [ ] Add dev containers or VS Code workspace (optional)
- [ ] Add Dockerfiles for each component
- [ ] Setup GitHub Actions for CI (lint, test, build)
- [ ] Configure Fly.io deploy or Helm charts
- [ ] Create initial README and setup instructions

---

## 1. Extension – Bug Capture Engine

### Content Script
- [ ] Inject recorder into active pages
- [ ] Record last N DOM events (clicks, inputs)
- [ ] Capture console errors
- [ ] Intercept XHR/fetch logs

### Background Script
- [ ] Handle “Send Bug” from popup or overlay
- [ ] Use `chrome.tabs.captureVisibleTab()` for screenshot
- [ ] Package screenshot + metadata

### UI Overlay
- [ ] Display floating “Send Bug” button
- [ ] Preview screenshot and data
- [ ] Send `POST /reports` with JWT auth

### Testing
- [ ] Log payloads to console for debugging
- [ ] Test screenshot and metadata accuracy

---

## 2. Backend – Report API

### Setup
- [ ] Create FastAPI app with PostgreSQL + Redis + Celery
- [ ] Configure S3-compatible storage (e.g., MinIO or AWS)
- [ ] Add Clerk.dev JWT middleware

### Features
- [ ] `/reports` accepts multipart/form-data:
  - [ ] `screenshot: file`
  - [ ] `metadata: JSON`
- [ ] Store screenshot in S3
- [ ] Store metadata in PostgreSQL
- [ ] Enqueue Celery enrichment task

### Testing
- [ ] Unit test upload and queue logic
- [ ] Integration test from extension → backend

---

## 3. Enrichment Worker – GPT Integration

- [ ] Setup Celery worker
- [ ] Fetch metadata + screenshot link
- [ ] Generate bug title and reproduction steps via GPT-4o
- [ ] Save AI output to database
- [ ] Send ticket to integration webhook if configured

### Testing
- [ ] Mock GPT API
- [ ] Test enrichment and webhook format

---

## 4. Dashboard – Report Viewer

### Auth and Layout
- [ ] Setup Clerk.dev for JWT auth
- [ ] Layout with sidebar and header
- [ ] Enforce RBAC (owner, admin, member)

### Report List
- [ ] Table view of reports
- [ ] Filter by status: pending, enriched, pushed
- [ ] Detail view with metadata and enrichment

### Controls
- [ ] “Resend to tracker” button
- [ ] “Edit steps” inline
- [ ] Delete report (soft-delete)

### Testing
- [ ] Fetch mock data
- [ ] Integration test: create → view → resend

---

## 5. Replay Timeline (Optional for MVP)

- [ ] Parse and store DOM/network logs
- [ ] Implement visual timeline scrubber
- [ ] Optionally highlight DOM elements during playback

---

## 6. Tracker Integrations

- [ ] OAuth setup for:
  - [ ] Jira
  - [ ] GitHub
  - [ ] Linear
- [ ] Store tokens and webhook URLs
- [ ] Format payload with metadata + enrichment
- [ ] Send to selected tracker
- [ ] Add deep link from tracker to dashboard

---

## 7. Auth, RBAC, and Enterprise Controls

- [ ] Enforce Clerk.dev JWT on all endpoints
- [ ] Add role-based access: owner, admin, member
- [ ] Setup SSO + SCIM via Clerk.dev
- [ ] Add audit log system (PostgreSQL)
- [ ] Dashboard view for audit logs

---

## 8. Observability and Monitoring

- [ ] Add OpenTelemetry instrumentation to FastAPI
- [ ] Forward traces and metrics to Grafana Cloud
- [ ] Setup Sentry for frontend and backend exceptions
- [ ] Add `/health` endpoint for all services

---

## 9. Deployment and Release

- [ ] CI pipeline: lint, test, build, deploy
- [ ] Publish extension to Chrome/Edge/Firefox stores
- [ ] Setup Stripe Checkout integration via Clerk.dev
- [ ] Create final docs:
  - [ ] Architecture overview
  - [ ] Local setup instructions
  - [ ] Environment variables
  - [ ] Deployment workflow


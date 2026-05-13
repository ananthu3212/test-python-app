# test-python-app

A deliberately vulnerable Python Flask application used to demonstrate the
portability of the shift-left security reusable workflow defined in:

**https://github.com/ananthu3212/shift-left-security-thesis**

---

## Purpose

This repository proves that any Python project can adopt a production-grade
shift-left security pipeline by adding **one workflow file** with 5 lines of
configuration — no tool installation or security expertise required.

---

## Intentional vulnerabilities

| Vulnerability | File | Type | Detected by |
|--------------|------|------|-------------|
| SQL Injection | `app.py` line 9 | CWE-89 | Semgrep |
| Tainted SQL string | `app.py` line 12 | CWE-89 | Semgrep |
| Outdated Flask 1.1.2 | `requirements.txt` | CVE-2023-30861 | Trivy |
| Outdated Werkzeug 1.0.1 | `requirements.txt` | CVE-2023-25577 | Trivy |
| Outdated Jinja2 2.11.3 | `requirements.txt` | CVE-2024-22195 | Trivy |

All vulnerabilities are intentional. This application is for security scanning
demonstration only and must never be deployed in a production environment.

---

## How the reusable workflow is called

`.github/workflows/security-scan.yml`:

```yaml
jobs:
  security:
    uses: ananthu3212/shift-left-security-thesis/.github/workflows/security-scan-reusable.yml@main
    with:
      docker-image-name: test-python-app
      semgrep-config: p/python
      trivy-severity: HIGH,CRITICAL
      fail-on-findings: true
```

This single file is the only security configuration in this repository.
Everything else — tool versions, scanning logic, dashboard generation — is
handled by the reusable workflow in the thesis repository.

---

## Security Dashboard

Findings are automatically published to GitHub Pages after every push:

**https://ananthu3212.github.io/test-python-app/**

---

## Related

- Thesis repository: https://github.com/ananthu3212/shift-left-security-thesis
- Thesis evaluation dashboard: https://ananthu3212.github.io/shift-left-security-thesis/
- Portability guide: https://github.com/ananthu3212/shift-left-security-thesis/blob/main/docs/PORTABILITY.md
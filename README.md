# Session 16: Calculator CI/CD

This separate repository, `vedanshun05/github-actions`, contains the calculator
homework and its GitHub Actions pipeline. The code and five existing tests come
from the session's `10-final-cicd-pipeline` lab.

## CI and CD

**CI (Continuous Integration)** tests and builds a code change. **CD (Continuous
Deployment)** runs the resulting build in a deployment environment.

The workflow is [session16-ci-cd.yml](./.github/workflows/session16-ci-cd.yml).
A push to `main` starts its `ci` and `cd` jobs:

```text
Push to main -> CI: secret check -> tests -> build -> Docker image -> artifacts
            -> CD: download image -> Kind -> Kubernetes Job -> result in logs
```

GitHub provides an Ubuntu runner for each job. A step is one operation within a
job. `needs: ci` lets the CD job start only after CI succeeds.

## Files and outputs

| File or artifact | Purpose |
| --- | --- |
| `app/calculator.py` | Calculator source. |
| `tests/test_calculator.py` | Five existing unit tests. |
| `requirements.txt` | Test dependencies. |
| `build.sh` | Generate build files and copy the calculator. |
| `Dockerfile` | Package the calculator in a Python image. |
| `calculator-build` | Downloadable build files from the CI job. |
| `calculator-image` | Built image archive passed to the CD job. |

The `DEMO_SECRET` repository secret demonstrates protected values. The workflow
checks that it exists without printing its value. Configure it in this repository.

CD loads the image into a temporary Kind cluster and runs `calculator-demo` as
a Kubernetes Job. Expected logs: `Deployed calculator: 10 + 5 = 15`. This CLI
application exits after running; it does not require a web server.

## Execution evidence

Commit and push the prepared files after configuring `DEMO_SECRET`. Then add
the actual successful Actions run URL and screenshots under `Outputs/manual/`:
CI/CD summary, passing tests, downloadable artifacts, and completed Job logs.
The earlier `hello-ci.yml` workflow remains as a separate learning exercise.

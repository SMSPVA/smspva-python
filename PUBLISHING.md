# Publishing to PyPI

The package name is `smspva-sdk`. Publication uses GitHub Actions OIDC, without a saved PyPI API token.

## One-time setup

1. In `SMSPVA/smspva-python`, create the GitHub environment `pypi`, allow deployment from `main` only, and require approval from `SMSPVA`.
2. In the PyPI account that will own the project, add a pending GitHub publisher under account publishing settings:

   | Field | Value |
   | --- | --- |
   | PyPI project name | `smspva-sdk` |
   | Repository owner | `SMSPVA` |
   | Repository name | `smspva-python` |
   | Workflow filename | `publish.yml` |
   | Environment | `pypi` |

The first successful publication creates the PyPI project. Configuring a pending publisher does not reserve the package name.

## Release

1. Update `project.version` in `pyproject.toml` and the changelog through a reviewed pull request. Run CI before merging.
2. From `main`, manually run **Publish to PyPI**, entering the exact Python version, such as `0.1.0a1`.
3. The workflow builds the wheel and source archive, checks their metadata, installs the wheel, and runs the tests and type checks.
4. Review the run and approve deployment to `pypi`. The separate publishing job receives the OIDC permission and uploads the checked artifacts with attestations.
5. Install the version from PyPI in a separate project and verify it before announcing the release. Alpha versions require an explicit version or `--pre`.

Do not reuse an already published version or move an existing release tag. A failed upload may have published one of the files; inspect PyPI before deciding how to recover. Keep account credentials, recovery codes and real message data out of issues and workflow logs.

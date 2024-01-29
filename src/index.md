# Hosted and managed Python package index services

These solutions are provided by organisations which are not affiliated with Python
packaging, and are generally not open-source nor free.

Want to add a service? [Make a request.](
  https://github.com/EpicWink/python-index-services/issues/new
)

## Gemfury

[Product page](https://fury.co/l/pypi-server/)
| [Documentation](https://gemfury.com/help/pypi-server/)

Note: private indexes are paid.

## Artifactory

[Product page](https://jfrog.com/artifactory/>)
| [Documentation](
  https://www.jfrog.com/confluence/display/JFROG/PyPI+Repositories/
)

Cached proxy for multiple package indexes (including PyPI), and hosting a
new package index (supporting upload) with fall-through. Can be self-hosted
(not for free).

## Nexus Repository Manager

[Product page](https://www.sonatype.com/products/nexus-repository/)
| [Documentation](
  https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repository
)

Cached proxy for multiple package indexes (including PyPI), and hosting a
new package index (supporting upload) with fall-through.

## Coherent Minds PyPI Filter

[Documentation](https://pypi.coherentminds.de/redoc/)

Only filters requests, redirecting to PyPI if not filtered, and blocking
requests otherwise.

## GitLab Package Registry

[Documentation](
  https://docs.gitlab.com/ee/user/packages/pypi_repository/
)

Private and public package index with optional fall-through, permissioning.

## AWS CodeArtifact
[Product page](https://aws.amazon.com/codeartifact/>)
| [Documentation](
  https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html
)

Private package index with optional cached fall-through to PyPI.

## Azure Artifacts

[Product page](https://azure.microsoft.com/en-us/products/devops/artifacts/)
| [Documentation](
  https://learn.microsoft.com/en-us/azure/devops/artifacts/quickstarts/python-packages/
)

Private package index with optional fall-through.

## Google Artifact Registry

[Product page](https://cloud.google.com/artifact-registry/)
| [Documentation](
  https://cloud.google.com/artifact-registry/docs/python/
)

Private package index with no fall-through nor mirroring.

# py-template
Template repository for Python projects at Aarhus Stadsarkiv.

#### GitHub Actions
This repository includes a simple GitHub Actions workflow that sets up `poetry` with caching and checks linting & types using `flake8`, `black`, and `mypy`.
It also includes the initial setup for testing and upload to [codecov](https://codecov.io/) as a commented block. This part of the workflow requires adding a [codecov token](https://docs.codecov.io/docs#section-getting-started) as a [GitHub secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets). In addition, the call to `pytest` must be updated with the relevant project name.

#### And finally...
Remember to change this `README` to suit your repository!

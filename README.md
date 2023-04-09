## Alpa-related pre-commit hooks

This repo contains Alpa related pre-commit-hooks for checking
your alpa repo before committing

### Hooks

- `check-necessary-files` -> Check if repository contains all necessary
  files to successfully build package. Checked files: packit config,
  alpa config, package metadata and spec file
- `check-packit-file` -> Check if packit file is correct. This uses
  `packit validate-config` command.
- `source0-uses-version` -> Check if version is defined in source0 via some
  macro. This means that if you change version tag in specfile, it is
  automatically propagated to source0.

### Usage

Add this to your `.pre-commit-config.yaml` file in the git root:

```yaml
- repo: https://github.com/alpa-team/pre-commit-hooks
  rev: example tag or commit sha
  hooks:
    - id: check-necessary-files
    - id: check-packit-file
    - id: source0-uses-version
```

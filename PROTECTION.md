# PROTECTION.md

## Branch Protection Rules Justification

To maintain code quality and ensure project stability, the following rules are applied to the `main` branch:

- **Require pull request reviews**: This ensures at least one peer reviews every code change before it's merged, helping catch bugs early.
- **Require status checks**: Our CI workflow runs all tests, so merging is blocked if tests fail. This enforces high-quality and tested code in the main branch.
- **Disable direct pushes**: All changes must go through Pull Requests. This protects the main branch from accidental or harmful commits.

These practices align with industry standards and are crucial for collaboration in team-based environments.


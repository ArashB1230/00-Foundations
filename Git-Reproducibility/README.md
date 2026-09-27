# Git Reproducibility

Status: Complete

`check_project.py` checks the minimum structure for a shareable Python project: a README, ignore rules, and at least one test module. It emits JSON for scripts and exits with code `1` when the project is incomplete.

Run it with:

```text
python check_project.py ..\SQL-and-Data-Structures
```

The unit tests cover both ready and incomplete projects.
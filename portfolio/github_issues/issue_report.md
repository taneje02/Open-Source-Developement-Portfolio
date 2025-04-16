# 🐛 GitHub Issues Collaboration Report

## 🎯 Objective

This report documents how I used GitHub Issues to simulate real-world collaboration on the **Yatzy Game** project. As an individual developer, I followed a professional open-source workflow by:
- Creating self-review issues
- Tracking and fixing a bug
- Merging a fix via a pull request
- Documenting obstacles and concerns

---

## 🗂️ Repository

- **Repo Name**: `Open-Source-Development-Portfolio`
- **Project**: Simplified Python-based Yatzy Game with scoring and testing.
- **Branch Used**: `main` (final), `bugfix/three-of-a-kind` (feature branch)

---

## 🔍 Identified Issue

### Issue #1 – Bug in `score_three_of_a_kind`
- **Issue identify by: Navneet Kaur
- **Title**: Incorrect result from `score_three_of_a_kind()` function
- **Description**: When three matching dice are present alongside two unmatched values, the function fails to return the expected score.
- **Labels**: `bug`, `self-review`

#### Example
```python
# Expected output: 3 * 2 = 6
yatzy = Yatzy([2, 2, 2, 5, 6])
yatzy.score_three_of_a_kind()  # returns 0 (incorrect)

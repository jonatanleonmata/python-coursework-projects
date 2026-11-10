# Verification notes

Environment: Python 3.14.5.

Scope: syntax review of 40 Python files; representative execution checks for the three selected programs. These checks are separate from course grading.

| Scenario | Result |
| --- | --- |
| Restaurant: complete order | passed |
| Restaurant: menu range and empty checkout | passed |
| Restaurant: negative custom tip is retried | passed |
| Treasure: trap, revisit, empty cell, treasure streak, completion | passed |
| Treasure: map with no treasure ends immediately | passed |
| Matrix: rectangular multiplication | passed |
| Matrix: incompatible dimensions | passed |
| Matrix: negative values | passed |
| Restaurant: text instead of numeric menu input | documented limitation (ValueError) |
| Treasure: coordinates outside the map | documented limitation (IndexError) |
| Matrix: fewer values than requested | documented limitation (IndexError) |

The Python code was copied without changes. Example outputs were captured by a runner that echoed input and seeded random generation; the runner is not part of the project code.

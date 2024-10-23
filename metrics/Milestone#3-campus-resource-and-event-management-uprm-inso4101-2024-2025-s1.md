# Milestone Data

## Date Generated: 2024-10-02
| Developer | Points Closed | Percent Contribution | Projected Grade | Lecture Topic Tasks |
| --------- | ------------- | -------------------- | --------------- | ------------------- |
| Total | 0 | /100% | /100% | 0 |


## Sprint Task Completion

| Developer | S1 (2024/10/01-2024/10/01) | S2 (2024/10/01-2024/10/01) |
|---|---|---|
# Metrics Generation Logs

| Message |
| ------- |
| ERROR: Error while parsing milestone dates: Invalid isoformat string: '2024-11-5T00:00:00' |
| Traceback (most recent call last): |
|   File "/home/runner/work/semester-project-campus-resource-and-event-management/semester-project-campus-resource-and-event-management/inso-gh-query-metrics/src/generateMilestoneMetricsForActions.py", line 42, in generateMetricsFromV2Config |
|     datetime.fromisoformat(f"{mData.get('startDate')}T00:00:00") |
| ValueError: Invalid isoformat string: '2024-11-5T00:00:00' |
| WARNING: startDate and/or endDate for Milestone #3 couldn't be interpreted, proceeding without decay. |
| ERROR: Project not found in org. Likely means the project board doesn't share the same name as the team. |
| Traceback (most recent call last): |
|   File "/home/runner/work/semester-project-campus-resource-and-event-management/semester-project-campus-resource-and-event-management/inso-gh-query-metrics/src/generateMilestoneMetricsForActions.py", line 62, in generateMetricsFromV2Config |
|     team_metrics = getTeamMetricsForMilestone( |
|                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^ |
|   File "/home/runner/work/semester-project-campus-resource-and-event-management/semester-project-campus-resource-and-event-management/inso-gh-query-metrics/src/generateTeamMetrics.py", line 204, in getTeamMetricsForMilestone |
|     for issue_dict in isses_from_gh_api(org=org, team=team): |
|   File "/home/runner/work/semester-project-campus-resource-and-event-management/semester-project-campus-resource-and-event-management/inso-gh-query-metrics/src/generateTeamMetrics.py", line 164, in isses_from_gh_api |
|     raise Exception( |
| Exception: Project not found in org. Likely means the project board doesn't share the same name as the team. |
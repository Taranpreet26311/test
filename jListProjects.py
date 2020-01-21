from jira import JIRA

jira = JIRA(basic_auth=('Taran Singh', 'SFl6rEayyFQeKb0d3ghT682D'), options={'server':'https://sudhanshu.atlassian.net/'})
issue = jira.issue('SD')
print(issue.fields.project.key) 
print(issue.fields.issuetype.name) 
print(issue.fields.reporter.displayName)
print(issue.fields.summary)
#test
import requests
from datetime import datetime
import csv



final_dataset = []
fmt = "%Y-%m-%dT%H:%M:%SZ"

page = 1

url = ("https://api.github.com/repos/hitechtraders/hitechtraders/pulls?state=closed&per_page=100&page=%d" % page)
res=requests.get(url,headers={"Authorization": 'Bearer <token>'})


repos=res.json()
while res.json() != []:
  print(page)
  page= page + 1
  url = ("https://api.github.com/repos/hitechtraders/hitechtraders/pulls?state=closed&per_page=100&page=%d" % page)
  res=requests.get(url,headers={"Authorization": 'Bearer token'})
  repos.extend(res.json())


print("Fetching PRs, Please Wait")
for data in repos:
  result = {}
  created_at = datetime.strptime(data['created_at'], fmt)
  closed_at = datetime.strptime(data['closed_at'], fmt)

  result['minutes_to_review'] = round((closed_at - created_at).total_seconds() / 60, 2)
  url_for_pr = ("https://api.github.com/repos/hitechtraders/hitechtraders/pulls/%d" % data['number'])
  res=requests.get(url_for_pr,headers={"Authorization": 'Bearer token'})
  result['line_of_code'] = res.json()['additions']
  result['user_name'] = res.json()['user']['login']
  result['pr_number'] = data['number']
  final_dataset.append(result)


print("Writing to csv, Please Wait")
keys = final_dataset[0].keys()
with open('pr_review_data.csv_1', 'w', newline='') as output_file:
  dict_writer = csv.DictWriter(output_file, keys)
  dict_writer.writeheader()
  dict_writer.writerows(final_dataset)

print("`done")

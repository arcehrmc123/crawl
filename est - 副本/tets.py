import pandas as pd

# df1=pd.read_csv('outsider_newrepo.csv',encoding='utf-8')
# df1=df1.drop_duplicates().reset_index(drop=True)
# print(df1)
# df2=pd.read_csv('OutsiderPushRepo.csv',encoding='utf-8')
# df2=df2.drop_duplicates().reset_index(drop=True)
# print(df2)
#
# d1=pd.merge(df2,df1,on=['contributor_login','repo_name','repo_id'],how='left')
# print(d1)
# d1.loc[pd.isna(d1['new_repo_name']),'new_repo_name']=d1['repo_name']
# print(d1)
# d1=d1[['contributor_login','repo_name','new_repo_name','repo_id']]
# d1.to_csv('OutsiderPushRepo1.csv',index=False,encoding='utf-8')
#
df1=pd.read_csv('OutsiderPushRepo1.csv',encoding='utf-8')
# print(df1[df1['repo_name']=='Juveb/a10-ansible'])
print(df1)
# data = {'a':1,'b':2,'c':3}
# print(data.keys())
# print(list(data.values()))
# print(data['a'])
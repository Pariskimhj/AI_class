#!/usr/bin/env python
# coding: utf-8

# In[20]:


# 2021.06.12 ~ 2022.06.12까지의 걸그룹 검색 빈도(네이버 데이터랩)
import pandas as pd
df = pd.read_excel('datalab.xlsx')
df = df.loc[:, ['블랙핑크','마마무','오마이걸','트와이스','레드벨벳']]
df.sum()
# 1년 간 블랙핑크가 가장 많이 검색되었음
# 광고모델 선정 활용


#UAS Pemrograman Komputer
#IF2112
#Jeraldo Letricio Halomoan Manulang
#12220080

import pandas as pd
import streamlit as st
import plotly.express as px

#merge data
data=pd.read_csv("produksi_minyak_mentah.csv")
datanegara=pd.read_json('kode_negara_lengkap.json')
datanegara=datanegara.rename(columns={"alpha-3":"kode_negara"})
data=pd.merge(datanegara,data,on='kode_negara')

#selektor
selectorn=data['name'].drop_duplicates()
selectort=data['tahun'].drop_duplicates()
selectorb=[*range(1, 250, 1)]

# Heading
st.title('Big Data of Countries oil Production (1971-2015)')
st.markdown('UAS IF2112 Pemrograman Komputer')
st.markdown('Jeraldo Letricio Halomoan Manulang')
st.markdown('12220080')

#PROBLEM I : Countries' Oil Production per Year
st.markdown('Countries Oil Production per Year')
selectn=st.selectbox('Select Country: ',selectorn)
datano1=data[data['name']==selectn]
datano1graph=px.line(datano1,x="tahun",y="produksi",title=str("Oil Produced by "+selectn))
st.plotly_chart(datano1graph)

#PROBLEM II : Oil Production N-Countries in Year-T
st.markdown('Oil Production N-Countries in T-Year')
selectt=st.select_slider('Select Year: ',selectort)
selectbn=st.select_slider('Select Sum of Displayed Countries: ',options=selectorb, value=5)
datano2=data[data['tahun']==selectt]
datano2=datano2.sort_values(["produksi"],ascending=[0])
datano2=datano2[:selectbn]
datano2graph=px.bar(datano2,x="name",y="produksi",title=str(str(selectbn)+" Top Oil Producing Countries in "+str(selectt)))
st.plotly_chart(datano2graph)

#PROBLEM III : Accumulated N-Countries Oil Production
st.markdown('Accumulated N-Countries Oil Production')
selectbn2=st.select_slider('Select Sum of Displayed Countries: ',options=selectorb, value=5, key="selectbn2")
datano3=data.groupby(["name"])["produksi"].sum().reset_index()
datano3=datano3.sort_values(["produksi"],ascending=[0])
datano3=datano3[:selectbn2]
datano3graph=px.bar(datano3,x="name",y="produksi",title=str(str(selectbn2)+" Top Countries on Accumulated Oil-Produced"))
st.plotly_chart(datano3graph)

#PROBLEM IV : Added Information of Countries' Oil Production
st.markdown('Added Information of Countries Oil Production')
selectt2=st.select_slider('Select Year: ',selectort,key="selectt2")

#Most Oil Producting Country on Year-T
st.markdown('Biggest Producting Country on Year-T')
datano4a=data[data['tahun']==selectt2]
datano4a=datano4a.sort_values(["produksi"],ascending=[0])
datano4a=datano4a[:1]
datano4a[["name","kode_negara","region","sub-region","produksi"]]
'''
________________________________________________________________________
'''
#Least Oil Producting Country on Year-T
st.markdown('Least Oil Producting Country on Year-T')
datano4b=data[data['tahun']==selectt2]
datano4b=datano4b.sort_values(["produksi"],ascending=[1])
datano4b=datano4b.loc[datano4b["produksi"]>0]
datano4b=datano4b[:1]
datano4b[["name","kode_negara","region","sub-region","produksi"]]
'''
________________________________________________________________________
'''
#Zero Production Accumulated Country
st.markdown('Zero Production Accumulated Country')
datano4c=data[data['tahun']==selectt2]
datano4c=datano4c.sort_values(["name"],ascending=[1])
datano4c=datano4c.loc[datano4c["produksi"]==0]
datano4c[["name","kode_negara","region","sub-region"]]

st.markdown('Information on Accumulated Oil Production')

#Most Accumulated Oil Producting Country on Year-T
st.markdown('Most Accumulated Oil Producting Country on Year-T')
datano4d=data.groupby(["name"])["produksi"].sum().reset_index()
datano4d=datano4d.sort_values(["produksi"],ascending=[0])
datatemp=data
datatemp.drop("produksi", axis=1, inplace=True)
datano4d=pd.merge(datano4d,datatemp,on='name')
datano4d=datano4d.drop_duplicates("name")
datano4d[:1][["name","kode_negara","region","sub-region","produksi"]]
'''
________________________________________________________________________
'''
#Least Accumulated Oil Producting Country on Year-T
st.markdown('Least Accumulated Oil Producting Country on Year-T')
datano4e=datano4d.sort_values(["produksi"],ascending=[1])
datano4e=datano4e.loc[datano4e["produksi"]>0]
datano4e=datano4e[:1]
datano4e[["name","kode_negara","region","sub-region","produksi"]]
'''
________________________________________________________________________
'''
#No.4f: Negara Produksi Nol Kumulatif
st.markdown('Negara dengan jumlah produksi nol kumulatif')
datano4f=datano4d.sort_values(["name"],ascending=[1])
datano4f=datano4f.loc[datano4f["produksi"]==0]
datano4f[["name","kode_negara","region","sub-region"]]

import pandas as pd

import streamlit as st

import plotly.express as px

dfEnergia = pd.read_csv("Registros_Energia.csv", sep=';', engine='python')

dfEnergia

dfEnergia.columns

dfConsumo = dfEnergia[ ['Registro_energia', 'Fecha_registro', 'Sucursal','Agregadoel'] ]

dfConsumo

dfConsumo.dtypes

dfConsumo["Registro_energia"].describe()

dfConsumo[dfConsumo["Registro_energia"].isnull()==True]

dfConsumo[dfConsumo["Sucursal"] =="Tekit"]

dfConsumo[(dfConsumo["Sucursal"] =="Tekit") & (dfConsumo["Fecha_registro"]=="2022-08-21")]

dfConsumo.at[604,'Registro_energia']=22291

dfConsumo.at[605,'Registro_energia']=22291

dfConsumo[(dfConsumo["Sucursal"] =="Tekit") & (dfConsumo["Fecha_registro"]=="2022-08-21")]

dfConsumo[(dfConsumo["Sucursal"] =="Tekit") & (dfConsumo["Fecha_registro"]=="2022-08-28")]

dfConsumo.at[855,'Registro_energia']=22376

dfConsumo[(dfConsumo["Sucursal"] =="Tekit") & (dfConsumo["Fecha_registro"]=="2022-08-28")]

dfConsumo["Registro_energia"].describe()

dfConsumo[(dfConsumo["Registro_energia"]==888888)]

dfConsumo[(dfConsumo["Registro_energia"]==9)]

dfConsumo[(dfConsumo["Sucursal"] =="Kanas&iacute;n") & (dfConsumo["Fecha_registro"]=="2022-08-15")]

dfConsumo[(dfConsumo["Sucursal"] =="Tekax") & (dfConsumo["Fecha_registro"]=="2022-08-06")]

dfConsumo[(dfConsumo["Sucursal"] =="Tekax") & (dfConsumo["Fecha_registro"]=="2022-08-08")]

dfConsumo.at[37, 'Registro_energia']=5924

dfConsumo[(dfConsumo["Sucursal"] =="Tekax") & (dfConsumo["Fecha_registro"]=="2022-08-06")]

dfConsumo["Fecha_registro"].describe()

dfConsumo["Sucursal"].describe()

dfConsumo["Sucursal"].unique()

dfConsumo["Sucursal"]=dfConsumo["Sucursal"].str.replace("Kanas&iacute;n","Kanasin" )

dfConsumo["Sucursal"].unique()

dfConsumo["Sucursal"]=dfConsumo["Sucursal"].str.replace("Man&iacute;","Mani" )

dfConsumo["Sucursal"]=dfConsumo["Sucursal"].str.replace("Um&aacute;n","Uman" )

dfConsumo["Sucursal"]=dfConsumo["Sucursal"].str.replace("Teabo Cl&iacute;nica","Teabo Clinica" )

dfConsumo["Sucursal"].unique()

dfConsumo[dfConsumo["Sucursal"].isnull()==True]

dfConsumo[dfConsumo["Fecha_registro"]=="2022-08-13"]["Sucursal"].value_counts()

dfConsumo[(dfConsumo["Sucursal"] =="Tekax") & (dfConsumo["Fecha_registro"]=="2022-08-13")]

dfConsumo[(dfConsumo["Sucursal"] =="Tekit") & (dfConsumo["Fecha_registro"]=="2022-08-13")]

dfConsumo[(dfConsumo["Sucursal"] =="Mani") & (dfConsumo["Fecha_registro"]=="2022-08-13")]

dfConsumo[(dfConsumo["Sucursal"] =="Teabo") & (dfConsumo["Fecha_registro"]=="2022-08-13")]

dfConsumo[dfConsumo["Fecha_registro"]=="2022-08-13"]

dfConsumo.drop([293,564,817],inplace=True)

dfConsumo[dfConsumo["Sucursal"].isnull()==True]

dfConsumo[dfConsumo["Fecha_registro"].isnull()==True]

dfConsumo[dfConsumo["Agregadoel"].isnull()==True]

dfConsumo.groupby(["Fecha_registro","Sucursal"]).count()

grupos = dfConsumo.groupby(["Fecha_registro","Sucursal"])

dfConsumo[dfConsumo.duplicated(keep=False)]

dfConsumo[(dfConsumo["Fecha_registro"] =="Teabo") & (dfConsumo["Fecha_registro"]=="2022-08-06")]

dfGrupos = dfConsumo.groupby(["Fecha_registro","Sucursal"],as_index=False).count()

dfGrupos.head()

dfGrupos[dfGrupos["Registro_energia"]>=3]   

dfConsumo[(dfConsumo["Fecha_registro"]=="2022-09-20")&(dfConsumo["Sucursal"]=="Tekax")]

dfFiltro=dfConsumo.groupby(["Sucursal","Fecha_registro"]).filter(lambda x:x['Registro_energia'].count()>=3)

dfFiltro.groupby

dfResultado=dfFiltro.groupby(["Sucursal","Fecha_registro"])["Registro_energia"].agg(['min','max'])

dfResultado=dfFiltro.groupby(["Sucursal","Fecha_registro"],as_index=False)["Registro_energia"].agg(['min','max'])

dfResultado["ConsumoDia"] = dfResultado["max"] - dfResultado["min"]

dfResultado["ConsumoDia"]

dfConsumo[(dfConsumo["Fecha_registro"]=="2022-08-06")&(dfConsumo["Sucursal"]=="Itzincab")]

dfGraficas = dfResultado.reset_index()

dfGraficas.head()



dfIt = dfGraficas[dfGraficas["Sucursal"]=="Itzincab"]

fig = px.line(dfIt, x="Fecha_registro",y="ConsumoDia", title="Consumo de Energia")

st.plotly_chart(fig, use_container_width=True)



import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:/Users/Admin/Downloads/Environment_Temperature_change_E_All_Data_NOFLAG.csv"
df = pd.read_csv(file_path)
df_melted = df.melt(
    id_vars=['Area', 'Element'],
    value_vars=[col for col in df.columns if col.startswith("Y")],
    var_name='Year',
    value_name='Temp'
)
df_melted['Year'] = df_melted['Year'].str.replace("Y", "").astype(int)
df_temp = df_melted[df_melted['Element'] == 'Temperature change']
df_world = df_temp[df_temp['Area'] == 'World']
plt.figure(figsize=(10,6))
sns.lineplot(data=df_world, x='Year', y='Temp', marker="o", color="red")
plt.title("Global Temperature Change Over Time", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid(True)
plt.show()
countries = ["India", "United States of America", "China", "Brazil"]
df_countries = df_temp[df_temp['Area'].isin(countries)]
plt.figure(figsize=(12,7))
sns.lineplot(data=df_countries, x='Year', y='Temp', hue='Area', marker="o")
plt.title("Country-wise Temperature Change (1961–2019)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.legend(title="Country")
plt.grid(True)
plt.show()
plt.figure(figsize=(10,6))
sns.histplot(df_world['Temp'], bins=20, kde=True, color="orange")
plt.title("Distribution of Global Temperature Anomalies", fontsize=14)
plt.xlabel("Temperature Anomaly (°C)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
plt.figure(figsize=(10,6))
sns.boxplot(data=df_countries, x="Area", y="Temp", hue="Area", palette="Set2", legend=False)
plt.title("Country-wise Temperature Change Distribution", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Temperature Anomaly (°C)")
plt.show()
df_heatmap = df_countries.pivot_table(
    index="Area", columns="Year", values="Temp"
)
plt.figure(figsize=(14,6))
sns.heatmap(df_heatmap, cmap="coolwarm", annot=False, cbar_kws={'label': 'Temp Change (°C)'})
plt.title("Heatmap of Temperature Change (1961–2019)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Country")
plt.show()


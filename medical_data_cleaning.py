df= pd.read_sql("select* from realworld_medical_dirty",engine)

df.head(20)

df.info()
df.describe()

df["Gender"]= df["Gender"].str.lower().str.strip()
df["Smoker"] = df["Smoker"].str.lower().str.strip()

df['Smoker'].unique()
df['Diagnosis'].unique()

df['Smoker'] = (df['Smoker'].astype(str).str.lower().str.strip().replace({'y': 'yes','n': 'no','nan': pd.NA}).fillna('unknown'))

df['Age'].isna
df['Age'] = df['Age'].fillna(df['Age'].median()) 

df['Blood_Pressure'] = pd.to_numeric(df['Blood_Pressure'])
df["Cholesterol"] = pd.to_numeric(df["Cholesterol"])

df["Blood_Pressure"] = df['Blood_Pressure'].fillna ( df["Blood_Pressure"].median())
df["Cholesterol"] =  df['Cholesterol'].fillna ( df["Cholesterol"].median())

df["Admission_Date"] = pd.to_datetime(df["Admission_Date"], errors="coerce")

df["Admission_year"] = df["Admission_Date"].dt.year
df["Admission_month"] = df["Admission_Date"].dt.month_name()
df["Admission_Day"] = df["Admission_Date"].dt.day
df["Admission_Dayname"] = df["Admission_Date"].dt.day_name()

df['Age_Group'] = pd.cut(df['Age'],bins=[0, 30, 45, 60, 100],labels=['Young', 'Adult', 'Middle-aged', 'Senior'])

df.groupby('Smoker')['Diagnosis'].value_counts(normalize=True)

df.groupby('Gender')['Cholesterol'].mean()

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

df['BMI_Category'] = df['BMI'].apply(bmi_category)


df['BMI_Category'].value_counts()

df['Admission_Weekday'] = df['Admission_Date'].dt.weekday
df['Admission_Weekday'].value_counts()


data = df.to_csv("Pandas_project_cleaned")


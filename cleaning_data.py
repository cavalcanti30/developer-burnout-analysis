import pandas as pd
import numpy as np

# Carregar dados
df = pd.read_csv('developer_burnout_dataset_7000.csv')

# 1. VISÃO GERAL
print(f"Shape: {df.shape}")
print(f"Colunas: {df.columns.tolist()}")
print(df.info())

# 2. VERIFICAR MISSING VALUES
missing = df.isnull().sum()
print("\nMissing values:")
print(missing[missing > 0])

# 3. LIMPEZA BÁSICA

# Remover linhas onde burnout_level está vazio (target vazio)
df = df.dropna(subset=['burnout_level'])
# print(df['burnout_level'].isna().sum())

# Para colunas numéricas, preencher com mediana (robusto para outliers)
numeric_cols = ['age', 'experience_years', 'daily_work_hours', 'sleep_hours', 
                'caffeine_intake', 'bugs_per_day', 'commits_per_day', 
                'meetings_per_day', 'screen_time', 'exercise_hours', 'stress_level']

for col in numeric_cols:
    if col in df.columns:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

# 4. REMOVER OUTLIERS EXTREMOS (opcional - mas vamos identificar primeiro)
# Vamos apenas identificar por enquanto

# 5. VERIFICAR RESULTADO
print(f"\nShape após limpeza: {df.shape}")
print(df[['age', 'stress_level', 'burnout_level']].head())

# Estatísticas descritivas
print(df.describe())

# Ver distribuição do burnout
print(df['burnout_level'].value_counts())
print(df['burnout_level'].value_counts(normalize=True) * 100)

df.to_csv('dev_burnout_dataset_clean.csv', index=False)
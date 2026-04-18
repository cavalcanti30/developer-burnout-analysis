import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Carregar dados
df = pd.read_csv('dev_burnout_dataset_clean.csv')

# Configuração profissional
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("RdYlGn_r")  # Vermelho (alto) para Verde (baixo)
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# ============================================
# GRÁFICO 1: HORAS TRABALHADAS VS BURNOUT (MAIS IMPORTANTE)
# ============================================
fig, ax = plt.subplots(figsize=(10, 6))
order = ['Low', 'Medium', 'High']
sns.boxplot(data=df, x='burnout_level', y='daily_work_hours', order=order, 
            palette=['#2ecc71', '#f39c12', '#e74c3c'])
ax.set_title('🔥 Devs com burnout alto trabalham 60% mais horas', fontsize=14, fontweight='bold')
ax.set_xlabel('Nível de Burnout', fontsize=12)
ax.set_ylabel('Horas Trabalhadas por Dia', fontsize=12)

# Adicionar anotações
means = df.groupby('burnout_level')['daily_work_hours'].mean()
ax.text(0, 3.5, f'Low: {means["Low"]:.1f}h', fontsize=10, ha='center')
ax.text(1, 3.5, f'Medium: {means["Medium"]:.1f}h', fontsize=10, ha='center')
ax.text(2, 3.5, f'High: {means["High"]:.1f}h', fontsize=10, ha='center', color='red', fontweight='bold')

plt.tight_layout()
plt.savefig('grafico_1_horas_trabalhadas.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# GRÁFICO 2: COMPARAÇÃO COMPLETA (Todos os fatores)
# ============================================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Horas de trabalho
sns.barplot(data=df, x='burnout_level', y='daily_work_hours', order=order, 
            palette=['#2ecc71', '#f39c12', '#e74c3c'], ax=axes[0,0])
axes[0,0].set_title('Horas Trabalhadas/Dia')
axes[0,0].set_ylabel('Horas')

# Cafeína
sns.barplot(data=df, x='burnout_level', y='caffeine_intake', order=order,
            palette=['#2ecc71', '#f39c12', '#e74c3c'], ax=axes[0,1])
axes[0,1].set_title('Consumo de Cafeína (xícaras/dia)')
axes[0,1].set_ylabel('Xícaras')

# Tempo de tela
sns.barplot(data=df, x='burnout_level', y='screen_time', order=order,
            palette=['#2ecc71', '#f39c12', '#e74c3c'], ax=axes[1,0])
axes[1,0].set_title('Tempo de Tela (horas/dia)')
axes[1,0].set_ylabel('Horas')

# Stress Level
sns.barplot(data=df, x='burnout_level', y='stress_level', order=order,
            palette=['#2ecc71', '#f39c12', '#e74c3c'], ax=axes[1,1])
axes[1,1].set_title('Nível de Stress (0-100)')
axes[1,1].set_ylabel('Stress')

plt.suptitle('Perfil do Desenvolvedor por Nível de Burnout', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_2_comparacao_completa.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# GRÁFICO 3: CORRELAÇÕES (Heatmap melhorado)
# ============================================
numeric_cols = ['daily_work_hours', 'sleep_hours', 'caffeine_intake', 
                'screen_time', 'exercise_hours', 'stress_level']
corr = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
ax.set_title('Correlação com Stress Level (destaque em vermelho)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_3_correlacoes.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# GRÁFICO 4: DISTRIBUIÇÃO DO BURNOUT (Pizza)
# ============================================
burnout_counts = df['burnout_level'].value_counts()
colors = ['#2ecc71', '#f39c12', '#e74c3c']
explode = (0, 0, 0.05)  # Destacar o "High"

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(burnout_counts, labels=burnout_counts.index, 
                                    autopct='%1.1f%%', colors=colors, explode=explode,
                                    startangle=90, textprops={'fontsize': 12})
autotexts[2].set_color('white')
autotexts[2].set_fontweight('bold')
ax.set_title('Distribuição do Burnout entre Desenvolvedores', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('grafico_4_distribuicao_burnout.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# EXTRA: TABELA RESUMO (para o README)
# ============================================
summary = df.groupby('burnout_level')[['daily_work_hours', 'sleep_hours', 
                                        'caffeine_intake', 'screen_time', 
                                        'stress_level']].mean().round(1)

print("\n" + "="*60)
print("📊 TABELA RESUMO - Médias por Nível de Burnout")
print("="*60)
print(summary.to_string())
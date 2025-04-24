import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# データ入力
haa = [10000, 12000, 11500, 9000, 11000]
laa = [3000, 4000, 3500, 2800, 3700]

# データフレーム化＆縦長形式に変換
df = pd.DataFrame({'HAA': haa, 'LAA': laa})
df_melted = df.melt(var_name='Group', value_name='Value')

# 箱ひげ図 + スウォームプロット
plt.figure(figsize=(10, 6))
sns.boxplot(x='Group', y='Value', data=df_melted)
sns.swarmplot(x='Group', y='Value', data=df_melted, color=".25")

# t検定とp値表示
p = stats.ttest_ind(df['HAA'], df['LAA']).pvalue
plt.text(0.5, max(df_melted['Value']) * 0.95, f'p-value = {p:.4f}', ha='center')

plt.title('HAA vs LAA Comparison')
plt.xlabel('Group')
plt.ylabel('Value')
plt.tight_layout()
plt.savefig('images/ttest_boxplot.png')  # グラフ画像を保存
plt.show()

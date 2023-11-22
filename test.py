import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 재현성을 위한 시드 설정
np.random.seed(0)

# 랜덤 데이터 생성
data = np.random.randn(100, 2)

# 서브플롯 생성
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 기술 통계: 평균과 중앙값
a, b = data[:, 0], data[:, 1]
axes[0, 0].bar(['평균', '중앙값'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='변수 1')
axes[0, 0].bar(['평균', '중앙값'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='변수 2')
axes[0, 0].legend()
axes[0, 0].set_title('기술 통계: 평균과 중앙값')

# 상관 분석
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('상관 분석')

# 변수들의 히스토그램
sns.histplot(data[:, 0], bins=15, color='blue', alpha=0.7, ax=axes[1, 0], label='변수 1')
sns.histplot(data[:, 1], bins=15, color='green', alpha=0.7, ax=axes[1, 0], label='변수 2')
axes[1, 0].set_xlabel('값')
axes[1, 0].set_ylabel('빈도')
axes[1, 0].set_title('변수들의 히스토그램')

# 변수 1 대 변수 2의 산점도
axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('변수 1')
axes[1, 1].set_ylabel('변수 2')
axes[1, 1].set_title('변수 1 대 변수 2의 산점도')

# 레이아웃 조정
plt.tight_layout()
plt.show()


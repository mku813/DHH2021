# DHH2021
Competition

https://www.digitalhealthhack.org/ai-1

## 주제
- 데이터 기반 최적의 치료를 선택해주는 의사 결정 AI를 개발하는 것을 목표로 합니다.

## 배경
- 유전자 분석 기술의 발달과 의료 데이터의 전산화로 인하여 방대한 데이터가 축적됨에 따라 이를 이용한 맞춤형 치료에 대한 관심이 높아지고 있다. 
- 환자 맞춤형 치료는 특히 암 환자의 맞춤형 항암 치료 분야에서 뚜렷한 성과를 보이고 있다. 이는 암 유전자 분석을 통해 변이 유전자에 타깃이 되는 약물을 찾아내는 과정을 통하여 이루어진다.
- 그러나, 환자의 데이터로부터 항암 효과와 인과 관계가 있는 유전자 변이를 찾아내는 과정은 매우 어렵다. 암 세포에서 유전자 변이는 수 천개 이상이 존재하며, 치료 효과와 유의한 연관성을 분석하기에는 환자의 데이터가 일반적으로 매우 적다. 또한 동일한 유전자 변이를 가진 암이라도 환자의 상태, 병의 진행 정도에 따라 치료의 효과가 다르게 나올 수 있으므로 단순 비교는 의미가 없다. 
- 항암 효과와 직접적인 인과관계가 있는 유전자를 찾기 위한 이상적인 조건은 똑같은 환자에서 그 유전자의 변이가 있는 경우와 없는 경우, 치료를 한 경우와 하지 않은 경우의 비교가 필요하다. 
- 그러나, 실제 이러한 조건은 불가능하기 때문에, 아래와 같은 문제를 해결해야 순수한 관심 유전자와 항암 효과의 인과관계를 규명할 수 있다. 1. 각 유전자 및 임상 요소들과 관심 유전자의 독립성 문제. 2. 유전자 및 환자 상태를 나타내는 임상 변수가 치료 배정에 미치는 직-간접 영향 3. 주어진 데이터 자체의 편향성 문제. 4. 관찰되지 않은 교란 변수의 영향 등이 있다.
- 의학 분야에서 이 모든 문제를 해결할 수 있는 가장 단순하면서 효과적인 방법은 무작위 치료 배분 방법 즉 randomized clinical trial이다.  이는 이론 적으로 치료와 관련된 각종 변수들의 효과를 무작위 법을 통해 무의미하게 만들어서 평균 치료효과 (average treatment effect)를 계산하게 된다. (이를   ignorability assumption 또는 exchangeability assumption이라고 한다.) 그러나, 이 방법은 실제로 임상에서 매우 제한적으로 사용가능한데, 그 이유는 비용 문제, 윤리 문제가 발생하기 때문이며, 특히, 유전자 분석에서는 매우 방대한 양의 환자 수가 필요하므로 사실상 불가능하다. 
- 그러므로, 이미 존재하는 데이터를 이용해서 가급적 정확한 인과 관계를 찾으려는 통계적 기법에 대한 연구가 진행되고 있다. 대표적인 예로 GWAS 기법의 FDR value, Mendelian randomization 등이 있다. 
- 인공 지능 분야 특히 강화학습 분야에서 과거 데이터를 이용하되 데이터가 가진 오류를 줄이는 연구들이 진행되고 있다. 이 연구 분야를 offline RL 이라고 부르며 최근 의학 데이터 연구, 로봇 연구 등 위험도가 크거나, 비용이 많이 드는 연구 분야에서 집중적인 연구가 이루어지고 있다.

## 챌린지의 목표
- 본 챌린지는 성균관대학교 삼성융합대학원의 의료인공지능연구소가 개발한 bio-health simulation data 를 이용하여 치료의 효과를 증가시키는 인과관계가 있는 유전자를 찾아내는 것을 목표로 한다. 

## 일정
- 2021.07.29(목) ~ 09.03(수) 참가모집
- 2021.09.03 데이터셋 공개
- 2021.10.08 결과물 제출

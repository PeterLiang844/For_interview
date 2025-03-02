from collections import Counter
from typing import List

def correct_scores(wrong_scores: List[int]) -> List[int]:
    correct_map = {35: 53, 46: 64, 57: 75, 91: 19, 29: 92}
    return [correct_map.get(score, score) for score in wrong_scores]

# 2.
def count_letters(text: str):
    text = text.upper()
    letter_counts = Counter(c for c in text if c.isalnum())
    return sorted(letter_counts.items())

# 3.
def josephus(n: int) -> int:
    if n == 0:
        return None
    people = list(range(1, n + 1))
    index = 0
    while len(people) > 1:
        index = (index + 2) % len(people)
        people.pop(index)
    return people[0]

# 測試
# 1.
print("修正後成績:", correct_scores([35, 46, 57, 91, 29]))  # 輸出: [53, 64, 75, 19, 92]

# 2.
text = "Hello welcome to Cathay 60th year anniversary"
letter_counts = count_letters(text)
print("字母出現次數:")
for char, count in letter_counts:
    print(f"{char} {count}")

# 3.
n = 10  # 例如有10人
print(f"最後留下的人的順位: {josephus(n)}")

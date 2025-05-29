import pickle
import os

filename = "score.bin"

if os.path.exists(filename):
    with open(filename, "rb") as file:
        scores = pickle.load(file)
    print("[파일 읽기]")
else:
    scores = []
    while True:
        score = int(input(f"#{len(scores)+1}? "))
        if score == -1:
            break
        scores.append(score)
    
    with open(filename, "wb") as file:
        pickle.dump(scores, file)

print("[점수 출력]")
print("개인점수:", *scores)
print("평균:", sum(scores)/len(scores) if scores else 0)

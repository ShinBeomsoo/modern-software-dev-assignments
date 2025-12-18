import subprocess
import os

# 채점할 파일 목록
files = [
    "k_shot_prompting.py",
    "chain_of_thought.py",
    "tool_calling.py",
    "self_consistency_prompting.py",
    "rag.py",
    "reflexion.py"
]

print("=" * 40)
print(" 🎓 과제 자동 채점기 (Auto-Grader)")
print("=" * 40)

results = {}

for script in files:
    print(f"▶️  Testing {script}...", end=" ", flush=True)

    try:
        # 스크립트 실행 및 출력 캡처 (로그 숨김)
        result = subprocess.run(
            ["python", script],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        # 출력에서 "SUCCESS" 키워드 찾기
        if "SUCCESS" in result.stdout:
            print("✅ PASS")
            results[script] = "PASS"
        else:
            print("❌ FAIL")
            results[script] = "FAIL"
            # 실패 시 디버깅을 위해 로그 일부 저장 또는 출력 가능
            # print(result.stdout) # 필요하면 주석 해제

    except Exception as e:
        print(f"⚠️  ERROR ({e})")
        results[script] = "ERROR"

print("\n" + "=" * 40)
print(" 📊 최종 성적표 (Final Scorecard)")
print("=" * 40)

score = 0
for script, status in results.items():
    icon = "✅" if status == "PASS" else "❌"
    print(f"{icon} {script:<30}: {status}")
    if status == "PASS":
        score += 10

print("-" * 40)
print(f"🏆 총점: {score} / 60")
print("=" * 40)

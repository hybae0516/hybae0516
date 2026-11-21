"""README의 '오늘의 한 줄'을 날짜(KST)에 맞춰 바꿉니다.

외부 API 없이 아래 목록에서 날짜별로 하나를 고르기 때문에
같은 날에는 몇 번 실행해도 같은 결과가 나옵니다.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re

QUOTES = [
    "오늘 배운 한 줄이 내일의 한 프로젝트가 된다.",
    "에러 메시지는 적이 아니라 가장 친절한 선생님이다.",
    "완벽한 코드보다 끝까지 완성한 코드가 낫다.",
    "모르는 걸 아는 것, 그게 배움의 시작이다.",
    "작게 만들고, 자주 실행하고, 천천히 고친다.",
    "어제의 나보다 한 줄 더 이해했다면 충분하다.",
    "막히는 순간이 바로 실력이 느는 순간이다.",
    "복사한 코드는 잊히지만, 이해한 코드는 남는다.",
    "print() 한 줄이 디버거보다 빠를 때도 있다.",
    "문제를 쪼개면 어려운 문제도 쉬운 문제 여러 개가 된다.",
    "커밋은 작게, 메시지는 친절하게.",
    "오늘 못 푼 문제는 내일의 내가 풀어 줄 것이다.",
    "읽기 좋은 코드는 미래의 나에게 보내는 편지다.",
    "천천히 가도 멈추지만 않으면 된다.",
    "버그를 고친 날은 코드를 한 줄도 안 쓴 날보다 값지다.",
    "예제를 따라 치는 것도 훌륭한 공부다.",
    "질문하는 데 드는 1분이 혼자 헤매는 1시간을 아낀다.",
    "변수 이름을 고민하는 시간은 낭비가 아니다.",
    "잘 쉬는 것도 개발의 일부다.",
    "기록하지 않은 배움은 금방 사라진다.",
    "작은 성공을 자주 경험하자.",
    "남과 비교하지 말고 어제의 나와 비교하자.",
    "코드가 돌아가면 기뻐하고, 왜 돌아가는지 알면 더 기뻐하자.",
    "공식 문서는 생각보다 친절하다.",
    "같은 실수를 두 번 하지 않으면 그걸로 성장이다.",
    "가장 좋은 학습법은 직접 만들어 보는 것이다.",
    "꾸준함은 재능을 이긴다.",
    "오늘의 삽질은 내일의 노하우가 된다.",
    "한 번에 다 하려 하지 말고, 오늘 할 수 있는 만큼만.",
    "Hello, World!에서 시작하지 않은 개발자는 없다.",
]

KST = timezone(timedelta(hours=9))
README = Path(__file__).resolve().parent.parent / "README.md"
PATTERN = re.compile(r"(<!-- QUOTE:START -->\n).*?(\n<!-- QUOTE:END -->)", re.DOTALL)


def main() -> None:
    today = datetime.now(KST).date()
    quote = QUOTES[today.toordinal() % len(QUOTES)]
    block = f"> {quote}\n>\n> <sub>📅 {today.isoformat()} 의 한 줄</sub>"

    text = README.read_text(encoding="utf-8")
    new_text, count = PATTERN.subn(lambda m: m.group(1) + block + m.group(2), text)
    if count != 1:
        raise SystemExit("README에서 QUOTE 마커를 찾지 못했습니다.")
    README.write_text(new_text, encoding="utf-8")
    print(f"[{today}] {quote}")


if __name__ == "__main__":
    main()

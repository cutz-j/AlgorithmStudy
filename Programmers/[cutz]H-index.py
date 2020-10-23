def solution(citations: list) -> int:
    # h-index = 논문 n 편, h번 이상 인용 --> h편 이상, 나머지 논문이 h번 이하 인용 -> max(h)
    # citations: citation numbers
    # length(citations) = papers: <= 10**3
    # citations: 0 ~ 10**4
    answer = 0
    # sorting O(nlogn)
    citations.sort(reverse=True)
    # if paper == 1:
    h = 0
    for num, c in enumerate(citations):  # O(n)
        if num + 1 <= c:
            h = num + 1

    answer = h
    return answer
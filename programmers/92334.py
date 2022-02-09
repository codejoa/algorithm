def solution(id_list, report, k):
    report = list(set(report))
    targetFilter = dict()
    answer = []

    for v in report:
        tempArr = v.split()

        if targetFilter.get(tempArr[1]):
            targetFilter[tempArr[1]].append(tempArr[0])
        else:
            targetFilter[tempArr[1]] = []
            targetFilter[tempArr[1]].append(tempArr[0])

    for v in id_list:
        count = 0
        for w in targetFilter.values():
            if len(w) >= k:
                if v in w:
                    count += 1
        answer.append(count)

    return answer
# 🔹 STUDENT 1
def input_scores():
    try:
        data = input("Enter scores separated by space: ").strip()

        if not data:
            return []

        scores = []

        for item in data.split():
            try:
                num = float(item)
                scores.append(num)
            except ValueError:
                return {
                    "error": "All inputs must be numbers"
                }

        return scores

    except Exception:
        return {
            "error": "Unexpected input error"
        }


# 🔹 STUDENT 2
def calculate_average(scores):
    if not scores:
        return {
            "message": "No scores available",
            "average": 0
        }

    for score in scores:
        if not isinstance(score, (int, float)):
            return {
                "error": "Invalid data in scores"
            }

    total = 0
    count = 0

    for score in scores:
        total += score
        count += 1

    average = total / count

    return {
        "average": average
    }


# 🔹 STUDENT 3
def find_min_max(scores):
    if not scores:
        return {
            "message": "No scores available",
            "min": None,
            "max": None
        }

    for score in scores:
        if not isinstance(score, (int, float)):
            return {
                "error": "Invalid data in scores"
            }

    min_score = scores[0]
    max_score = scores[0]

    for score in scores:
        if score < min_score:
            min_score = score
        if score > max_score:
            max_score = score

    return {
        "min": min_score,
        "max": max_score
    }


# 🔹 STUDENT 4 (SƏN)
def analyze_pass_fail(scores):

    if not scores:
        return {
            "message": "No scores available",
            "results": [],
            "pass_count": 0,
            "fail_count": 0,
            "total_students": 0
        }

    PASS_MARK = 50

    results = []
    pass_count = 0
    fail_count = 0

    for score in scores:

        if not isinstance(score, (int, float)):
            return {
                "error": "Invalid data in scores"
            }

        if score >= PASS_MARK:
            results.append("PASS")
            pass_count += 1
        else:
            results.append("FAIL")
            fail_count += 1

    return {
        "results": results,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "total_students": len(scores)
    }

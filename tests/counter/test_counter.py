from src.counter import count_ocurrences


def test_counter():
    javascript = count_ocurrences("src/jobs.csv", "JavaScript")
    python = count_ocurrences("src/jobs.csv", "Python")

    assert javascript == 122
    assert python == 1639
    assert javascript != python

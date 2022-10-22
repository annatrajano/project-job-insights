from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = 'tests/mocks/brazilians_jobs.csv'
    result = {"title": "Maquinista", "salary": "2000", "type": "trainee"}
    assert result in read_brazilian_file(path)

def test_first():
    try:
        exec(open("dany's_file.py").read())
    except(not Exception):
        print("тест прошёд")
        pass

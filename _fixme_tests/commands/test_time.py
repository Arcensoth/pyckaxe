from pyckaxe import commands


def test_time():
    assert "time" == str(commands.time)


def test_time_add_time():
    assert "time add 3000" == str(commands.time.add.time(3000))


def test_time_add_call():
    assert "time add 3000" == str(commands.time.add(3000))


def test_time_query():
    assert "time query" == str(commands.time.query)


def test_time_query_day():
    assert "time query day" == str(commands.time.query.day)


def test_time_query_daytime():
    assert "time query daytime" == str(commands.time.query.daytime)


def test_time_query_gametime():
    assert "time query gametime" == str(commands.time.query.gametime)


def test_time_set():
    assert "time set" == str(commands.time.set)


def test_time_set_time():
    assert "time set 9000" == str(commands.time.set.time(9000))


def test_time_set_call():
    assert "time set 9000" == str(commands.time.set(9000))


def test_time_day():
    assert "time set day" == str(commands.time.set.day)


def test_time_midnight():
    assert "time set midnight" == str(commands.time.set.midnight)


def test_time_night():
    assert "time set night" == str(commands.time.set.night)


def test_time_noon():
    assert "time set noon" == str(commands.time.set.noon)

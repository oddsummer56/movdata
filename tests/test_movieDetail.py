from movdata.movieDetail import save_movieDetail

def test_save_movieDetail():
    for y in range(2015, 2022):
        r = save_movieDetail(year=y, sleep_time=0.1)
    assert r

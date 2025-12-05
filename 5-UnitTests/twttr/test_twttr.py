from twttr import shorten


def test_twttr():
    assert shorten("twitter") == "Output: #twttr"
    assert shorten("hello world") == "Output: #hll wrld"
    assert shorten("elon musk sucks") == "Output: #ln msk scks"
    assert shorten("qwerty") == "Output: #qwrty"
    assert shorten("eilugfhilesbgibgvhhskjfbsdj") == "Output: #lgfhlsbgbgvhhskjfbsdj"

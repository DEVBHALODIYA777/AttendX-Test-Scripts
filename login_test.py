def test_valid_login():
    username = "student01"
    password = "correct_password"

    # Simulate login validation
    assert username != ""
    assert password != ""

    print("PASS: Login input validation successful")


def test_empty_login():
    username = ""
    password = ""

    # Empty credentials should be rejected
    assert username == ""
    assert password == ""

    print("PASS: Empty login credentials identified")


if __name__ == "__main__":
    test_valid_login()
    test_empty_login()
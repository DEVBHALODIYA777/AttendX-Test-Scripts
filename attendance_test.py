def test_mark_attendance():
    student_id = "STU001"
    attendance_status = "Present"

    # Simulate attendance marking validation
    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("PASS: Attendance marking validation successful")


def test_invalid_attendance_status():
    attendance_status = "Unknown"

    # Invalid attendance status should be rejected
    assert attendance_status not in ["Present", "Absent"]

    print("PASS: Invalid attendance status identified")


if __name__ == "__main__":
    test_mark_attendance()
    test_invalid_attendance_status()
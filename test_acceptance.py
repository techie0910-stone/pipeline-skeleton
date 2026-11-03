import subprocess, sys

def test_user_sees_discounted_price():
    result = subprocess.run([sys.executable, "app.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "8000원" in result.stdout

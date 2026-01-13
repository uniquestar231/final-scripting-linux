import subprocess
result = subprocess.run(['echo', 'python!'])
print(f"Return code: {result.returncode}")
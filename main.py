import subprocess, signal, sys

print("🌙 Starting SeizureGuard...")
dashboard = subprocess.Popen(["python3", "dashboard.py"])
detector  = subprocess.Popen(["python3", "detector.py"])

def shutdown(*_):
    print("\nShutting down...")
    detector.terminate()
    dashboard.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)
detector.wait()
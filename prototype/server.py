"""
Lightweight Web Server for AERO-SHIELD Glassmorphic Prototype
Serves the prototype locally on port 8085 with zero external dependencies.
Tracks its PID to enable clean one-click termination.
"""
import os
import sys
import signal
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8085

class PrototypeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        directory = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, directory=directory, **kwargs)

    def log_message(self, format, *args):
        # Keep console clean
        pass

def run():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pid_file = os.path.join(base_dir, "prototype.pid")
    pid = os.getpid()
    
    with open(pid_file, "w") as f:
        f.write(str(pid))
        
    server = HTTPServer(("127.0.0.1", PORT), PrototypeHandler)
    print("=" * 65)
    print("AERO-SHIELD PROTOTYPE SERVER RUNNING")
    print(f"URL: http://localhost:{PORT}/")
    print(f"PID: {pid}")
    print("=" * 65)
    print("Press Ctrl+C or run STOP_PROTOTYPE.bat to stop the server.")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        if os.path.exists(pid_file):
            try:
                os.remove(pid_file)
            except Exception:
                pass
        print("\n[AERO-SHIELD] Server cleanly shut down.")

if __name__ == "__main__":
    run()

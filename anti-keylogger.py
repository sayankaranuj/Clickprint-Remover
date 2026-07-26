# kill_pynput_keylogger.py
import psutil
import os
import time

# Tokens we consider highly suspicious for Python keyloggers
SUSPICIOUS = ["pynput", "keylog", "keylogger", "keystroke", "keyboard"]

def looks_like_python(proc):
    """Return True if process name or cmdline suggests a Python process."""
    try:
        name = (proc.info.get('name') or "").lower()
        cmdline_list = proc.info.get('cmdline') or []
        cmdline = " ".join(map(str, cmdline_list)).lower()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False
    return "python" in name or "python" in cmdline or name.startswith("py")

def cmdline_suspicious(proc):
    """Check if cmdline contains suspicious tokens or suspicious script names."""
    try:
        cmdline_list = proc.info.get('cmdline') or []
        cmdline = " ".join(map(str, cmdline_list)).lower()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False
    return any(tok in cmdline for tok in SUSPICIOUS)

def memory_maps_suspicious(proc):
    """Best-effort: inspect memory-mapped paths for 'pynput' or similar tokens."""
    try:
        for m in proc.memory_maps():
            path = (getattr(m, "path", "") or "").lower()
            if not path:
                continue
            if any(tok in path for tok in SUSPICIOUS):
                return True
    except (psutil.AccessDenied, psutil.NoSuchProcess, AttributeError):
        return False
    return False

def open_files_suspicious(proc):
    """Check open files for suspicious names (log files or modules)."""
    try:
        for of in proc.open_files():
            path = (of.path or "").lower()
            if any(tok in path for tok in SUSPICIOUS):
                return True
    except (psutil.AccessDenied, psutil.NoSuchProcess, AttributeError):
        return False
    return False

def terminate_proc(proc):
    """Try polite terminate, then force kill if needed."""
    try:
        proc.terminate()
        proc.wait(timeout=3)
        return True, "terminated"
    except Exception:
        try:
            proc.kill()
            return True, "killed"
        except Exception as e:
            return False, f"failed: {e}"

def main():
    print("Running scan -> will terminate any Python processes matching 'pynput' or keylogger tokens.")
    found_any = False
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if not looks_like_python(proc):
                continue

            reasons = []
            if cmdline_suspicious(proc):
                reasons.append("suspicious_cmdline")
            if memory_maps_suspicious(proc):
                reasons.append("pynput_in_memory_maps")
            if open_files_suspicious(proc):
                reasons.append("suspicious_open_files")

            if reasons:
                found_any = True
                pid = proc.pid
                name = proc.info.get('name')
                cmd = " ".join(map(str, proc.info.get('cmdline') or []))
                print(f"[!] Detected PID={pid} Name={name} CMD={cmd} Reasons={reasons}")
                ok, status = terminate_proc(proc)
                if ok:
                    print(f"    -> Successfully {status} PID {pid}")
                else:
                    print(f"    -> Could not stop PID {pid}: {status}")

        except (psutil.NoSuchProcess, psutil.ZombieProcess):
            continue
        except psutil.AccessDenied:
            # can't inspect this process — skip it
            continue

    if not found_any:
        print("No matching keylogger-like Python processes found.")

if __name__ == "__main__":
    main()

import os
import subprocess
from pathlib import Path

def run(cmd):
    print(f"\n[+] {cmd}\n")
    subprocess.run(cmd, shell=True, check=False)

def main():
    print("\n=== CSIS4440 Integrated Forensic + Security Pipeline ===\n")

    device = input("Enter emulator/device ID (from 'adb devices', e.g. emulator-5554): ").strip()
    base_out = input("Enter output directory (e.g. ./group7_output): ").strip()

    base = Path(base_out)
    data_out = base / "data"
    apk_out = base / "apks"
    jadx_out = base / "jadx"
    drozer_help = base / "drozer_cheatsheet.txt"

    for p in [data_out, apk_out, jadx_out]:
        p.mkdir(parents=True, exist_ok=True)

    # 1) Ask for target packages
    print("\nEnter package names (one per line).")
    print("For example:")
    print("  com.dropbox.android")
    print("  com.instagram.lite")
    print("  com.spotify.music")
    print("  com.wallet.crypto.trustapp")
    print("  com.android.insecurebankv2")
    print("Empty line to finish.\n")

    packages = []
    while True:
        pkg = input("Package: ").strip()
        if not pkg:
            break
        packages.append(pkg)

    if not packages:
        print("No packages provided, exiting.")
        return

    # 2) For each package: pull /data/data + APK
    drozer_lines = []
    for pkg in packages:
        print(f"\n=== Processing {pkg} ===")

        # ADB data extraction 
        pkg_data_dir = data_out / pkg
        pkg_data_dir.mkdir(exist_ok=True)
        run(f"adb -s {device} pull /data/data/{pkg} \"{pkg_data_dir}\"")

        # APK path + pull (for MobSF + JADX)
        print("[*] Locating APK path via pm path...")
        result = subprocess.run(
            f"adb -s {device} shell pm path {pkg}",
            shell=True,
            capture_output=True,
            text=True
        )
        apk_path = None
        for line in result.stdout.splitlines():
            line = line.strip()
            if line.startswith("package:"):
                apk_path = line.split("package:")[-1]
                break

        if not apk_path:
            print(f"[!] Could not find APK path for {pkg}")
            continue

        local_apk = apk_out / f"{pkg}.apk"
        run(f"adb -s {device} pull {apk_path} \"{local_apk}\"")

        # 3) Optional: prepare JADX decompilation directory
        pkg_jadx_dir = jadx_out / pkg
        pkg_jadx_dir.mkdir(exist_ok=True)
        print(f"[*] You can now run JADX on: {local_apk}")
        print(f"    Example: jadx -d \"{pkg_jadx_dir}\" \"{local_apk}\"\n")

        # 4) Build Drozer command cheat-sheet for this package
        drozer_lines.append(f"=== Drozer commands for {pkg} ===")
        drozer_lines.append(f"run app.package.attacksurface {pkg}")
        drozer_lines.append(f"run app.activity.info -a {pkg}")
        drozer_lines.append(f"run app.provider.info -a {pkg}")
        drozer_lines.append(f"run app.broadcast.info -a {pkg}")
        drozer_lines.append("")  # blank line

    # 5) Save Drozer helper file
    drozer_help.write_text(
        "Drozer helper commands (run these inside 'drozer console connect'):\n\n"
        + "\n".join(drozer_lines),
        encoding="utf-8"
    )

    print("\n Pipeline finished.")
    print(f"[i] Extracted app data under: {data_out}")
    print(f"[i] Pulled APK files under:  {apk_out}")
    print(f"[i] Drozer cheatsheet saved: {drozer_help}")
    print(f"[i] Decompilation folders prepared under: {jadx_out}")
    print("\nYou can now:")
    print("  Run ALEAPP on the data/ folder .")
    print("  Upload APKs to MobSF .")
    print("  Decompile APKs with JADX .")
    print("  Paste drozer commands from drozer_cheatsheet.txt.")

if __name__ == '__main__':
    main()

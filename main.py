import subprocess
import os
from pyfiglet import Figlet
import time
import json

distros = ['AIX', 'Alpine', 'AlterLinux', 'Anarchy', 'Android', 'Antergos', 'antiX',
           'AOSC OS', 'AOSC OS/Retro', 'Apricity', 'ArcoLinux', 'ArchBox', 'ARCHlabs', 'ArchStrike', 'XFerience', 'ArchMerge', 'Arch', 'Artix', 'Arya', 'Bedrock', 'Bitrig', 'BlackArch', 'BLAG', 'BlankOn', 'BlueLight', 'bonsai', 'BSD', 'BunsenLabs', 'Calculate', 'Carbs', 'CentOS', 'Chakra', 'ChaletOS', 'Chapeau', 'Chrom', 'Cleanjaro', 'ClearOS', 'Clear_Linux', 'Clover', 'Condres', 'Container_Linux', 'CRUX', 'Cucumber', 'Debian', 'Deepin', 'DesaOS', 'Devuan', 'DracOS', 'DarkOs', 'DragonFly', 'Drauger', 'Elementary', 'EndeavourOS', 'Endless', 'EuroLinux', 'Exherbo', 'Fedora', 'Feren', 'FreeBSD', 'FreeMiNT', 'Frugalware', 'Funtoo', 'GalliumOS', 'Garuda', 'Gentoo', 'Pentoo', 'gNewSense', 'GNOME', 'GNU', 'GoboLinux', 'Grombyang', 'Guix', 'Haiku', 'Huayra', 'Hyperbola', 'janus', 'Kali', 'KaOS', 'KDE_neon', 'Kibojoe', 'Kogaion', 'Korora', 'KSLinux', 'Kubuntu', 'LEDE', 'LFS', 'Linux_Lite', 'LMDE', 'Lubuntu', 'Lunar', 'macos', 'Mageia', 'MagpieOS', 'Mandriva', 'Manjaro', 'Maui', 'Mer', 'Minix', 'LinuxMint', 'MX_Linux', 'Namib', 'Neptune', 'NetBSD', 'Netrunner', 'Nitrux', 'NixOS', 'Nurunner', 'NuTyX', 'OBRevenge', 'OpenBSD', 'openEuler', 'OpenIndiana', 'openmamba', 'OpenMandriva', 'OpenStage', 'OpenWrt', 'osmc', 'Oracle', 'OS Elbrus', 'PacBSD', 'Parabola', 'Pardus', 'Parrot', 'Parsix', 'TrueOS', 'PCLinuxOS', 'Peppermint', 'popos', 'Porteus', 'PostMarketOS', 'Proxmox', 'Puppy', 'PureOS', 'Qubes', 'Radix', 'Raspbian', 'Reborn_OS', 'Redstar', 'Redcore', 'Redhat', 'Refracted_Devuan', 'Regata', 'Rosa', 'sabotage', 'Sabayon', 'Sailfish', 'SalentOS', 'Scientific', 'Septor', 'SereneLinux', 'SharkLinux', 'Siduction', 'Slackware', 'SliTaz', 'SmartOS', 'Solus', 'Source_Mage', 'Sparky', 'Star', 'SteamOS', 'SunOS', 'openSUSE_Leap', 'openSUSE_Tumbleweed', 'openSUSE', 'SwagArch', 'Tails', 'Trisquel', 'Ubuntu-Budgie', 'Ubuntu-GNOME', 'Ubuntu-MATE', 'Ubuntu-Studio', 'Ubuntu', 'Venom', 'Void', 'Obarun', 'windows10', 'Windows7', 'Xubuntu', 'Zorin', 'IRIX']
for distro in range(len(distros)):
    distros[distro] = distros[distro].lower()
distros.sort()

neofetches = {}
names = {}
hasold = {}
hassmall = {}
columns, _ = os.get_terminal_size()
progress_width = int(min(len(distros), columns) / 1.5)
tux = None


def cmd(command):
    os.system(command)


def has(distro):
    global neofetches
    neofetches[distro] = {}
    neofetches[distro]["normal"] = os.popen(
        f'neofetch --ascii_distro "{distro}" --config ./config').read()
    temp_small = os.popen(
        f'neofetch --ascii_distro "{distro}_small" --config ./config').read()
    hassmall[distro] = temp_small != neofetches[distro]["normal"] and temp_small != tux
    if temp_small != neofetches[distro]["normal"] and temp_small != tux:
        neofetches[distro]["small"] = temp_small

    temp_old = os.popen(
        f'neofetch --ascii_distro "{distro}_old" --config ./config').read()
    hasold[distro] = temp_old != neofetches[distro]["normal"] and temp_old != tux
    if temp_old != neofetches[distro]["normal"] and temp_old != tux:
        neofetches[distro]["old"] = temp_old


def main():
    global neofetches
    global distros
    global hasold
    global hassmall
    global columns
    global tux
    global names
    try:
        if os.path.exists("distros.json"):
            with open("distros.json", "r") as f:
                data = json.load(f)
                distros = data["distros"]
                names = data["names"]
                neofetches = data["neofetches"]
                hasold = data["hasold"]
                hassmall = data["hassmall"]
                tux = data["tux"]
            print("there is a distros.json file, no need to generate it")
        else:
            print("please wait, distro names are being generated...")
            t = time.time()
            for distro in range(len(distros)):
                names[distros[distro]] = Figlet(
                    "standard").renderText(distros[distro])
                progress = int(distro / (len(distros) / progress_width))
                print(
                    f'| {progress * "="}O{(progress_width - progress - 1) * "-"} |', end="\r")
            print(f"\ndone! in {int((time.time() - t) * 100) / 100}s")

            print("please wait, generating distro variants...")
            tux = os.popen(
                f'neofetch --ascii_distro "linux" --config ./config').read()
            t = time.time()
            for distro in range(len(distros)):
                has(distros[distro])
                progress = int(distro / (len(distros) / progress_width))

                print(
                    f'| {progress * "="}O{(progress_width - progress - 1) * "-"} |', end="\r")
            print(f"\ndone! in {int((time.time() - t) * 100) / 100}s")
            with open("distros.json", "w") as f:
                json.dump(
                    {
                        "distros": distros,
                        "names": names,
                        "neofetches": neofetches,
                        "hasold": hasold,
                        "hassmall": hassmall,
                        "tux": tux
                    },
                    f
                )

        with open('./config', 'w') as f:
            f.write(f'''print_info() {{\nprin \n}}''')
        input("press [enter] to start")

        for distro in distros:
            subprocess.call(["clear"])
            distro = distro.strip()

            print(neofetches[distro]["normal"])
            if hasold[distro]:
                print(neofetches[distro]["old"])
            if hassmall[distro]:
                print(neofetches[distro]["small"])
            print(names[distro])
            input()
    except Exception as e:
        print("an error occured")
        print(e)
        answer = input(
            "do you want to regenerate the distros.json file? [Y/n]")
        if len(answer) == 0 or answer.lower() == "y":
            try:
                os.remove("distros.json")
                print("deleted distros.json")
            except:
                print("it seems that there is no distros.json, so no need to delete it")
            main()
        else:
            print("ok :(")


if __name__ == "__main__":
    main()

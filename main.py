import argparse
import subprocess
import re
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Traceroute script to list IPs of hops.")
    parser.add_argument("destination", type=str, help="URL or IP address to trace route to.")
    parser.add_argument("-p", "--progressive", action="store_true",
                        help="Display IPs progressively as they are discovered.") # Option facultative qui permet d'afficher les sauts au fur et a mesure qu'ils sont découverts
    parser.add_argument("-o", "--output-file", type=str,
                        help="File name to save the traceroute result.") # Option facultative qui permet de sauvegarder le résultat de la commande dans un fichier
    return parser.parse_args()

# Fonction qui va permettre d'extraire une adresse IP de chaque ligne de sortie générée par traceroute
def extract_ips_from_traceroute_output(line):
    # Regex to match IP addresses
    ip_regex = re.compile(r"\((\d{1,3}(?:\.\d{1,3}){3})\)")
    match = ip_regex.search(line)
    return match.group(1) if match else None

def perform_traceroute(destination, progressive, output_file):
    try:
        process = subprocess.Popen(["traceroute", destination], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) # On lance la commande traceroute avec la destination passée en paramètre
        result_ips = []

        with open(output_file, "w") if output_file else sys.stdout as output:
            while True:
                line = process.stdout.readline()
                if not line:
                    break

                ip = extract_ips_from_traceroute_output(line) # Fonction appelée pour extraire l'adresse IP de traceroute
                if ip:
                    result_ips.append(ip)
                    if progressive:
                        print(ip, file=output)


            process.wait()

            if not progressive:
                for ip in result_ips:
                    print(ip, file=output)

    except FileNotFoundError:
        print("Error: 'traceroute' command not found. Please install it first.", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def main():
    args = parse_arguments()
    perform_traceroute(args.destination, args.progressive, args.output_file)

if __name__ == "__main__":
    main()


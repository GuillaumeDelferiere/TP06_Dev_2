# Traceroute Script

Ce script Python permet d'exécuter la commande `traceroute` pour lister les adresses IP des sauts (hops) vers une destination donnée.

## Prérequis

- Python 3.x
- La commande `traceroute` doit être installée sur votre système.

## Installation

Clonez ce dépôt et accédez au répertoire du projet :

```bash
git clone <https://github.com/GuillaumeDelferiere/TP06_Dev_2>
cd TP06_Dev_2
```
## Utilisation
Exécuter le script `traceroute.py` en spécifiant l'adresse IP ou le nom de domaine de la destination :

```bash
python traceroute.py <destination> [options]
```
### Options
-p, --progressive : Affiche les adresses IP des sauts de manière progressive.
-o, --output-file : Enregistre les adresses IP des sauts dans un fichier texte.
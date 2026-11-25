# Calculateur de sous-réseaux Azure

Outil en Python pour planifier des réseaux virtuels sur Microsoft Azure.

## Fonctionnalités
- Analyse d'un réseau en notation CIDR (ex : 10.0.0.0/16)
- Calcul des adresses utilisables selon les règles d'Azure (5 adresses réservées par sous-réseau)
- Détection réseau privé / public
- Découpage automatique en sous-réseaux /24

## Utilisation
python calculateur_reseau.py

## Ce que j'ai appris
- La notation CIDR et les masques de sous-réseau
- Les adresses réservées par Azure
- Le module ipaddress de Python
<img width="853" height="380" alt="image" src="https://github.com/user-attachments/assets/258eee46-d9b9-4670-b602-dd2e4b52ee15" />

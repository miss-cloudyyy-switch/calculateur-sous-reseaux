import ipaddress
import sys

print("=== Calculateur de sous-réseaux Azure ===")
saisie = input("Entre un réseau (ex : 10.0.0.0/16) : ")


try:
    reseau = ipaddress.ip_network(saisie, strict=False)
except ValueError:
    print(" Adresse invalide. Exemple valide : 10.0.0.0/16")
    sys.exit()



total = reseau.num_addresses
print(f"\nRéseau            : {reseau}")
print(f"Masque            : {reseau.netmask}")
print(f"Adresses totales  : {total}")
print(f"Type              : {'Privé ' if reseau.is_private else 'Public '}")


if total >= 8:
    print(f"Utilisables Azure : {total - 5}")
    print(f"1re IP utilisable : {reseau[4]}")
    print(f"Dernière IP       : {reseau[-2]}")

if reseau.prefixlen < 24:
    print("\nDécoupage en sous-réseaux /24 (les 5 premiers) :")
    for i, sous_reseau in enumerate(reseau.subnets(new_prefix=24)):
        if i == 5:
            break
        print(f"  Sous-réseau {i + 1} : {sous_reseau}")
# API Choice

- Étudiant : Gwenelle KOI
- API choisie : ipify
- URL base : https://api.ipify.org
- Documentation officielle / README : https://www.ipify.org/
- Auth : None 
- Endpoints testés :
  - GET /?format=json
  - GET /?format=text
- Hypothèses de contrat (champs attendus, types, codes) :
  Code HTTP attendu : 200
  Content-Type attendu : application/json
  Champ obligatoire : ip
  Type attendu : string
  Format attendu : adresse IPv4 valide (ex : 192.168.1.1)
  En cas de mauvais paramètre : erreur HTTP possible (400 ou réponse inattendue)
- Limites / rate limiting connu :
  API publique sans authentification
  Pas de limite stricte officiellement documentée
  Utilisation raisonnable recommandée pour éviter le blocage temporaire
- Risques (instabilité, downtime, CORS, etc.) :
  API externe donc dépendante de la disponibilité du service
  Possibilité de downtime temporaire
  Timeout réseau possible
  Variation de latence selon la connexion
  Risque faible car endpoint simple et stable

# VaryConsensus-Rendu

Nous avons codé naïvement sous plusieurs languages le test d'associativité :

### Python : (Moyenne de 82% en temps normal)
```bash
    python run Associativity.py 
```

### C : (Moyenne de 75% en temps normal)
```bash
    gcc Associativity.c -o associativity 
    ./associativity
```

### Java : (Moyenne de 82% en temps normal)
```bash
    java Associativity.java 
```

Puis par la suite nous avons réfléchi à l'origine de ces différences : 

- Le type des variables
- Le language utilisé
- La librairie utilisée pour générer des nombres aléatoires (et sa version potentiellement)
- La précision des flottants sur une opération d'association
- Le type d'opération d'associativité effectué

Enfin nous avons créé un Dockerfile pour essayer de faire varier certains des paramètres ci-dessus pour en déduire ce qui crée ces changements.

Générer l'image Docker :
```bash
    docker build -t runtime_parameter .
```

Lancer le container et sauvegarder l'entrée dans un volume (output du dossier courant ici en l'occurence) :
```bash
    docker run -v ./output:/app/output:rw runtime_parameter
```

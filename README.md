Petit récap de l'avancement du projet

Ce projet est un réseau social du genre TikTok mais pour le moment avec des photos a la place des vidéos!


L'objectif étant de s'améliorer et se familiariser au mieux à l'usage de Django

Pour commencer data model:
	voir schéma à la racine du projet !


Les fonctionnalités à développer (le strict minimum et nécessaire)
	->	Inscription, connexion (par MAIL) et suppression de compte
	-> 	Gestion de compte utilisateur : afficher les statistiques de l’utilisateur sur sa page (nombre de photo vue, de like, ... etc)
	-> 	Pouvoir uploader des photos sur le fil ou en photo de profile
	-> 	Système d’ajout/suppression des comptes suivis
	-> 	Flux de photos aléatoires qui s’affiche lorsque l’on scroll
	-> 	Système de like sur une photo


Le développement

	Je commence par préparer mon environnement
		- setup d'un venv
		- création des différentes apps nécessaires au projet
		- création des templates de base (base.html)
		- création des templates les plus importants (connexion, inscription, navbar)
		- installation de la librairie CSS Bulma (Lien à la fin du README pour la source)
	
	J'attaque le développement des éléments du projet:
		- petite retouche de settings.py (ajout des dossier static et templates + références vers les différentes apps )
		- création des models des différentes apps






Liens de sources / Annexes :

	BULMA CSS :
		https://bulma.io/documentation/start/overview/  							---> Documentation
		https://github.com/jgthms/bulma/releases/download/1.0.2/bulma-1.0.2.zip  	---> Téléchargement de la librairie

	Django documentation :
		https://www.djangoproject.com
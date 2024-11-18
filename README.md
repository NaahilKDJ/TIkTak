Petit récap de l'avancement du projet

Data Model
  Utilisateur
	  id
	  email
	  mdp
	  nom
	  prenom
	  date de naissance
	  date de création du compte
	  type de profil (public/privé)
	  photo de profile

  Publication:
	  id
	  titre --> optionnel
	  auteur/créateur
		      /* collaborateur(s) --> a voir */
	  date de création
	  date de modification --> potentiellement
			    nombres de likes --> optionnel
	  lien d'accès ou de visualisation
	  visibilité (public/privé)
		      /* tags */
	

  Likes:
	  id_publication
	  utilisateur ayant liké
	  date de like

  Suivis
	  id_suiveur
	  id_suivis
	  date de suivis

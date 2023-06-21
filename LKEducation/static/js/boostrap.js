
var d = new Date();
var dm = d.getMonth() + 1;
var dan = d.getYear();
calendrier(dm, dan+1900)
// if(dan < 999) dan+=1900;
// for (let index = 1; index < 13; index++) {
   
    
// }

function calendrier(mois,an) {
nom_mois = new Array
("Janvier","F&eacute;vrier","Mars","Avril","Mai","Juin","Juillet",
"Ao&ucirc;t","Septembre","Octobre","Novembre","D&eacute;cembre");
jour = new Array ("Lun.","Mar.","Mer.","Jeu.","Ven.","Sam.","Dim.");

var police_entete = "Verdana,Arial"; /* police entête de calendrier  */
var taille_pol_entete = 3;           /* taille de police 1-7 entête de calendrier  */
var couleur_pol_entete = "#FFFFFF";     /* couleur de police entête de calendrier  */
var arrplan_entete = "#000066";        /* couleur d'arrière plan entête de calendrier  */
var police_jours = "Verdana,Arial"; /* police affichage des jours  */
var taille_pol_jours = 3;           /* taille de police 1-7 affichage des jours  */
var coul_pol_jours = "#FFFFFF";     /* couleur de police affichage des jours  */
var arrplan_jours = "#fff";        /* couleur d'arrière plan affichage des jours  */
var couleur_dim = "#343434";        /* couleur de police pour dimanches  */
var couleur_cejour = "#FFFFFF";        /* couleur d'arrière plan pour aujourd'hui  */

var maintenant = new Date();
var ce_mois = maintenant.getMonth() + 1;
var cette_annee = maintenant.getYear();
if(cette_annee < 999) cette_annee+=1900;
var ce_jour = maintenant.getDate();
var temps = new Date(an,mois-1,1);
var Start = temps.getDay();

if(Start > 0) Start--;
else Start = 6;
var Stop = 31;
if(mois==4 ||mois==6 || mois==9 || mois==11 ) --Stop;
if(mois==2) {
 Stop = Stop - 3;
 if(an%4==0) Stop++;
 if(an%100==0) Stop--;
 if(an%400==0) Stop++;
}
document.write('<table class="w-full h-full" cellpadding="1" cellspacing="1">');
var entete_mois = nom_mois[mois-1] + " " + an;
inscrit_entete(entete_mois,arrplan_entete,couleur_pol_entete,taille_pol_entete,police_entete);
var nombre_jours = 1;
for(var i=0;i<=5;i++) {
  document.write("<tr>");
  for(var j=0;j<=5;j++) {
    if((i==0)&&(j < Start)) {
     inscrit_cellule("&#160;",arrplan_jours,coul_pol_jours,taille_pol_jours,police_jours) ; 
      } else {
      if(nombre_jours > Stop)
        inscrit_cellule("&#160;",arrplan_jours,coul_pol_jours,taille_pol_jours,police_jours);
      else {
        if((an==cette_annee)&&(mois==ce_mois)&&(nombre_jours==ce_jour))
         inscrit_cellule(nombre_jours,couleur_cejour,coul_pol_jours,taille_pol_jours,police_jours);
        else
         inscrit_cellule(nombre_jours,arrplan_jours,coul_pol_jours,taille_pol_jours,police_jours);
         
        nombre_jours++;
        }
      }
    }
    if(nombre_jours > Stop)
      inscrit_cellule("&#160;",arrplan_jours,couleur_dim,taille_pol_jours,police_jours);
    else {
      if((an==cette_annee)&&(mois==ce_mois)&&(nombre_jours==ce_jour))
        inscrit_cellule(nombre_jours,couleur_cejour,couleur_dim,taille_pol_jours,police_jours);
      else
        inscrit_cellule(nombre_jours,arrplan_jours,couleur_dim,taille_pol_jours,police_jours);
      nombre_jours++;
    }
    document.write("<\/tr>");
  }
document.write("<\/table>");
}
var ac
function getDate(params) {
  if (ac != params) {
    var old = document.getElementById(ac);
    if (old) {
      old.classList.remove('bg-white')
      old.classList.remove('text-blue-600')
      old.classList.remove('rounded-md')
      old.classList.add('text-white')
      old = ''
    }
    ac = params
    document.getElementById("dateR").value = params
    document.getElementById(params).classList.remove('text-white')
    document.getElementById(params).classList.add('bg-white')
    document.getElementById(params).classList.add('text-blue-600')
    document.getElementById(params).classList.add('rounded-md')
   
  }else{
    document.getElementById(params).classList.add('text-white')
    document.getElementById(params).classList.remove('bg-white')
    document.getElementById(params).classList.remove('text-blue-600')
    document.getElementById(params).classList.remove('rounded-md')

  }
 
} 
function inscrit_entete(titre_mois,couleurAP,couleurpolice,taillepolice,police) {
document.write("<tr colspan='1' class='text-center' >");
document.write('<td class="text-white font-bold text-2xl" align="center" colspan="7" valign="middle" >');
document.write(titre_mois);
document.write("<\/td><\/tr>");
document.write("<tr>");
for(var i=0;i<=6;i++)
  inscrit_cellule(jour[i],couleurAP,couleurpolice,taillepolice,police);
document.write("<\/tr>");
}
function nextStep(){
  document.getElementById('step1').classList.replace('block', 'hidden')
  document.getElementById('step2').classList.replace('hidden', 'block')
}
function previousStep(){
  document.getElementById('step1').classList.replace('hidden', 'block')
  document.getElementById('step2').classList.replace('block', 'hidden')
}
function inscrit_cellule(contenu,couleurAP,couleurpolice,taillepolice,police) {
  var formatData = contenu
  var mois = dm
  if (parseInt(contenu)) {
    if (parseInt(contenu) < 10) {
      contenu = '0' + contenu
    }
    if (parseInt(mois) < 10) {
      mois = '0' + mois
    }
    formatData = `${dan+1900}-${mois}-${contenu}`
  document.write(`<td id="${formatData}" onclick="getDate('${formatData}')" align="center" valign="middle" class="p-3 text-white cursor-pointer my-2 mx-2" >`);
    
  }else{
  document.write(`<td align="center" valign="middle" class="p-3 text-white cursor-pointer my-2 mx-2" >`);

  }
  document.write('<font size="'+taillepolice+'" class="cursor-pointer"  face="'+police+'">');
  document.write(contenu);
  document.write("<\/font><\/td>");
}


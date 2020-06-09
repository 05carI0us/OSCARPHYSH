#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#


#Contains all ActionManager/main_runner.py translation strings
import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _


default_palette = theme.default_palette

def check_version():                    #WILL BE MOVED FROM HERE
    with open('version.txt') as f:      # THIS WILL BE MOVED TOO
        #ver_current = f.read()         # DONT REMOVE THESE COMMENTS
        #version = ver_current.strip()  # TO-DO
        return f.read().strip()
version = check_version()

lang_start_main_menu = {
    "version_by_darksec": _("                                              {2}[{0}v {3}{2}]{0} BY:DARKSEC and 05carI0us{1}").format(default_palette[4], default_palette[2], default_palette[0], version),
    "short_description": _("{1}[{0} Modern Phishing Tool With Advanced Functionality MAINTENANT EN FRANÇAIS ET DU VRAI PAS CELUI DE GOOGLE TRADUCTION{1}]").format(default_palette[2],default_palette[0]),
    "features_summary" : _("{1}[{0} OUTIL, DE PHYSHING, DE TRACKEUR DE TOUCHE, AVEC 40 SITES ACCESSIBLES. {1}]").format(default_palette[2], default_palette[0]),
    "down_line" : "{0}________________________________________________________________________________".format(default_palette[0]),
    "attack_vector_message" : _("------------------------\nCHOISIS L'ATTAQUE DE VECTEUR QUE TU VEUX:\n------------------------"),
    "phishing_modules_header" : _("\n{0}PHISHING-MODULES:").format(default_palette[0]),
    "phishing_modules_list" : 
    [ ['{0}[{1}01{0}]{1} Facebook',      '{0}[{1}13{0}]{1} Steam',      '{0}[{1}25{0}]{1} Badoo',          '{0}[{1}37{0}]{1} PlayStation'],
      ['{0}[{1}02{0}]{1} Google',        '{0}[{1}14{0}]{1} VK',         '{0}[{1}26{0}]{1} CryptoCurrency', '{0}[{1}38{0}]{1} Xbox'],
      ['{0}[{1}03{0}]{1} LinkedIn',      '{0}[{1}15{0}]{1} iCloud',     '{0}[{1}27{0}]{1} DevianArt',      '{0}[{1}39{0}]{1} CUSTOM(1)'],
      ['{0}[{1}04{0}]{1} GitHub',        '{0}[{1}16{0}]{1} GitLab',     '{0}[{1}28{0}]{1} DropBox',        '{0}[{1}40{0}]{1} CUSTOM(2)'],
      ['{0}[{1}05{0}]{1} StackOverflow', '{0}[{1}17{0}]{1} Netflix',    '{0}[{1}29{0}]{1} eBay'],
      ['{0}[{1}06{0}]{1} WordPress',     '{0}[{1}18{0}]{1} Origin',     '{0}[{1}30{0}]{1} MySpace'],
      ['{0}[{1}07{0}]{1} Twitter',       '{0}[{1}19{0}]{1} Pinterest',  '{0}[{1}31{0}]{1} PayPal'],
      ['{0}[{1}08{0}]{1} Instagram',     '{0}[{1}20{0}]{1} ProtonMail', '{0}[{1}32{0}]{1} Shopify'],
      ['{0}[{1}09{0}]{1} Snapchat',      '{0}[{1}21{0}]{1} Spotify',    '{0}[{1}33{0}]{1} Verizon'],
      ['{0}[{1}10{0}]{1} Yahoo',         '{0}[{1}22{0}]{1} Quora',      '{0}[{1}34{0}]{1} Yandex'],
      ['{0}[{1}11{0}]{1} Twitch',        '{0}[{1}23{0}]{1} PornHub',    '{0}[{1}35{0}]{1} Reddit'],
      ['{0}[{1}12{0}]{1} Microsoft',     '{0}[{1}24{0}]{1} Adobe',      '{0}[{1}36{0}]{1} Subito.it']],
    "additional_modules" : _("\n{0}OUTILS ADDITINNELS :").format(default_palette[0]),
    "additional_modules_list" : 
    [ [_('{0}[{1}0A{0}]{1} OBTENIR LA LOCALISATION DE LA VICTIME')]],
    "operation_mode" : _("\nMODE OPÉRATOIRE:\n"),
    "facebook_operation_modes" :
    [ [_('{0}[{1}1{0}]{1} PHYSHING STANDARD'),                                      _('{0}[{1}3{0}]{1} OUTIL DE PHYSHING FACEBOOK AVEC UNE FAUSSE PAGE DE SÉCURITÉ(security_mode)')],
      [_('{0}[{1}2{0}]{1} Méthode avancée de classement des sondages(Poll_mode/login_with)'), _('{0}[{1}4{0}]{1} PHYSHING DE FACEBOOK + MESSENGER EN MEME TEMPS(messenger_mode)')]],
    "google_operation_modes" :
    [ [_('{0}[{1}1{0}]{1} PHYSHING STANDARD'),                  _('{0}[{1}3{0}]{1} NOUVEAU MOTEUR DE RECHERCHE')],
      [_('{0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)')]],
    "instagram_operation_modes" :
    [ [_('{0}[{1}1{0}]{1} Standard Instagram Web Page Phishing'),            _('{0}[{1}4{0}]{1} Badge certifié (Duper les utilisateurs en leur disant que ils peuvent obtenir le bage bleu certifié)')],
      [_('{0}[{1}2{0}]{1} Autoliker pour Instagram (Pour duper les utilisateurs)'), _('{0}[{1}5{0}]{1} Instafollower (Fausse page prétendant vous faire gagner des abbonés)')],
      [_('{0}[{1}3{0}]{1} Scénario avancé (Apparait comme un profile Instagram)')]],
    "VK_operation_modes" :
    [ [_('{0}[{1}1{0}]{1} Standard VK Web Page Phishing'), _('{0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)')]],
    "reddit_operation_modes" :
    [ [_('{0}[{1}1{0}]{1} Nouvelle page Reddit'), _('{0}[{1}2{0}]{1} Ancienne page Reddit')]],
    "additional_module_location_operation_modes" :
    [ [_('{0}[{1}1{0}]{1} NEAR YOU (La page web semble légitime)'), _('{0}[{1}2{0}]{1} GDRIVE (Demande une autorisation de localisation pour rediriger GDRIVE)')]]


}
lang_start_phishing_page = {
    "custom_folder_directory" : _('\n {0}[{1}*{0}]{1} LE DOSSIER CIBLE PERSONALISÉ EST {0}WebPages/{page}').format(default_palette[0], default_palette[4], page = 'page'),
    "manual_reading_suggestion" : _('\n {0}[{1}*{0}]{1} Veuillez lire le fichier manual.txt disponible à l\'adresse {0}[WebPages/{page}]').format(default_palette[0], default_palette[4], page = 'page'),
    "press_enter_to_contunue_if_setup_correctly" : _('\n {0}[{1}*{0}]{1} SI VOUS AVEZ BIEN TOUT INSTALLEZ ALORS, {0}APPUYER ENTRÉE ET BOOM!').format(default_palette[0], default_palette[4]),
    "copying_your_files" : _('\n {0}[{1}*{0}]{1} Copie de fichiers vers Server/www Folder...').format(default_palette[0], default_palette[4]),
    "https_suggestion" : _("\n{0}[{1}*{0}]{1} MERCI D\'UTILISER TUNNEL/URL '{0}https{1}' \n{0}[{1}*{0}]{1} LES NAVIGATEURS NE FONT CONFIANCE QUE AU LIEN HTTPS POUR PARTAGER LEUR LOCALISTATION\n").format(default_palette[0], default_palette[4]),
    "gdrive_suggestion" : _('{0}[{1}*{0}]{1} {0}Tip: {1}UTILISER UNE URL D\'UN DOSSIER DRIVE SI C\'EST DEMANDÉ.').format(default_palette[0], default_palette[4])
}

lang_enter_custom_redirecting_url = {
    "enter_redirecting_url_header" : _('{0}\n-------------------------------\n{1}[ METTEZ LE LIEN DE REDIRECTION ICI ] {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "enter_redirecting_url_prompt" : _('\n{0}[{1}*{0}]INSERER UNE URL DE REDIRECTION PERSONALISÉE:').format(default_palette[0], default_palette[4]),
    "redirect_here" : _('\n{0}LIEN DE REDIRECTION ICI>>> {1}').format(default_palette[0], default_palette[2])
}
             
#
#

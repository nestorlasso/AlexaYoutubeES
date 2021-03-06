# -*- coding: utf-8 -*-

# To run as an Alexa hosted skill:
# 1. Uncomment lines 9-14 below
# 2. Insert your Google developer key in line 10
# 3. Make sure to add this strings.py file to the lambda folder
# 4. Make sure to add pytube to the requirements.txt file in the lambda folder

#environ = {
#    "DEVELOPER_KEY": "insert_your_key_here",
#    "youtube_dl": "false",
#    "youtube_dl_error_mirror": "",
#    "AWS_LAMBDA_FUNCTION_NAME": ""
#}

locales = {
    'en-GB': 'Europe/London',
    'en-US': 'America/New York',
    'en-CA': 'America/New York',
    'en-AU': 'Australia/Sydney',
    'en-IN': 'Asia/Kolkata',
    'fr-FR': 'Europe/Paris',
    'fr-CA': 'America/New York',
    'de-DE': 'Europe/Berlin',
    'it-IT': 'Europe/Rome',
    'es-ES': 'Europe/Madrid',
    'es-MX': 'America/Mexico City',
    'ja-JP': 'Asia/Tokyo',
    'pt-BR': 'Brasil/Sao Paulo'
}

strings_en = {
'welcome1':"Welcome to Youtube. Say, for example, play videos by The Beatles.",
'welcome2':"Or you can say, shuffle songs by Michael Jackson.",
'help':"For example say, play videos by Fall Out Boy",
'illegal':"You can't do that with this skill.",
'gonewrong':"Sorry, something's gone wrong",
'playlist':"The playlist",
'channel':"The channel",
'video':"The video",
'notworked':"hasn't worked, shall I try the next one?",
'playing':"Playing",
'pausing':"Pausing",
'nomoreitems':"There are no more items in the playlist.",
'resuming':"Resuming",
'noresume':"I wasn't able to resume playing.",
'novideo':"I wasn't able to play a video.",
'notitle':"I can't find out the name of the current video.",
'nowplaying':"Now playing",
'nothingplaying':"Nothing is currently playing.",
'sorryskipby':"Sorry, I didn't hear how much to skip by",
'sorryskipto':"Sorry, I didn't hear where to skip to",
'ok':"OK",
'currentposition':"The current position is",
'hours':"hours",
'hour':"hour",
'minutes':"minutes",
'minute':"minute",
'seconds':"seconds",
'second':"second",
'throttled':"This skill is being throttled by YouTube, please try again later.",
'error403':"Sorry, this skill has hit it's usage limit for today.",
'apikeyerror':"Sorry, there was a problem with the Youtube API key.",
'youtubeerror':"There was a problem with the youtube search response.",
'nochannelid':"You do not have a channel id set.",
'noplaylistresults':"There were no playlist results found.",
'nomoreplaylists':"There are no more playlist results.",
'noplaylistplaying': "No playlist Playning now",
'addedfavo':"Video added to Favorites",
'addedplaylistfavo':"PLaylist added to Favorites",
'listerror':"Youtube Favorites List or authorizations not present",
'updateavailable': "Skill Update Available, Go To GitHub for upgrade. ",
}
strings_fr = {
'welcome1':"Bienvenue sur Youtube. Dite, par exemple, jouer une vid??o de Madonna.",
'welcome2':"Ou vous pouvez dire, chanson al??atoire de Michael Jackson.",
'help':"Par exemple dite, joue une vid??o de Michael Jackson",
'illegal':"Vous ne pouvez pas faire ??a avec cette skill.",
'gonewrong':"D??sol??, quelque chose n'a pas fonctionn??",
'playlist':"La playlist",
'channel':"La cha??ne",
'video':"The vid??o",
'notworked':"ne fonctionne pas, dois je essayer la suivante ?",
'playing':"Lecture de",
'pausing':"En pause",
'nomoreitems':"Il n'y a plus rien ?? lire dans cette playlist.",
'resuming':"Reprise",
'noresume':"Je n'ai pas pu reprendre la lecture.",
'novideo':"Je ne peux pas lire la vid??o.",
'notitle':"Je ne retrouve pas le nom de cette vid??o.",
'nowplaying':"Vous ??coutez ",
'nothingplaying':"Il n'y a aucune lecture en cours.",
'sorryskipby':"D??sol??, je n'ai pas compris de combien je devais avancer ou reculer.",
'sorryskipto':"D??sol??, je n'ai pas compris de combien je devais avancer ou reculer.",
'ok':"OK",
'currentposition':"La position actuelle est",
'hours':"heures",
'hour':"heure",
'minutes':"minutes",
'minute':"minute",
'seconds':"secondes",
'second':"seconde",
'updateavailable': "Mise ?? jour Skill disponible, acc??dez ?? GitHub pour la mise ?? niveau. ",
}
strings_it = {
'welcome1':"Benvenuto su YouTube. D??, per esempio, riproduci video dei Beatles.",
'welcome2':"Oppure puoi dire, canzoni casuali di Michael Jackson.",
'help':"Per esempio d??, riproduci i video dei Fall out Boy",
'illegal':"Non puoi fare questo con questa skill.",
'gonewrong':"Spiacente, qualcosa ?? andato storto",
'playlist':"La playlist",
'channel':"Il canale",
'video':"Il video",
'notworked':"non ha funzionato, dovrei provare la prossima?",
'playing':"Riproduco",
'pausing':"Ciao da Youtube",
'nomoreitems':"Non ci sono pi?? elementi nella playlist.",
'resuming':"Riprendo",
'noresume':"Non ero in grado di riprendere il video.",
'novideo':"Non ero in grado di riprodurre un video",
'notitle':"Non riesco a trovare il nome del video corrente.",
'nowplaying':"Ora riproduco",
'nothingplaying':"Al momento non sto riproducendo nulla.",
'sorryskipby':"Spiacente, non ho capito di quanto saltare",
'sorryskipto':"Spiacente, non ho capito dove saltare",
'ok':"OK",
'currentposition':"La posizione attuale ??",
'hours':"ore",
'hour':"ora",
'minutes':"minuti",
'minute':"minuto",
'seconds':"secondi",
'second':"secondo",
'throttled':"Questa skill ?? stata limitata da YouTube, riprova pi?? tardi.",
'error403':"Spiacente, questa skill ha raggiunto il limite giornaliero di Youtube per oggi.",
'apikeyerror':"Spiacenti, si ?? verificato un problema con la chiave API di YouTube.",
'youtubeerror':"Si ?? verificato un problema con la ricerca di YouTube.",
'nochannelid':"Non hai un ID canale impostato.",
'noplaylistresults':"Non sono state trovate playlist.",
'nomoreplaylists':"Non ci sono pi?? playlist.",
'addedfavo':"Il video ?? stato aggiunto ai preferiti",
'addedplaylistfavo':"La Playlist ?? stata aggiunta ai preferiti",
'listerror':"Lista Youtube Favorites o permessi non presenti",
'noplaylistplaying': "Nessuna Playlist in riproduzione",
'updateavailable': "Aggiornamento della SKill Disponibile, Vai Su GitHub per aggiornare. ",
}
strings_de = {
'welcome1':"Herzlich willkommen bei Youtube. Was kann ich f??r Dich tun? Sage zum Beispiel 'spiel Videos von The Beatles'.",
'welcome2':"Oder sag misch Songs von Michael Jackson.",
'help':"Sag zum Beispiel 'spiel Videos von Fall Out Boy ab' um Videos von Fall Out Boy abzuspielen.",
'illegal':"Das kannst Du mit diesen Skill nicht tun.",
'gonewrong':"Das tut mir Leid, das hat nicht funktioniert",
'playlist':"Die Wiedergabeliste",
'channel':"Der Kanal",
'video':"Das Video",
'notworked':"hat nicht funktioniert, soll ich das n??chste Element versuchen?",
'playing':"Spiele",
'pausing':"Pausieren",
'nomoreitems':"Die Wiedergabeliste enth??lt keine weiteren Elemente.",
'resuming':"Fortsetzen",
'noresume':"Leider konnte ich nicht weiter spielen.",
'novideo':"Dieses Video konnte ich nicht abspielen.",
'notitle':"Ich kann den Namen des aktuellen Videos nicht finden.",
'nowplaying':"Es l??uft gerade",
'nothingplaying':"Es wird momentan kein Song abgespielt.",
'sorryskipby':"Entschuldigung, ich habe nicht verstanden, wie viel ich ??berspringen soll",
'sorryskipto':"Entschuldigung, ich habe nicht verstanden, wohin ich springen soll",
'ok':"OK",
'currentposition':"Die aktuelle Position ist",
'hours':"Stunden",
'hour':"Stunde",
'minutes':"Minuten",
'minute':"Minute",
'seconds':"Sekunden",
'second':"Sekunde",
'updateavailable': "Skill Update verf??gbar. Gehen Sie zu GitHub, um ein Upgrade durchzuf??hren. ",
}
strings_es = {
'welcome1':"Bienvenido a Youtube. Di, por ejemplo, pon canciones de Mozart.",
'welcome2':"O puedes decir, canciones en aleatorio de Vivaldi.",
'help':"Por ejemplo di, pon un v??deo de Relajaci??n. O pon una lista aleatoria de sonidos de lluvia.",
'illegal':"No puedes hacer eso con esta skill.",
'gonewrong':"Lo siento, ha ocurrido un error.",
'playlist':"La playlist",
'channel':"El canal",
'video':"El v??deo",
'notworked':"No ha funcionado, pruebo con la siguiente?",
'playing':"Sonando",
'pausing':"Para.",
'nomoreitems':"No hay mas items en la playlist.",
'resuming':"Resumiendo.",
'noresume':"No es posible continuar.",
'novideo':"No se puede reproducir el v??deo.",
'notitle':"No puedo encontrar el t??tulo del v??deo.",
'nowplaying':"Ahora suena",
'nothingplaying':"No est?? sonando nada.",
'sorryskipby':"Lo siento, no he o??do cuanto adelantar.",
'sorryskipto':"Lo siento, no he o??do a donde adelantar.",
'ok':"OK",
'currentposition':"La posici??n actual es",
'hours':"horas",
'hour':"hora",
'minutes':"minutos",
'minute':"minuto",
'seconds':"segundos",
'second':"segundo",
'updateavailable': "Actualizaci??n de habilidades disponible, ve a GitHub para actualizar. ",
}
strings_ja = {
'welcome1':"?????????????????????????????????.  ?????????, ?????????????????????????????????????????? ??????????????????????????????.",
'welcome2':"????????????, ?????????????????????????????????????????????????????????????????? ??????????????????????????????.",
'help':"?????????, ??????????????????????????????????????????????????????????????????????????????????????????.",
'illegal':"????????????????????????????????????????????????????????????.",
'gonewrong':"???????????????, ???????????????????????????????????????.",
'playlist':"??????????????????",
'channel':"???????????????",
'video':"??????",
'notworked':"???????????????????????????????????????. ??????????????????????",
'playing':"?????????",
'pausing':"?????????",
'nomoreitems':"?????????????????????????????????????????????????????????.",
'resuming':"?????????",
'noresume':"???????????????????????????????????????.",
'novideo':"???????????????????????????????????????.",
'notitle':"???????????????????????????????????????????????????????????????.",
'nowplaying':"?????????",
'nothingplaying':"?????????????????????????????????.",
'sorryskipby':"???????????????. ???????????????????????????????????????????????????????????????.",
'sorryskipto':"???????????????. ???????????????????????????????????????????????????????????????.",
'ok':"??????.",
'currentposition':"????????????????????????,",
'hours':"??????",
'hour':"??????",
'minutes':"???",
'minute':"???",
'seconds':"???",
'second':"???",
'updateavailable': "Skill Update Available, Go To GitHub for upgrade. ",
}
strings_pt = {
'welcome1':"Bem vindo ao Youtube. Diga, por exemplo, toque um v??deo dos Beatles.",
'welcome2':"Ou voc?? pode dizer, toque m??sicas de Michael Jackson.",
'help':"Por exemplo, diga, toque v??deos de Fall Out Boy",
'illegal':"Voc?? n??o pode fazer isso com essa skill.",
'gonewrong':"Desculpe, algo deu errado",
'playlist':"A playlist",
'channel':"O canal",
'video':"O v??deo",
'notworked':"n??o funcionou, devo tentar o pr??ximo?",
'playing':"Tocando",
'pausing':"Pausando",
'nomoreitems':"Existem mais itens na playlist.",
'resuming':"Retomando",
'noresume':"N??o consegui voltar a tocar.",
'novideo':"N??o consegui tocar o v??deo.",
'notitle':"N??o encontrei o nome do v??deo atual.",
'nowplaying':"Tocando agora",
'nothingplaying':"Nada est?? tocando atualmente.",
'sorryskipby':"Desculpe, n??o ouvi quanto tenho que pular",
'sorryskipto':"Desculpe, n??o entendi para onde tenho que pular",
'ok':"OK",
'currentposition':"A posi????o atual ??",
'hours':"horas",
'hour':"hora",
'minutes':"minutos",
'minute':"minuto",
'seconds':"segundos",
'second':"segundo",
'updateavailable': "Skill Update Available, Go To GitHub for upgrade. ",
}

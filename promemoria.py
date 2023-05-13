import datetime
import threading
import time
import winsound
import win32api
import win32con

def set_reminder():
    while True:
        reminder_time = input("Inserisci la data e l'ora del promemoria (formato: gg/mm/aaaa hh:mm), o 'q' per uscire: ")

        if reminder_time.lower() == 'q':
            break

        reminder_text = input("Inserisci cosa deve ricordarti il promemoria: ")

        try:
            reminder_datetime = datetime.datetime.strptime(reminder_time, "%d/%m/%Y %H:%M")
            current_datetime = datetime.datetime.now()
            time_difference = reminder_datetime - current_datetime

            if time_difference.total_seconds() < 0:
                print("Hai inserito un'ora passata.")
                continue

            # Calcola il ritardo in secondi
            delay_seconds = time_difference.total_seconds()

            # Avvia il thread per inviare il promemoria
            t = threading.Thread(target=wait_and_notify, args=(delay_seconds, reminder_text))
            t.start()

            print("Promemoria impostato.")

        except ValueError:
            print("Formato data e ora non valido. Assicurati di inserire il formato corretto (gg/mm/aaaa hh:mm).")


def wait_and_notify(delay, reminder_text):
    time.sleep(delay)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    win32api.MessageBox(0, reminder_text, "Promemoria", win32con.MB_OK)


def show_instructions():
    instructions = """
    Benvenuto nel programma di promemoria! -- Andrea Ianni

    Questo programma ti consente di impostare promemoria per ricordarti appuntamenti, compiti o eventi importanti.

    Per impostare un promemoria, segui le seguenti istruzioni:
    1. Inserisci la data e l'ora del promemoria nel formato 'gg/mm/aaaa hh:mm'.
    2. Inserisci il testo del promemoria.
    3. Premi Invio per confermare.
    4. Lascia il programma aperto altrimenti il tuo promemoria verrà cancellato, purtroppo non ho inserito una funzione che permettesse al programma di 
    funzionare anche da chiuso poichè è ancora in alpha!

    Puoi creare più promemoria consecutivamente. Per uscire dal programma, inserisci 'q' come data e ora del promemoria.

    Buon lavoro!
    """

    print(instructions)


# Funzione principale per avviare il programma
def main():
    show_instructions()
    set_reminder()


# Avvia il programma
if __name__ == "__main__":
    main()

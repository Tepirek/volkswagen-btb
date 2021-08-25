export default {
  nav: {
    profile: 'Profil',
    new_report: 'Nowy raport',
    my_reports: 'Moje raporty',
    statistics: 'Statystyki',
    history: 'Historia',
    logout: 'Wyloguj się'
  },
  report: {
    toolbar: {
      new: 'Stwórz nowy raport',
      my_reports: 'Moje raporty'
    },
    bug_dialog: {
      title: 'Konfiguracja',
      continue: 'Kontynuuj',
      required_field: {
        required_error_type: 'To pole jest wymagane',
        required_inclusion_type: 'To pole jest wymagane!'
      },
      labels: {
        error_type: 'Rodzaj błędu',
        inclusion_type: 'Rodzaj wtrącenia'
      }
    },
    edit_dialog: {
      title: 'Konfiguracja',
      flip_element: 'Obróć element',
      buttons: {
        go_back_button: 'Wróć',
        go_next_button: 'Dalej',
        apply_button: 'Zastosuj'
      },
      labels: {
        error_type: 'Rodzaj błędu',
        inclusion_type: 'Rodzaj wtrącenia'
      },
      required_field: {
        required_error_type: 'To pole jest wymagane',
        required_inclusion_type: 'To pole jest wymagane!'
      }
    },
    new_report: {
      title: 'Konfiguracja',
      continue: 'Kontynuuj',
      summary: 'Podumowanie',
      labels: {
        color: 'Kolor',
        pin: 'PIN',
        body_type: 'Typ karoserii'
      },
      required_field: {
        required_body_type: 'To pole jest wymagane!',
        required_color_type: 'To pole jest wymagane!',
        required_pin: 'To pole jest wymagane!'
      }
    },
    summary: {
      report_number: 'Podsumowanie raportu #',
      base_info: 'Informacje ogólne',
      checked_errors: 'Wykaz zaznaczonych błędów',
      template_preview: 'Podgląd zaznaczonych błędów',
      template_toggle: 'Obróc szablon',
      not_sended: 'Nie wysłano',
      buttons: {
        send_button: 'Wyślij',
        go_back_button: 'Wróć'
      }
    },
    report_list: {
      report_number: 'Raport: #',
      buttons: {
        preview: 'Podgląd',
        edit: 'Edycja'
      }
    }
  },
  point_delete_dialog: {
    delete_point: 'Usuń punkt',
    buttons: {
      cancel: 'Anuluj',
      delete: 'Usuń'
    }
  },
  profile: {
    toolbar: {
      title: 'Profil użytkownika'
    },
    card: {
      settings: {
        password: 'Zmień hasło',
        language: 'Zmień język'
      },
      password: {
        current: 'Obecne hasło',
        new: 'Nowe hasło',
        repeat: 'Powtórz nowe hasło'
      },
      language: {
        label: 'Język',
        pl: 'Język polski',
        us: 'English',
        ua: 'Українська мова'
      },
      confirm: 'Zatwierdź',
      cancel: 'Anuluj'
    }
  },
  statistics: {
    title: 'Statystyki',
    type: {
      weekly: 'Statystyki tygodniowe',
      monthly: 'Statystyki miesięczne',
      yearly: 'Statystyki roczne'
    },
    filters: {
      title: 'Filtry',
      summary_type: 'Typy podsumowania',
      time_start: 'Zakres od:',
      time_end: 'Zakres do:',
      find_summaries: 'Szukaj podsumowań',
      types: {
        weekly: 'Podsumowania tygodniowe',
        monthly: 'Podsumowania miesięczne',
        yearly: 'Podsumowania roczne',
        custom: 'Podsumowania niestandardowe'
      },
      type: {
        weekly: 'Podsumowanie tygodniowe',
        monthly: 'Podsumowanie miesięczne',
        yearly: 'Podsumowanie roczne',
        custom: 'Podsumowanie niestandardowe'
      }
    },
    required_field: 'To pole jest wymagane!',
    new_summaries: {
      title: 'Nowe podsumowanie',
      time_start: 'Zakres od:',
      time_end: 'Zakres do:',
      create_summary: 'Stwórz podsumowanie'
    }
  },
  history: {
    toolbar: {
      title: 'Historia'
    },
    actions: {
      report_created: 'Utworzono nowy raport',
      report_updated: 'Wysłano raport',
      summary_created: 'Stworzono podsumowanie'
    }
  },
  auth: {
    login: {
      form: {
        title: 'Logowanie',
        login_button: 'Zaloguj',
        labels: {
          username: 'ID pracownika',
          password: 'Hasło'
        },
        errors: {
          required_field: {
            required_login: 'To pole jest wymagane!',
            required_password: 'To pole jest wymagane!'
          }
        }
      }
    },
    logout: {
      form: {
        logout_button: 'Wyloguj'
      }
    },
    notifications: {
      login_failure: 'Nie udało się zalogować. Sprawdź wprowadzone dane!',
      logout_success: 'Pomyślnie wylogowano!'
    }
  },
  faq: {
    title: 'Pomoc',
    statistics: {
      from: 'Data początkowa - dzień, od którego raporty brane są pod uwagę',
      to: 'Data końcowa - dzień, do którego raporty brane są do utworzenia podsumowania',
      type: 'Typ podsumowania - tygodniowe, miesięczne i roczne - dla rocznych podsumowań znika możliwość filtrowania po dacie',
      pdf: 'Plik w formacie pdf zawierający podsumowanie'
    },
    profile: {
      username: 'Nazwa pracownika',
      phone: 'Telefon',
      email: 'Email'
    },
    new_report: {
      body_type: 'Typ karoserii - jest wymagane',
      color: 'Kolor - jest wymagane',
      pin: 'PIN - jest wymagane'
    },
    list_report: {
      body_type: 'Typ karoserii',
      color: 'Kolor',
      pedding: 'Ikona informująca o tym, że raport jest jeszcze w trakcie tworzenia',
      done: 'Ikona informująca o tym, że proces tworzenia raportu został już ukończony',
      create_at: 'Data utworzenia raportu',
      done_at: 'Data ukończenia raportu'
    },
    history: {
      description: 'Zamieszczony jest tu dziennik aktywności danego pracownika. W dymkach widoczna jest historia jego poczynań w kolejności chronologicznej.'
    },
    create_report: {
      bug: 'Wybierz rodzaj błędu',
      pen: 'Zmień możliwość zaznaczania błędów na ich usuwanie i odwrotnie',
      arrow_right: 'Przejdź do kolejnego elementu',
      arrow_left: 'Przejdź do poprzedniego elementu'
    }
  },
  notifications: {
    delete_point: 'Usunięto punkt!',
    create_report: 'Utworzono raport!',
    update_report: 'Raport został wysłany!',
    create_summary: 'Utworzono podsumowanie!',
    all_summaries: 'Oto wyniki wyszukiwania!'
  }
}

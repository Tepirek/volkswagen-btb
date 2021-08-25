export default {
  nav: {
    profile: 'Профіль',
    new_report: 'Новий звіт',
    my_reports: 'Мої звіти',
    statistics: 'Статистика',
    history: 'Історія',
    logout: 'Вийти'
  },
  report: {
    toolbar: {
      new: 'Створіть новий звіт',
      my_reports: 'Мої звіти'
    },
    bug_dialog: {
      title: 'Конфігурація',
      continue: 'Продовжуй',
      required_field: {
        required_error_type: 'Це поле є обов\'язковим!',
        required_inclusion_type: 'Це поле є обов\'язковим!'
      },
      labels: {
        error_type: 'Тип помилки',
        inclusion_type: 'Тип включення'
      }
    },
    edit_dialog: {
      title: 'Конфігурація',
      flip_element: 'Поверніть елемент',
      buttons: {
        go_back_button: 'Повернутися',
        go_next_button: 'Далі',
        apply_button: 'Застосувати'
      },
      labels: {
        error_type: 'Тип помилки',
        inclusion_type: 'Тип включення'
      },
      required_field: {
        required_error_type: 'Це поле є обов\'язковим!',
        required_inclusion_type: 'Це поле є обов\'язковим!'
      }
    },
    new_report: {
      title: 'Конфігурація',
      continue: 'Продовжуй',
      summary: 'Резюме',
      labels: {
        color: 'Колір',
        pin: 'PIN',
        body_type: 'Тип кузова автомобіля'
      },
      required_field: {
        required_body_type: 'Це поле є обов\'язковим!',
        required_color_type: 'Це поле є обов\'язковим!',
        required_pin: 'Це поле є обов\'язковим!'
      }
    },
    summary: {
      report_number: 'Короткий зміст звіту #',
      base_info: 'Загальна інформація',
      checked_errors: 'Список позначених помилок',
      template_preview: 'Попередній перегляд позначених помилок',
      template_toggle: 'Поверніть шаблон',
      not_sended: 'Не надіслано',
      buttons: {
        send_button: 'Надіслати',
        go_back_button: 'Повернутися'
      }
    },
    report_list: {
      report_number: 'Звіт: #',
      buttons: {
        preview: 'Деталі',
        edit: 'Редагувати'
      }
    }
  },
  point_delete_dialog: {
    delete_point: 'Видалити точку',
    buttons: {
      cancel: 'Скасувати',
      delete: 'Видалити'
    }
  },
  profile: {
    toolbar: {
      title: 'Профіль користувача'
    },
    card: {
      settings: {
        password: 'Змінити пароль ',
        language: 'Змінити мову '
      },
      password: {
        current: 'Поточний пароль ',
        new: 'Новий пароль ',
        repeat: 'Повторіть новий пароль '
      },
      language: {
        label: 'Language',
        pl: 'Język polski',
        us: 'English',
        ua: 'Українська мова'
      },
      confirm: 'Підтвердити',
      cancel: 'Скасувати'
    }
  },
  statistics: {
    title: 'Статистика',
    type: {
      weekly: 'Щотижнева статистика',
      monthly: 'Щомісячна статистика',
      yearly: 'Щорічна статистика'
    },
    filters: {
      title: 'Фільтри ',
      summary_type: 'Резюме типи ',
      time_start: 'В діапазоні від: ',
      time_end: 'Діапазон до: ',
      find_summaries: 'Пошук резюме',
      types: {
        weekly: 'Щотижневі резюме',
        monthly: 'Щомісячні підсумки',
        yearly: 'Щорічні підсумки',
        custom: 'Спеціальні резюме'
      },
      type: {
        weekly: 'Щотижневий підсумок',
        monthly: 'Щомісячний зведення',
        yearly: 'Річний підсумок',
        custom: 'Спеціальний підсумок'
      }
    },
    required_field: 'Це поле є обов\'язковим!',
    new_summaries: {
      title: 'Нове резюме',
      time_start: 'В діапазоні від: ',
      time_end: 'Діапазон до: ',
      create_summary: 'Створіть резюме'
    }
  },
  history: {
    toolbar: {
      title: 'Історія'
    },
    actions: {
      report_created: 'Створено новий звіт',
      report_updated: 'Звіт надіслано',
      summary_created: 'Було зроблено резюме'
    }
  },
  auth: {
    login: {
      form: {
        title: 'Увійти',
        login_button: 'Увійти',
        labels: {
          username: 'Ідентифікаційний номер працівника',
          password: 'Пароль'
        },
        errors: {
          required_field: {
            required_login: 'Це поле є обов\'язковим!',
            required_password: 'Це поле є обов\'язковим!'
          }
        }
      }
    },
    logout: {
      form: {
        logout_button: 'вийти'
      }
    },
    notifications: {
      login_failure: 'Не вдалося увійти. Перевірте введені дані!',
      logout_success: 'Вихід успішний!'
    }
  },
  faq: {
    title: 'Допомога',
    statistics: {
      from: 'Дата початку - дата, з якої звіти беруться до уваги ',
      to: 'Дата завершення - дата, до якої приймаються звіти для створення підсумку ',
      type: 'Тип підсумків - Щотижневий, Щомісячний та Щорічний - Фільтрація за датою більше не доступна для щорічних резюме',
      pdf: 'PDF -файл, що містить резюме '
    },
    profile: {
      username: 'Ім\'я користувача ',
      phone: 'Телефон',
      email: 'Email'
    },
    new_report: {
      body_type: 'Тип кузова автомобіля - обов\'язковий ',
      color: 'Колір - обов\'язковий',
      pin: 'PIN - обов\'язковий'
    },
    list_report: {
      body_type: 'Тип кузова автомобіля ',
      color: 'Колір',
      pedding: 'Значок, який повідомляє, що звіт ще створюється ',
      done: 'Значок, який повідомляє, що процес створення звіту вже завершено ',
      create_at: 'Дата створення звіту',
      done_at: 'Дата складання звіту '
    },
    history: {
      description: 'Журнал діяльності співробітника розміщено тут. На кульці показано хронологічну історію його дій.'
    },
    create_report: {
      bug: 'Вибрати тип помилки ',
      pen: 'Змініти можливість позначення помилок, щоб видалити їх і навпаки ',
      arrow_right: 'Перейти до наступного пункту',
      arrow_left: 'Перейти до попереднього пункту'
    }
  },
  notifications: {
    delete_point: 'Точка знята!',
    create_report: 'Звіт створено!',
    update_report: 'Звіт надіслано!',
    create_summary: 'Резюме створено!',
    all_summaries: 'Ось результати пошуку!'
  }
}

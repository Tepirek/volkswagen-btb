export default {
  nav: {
    profile: 'Profile',
    new_report: 'New report',
    my_reports: 'My reports',
    statistics: 'Statistics',
    history: 'History',
    logout: 'Logout'
  },
  report: {
    toolbar: {
      new: 'Create new report',
      my_reports: 'My reports'
    },
    bug_dialog: {
      title: 'Configuration',
      continue: 'Continue',
      required_field: {
        required_error_type: 'This field is required!',
        required_inclusion_type: 'This field is required!'
      },
      labels: {
        error_type: 'The type of error',
        inclusion_type: 'The type of inclusion'
      }
    },
    edit_dialog: {
      title: 'Configuration',
      flip_element: 'Toggle element',
      buttons: {
        go_back_button: 'Back',
        go_next_button: 'Next',
        apply_button: 'Apply'
      },
      labels: {
        error_type: 'The type of error',
        inclusion_type: 'The type of inclusion'
      },
      required_field: {
        required_error_type: 'This field is required!',
        required_inclusion_type: 'This field is required!'
      }
    },
    new_report: {
      title: 'Configuration',
      continue: 'Continue',
      summary: 'Summary',
      labels: {
        color: 'Color',
        pin: 'PIN',
        body_type: 'Body type'
      },
      required_field: {
        required_body_type: 'This field is required!',
        required_color_type: 'This field is required!',
        required_pin: 'This field is required!'
      }
    },
    summary: {
      report_number: 'Summary of the report #',
      base_info: 'General Information',
      checked_errors: 'List of marked errors',
      template_preview: 'Preview of selected errors ',
      template_toggle: 'Rotate the template ',
      not_sended: 'Not sent',
      buttons: {
        send_button: 'Send',
        go_back_button: 'Back'
      }
    },
    report_list: {
      report_number: 'Report: #',
      buttons: {
        preview: 'Preview',
        edit: 'Edit'
      }
    }
  },
  point_delete_dialog: {
    delete_point: 'Delete point',
    buttons: {
      cancel: 'Cancel',
      delete: 'Delete'
    }
  },
  profile: {
    toolbar: {
      title: 'User profile'
    },
    card: {
      settings: {
        password: 'Change password',
        language: 'Change language'
      },
      password: {
        current: 'Current password',
        new: 'New password',
        repeat: 'Repeat new password'
      },
      language: {
        label: 'Language',
        pl: 'Język polski',
        us: 'English',
        ua: 'Українська мова'
      },
      confirm: 'Confirm',
      cancel: 'Cancel'
    }
  },
  statistics: {
    title: 'Statistics',
    type: {
      weekly: 'Weekly statistics',
      monthly: 'Monthly statistics',
      yearly: 'Yearly statistics'
    },
    filters: {
      title: 'Filters',
      summary_type: 'Summary types',
      time_start: 'Range from: ',
      time_end: 'Range to: ',
      find_summaries: 'Search for summaries',
      types: {
        weekly: 'Weekly summaries',
        monthly: 'Monthly summaries',
        yearly: 'Yearly summaries',
        custom: 'Custom summaries'
      },
      type: {
        weekly: 'Weekly summary',
        monthly: 'Monthly summary',
        yearly: 'Yearly summary',
        custom: 'Custom summary'
      }
    },
    required_field: 'This field is required!',
    new_summaries: {
      title: 'New summary',
      time_start: 'Range from: ',
      time_end: 'Range to: ',
      create_summary: 'Create summary'
    }
  },
  history: {
    toolbar: {
      title: 'History'
    },
    actions: {
      report_created: 'A new report has been created',
      report_updated: 'Report sent',
      summary_created: 'A summary was made'
    }
  },
  auth: {
    login: {
      form: {
        title: 'Login',
        login_button: 'Login',
        labels: {
          username: 'ID worker',
          password: 'Password'
        },
        errors: {
          required_field: {
            required_login: 'This field is required!',
            required_password: 'This field is required!'
          }
        }
      }
    },
    logout: {
      form: {
        logout_button: 'Logout'
      }
    },
    notifications: {
      login_failure: 'Login failed. Check the entered data!',
      logout_success: 'Logout successful!'
    }
  },
  faq: {
    title: 'Help',
    statistics: {
      from: 'Start date - the date from which the reports are taken to create a summary',
      to: 'End date - the date until which reports are taken to create a summary',
      type: 'Summary type - Weekly, Monthly, and Yearly - Filtering by date is no longer available for yearly summaries',
      pdf: 'A pdf file containing a summary'
    },
    profile: {
      username: 'Username',
      phone: 'Phone',
      email: 'Email'
    },
    new_report: {
      body_type: 'Car body type - required',
      color: 'Color - is required',
      pin: 'PIN - is required'
    },
    list_report: {
      body_type: 'Car body type',
      color: 'Color',
      pedding: 'Icon informing that the report is still being created',
      done: 'Icon informing that the report creation process has already been completed',
      create_at: 'Report creation date',
      done_at: 'The date the report was completed'
    },
    history: {
      description: 'A log of the employee\'s activity is posted here. The balloon shows the history of his actions in chronological order.'
    },
    create_report: {
      bug: 'Select the type of error',
      pen: 'Change the ability to mark errors to delete them and vice versa',
      arrow_right: 'Go to the next item',
      arrow_left: 'Go to the previous item'
    }
  },
  notifications: {
    delete_point: 'Point has beem removed!',
    create_report: 'Report has been created!',
    update_report: 'The report has been sent!',
    create_summary: 'Summary has been created!',
    all_summaries: 'Here are the search results!'
  }
}

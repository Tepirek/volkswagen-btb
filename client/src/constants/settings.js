import { BASE_URL } from '../constants'

export const LANGUAGE_PL = 'pl'
export const LANGUAGE_US = 'us'
export const LANGUAGE_UA = 'ua'

export const LANGUAGES = [
  LANGUAGE_PL,
  LANGUAGE_US,
  LANGUAGE_UA
]

export const COUNTRY_FLAGS = {
  [`${LANGUAGE_PL}`]: `${BASE_URL}/media/flags/${LANGUAGE_PL}.svg`,
  [`${LANGUAGE_US}`]: `${BASE_URL}/media/flags/${LANGUAGE_US}.svg`,
  [`${LANGUAGE_UA}`]: `${BASE_URL}/media/flags/${LANGUAGE_UA}.svg`
}
